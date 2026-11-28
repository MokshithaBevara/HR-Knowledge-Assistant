from src.vector_store import get_vector_store
from src.embeddings import generate_embedding
from src.config import TOP_K, DISTANCE_THRESHOLD


def retrieve_documents(question):

    collection = get_vector_store()

    if collection.count() == 0:
        return []

    query_embedding = generate_embedding(question)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(TOP_K, collection.count())
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    retrieved_results = []

    for document, metadata, distance in zip(
        documents, metadatas, distances
    ):
        if distance <= DISTANCE_THRESHOLD:
            retrieved_results.append({
                "content": document,
                "section": metadata["section"],
                "distance": distance
            })

    if not retrieved_results and documents:
        retrieved_results.append({
            "content": documents[0],
            "section": metadatas[0]["section"],
            "distance": distances[0]
        })

    return retrieved_results