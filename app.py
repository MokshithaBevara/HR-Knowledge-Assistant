import streamlit as st
from groq import Groq

from src.rag_pipeline import generate_answer

# Page configuration
st.set_page_config(
    page_title="HR Knowledge Assistant",
    page_icon="📚",
    layout="centered"
)

# Initialize Groq
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

# App heading
st.title("📚 HR Knowledge Assistant")

st.write(
    "Your AI-powered assistant for answering "
    "employee questions using the HR handbook."
)
if st.button("Clear Conversation"):
    st.session_state.messages = []
    st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
st.write("### Try asking:")

suggestions = [
    "How many casual leaves are provided per year?",
    "What is the work-from-home policy?",
    "How many weeks of maternity leave are provided?",
    "What are the working hours?"
]

for suggestion in suggestions:
    if st.button(suggestion):
        st.session_state.selected_question = suggestion

# User input
question = st.chat_input("Ask a question about HR policies...")

if "selected_question" in st.session_state:
    question = st.session_state.pop("selected_question")

if question:
    # Display user question
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("Searching the HR handbook..."):
            answer = generate_answer(
                                    question,
                                    client,
                                    st.session_state.messages[:-1]
                                    )

        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )