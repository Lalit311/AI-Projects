from pathlib import Path
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

DATABASE_PATH = BASE_DIR / "database" / "finance.db"

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "gemini-2.5-flash"
)

class Settings(BaseSettings):
    # Workflow LLM
    WORKFLOW_BASE_URL: str = ""
    WORKFLOW_TASK_ID: str = ""
    WORKFLOW_ID: str = ""
    WORKFLOW_PAT_TOKEN: str = ""
    
settings = Settings()
