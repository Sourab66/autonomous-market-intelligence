from app.llm import llm
from app.prompts.content_prompt import CONTENT_PROMPT
from app.schemas.content_schema import CampaignContent
from app.utils.llm_metrics import invoke_with_metrics


def content_agent(state):

    print("Running Content Agent...")

    prompt = CONTENT_PROMPT.format(

        strategy=state["strategy"]

    )

    result = invoke_with_metrics(

        llm.with_structured_output(
            CampaignContent
        ),

        prompt

    )

    response = result["response"]

    return {

        "campaign_content": response.model_dump(),

        "content_execution_time": result["execution_time"],

        "content_tokens": result["tokens"],

        "content_cost": result["cost"]

    }