from app.llm import llm
from app.prompts.market_prompt import MARKET_PROMPT
from app.schemas.market_schema import MarketReport
from app.tools.tavily_tool import search_market
from app.utils.llm_metrics import invoke_with_metrics


def market_agent(state):

    print("Running Market Agent...")

    research = search_market(
        f"""
        {state['industry']} market trends,
        opportunities,
        risks,
        latest industry news,
        market growth
        """
    )

    prompt = MARKET_PROMPT.format(

        industry=state["industry"],

        goal=state["goal"],

        search_results=research["answer"],

        sources=research["sources"]

    )

    result = invoke_with_metrics(
        llm.with_structured_output(MarketReport),
        prompt
    )

    response = result["response"]

    return {

        "market_report": response.model_dump(),

        "market_sources": research["sources"],

        "market_timestamp": research["timestamp"],

        "market_execution_time": result["execution_time"],

        "market_tokens": result["tokens"],

        "market_cost": result["cost"]

    }