import ollama
from src.config import EMBEDDING_MODEL


def generate_embedding(text):
    response = ollama.embed(
        model=EMBEDDING_MODEL,
        input=text
    )

    return response["embeddings"][0]