import chromadb
from src.embeddings import generate_embedding


def get_vector_store():
    client = chromadb.PersistentClient(path="./chroma_db")

    collection = client.get_or_create_collection(
        name="hr_documents"
    )

    return collection


def add_documents(chunks):
    collection = get_vector_store()

    # Remove previously indexed documents
    existing = collection.get()

    if existing["ids"]:
        collection.delete(ids=existing["ids"])

    # Store text, embeddings, and section metadata
    for i, chunk in enumerate(chunks):

        content = chunk["content"]
        section = chunk["section"]

        embedding = generate_embedding(content)

        collection.add(
            ids=[f"chunk_{i}"],
            documents=[content],
            embeddings=[embedding],
            metadatas=[{"section": section}]
        )

    return collection