def format_docs(docs):

    context_parts = []

    for doc in docs:
        context_parts.append(
            f"""
            DOCUMENT:
            {doc.metadata['source_file']}

            PAGE:
            {doc.metadata['page']}

            CONTENT:
            {doc.page_content}
            """
        )

    return "\n\n".join(context_parts)


def prompt_to_string(prompt):

    if hasattr(prompt, "to_string"):
        return prompt.to_string()

    return str(prompt)