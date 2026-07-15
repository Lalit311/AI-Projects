from pydantic import BaseModel


class Source(
    BaseModel
):

    document: str

    page: int


class QuestionResponse(
    BaseModel
):

    answer: str

    sources: list[Source]