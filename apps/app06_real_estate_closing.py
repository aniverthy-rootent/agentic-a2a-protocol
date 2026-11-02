"""Real Estate Closing Network

Task: Close a home sale among buyer, seller, bank and title company.
Framework: the A2A (Agent2Agent) protocol
"""
from runtime import run_app

SLUG = 'real_estate_closing'
TITLE = 'Real Estate Closing Network'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Close a home sale among buyer, seller, bank and title company.'

# (key, role, instruction)
AGENTS = [
    ('buyer_agent', 'Buyer Agent', 'Submit offer terms.'),
    ('seller_agent', 'Seller Agent', 'Respond to terms.'),
    ('bank_agent', 'Bank Agent', 'Confirm financing.'),
    ('title_agent', 'Title Agent', 'Confirm title.'),
    ('escrow_agent', 'Escrow Agent', 'Schedule closing.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
