from feedback.rule_engine import (
    get_rules
)

def build_prompt(query, evidence):

    preferences = get_rules()

    context = "\n\n".join(
        evidence
    )

    preference_text = "\n".join(
        preferences
    )

    prompt = f"""
You are an internal legal analyst.

Operator Preferences:

{preference_text}

Use ONLY the evidence provided.

Question:
{query}

Evidence:
{context}

Generate a legal summary.
"""

    return prompt