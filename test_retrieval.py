from retrieval.retriever import retrieve

query = "When was legal notice issued?"

results = retrieve(query)

for i, result in enumerate(results):

    print("\n")
    print(f"Evidence {i+1}")
    print("-" * 50)
    print(result)