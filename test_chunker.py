from retrieval.chunker import create_chunks

text = "Hello World " * 100

chunks = create_chunks(text)

print("Chunks:", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0])