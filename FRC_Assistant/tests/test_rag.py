# from src.chains.rag_chain import ask_question

# # question = input("Ask Compliance Question: ")
# question = "What are the KYC requirements for customer identification?"
# result = ask_question(question)

# print("\n" + "=" * 80)
# print("\nANSWER\n")
# print(result["answer"])
# print("\n" + "=" * 80)
# print("\nSOURCES\n")

# for source in result["sources"]:
#     print(
#         f"{source['document']} "
#         f"(Page {source['page']})"
#     )
    
from src.chains.rag_service import RAGService

rag = RAGService()

while True:
    question = input("Ask Question: ")

    if question.lower() == "exit":
        break

    result = rag.ask(question)

    print("\nANSWER\n")
    print(result["answer"])
    
    print("\nSOURCES\n")
    for source in result["sources"]:
        print(
            f"{source['document']} "
            f"(Page {source['page']})"
        )