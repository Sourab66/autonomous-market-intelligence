from app.llm import llm
from app.prompts.competitor_prompt import COMPETITOR_PROMPT
from app.schemas.competitor_schema import CompetitorReport
from app.tools.tavily_tool import search_market


def competitor_agent(state):

    search_results = search_market(
        f"{state['industry']} top competitors pricing"
    )

    prompt = COMPETITOR_PROMPT.format(
        market_report=state["market_report"],
        competitor_search_results=search_results
    )

    structured_llm = llm.with_structured_output(
        CompetitorReport
    )

    response = structured_llm.invoke(prompt)

    return {
        "competitor_report": response.model_dump()
    }