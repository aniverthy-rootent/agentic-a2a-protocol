"""Recruitment Exchange

Task: Match a candidate pool from an agency to an employer.
Framework: the A2A (Agent2Agent) protocol
"""
from runtime import run_app

SLUG = 'recruitment_exchange'
TITLE = 'Recruitment Exchange'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Match a candidate pool from an agency to an employer.'

# (key, role, instruction)
AGENTS = [
    ('employer_agent', 'Employer Agent', 'Post requirements.'),
    ('agency_agent', 'Agency Agent', 'Present candidates.'),
    ('background_check_agent', 'Background Check Agent', 'Verify claims.'),
    ('scheduling_agent', 'Scheduling Agent', 'Arrange interviews.'),
    ('offer_agent', 'Offer Agent', 'Negotiate offer.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
