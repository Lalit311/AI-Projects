import streamlit as st
import requests

API_URL = "http://localhost:8081/ask"

st.set_page_config(
    page_title="FRC Assistant",
    page_icon="🏦",
    layout="wide"
)

with st.sidebar:

    st.title("🏦 FRC Assistant")

    st.markdown("---")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

st.title("🏦 Financial Regulatory Compliance Assistant")
st.caption(
    "Ask questions about RBI and SEBI regulations"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.markdown(
            message["content"]
        )

question = st.chat_input(
    "Ask a compliance question..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner(
            "Thinking..."
        ):

            response = requests.post(
                API_URL,
                json={
                    "question": question
                }
            )

            result = response.json()

            answer = result["answer"]

            sources = result["sources"]

            source_text = "\n\n### Sources\n"

            for source in sources:

                source_text += (
                    f"- {source['document']} "
                    f"(Page {source['page']})\n"
                )

            final_response = (
                answer
                + source_text
            )

            st.markdown(
                final_response
            )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": final_response
        }
    )