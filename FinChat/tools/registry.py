from tools.sql_tool import SQLTool
from tools.analytics_tool import AnalyticsTool
from tools.rag_tool import RAGTool
from tools.recommendation_tool import RecommendationTool

TOOL_REGISTRY = {
    "sql_tool": {
        "instance": SQLTool(),
        "requires": []
    },
    "analytics_tool": {
        "instance": AnalyticsTool(),
        "requires": ["sql_tool"]
    },
    "recommendation_tool": {
        "instance": RecommendationTool(),
        "requires": ["analytics_tool"]
    },
    "rag_tool": RAGTool(),
}