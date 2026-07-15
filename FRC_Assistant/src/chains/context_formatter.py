def format_docs(docs):

    formatted = []

    for doc in docs:

        formatted.append(
            f"""
            DOCUMENT:
            {doc.metadata['source_file']}

            PAGE:
            {doc.metadata['page']}

            CONTENT:
            {doc.page_content}
            """
        )

    return "\n\n".join(formatted)