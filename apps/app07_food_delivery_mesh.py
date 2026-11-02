"""Food Delivery Mesh

Task: Order dinner from two restaurants with one courier.
Framework: the A2A (Agent2Agent) protocol
"""
from runtime import run_app

SLUG = 'food_delivery_mesh'
TITLE = 'Food Delivery Mesh'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Order dinner from two restaurants with one courier.'

# (key, role, instruction)
AGENTS = [
    ('customer_agent', 'Customer Agent', 'Place order.'),
    ('restaurant_agent', 'Restaurant Agent', 'Confirm menu and time.'),
    ('courier_agent', 'Courier Agent', 'Plan pickup.'),
    ('payment_agent', 'Payment Agent', 'Authorize payment.'),
    ('support_agent', 'Support Agent', 'Handle issues.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
