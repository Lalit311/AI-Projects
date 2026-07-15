from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


def load_policy(file_path: str) -> str:

    file_path = Path(file_path)

    if file_path.suffix.lower() == ".pdf":

        loader = PyPDFLoader(str(file_path))

        docs = loader.load()

        return "\n".join(
            doc.page_content
            for doc in docs
        )

    elif file_path.suffix.lower() == ".txt":

        return file_path.read_text(
            encoding="utf-8"
        )

    else:

        raise ValueError(
            f"Unsupported file type: "
            f"{file_path.suffix}"
        )