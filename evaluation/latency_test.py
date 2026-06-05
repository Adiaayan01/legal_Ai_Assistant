import time

from retrieval.retriever import retrieve

query = "Create a case fact summary."

start = time.time()

results = retrieve(query)

end = time.time()

print(f"Retrieval Time: {end-start:.2f} seconds")
print(f"Chunks Retrieved: {len(results)}")