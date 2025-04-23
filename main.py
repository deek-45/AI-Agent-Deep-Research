from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import tool
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from graphs.dual_agent_graph import ResearchAgent, WriterAgent
from typing import TypedDict, List

class GraphState(TypedDict):
    question: str
    research: List[str]
    draft: str

def build_graph(question):
    search = TavilySearchResults()
    tools = [search]

    initial_state = {
        "question": question,
        "research": [],
        "draft": ""
    }

    graph = StateGraph(GraphState)
    graph.add_node("research_agent", RunnableLambda(ResearchAgent(tools)))
    graph.add_node("writer_agent", RunnableLambda(WriterAgent()))
    graph.set_entry_point("research_agent")
    graph.add_edge("research_agent", "writer_agent")
    graph.add_edge("writer_agent", END)
    app = graph.compile()

    return app.invoke(initial_state)

if __name__ == "__main__":
    print("Running AI Agent Deep Research...")
    result = build_graph("What is the latest research on LLM Agents?")
    print("\nFinal Draft:")
    print(result["draft"])
