from app.llm import llm
from app.prompts.strategy_prompt import STRATEGY_PROMPT
from app.schemas.strategy_schema import StrategyReport
from app.utils.llm_metrics import invoke_with_metrics


def strategy_agent(state):

    print("Running Strategy Agent...")

    prompt = STRATEGY_PROMPT.format(

        market_report=state["market_report"],

        competitor_report=state["competitor_report"],

        trend_report=state["trend_report"]

    )

    result = invoke_with_metrics(

        llm.with_structured_output(
            StrategyReport
        ),

        prompt

    )

    response = result["response"]

    return {

        "strategy": response.model_dump(),

        "strategy_execution_time": result["execution_time"],

        "strategy_tokens": result["tokens"],

        "strategy_cost": result["cost"]

    }