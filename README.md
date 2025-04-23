# AI Agent-Based Deep Research

This project implements a dual-agent research assistant using LangChain, Tavily, and LangGraph. It demonstrates an AI workflow where one agent performs web research and another generates a summarized draft.

## Features
- 🔍 **Tavily Integration**: Uses Tavily for real-time search results.
- 🧠 **Dual-Agent System**: LangGraph ResearchAgent → WriterAgent.
- 🌐 **Web App**: Simple Streamlit frontend for input/output.

## How to Run

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Set API Key
```bash
export TAVILY_API_KEY=your_key_here
```

### 3. Launch Streamlit App
```bash
streamlit run app.py
```
