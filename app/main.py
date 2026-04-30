from fastapi import FastAPI
from app.schemas import AnalyticsRequest
from app.agent import RetailAnalyticsAgent

app = FastAPI(title="Agentic Retail Analytics Copilot")

agent = RetailAnalyticsAgent()

@app.get("/")
def health_check():
    return {"status": "running"}

@app.post("/analyze")
def analyze(request: AnalyticsRequest):
    return agent.run(
        region=request.region,
        category=request.category
    )