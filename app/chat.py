from app.graph.builder import graph

thread_id = "user_1"

while True:

    industry = input("Industry: ")
    goal = input("Goal: ")

    result = graph.invoke(
        {
            "industry": industry,
            "goal": goal
        },
        config={
            "configurable": {
                "thread_id": thread_id
            }
        }
    )

    print("\nFINAL OUTPUT:\n")
    print(result)

    again = input("\nRun again? (yes/no): ")

    if again.lower() != "yes":
        break