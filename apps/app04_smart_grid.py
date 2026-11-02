"""Smart Grid Negotiation

Task: Balance a neighborhood's solar surplus and EV charging.
Framework: the A2A (Agent2Agent) protocol
"""
from runtime import run_app

SLUG = 'smart_grid'
TITLE = 'Smart Grid Negotiation'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = "Balance a neighborhood's solar surplus and EV charging."

# (key, role, instruction)
AGENTS = [
    ('household_agent', 'Household Agent', 'Report demand.'),
    ('solar_producer_agent', 'Solar Producer Agent', 'Offer surplus.'),
    ('battery_agent', 'Battery Agent', 'Offer storage.'),
    ('grid_operator_agent', 'Grid Operator Agent', 'Set limits.'),
    ('billing_agent', 'Billing Agent', 'Settle prices.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
