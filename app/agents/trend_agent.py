from app.llm import llm
from app.tools.tavily_tool import search_market


def trend_agent(state):

    print("Running Trend Agent...")

    search_results = search_market(
        f"latest trends in {state['industry']} industry 2025"
    )

    prompt = f"""
    You are an industry research analyst.

    Industry:
    {state['industry']}

    Latest Industry Research:
    {search_results}

    Analyze the research and identify the 5 most important trends.

    For each trend provide:

    1. Trend Name
    2. Why it matters
    3. Business impact

    Use evidence from the research.

    Avoid generic statements.

    Return a professional trend analysis report.
    """

    response = llm.invoke(prompt)

    return {
        "trend_report": response.content
    }
