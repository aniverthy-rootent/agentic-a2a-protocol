"""Hospital Referral Network (educational)

Task: Refer a patient between a clinic, lab and specialist.
Framework: the A2A (Agent2Agent) protocol
"""
from runtime import run_app

SLUG = 'healthcare_referral'
TITLE = 'Hospital Referral Network (educational)'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Refer a patient between a clinic, lab and specialist.'

# (key, role, instruction)
AGENTS = [
    ('clinic_agent', 'Clinic Agent', 'Create referral.'),
    ('lab_agent', 'Lab Agent', 'Schedule tests.'),
    ('specialist_agent', 'Specialist Agent', 'Propose appointment.'),
    ('insurance_agent', 'Insurance Agent', 'Check authorization.'),
    ('patient_liaison_agent', 'Patient Liaison Agent', 'Notify patient.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
