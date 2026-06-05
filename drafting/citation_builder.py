def attach_citations(
    draft,
    evidence
):

    citations = "\n\nSUPPORTING EVIDENCE\n"

    for i, chunk in enumerate(
        evidence
    ):

        citations += (
            f"\n[Evidence {i+1}]\n"
        )

        citations += chunk

        citations += "\n"

    return draft + citations