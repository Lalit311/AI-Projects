import json

from src.chains.rag_service import (
    RAGService
)

rag = RAGService()

with open(
    "data/evaluation/questions.json"
) as f:

    questions = json.load(f)

results = []

for item in questions:

    question = item["question"]

    response = rag.ask(question)

    results.append(
        {
            "question": question,
            "answer":
                response["answer"],
            "contexts":
                response["sources"]
        }
    )

print(results)