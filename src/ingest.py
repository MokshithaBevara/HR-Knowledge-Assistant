from src.document_loader import load_document
from src.text_splitter import split_text
from src.vector_store import add_documents


def ingest_handbook():
    print("Loading HR handbook...")

    text = load_document()

    print("Splitting handbook into chunks...")

    chunks = split_text(text)

    print(f"Created {len(chunks)} chunks.")

    print("Generating embeddings and storing documents...")

    add_documents(chunks)

    print("HR handbook successfully indexed!")


if __name__ == "__main__":
    ingest_handbook()