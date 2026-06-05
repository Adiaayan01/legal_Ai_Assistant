import ollama

from drafting.prompt_builder import (
    build_prompt
)

def generate_draft(
    query,
    evidence
):

    prompt = build_prompt(
        query,
        evidence
    )

    response = ollama.chat(
        model="llama3.1",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response[
        "message"
    ]["content"]