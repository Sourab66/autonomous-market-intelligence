from app.llm import llm
from app.prompts.strategy_prompt import STRATEGY_PROMPT
from app.schemas.strategy_schema import StrategyReport


def strategy_agent(state):

   

    print("Running Strategy Agent...")

  

    prompt = STRATEGY_PROMPT.format(
        market_report=state["market_report"],
        competitor_report=state["competitor_report"],
        trend_report=state["trend_report"]
    )

    structured_llm = llm.with_structured_output(
        StrategyReport
    )

    response = structured_llm.invoke(prompt)

    return {
        "strategy": response.model_dump()
    }