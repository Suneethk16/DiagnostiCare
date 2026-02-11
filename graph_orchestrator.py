from langgraph.graph import StateGraph, END
from schemas.graph_state import AgentState

from agents.document_agent import document_agent
from agents.reasoning_agent import reasoning_agent
from agents.action_agent import action_agent
from agents.safety_agent import safety_agent


# -------- Agent Nodes --------

def document_node(state: AgentState):
    document = document_agent(state["report_text"])
    return {"document": document}


def reasoning_node(state: AgentState):
    reasoning = reasoning_agent(state["document"])
    return {"reasoning": reasoning}


def action_node(state: AgentState):
    actions = action_agent(state["reasoning"])
    return {"actions": actions}


def safety_node(state: AgentState):
    safety = safety_agent(state["actions"])
    return {"safety": safety}


# -------- Build Graph --------

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("document", document_node)
    graph.add_node("reasoning", reasoning_node)
    graph.add_node("action", action_node)
    graph.add_node("safety", safety_node)

    graph.set_entry_point("document")

    graph.add_edge("document", "reasoning")
    graph.add_edge("reasoning", "action")
    graph.add_edge("action", "safety")
    graph.add_edge("safety", END)

    return graph.compile()
