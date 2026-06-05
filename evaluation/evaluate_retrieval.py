from retrieval.retriever import retrieve

test_queries = [
    {
        "query": "When was legal notice issued?",
        "expected": "20/03/2024"
    },
    {
        "query": "Who is the plaintiff?",
        "expected": "John Doe"
    },
    {
        "query": "Who is the defendant?",
        "expected": "ABC Builders"
    }
]

correct = 0

for test in test_queries:

    results = retrieve(test["query"])

    combined = " ".join(results)

    if test["expected"] in combined:
        correct += 1

accuracy = (correct / len(test_queries)) * 100

print("\nRetrieval Accuracy")

print(f"{accuracy:.2f}%")