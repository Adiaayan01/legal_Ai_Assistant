import pickle

from retrieval.chunker import (
    create_chunks
)

from retrieval.embeddings import (
    create_embeddings
)

from retrieval.vector_store import (
    create_faiss_index,
    save_index
)

with open(
    "data/sample_case.txt",
    "r"
) as f:

    text = f.read()

chunks = create_chunks(text)

vectors = create_embeddings(
    chunks
)

index = create_faiss_index(
    vectors
)

save_index(index)

with open(
    "outputs/chunks.pkl",
    "wb"
) as f:

    pickle.dump(
        chunks,
        f
    )

print(
    "FAISS Index Created"
)