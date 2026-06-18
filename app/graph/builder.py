from langgraph.graph import StateGraph
from langgraph.graph import START, END

from app.graph.state import AgentState
from app.memory import memory

from app.agents.market_agent import market_agent
from app.agents.competitor_agent import competitor_agent
from app.agents.trend_agent import trend_agent
from app.agents.strategy_agent import strategy_agent
from app.agents.approval_agent import approval_agent
from app.agents.content_agent import content_agent

from app.graph.router import approval_router

builder = StateGraph(AgentState)

# Nodes
builder.add_node("market_agent", market_agent)
builder.add_node("competitor_agent", competitor_agent)
builder.add_node("trend_agent", trend_agent)
builder.add_node("strategy_agent", strategy_agent)
builder.add_node("approval_agent", approval_agent)
builder.add_node("content_agent", content_agent)

# Start
builder.add_edge(START, "market_agent")

# Parallel Branches
builder.add_edge(
    "market_agent",
    "competitor_agent"
)

builder.add_edge(
    "market_agent",
    "trend_agent"
)

# Join Point
builder.add_edge(
    "competitor_agent",
    "strategy_agent"
)

builder.add_edge(
    "trend_agent",
    "strategy_agent"
)

# Approval
builder.add_edge(
    "strategy_agent",
    END
)

builder.add_edge(
    "content_agent",
    END
)

graph = builder.compile(
    checkpointer=memory
)