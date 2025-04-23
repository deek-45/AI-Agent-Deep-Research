## File: graphs/dual_agent_graph.py

from langchain_core.agents import AgentFinish
from langchain_core.runnables import RunnableConfig
from langchain.agents import tool
from typing import List, Dict

class ResearchAgent:
    def __init__(self, tools):
        self.tools = tools

    def __call__(self, state):
        print("[ResearchAgent] Running research phase...")
        query = state["question"]
        results = self.tools[0].run(query)
        state["research"] = results
        return state

class WriterAgent:
    def __call__(self, state):
        print("[WriterAgent] Drafting output...")
        research_points: List[Dict] = state["research"]
        question = state["question"]

        draft = f" 📝 Question:\n{question}\n\n 📚 Research Summary:\n"
        for idx, point in enumerate(research_points, 1):
            draft += f"\n{idx}. [{point['title']}]({point['url']})\n\n{point['content'][:500]}...\n"

        state["draft"] = draft
        return state
