"""Airline-Hotel-Car Alliance

Task: Book a business trip bundle across three companies.
Framework: the A2A (Agent2Agent) protocol
"""
from runtime import run_app

SLUG = 'travel_alliance'
TITLE = 'Airline-Hotel-Car Alliance'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Book a business trip bundle across three companies.'

# (key, role, instruction)
AGENTS = [
    ('airline_agent', 'Airline Agent', 'Offer flights.'),
    ('hotel_agent', 'Hotel Agent', 'Offer rooms.'),
    ('car_rental_agent', 'Car Rental Agent', 'Offer vehicles.'),
    ('bundler_agent', 'Bundler Agent', 'Combine offers.'),
    ('payment_agent', 'Payment Agent', 'Split payment.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
