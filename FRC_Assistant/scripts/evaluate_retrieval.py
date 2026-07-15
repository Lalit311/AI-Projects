import json

from src.retrieval.hybrid_retriever import HybridRetriever

retriever = HybridRetriever()

with open(
    "data/evaluation/retrieval_test_cases.json",
    "r"
) as f:

    test_cases = json.load(f)

correct = 0

print("\n" + "=" * 100)
print("RETRIEVAL EVALUATION")
print("=" * 100)

for idx, test_case in enumerate(
    test_cases,
    start=1
):

    question = test_case["question"]

    expected_doc = (
        test_case["expected_document"]
    )

    docs = retriever.retrieve(
        question
    )

    retrieved_doc = docs[0].metadata[
        "source_file"
    ]

    is_correct = (
        retrieved_doc ==
        expected_doc
    )

    if is_correct:
        correct += 1

    print(
        f"\nTest #{idx}"
    )

    print(
        f"Question: {question}"
    )

    print(
        f"Expected: {expected_doc}"
    )

    print(
        f"Retrieved: {retrieved_doc}"
    )

    print(
        f"Result: {'PASS' if is_correct else 'FAIL'}"
    )

accuracy = (
    correct /
    len(test_cases)
) * 100

print("\n" + "=" * 100)

print(
    f"Accuracy: {accuracy:.2f}%"
)

print("=" * 100)