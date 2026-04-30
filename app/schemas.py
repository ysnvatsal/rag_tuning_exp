from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class AnalyticsRequest(BaseModel):
    region: str
    category: str
    question: Optional[str] = None


class ToolResult(BaseModel):
    tool_name: str
    result: Dict[str, Any]


class AgentResponse(BaseModel):
    summary: str
    evidence: List[ToolResult]
    likely_cause: str
    recommended_action: str