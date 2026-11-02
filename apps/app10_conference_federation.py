"""Conference Federation

Task: Merge schedules from three co-located conferences.
Framework: the A2A (Agent2Agent) protocol
"""
from runtime import run_app

SLUG = 'conference_federation'
TITLE = 'Conference Federation'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Merge schedules from three co-located conferences.'

# (key, role, instruction)
AGENTS = [
    ('organizer_agent', 'Organizer Agent', 'Publish sessions.'),
    ('speaker_agent', 'Speaker Agent', 'Confirm availability.'),
    ('room_agent', 'Room Agent', 'Allocate rooms.'),
    ('attendee_agent', 'Attendee Agent', 'Build personal agenda.'),
    ('conflict_resolver_agent', 'Conflict Resolver Agent', 'Resolve clashes.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
