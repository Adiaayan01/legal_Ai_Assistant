from retrieval.retriever import (
    retrieve
)

from drafting.generator import (
    generate_draft
)

from drafting.citation_builder import (
    attach_citations
)

query = """
Create a case fact summary.
"""

evidence = retrieve(query)

draft = generate_draft(
    query,
    evidence
)

final_output = attach_citations(
    draft,
    evidence
)

print(final_output)