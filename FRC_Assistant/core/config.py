from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "FRC Assistant"
    VERSION: str = "1.0.0"
    
    LLM_PROVIDER: str = "CustomLLM" # COPILOT OR CustomLLM
    
    # Copilot
    MODEL: str = "gpt-5-mini"

    # Workflow LLM
    WORKFLOW_BASE_URL: str = ""
    WORKFLOW_TASK_ID: str = ""
    WORKFLOW_ID: str = ""
    WORKFLOW_PAT_TOKEN: str = ""

    class Config:
        env_file = ".env"


settings = Settings()