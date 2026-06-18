from typing import TypedDict

class AgentState(TypedDict):
    industry: str
    goal: str

    market_report: dict
    competitor_report: dict
    trend_report: str
    strategy: dict
    

    approved: bool

    campaign_content: dict