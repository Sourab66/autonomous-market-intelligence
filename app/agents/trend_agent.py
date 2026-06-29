from app.llm import llm
from app.tools.tavily_tool import search_market
from app.utils.llm_metrics import invoke_with_metrics


def trend_agent(state):

    print("Running Trend Agent...")

    research = search_market(
        f"""
        Latest trends in
        {state['industry']}
        industry
        """
    )

    prompt = f"""
You are a Senior Industry Trend Analyst.

Industry

{state['industry']}

Latest Research Summary

{research["answer"]}

Research Sources

{research["sources"]}

Identify the five most important trends currently shaping this industry.

For every trend include:

Trend Name

Why it matters (2-3 lines)

Business Impact (2-3 lines)

Only use evidence from the supplied research.

Avoid generic business advice.

Write like a professional market analyst.
"""

    result = invoke_with_metrics(
        llm,
        prompt
    )

    response = result["response"]

    return {

        "trend_report": response.content,

        "trend_sources": research["sources"],

        "trend_timestamp": research["timestamp"],

        "trend_execution_time": result["execution_time"],

        "trend_tokens": result["tokens"],

        "trend_cost": result["cost"]

    }