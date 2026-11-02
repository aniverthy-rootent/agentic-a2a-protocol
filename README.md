# agentic-a2a-protocol

**11 multi-agent applications built with the A2A (Agent2Agent) protocol.**  
Theme: _Cross-organization agents talking over the A2A protocol_

The [A2A protocol](https://a2a-protocol.org) lets independently owned agents discover each other through **Agent Cards** and collaborate over JSON-RPC (`message/send`, `tasks/get`). Here every agent is its own A2A server.

## Quick start (no API key needed)

```bash
pip install -r requirements.txt
python run_all.py                       # run all 11 apps
python -m apps.app01_freight_marketplace   # run a single app
pytest -q                               # smoke tests for every app
```

Every app runs against a deterministic offline model (`common/offline_llm.py`) so you can watch the orchestration work without credentials.

## How it works

`runtime.py` builds one small Starlette A2A server per agent (agent card at `/.well-known/agent-card.json` plus a JSON-RPC endpoint). A coordinator fetches the cards, then sends A2A messages along the app's dependency graph; results come back as completed Tasks with artifacts. Servers are mounted in-process via httpx's ASGI transport so no ports are needed; swap the `base_url` for real hosts to span machines or organizations.

## Using a real model

Inside `call_llm` in `runtime.py` call any model; each agent server owns its own model and credentials, which is the point of A2A. You can also serve any agent app with uvicorn and register its URL instead of the in-process one.

## Applications

| # | Application | Agents | Roles |
|---|---|---|---|
| 1 | Freight Marketplace | 5 | Shipper Agent, Carrier Agent, Customs Agent, Insurance Agent, Tracking Agent |
| 2 | Airline-Hotel-Car Alliance | 5 | Airline Agent, Hotel Agent, Car Rental Agent, Bundler Agent, Payment Agent |
| 3 | Hospital Referral Network (educational) | 5 | Clinic Agent, Lab Agent, Specialist Agent, Insurance Agent, Patient Liaison Agent |
| 4 | Smart Grid Negotiation | 5 | Household Agent, Solar Producer Agent, Battery Agent, Grid Operator Agent, Billing Agent |
| 5 | Cross-Journal Peer Review | 5 | Editor Agent, Reviewer Agent, Plagiarism Agent, Ethics Agent, Decision Agent |
| 6 | Real Estate Closing Network | 5 | Buyer Agent, Seller Agent, Bank Agent, Title Agent, Escrow Agent |
| 7 | Food Delivery Mesh | 5 | Customer Agent, Restaurant Agent, Courier Agent, Payment Agent, Support Agent |
| 8 | Recruitment Exchange | 5 | Employer Agent, Agency Agent, Background Check Agent, Scheduling Agent, Offer Agent |
| 9 | Relief Supply Exchange | 5 | Needs Agent, Donor Agent, Logistics Agent, Verification Agent, Reporting Agent |
| 10 | Conference Federation | 5 | Organizer Agent, Speaker Agent, Room Agent, Attendee Agent, Conflict Resolver Agent |
| 11 | Reinsurance Placement | 5 | Broker Agent, Primary Insurer Agent, Reinsurer A Agent, Reinsurer B Agent, Compliance Agent |

Full per-agent instructions are in [AGENTS.md](AGENTS.md).

Each app uses one of two data-flow patterns (see `common/flow.py`):
`sequential` (each agent builds on the previous) or `fanout` (a planner, parallel specialists, then a merger).

## License

MIT
