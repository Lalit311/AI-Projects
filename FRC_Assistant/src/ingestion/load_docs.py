from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_documents(folder_path: str):

    documents = []

    pdf_files = Path(folder_path).glob("*.pdf")

    for pdf_file in pdf_files:

        print(f"Loading: {pdf_file.name}")

        loader = PyPDFLoader(str(pdf_file))

        pages = loader.load()

        for page in pages:

            page.metadata = {
            "source_file": pdf_file.name,
            "document_type": "regulation",
            "regulator": (
                "RBI"
                if "rbi" in str(pdf_file).lower()
                else "SEBI"
            ),
            "page": page.metadata.get("page"),
            "total_pages": page.metadata.get("total_pages")
        }

            documents.append(page)

    return documents