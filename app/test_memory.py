from app.graph.builder import graph

config = {
    "configurable": {
        "thread_id": "user_1"
    }
}

# First run
graph.invoke(
    {
        "industry": "AI SaaS",
        "goal": "Increase Signups"
    },
    config=config
)

# Retrieve saved memory
state = graph.get_state(config)

print("\nMEMORY:\n")
print(state.values)