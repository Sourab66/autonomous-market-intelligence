from langgraph.graph import StateGraph
from langgraph.graph import START, END

from app.graph.state import AgentState
from app.agents.content_agent import content_agent

builder = StateGraph(AgentState)

builder.add_node(
    "content_agent",
    content_agent
)

builder.add_edge(
    START,
    "content_agent"
)

builder.add_edge(
    "content_agent",
    END
)

content_graph = builder.compile()