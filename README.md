# HR Knowledge Assistant

A Retrieval-Augmented Generation (RAG) based AI application that helps employees find accurate answers to HR-related questions using company handbook documents.

## 📌 Project Overview

HR Knowledge Assistant simplifies access to company HR policies by allowing employees to ask questions in natural language.

The application uses semantic search to retrieve relevant information from HR handbook documents and generates context-aware responses using a Large Language Model (LLM).

## ✨ Features

- **HR Policy Question Answering:** Get answers to questions about company policies.
- **Retrieval-Augmented Generation (RAG):** Generates responses using retrieved handbook information.
- **Semantic Search:** Finds relevant content based on the meaning of queries.
- **Vector Database:** Stores and retrieves document embeddings using ChromaDB.
- **AI-Powered Responses:** Integrates Groq API for response generation.
- **Interactive Interface:** Chat-based interface built with Streamlit.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | User interface |
| ChromaDB | Vector database |
| Sentence Transformers | Text embeddings |
| Groq API | LLM-powered response generation |

## ⚙️ How It Works

1. **Document Processing:** HR handbook documents are loaded and processed.
2. **Text Embedding:** Sentence Transformers converts text into numerical embeddings.
3. **Vector Storage:** Embeddings are stored in ChromaDB.
4. **Semantic Retrieval:** Relevant handbook sections are retrieved based on the user's query.
5. **Response Generation:** Retrieved context is passed to the Groq-powered LLM to generate an appropriate response.
6. **User Interaction:** Answers are displayed through the Streamlit chat interface.

## 📸 Application Screenshot

![HR Knowledge Assistant](https://github.com/user-attachments/assets/4d92ca0f-be75-4765-9c5b-d839d0800758)

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or later
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

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure your Groq API key**

Configure your Groq API key using the method expected by your application. Never commit API keys or other secrets to GitHub.

**5. Run the application**

```bash
streamlit run app.py
```

## 🎯 Project Objective

The objective of this project is to demonstrate how Retrieval-Augmented Generation, semantic search and vector databases can be combined to build a practical AI-powered document question-answering application.

## 🔮 Future Improvements

- Support for multiple document formats.
- Improved retrieval accuracy.
- Source references for generated answers.
- Document upload functionality.
