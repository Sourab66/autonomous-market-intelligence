from app.llm import llm
from app.prompts.competitor_prompt import COMPETITOR_PROMPT
from app.schemas.competitor_schema import CompetitorReport
from app.tools.tavily_tool import search_market
from app.utils.llm_metrics import invoke_with_metrics


def competitor_agent(state):

    print("Running Competitor Agent...")

    research = search_market(
        f"""
        Top competitors in {state['industry']},
        company websites,
        pricing,
        product comparison
        """
    )

    prompt = COMPETITOR_PROMPT.format(

        market_report=state["market_report"],

        competitor_search_results=research["answer"],

        sources=research["sources"]

    )

    result = invoke_with_metrics(
        llm.with_structured_output(CompetitorReport),
        prompt
    )

    response = result["response"]

    return {

        "competitor_report": response.model_dump(),

        "competitor_sources": research["sources"],

        "competitor_timestamp": research["timestamp"],

        "competitor_execution_time": result["execution_time"],

        "competitor_tokens": result["tokens"],

        "competitor_cost": result["cost"]

    }