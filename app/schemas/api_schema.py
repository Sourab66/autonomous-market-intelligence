from pydantic import BaseModel


class MarketRequest(BaseModel):
    industry: str
    goal: str


class CampaignRequest(BaseModel):
    strategy: dict