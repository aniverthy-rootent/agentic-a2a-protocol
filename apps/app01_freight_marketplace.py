"""Freight Marketplace

Task: Ship 12 pallets from Rotterdam to Milan within 4 days.
Framework: the A2A (Agent2Agent) protocol
"""
from runtime import run_app

SLUG = 'freight_marketplace'
TITLE = 'Freight Marketplace'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Ship 12 pallets from Rotterdam to Milan within 4 days.'

# (key, role, instruction)
AGENTS = [
    ('shipper_agent', 'Shipper Agent', 'Post the shipment request.'),
    ('carrier_agent', 'Carrier Agent', 'Bid with rates.'),
    ('customs_agent', 'Customs Agent', 'Pre-clear documents.'),
    ('insurance_agent', 'Insurance Agent', 'Quote cargo cover.'),
    ('tracking_agent', 'Tracking Agent', 'Provide tracking plan.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
