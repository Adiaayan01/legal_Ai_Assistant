from retrieval.retriever import retrieve
from drafting.generator import generate_draft

query = "Create a case fact summary."

evidence = retrieve(query)

draft = generate_draft(
    query,
    evidence
)

print("\n=== GENERATED DRAFT ===\n")
print(draft)

evidence_text = " ".join(evidence)

grounded = True

for keyword in [
    "John Doe",
    "ABC Builders"
]:

    if keyword not in draft:
        grounded = False

print("\n=== EVALUATION ===")
print(f"Grounded: {grounded}")