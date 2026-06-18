from app.llm import llm

response = llm.invoke(
    "Tell me 3 trends in AI SaaS."
)

print(response.content)