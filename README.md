# 📚 HR Knowledge Assistant

An AI-powered HR knowledge assistant built using Retrieval-Augmented Generation (RAG). It enables employees to ask questions about company policies in natural language and receive context-aware answers grounded in HR handbook documents.

## 📌 Project Overview

Finding specific information in lengthy HR handbooks can be time-consuming.

The HR Knowledge Assistant addresses this problem by combining semantic search, vector databases, and Large Language Models (LLMs) to retrieve relevant handbook information and generate answers based on the retrieved context.

The application also supports conversational follow-up questions and displays the relevant HR handbook sections used to generate responses.

## ✨ Features

- **HR Policy Question Answering:** Ask questions about company policies using natural language.
- **Retrieval-Augmented Generation:** Generates answers grounded in retrieved handbook content.
- **Semantic Search:** Retrieves relevant information based on query meaning.
- **Local Text Embeddings:** Generates embeddings using Ollama and the `nomic-embed-text` model.
- **Vector Database:** Stores and retrieves document embeddings using ChromaDB.
- **Conversational Follow-ups:** Understands contextual questions using conversation history.
- **Source References:** Displays relevant HR handbook section names.
- **Relevance Filtering:** Filters retrieved chunks using similarity distance.
- **Interactive Chat Interface:** Provides a conversational interface using Streamlit.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Interactive user interface |
| Ollama | Local embedding generation |
| nomic-embed-text | Text embedding model |
| ChromaDB | Vector storage and semantic retrieval |
| Groq API | LLM-powered response generation |
| Git & GitHub | Version control |

## ⚙️ How It Works

The application follows a Retrieval-Augmented Generation workflow.

1. **Document Loading:** Loads the HR handbook from the data directory.
2. **Text Splitting:** Divides the handbook into smaller chunks while preserving section headings.
3. **Embedding Generation:** Uses Ollama's `nomic-embed-text` model to convert text chunks into numerical embeddings.
4. **Vector Storage:** Stores document chunks, embeddings, and section metadata in ChromaDB.
5. **Query Processing:** Converts user questions into embeddings and searches for semantically relevant chunks.
6. **Context Preparation:** Passes retrieved handbook content to the language model.
7. **Response Generation:** Uses the Groq API to generate answers based on the retrieved context.
8. **Conversational Retrieval:** Rewrites follow-up questions into standalone questions using conversation history.
9. **Source References:** Displays the handbook sections associated with retrieved information.

## 🏗️ Project Structure

```text
HR-Knowledge-Assistant/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── data/
│   └── Hrhandbook.txt
│
├── src/
│   ├── config.py
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── ingest.py
│   ├── retriever.py
│   └── rag_pipeline.py
│
├── test_embeddings.py
├── test_ollama.py
├── test_rag.py
└── test_retrieval.py
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12
- Ollama
- Groq API key

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/MokshithaBevara/HR-Knowledge-Assistant.git
```

**2. Navigate to the project directory**

```bash
cd HR-Knowledge-Assistant
```

**3. Create and activate a virtual environment**

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Set up Ollama**

Install Ollama and download the embedding model:

```bash
ollama pull nomic-embed-text
```

Make sure the Ollama service is running before starting the application.

**6. Configure the Groq API key**

Create a `.streamlit/secrets.toml` file and add:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Never upload this file or expose your API key publicly.

**7. Index the HR handbook**

Run:

```bash
python -m src.ingest
```

This processes the handbook, generates embeddings, and stores the indexed documents in ChromaDB.

**8. Run the application**

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal.

## 🧪 Testing

The project includes separate scripts for testing important components:

- `test_embeddings.py` – Tests local embedding generation.
- `test_ollama.py` – Checks Ollama integration.
- `test_retrieval.py` – Tests semantic document retrieval.
- `test_rag.py` – Tests the RAG answer-generation pipeline.

## 🔮 Future Improvements

- Support for PDF and additional document formats.
- Improved retrieval accuracy and contextual relevance.
- More advanced document management.
- Enhanced source-level citations.
- Deployment for wider accessibility.

## 🎯 Project Objective

This project demonstrates the practical implementation of Retrieval-Augmented Generation by integrating local embedding models, semantic search, vector databases, and LLM-powered response generation into an interactive document question-answering application.

## Community

Built as part of my AI development journey.

GrowthX Off Campus Code: B4AFFT