from src.retriever import retrieve_documents

questions = [
    "How many casual leaves are provided per year?",
    "What is the maximum earned leave carry-forward limit?",
    "What is the company's work from home policy?",
    "What are the employee performance evaluation procedures?"
]

for question in questions:

    print("\n" + "=" * 60)
    print("QUESTION:", question)
    print("=" * 60)

    results = retrieve_documents(question)

    for result in results:
        print("\nSection:", result["section"])
        print("Distance:", round(result["distance"], 4))
        print("Content:", result["content"][:200])