from app.llm import llm

def trend_agent(state):

    print("Running Trend Agent...")

    prompt = f"""
    Find latest trends in:

    Industry: {state['industry']}

    Return top 5 trends.
    """

    response = llm.invoke(prompt)

    return {
        "trend_report": response.content
    }