import faiss
import pickle

from sentence_transformers import (
    SentenceTransformer
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def retrieve(query, top_k=3):

    index = faiss.read_index(
        "outputs/faiss.index"
    )

    with open(
        "outputs/chunks.pkl",
        "rb"
    ) as f:

        chunks = pickle.load(f)

    query_vector = model.encode(
        [query]
    )

    distances, indices = index.search(
        query_vector,
        top_k
    )

    results = []

    for idx in indices[0]:
        results.append(
            chunks[idx]
        )

    return results