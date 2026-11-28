import streamlit as st
from huggingface_hub import InferenceClient

hf_token = st.secrets["HF_TOKEN"]

client = InferenceClient(
    model="sentence-transformers/all-MiniLM-L6-v2",
    token=hf_token
)

embedding = client.feature_extraction(
    "What is the company's leave policy?"
)

print("Embedding generated successfully!")
print("Embedding shape:", embedding.shape)
print("First five values:", embedding.flatten()[:5])