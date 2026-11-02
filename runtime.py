"""A2A runtime: every agent is an independent A2A server.

Each agent exposes
  GET  /.well-known/agent-card.json   (Agent Card: name, skills, endpoint)
  POST /                              (JSON-RPC 2.0: message/send, tasks/get)
A coordinator discovers the cards, then sends A2A messages along the
dependency graph from common.flow. Servers are mounted in-process through
httpx's ASGI transport, so no ports are opened; point `base_url` at real
hosts to run the same code across organizations.
"""
from __future__ import annotations

import asyncio
import uuid

import httpx
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route

from common.flow import compose_input, dependencies, execution_layers, system_prompt
from common.offline_llm import offline_complete

PROTOCOL_VERSION = "0.3.0"


def call_llm(system: str, user: str) -> str:
    """Replace with a real model call inside an agent server."""
    return offline_complete(system, user)


def make_agent_server(key: str, role: str, instruction: str, base_url: str) -> Starlette:
    card = {
        "protocolVersion": PROTOCOL_VERSION,
        "name": role,
        "description": instruction,
        "url": base_url,
        "version": "1.0.0",
        "capabilities": {"streaming": False, "pushNotifications": False},
        "defaultInputModes": ["text/plain"],
        "defaultOutputModes": ["text/plain"],
        "skills": [{"id": key, "name": role, "description": instruction, "tags": [key]}],
    }
    tasks: dict[str, dict] = {}

    async def agent_card(request: Request) -> JSONResponse:
        return JSONResponse(card)

    async def rpc(request: Request) -> JSONResponse:
        body = await request.json()
        rid, method, params = body.get("id"), body.get("method"), body.get("params", {})
        if method == "message/send":
            text = "".join(p.get("text", "") for p in params["message"]["parts"] if p.get("kind") == "text")
            answer = call_llm(system_prompt(role, instruction), text)
            task_id = str(uuid.uuid4())
            task = {
                "kind": "task", "id": task_id, "contextId": params["message"].get("contextId", task_id),
                "status": {"state": "completed"},
                "artifacts": [{"artifactId": str(uuid.uuid4()), "name": key,
                               "parts": [{"kind": "text", "text": answer}]}],
            }
            tasks[task_id] = task
            return JSONResponse({"jsonrpc": "2.0", "id": rid, "result": task})
        if method == "tasks/get":
            task = tasks.get(params.get("id"))
            if task:
                return JSONResponse({"jsonrpc": "2.0", "id": rid, "result": task})
            return JSONResponse({"jsonrpc": "2.0", "id": rid, "error": {"code": -32001, "message": "Task not found"}})
        return JSONResponse({"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": "Method not found"}})

    return Starlette(routes=[
        Route("/.well-known/agent-card.json", agent_card),
        Route("/", rpc, methods=["POST"]),
    ])


async def send_message(client: httpx.AsyncClient, base_url: str, text: str) -> str:
    payload = {"jsonrpc": "2.0", "id": str(uuid.uuid4()), "method": "message/send",
               "params": {"message": {"kind": "message", "role": "user",
                                      "messageId": str(uuid.uuid4()),
                                      "parts": [{"kind": "text", "text": text}]}}}
    resp = await client.post(base_url + "/", json=payload)
    resp.raise_for_status()
    task = resp.json()["result"]
    assert task["status"]["state"] == "completed"
    return task["artifacts"][0]["parts"][0]["text"]


async def _run(agents, task, pattern):
    deps = dependencies(pattern, len(agents))
    clients: list[httpx.AsyncClient] = []
    cards = []
    for key, role, instr in agents:
        base = f"http://{key}.agents.local"
        app = make_agent_server(key, role, instr, base)
        client = httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url=base)
        clients.append(client)
        card = (await client.get("/.well-known/agent-card.json")).json()  # discovery
        cards.append(card)
    outputs: dict[str, str] = {}

    async def call(i: int) -> None:
        key, role, _ = agents[i]
        ups = [(agents[j][1], outputs[agents[j][0]]) for j in deps[i]]
        outputs[key] = await send_message(clients[i], cards[i]["url"], compose_input(task, ups))

    try:
        for layer in execution_layers(pattern, len(agents)):
            await asyncio.gather(*(call(i) for i in layer))
    finally:
        for c in clients:
            await c.aclose()
    return {key: outputs[key] for key, _, _ in agents}


def run_app(title, agents, task, pattern="sequential", provider=None) -> dict:
    return asyncio.run(_run(agents, task, pattern))
