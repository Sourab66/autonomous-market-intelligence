from fastapi import FastAPI

from app.graph.builder import graph

app = FastAPI(
    title="Autonomous Market Intelligence API"
)


@app.get("/")
def home():

    return {
        "message": "API Running"
    }


@app.post("/generate")
def generate_strategy(
    industry: str,
    goal: str
):

    config = {
        "configurable": {
            "thread_id": "api_user"
        }
    }

    result = graph.invoke(
        {
            "industry": industry,
            "goal": goal
        },
        config=config
    )

    return result