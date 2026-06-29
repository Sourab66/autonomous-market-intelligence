from fastapi import FastAPI
import uuid

from app.graph.builder import graph
from app.content_only import content_graph
from app.schemas.api_schema import MarketRequest, CampaignRequest

app = FastAPI(
    title="Autonomous Market Intelligence API"
)


@app.get("/")
def home():

    return {
        "message": "API Running Successfully"
    }


@app.post("/market-analysis")
def market_analysis(request: MarketRequest):

    config = {
        "configurable": {
            "thread_id": str(uuid.uuid4())
        }
    }

    result = graph.invoke(
        {
            "industry": request.industry,
            "goal": request.goal
        },
        config=config
    )

    return result


@app.post("/campaign")
def generate_campaign(request: CampaignRequest):

    result = content_graph.invoke(
        {
            "strategy": request.strategy
        }
    )

    return result