from fastapi import APIRouter

from app.models.request import (
    QuestionRequest
)

from app.models.response import (
    QuestionResponse
)

from src.chains.rag_service import (
    RAGService
)

router = APIRouter()

rag_service = RAGService()


@router.post(
    "/ask",
    response_model=
    QuestionResponse
)
def ask_question(
    request:
    QuestionRequest
):

    result = rag_service.ask(
        request.question
    )

    return result