"""Reinsurance Placement

Task: Place a risk with two reinsurers.
Framework: the A2A (Agent2Agent) protocol
"""
from runtime import run_app

SLUG = 'insurance_reinsurance'
TITLE = 'Reinsurance Placement'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Place a risk with two reinsurers.'

# (key, role, instruction)
AGENTS = [
    ('broker_agent', 'Broker Agent', 'Present the risk.'),
    ('primary_insurer_agent', 'Primary Insurer Agent', 'Describe retention.'),
    ('reinsurer_a_agent', 'Reinsurer A Agent', 'Quote.'),
    ('reinsurer_b_agent', 'Reinsurer B Agent', 'Quote.'),
    ('compliance_agent', 'Compliance Agent', 'Check regulations.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
