"""Relief Supply Exchange

Task: Match donor offers to shelter needs after an earthquake.
Framework: the A2A (Agent2Agent) protocol
"""
from runtime import run_app

SLUG = 'disaster_relief_exchange'
TITLE = 'Relief Supply Exchange'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Match donor offers to shelter needs after an earthquake.'

# (key, role, instruction)
AGENTS = [
    ('needs_agent', 'Needs Agent', 'Publish needs.'),
    ('donor_agent', 'Donor Agent', 'Publish offers.'),
    ('logistics_agent', 'Logistics Agent', 'Plan transport.'),
    ('verification_agent', 'Verification Agent', 'Verify requests.'),
    ('reporting_agent', 'Reporting Agent', 'Publish transparency report.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
