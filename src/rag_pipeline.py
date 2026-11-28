from src.retriever import retrieve_documents
from src.config import LLM_MODEL

def generate_answer(question, client, chat_history=None):

    # Step 1: Prepare conversation history
    history = ""

    if chat_history:
        for message in chat_history[-6:]:
            history += f"{message['role']}: {message['content']}\n"

    # Step 2: Rewrite follow-up question
    rewrite_prompt = f"""
    Convert the latest user question into a standalone question.

    Use the conversation history to understand references
    such as "they", "it", "that", and "the limit".

    If the question is already standalone, keep it unchanged.

    Conversation History:
    {history}

    Latest Question:
    {question}

    Return only the rewritten question.
    """

    rewritten = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": rewrite_prompt}],
        temperature=0
    )

    standalone_question = rewritten.choices[0].message.content.strip()

    # Step 3: Retrieve documents using rewritten question
    documents = retrieve_documents(standalone_question)

    if not documents:
        return "I couldn't find that information in the HR handbook."

    # Step 4: Prepare context
    context = "\n\n".join(
        f"Section: {doc['section']}\nContent: {doc['content']}"
        for doc in documents
    )

    # Step 5: Generate answer
    prompt = f"""
    You are an HR assistant.

    Answer using ONLY the information in the HR handbook context.

    Important rules:
    1. The retrieved context may contain irrelevant information.
    2. Only use information that directly answers the user's question.
    3. Do not make assumptions or combine unrelated information.
    4. If the context does not directly answer the question,
       respond: "I couldn't find that information in the HR handbook."
    5. Include only the section names that directly support your answer.

    If the answer is unavailable in the context,
    say that you couldn't find the information in the HR handbook.

    HR Handbook Context:
    {context}

    User Question:
    {question}

    Standalone Question:
    {standalone_question}

    Answer:
    """

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    answer = response.choices[0].message.content

    # Collect source section names
    sources = list(dict.fromkeys(
        doc["section"] for doc in documents
    ))

    source_text = "\n\n**Sources:** " + ", ".join(sources)

    return answer + source_text