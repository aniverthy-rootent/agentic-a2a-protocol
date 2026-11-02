"""Cross-Journal Peer Review

Task: Coordinate review of a manuscript across two journals.
Framework: the A2A (Agent2Agent) protocol
"""
from runtime import run_app

SLUG = 'academic_peer_review'
TITLE = 'Cross-Journal Peer Review'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Coordinate review of a manuscript across two journals.'

# (key, role, instruction)
AGENTS = [
    ('editor_agent', 'Editor Agent', 'Assign reviewers.'),
    ('reviewer_agent', 'Reviewer Agent', 'Write review.'),
    ('plagiarism_agent', 'Plagiarism Agent', 'Similarity check.'),
    ('ethics_agent', 'Ethics Agent', 'Ethics check.'),
    ('decision_agent', 'Decision Agent', 'Summarize decision.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
