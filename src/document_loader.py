from pathlib import Path

def load_document(file_path="data/Hrhandbook.txt"):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Document not found: {file_path}")

    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    return text