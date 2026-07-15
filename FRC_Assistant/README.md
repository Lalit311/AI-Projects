# FRC Assistant

FRC Assistant is a compliance-focused software project designed to streamline regulatory data ingestion, retrieval, and evaluation for financial organizations. It supports integration with RBI, SEBI, and other policy sources, leveraging modern SDLC best practices for security, performance, and maintainability. 
It's a RAG-based application integrates information retrieval (using vector databases like ChromaDB) with large language models (LLMs) to generate accurate, context-aware responses. This approach ensures that answers are grounded in your organization’s data, improving reliability and traceability—especially important for compliance and regulatory use cases

---

## Features

- **Automated Data Ingestion:** Structured pipelines for RBI, SEBI, and custom policy sources.
- **Vector Search & Retrieval:** Efficient document retrieval using vector databases.
- **LLM Service Integration:** Advanced language model chains for compliance Q&A.
- **Extensible API Layer:** Modular endpoints for compliance checks and evaluation.
- **Robust Testing:** Comprehensive test suite for all modules.

---

## Directory Structure
FRC_Assistant/
├── app/
│   ├── api/
│   └── models/
├── chroma_db/
├── core/
├── data/
│   ├── evaluation/
│   ├── policies/
│   ├── rbi/
│   └── sebi/
├── frontend/
├── scripts/
├── src/
│   ├── chains/
│   ├── compliance/
│   ├── ingestion/
│   ├── llmservice/
│   ├── retrieval/
│   ├── utils/
│   └── vectorstore/
├── tests/

---

### Prerequisites

- **Python 3.9+** (or as specified in your environment)
- **ChromaDB** for vector storage
- Other dependencies as specified in `requirements.txt` (if present)

### Installation

1. **Clone the repository:**
    ```bash
    git clone <repo-url>
    cd FRC_Assistant
    ```

2. **Set up a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**
    - Create a `.env` file in the root directory.
    - Add required secrets and configuration (see below).

---
