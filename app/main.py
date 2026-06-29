import time
import uuid

from app.graph.builder import graph

start = time.time()

config = {
    "configurable": {
        "thread_id": str(uuid.uuid4())
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