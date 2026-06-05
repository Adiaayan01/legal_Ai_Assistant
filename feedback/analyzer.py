import ollama

def extract_rule(
    original,
    edited
):

    prompt = f"""
Compare the drafts.

Original Draft:
{original}

Edited Draft:
{edited}

Identify reusable drafting preferences.

Examples:

- Use cautious language
- Add citations
- Prefer timeline format
- Avoid definitive claims

Return only concise rules.
"""

    response = ollama.chat(
        model="llama3.1",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]