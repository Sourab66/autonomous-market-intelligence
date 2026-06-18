from app.llm import llm
from app.prompts.content_prompt import CONTENT_PROMPT
from app.schemas.content_schema import CampaignContent


def content_agent(state):
    print("Running Content Agent...")

    prompt = CONTENT_PROMPT.format(
        strategy=state["strategy"]
    )

    structured_llm = llm.with_structured_output(
        CampaignContent
    )

    response = structured_llm.invoke(prompt)

    return {
        "campaign_content": response.model_dump()
    }