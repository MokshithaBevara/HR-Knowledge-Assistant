import ollama

response = ollama.embed(
    model="nomic-embed-text",
    input="What is the company's leave policy?"
)

embedding = response["embeddings"][0]

print("Embedding generated successfully!")
print("Embedding dimensions:", len(embedding))
print("First five values:", embedding[:5])