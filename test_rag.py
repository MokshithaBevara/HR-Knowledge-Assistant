import streamlit as st
from groq import Groq

from src.rag_pipeline import generate_answer

# Initialize Groq client
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

# Ask a question
question = "How many casual leaves are provided per year?"

# Generate answer
answer = generate_answer(question, client)

print("\nQuestion:", question)
print("\nAnswer:", answer)