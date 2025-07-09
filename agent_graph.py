from typing import TypedDict, Annotated
from langgraph.graph import StateGraph
from langchain_ollama import OllamaLLM
import asyncio

# Define the Graph State
class GraphState(TypedDict):
    input: Annotated[str, "state:single"]
    output: Annotated[str, "state:single"]

# Initialize the LLM
llm = OllamaLLM(model="mistral")

# Router Node
async def router_node(state: GraphState):
    prompt = state["input"]
    if "summarize" in prompt.lower():
        return {"next": "summarizer"}
    elif any(op in prompt for op in ["+", "-", "*", "/"]):
        return {"next": "math"}
    return {"next": "fallback"}

# Math Node
async def math_node(state: GraphState):
    prompt = state["input"]
    try:
        result = eval(prompt)
        return {"output": f"Math Result: {result}"}
    except Exception as e:
        return {"output": f"Error: {str(e)}"}

# Summarizer Node
async def summary_node(state: GraphState):
    prompt = state["input"]
    response = await llm.ainvoke(f"Summarize this: {prompt}")
    return {"output": f"Summary: {response}"}

# Fallback Node
async def fallback_node(state: GraphState):
    return {"output": "Unsupported command. Try math or summarize."}

# Printer Node
async def printer_node(state: GraphState):
    print("Final Output:", state["output"])
    return state

# Build the Agent Graph
def build_agent_graph():
    graph = StateGraph(GraphState)

    graph.add_node("router", router_node)
    graph.add_node("math", math_node)
    graph.add_node("summarizer", summary_node)
    graph.add_node("fallback", fallback_node)
    graph.add_node("final", printer_node)

    graph.set_entry_point("router")
    graph.add_edge("router", "math")
    graph.add_edge("router", "summarizer")
    graph.add_edge("router", "fallback")
    graph.add_edge("math", "final")
    graph.add_edge("summarizer", "final")
    graph.add_edge("fallback", "final")

    return graph.compile()

# Run the Agent
def run_agent():
    app = build_agent_graph()

    async def run_all_tests():
        print("--- Summary Test ---")
        await app.ainvoke({"input": "summarize: LangGraph is a graph-based LLM orchestrator."})
        print("--- Math Test ---")
        await app.ainvoke({"input": "15 * 7 - 3"})
        print("--- Fallback Test ---")
        await app.ainvoke({"input": "translate this to French"})

    asyncio.run(run_all_tests())

if __name__ == "__main__":
    run_agent()
