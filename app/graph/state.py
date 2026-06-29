from typing import TypedDict


class AgentState(TypedDict):

    industry: str
    goal: str

    # Reports

    market_report: dict
    competitor_report: dict
    trend_report: str
    strategy: dict
    campaign_content: dict

    # Sources

    market_sources: list
    competitor_sources: list
    trend_sources: list

    # Timestamps

    market_timestamp: str
    competitor_timestamp: str
    trend_timestamp: str

    # Execution Time

    market_execution_time: float
    trend_execution_time: float
    competitor_execution_time: float
    strategy_execution_time: float
    content_execution_time: float

    # Tokens

    market_tokens: dict
    trend_tokens: dict
    competitor_tokens: dict
    strategy_tokens: dict
    content_tokens: dict

    # Cost

    market_cost: float
    trend_cost: float
    competitor_cost: float
    strategy_cost: float
    content_cost: float

    approved: bool