import faiss
import numpy as np

def create_faiss_index(vectors):

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        np.array(vectors)
    )

    return index

def save_index(index):

    faiss.write_index(
        index,
        "outputs/faiss.index"
    )