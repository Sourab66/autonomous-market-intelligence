import time

from app.graph.builder import graph

start = time.time()

config = {
    "configurable": {
        "thread_id": "user_1"
    }
}

result = graph.invoke(
    {
        "industry": "AI SaaS",
        "goal": "Increase Signups"
    },
    config=config
)

end = time.time()

print(result)

print(
    f"\nExecution Time: {round(end-start,2)} seconds"
)