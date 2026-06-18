from app.llm import llm
from app.prompts.market_prompt import MARKET_PROMPT
from app.schemas.market_schema import MarketReport
from app.tools.tavily_tool import search_market


def market_agent(state):

    print("Running Market Agent...")

    search_results = search_market(
        f"{state['industry']} market trends competitors opportunities"
    )

    prompt = MARKET_PROMPT.format(
        industry=state["industry"],
        goal=state["goal"],
        search_results=search_results
    )

    structured_llm = llm.with_structured_output(
        MarketReport
    )

    response = structured_llm.invoke(prompt)

    return {
        "market_report": response.model_dump()
    }