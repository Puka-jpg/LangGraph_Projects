from settings import settings

from langchain_groq import ChatGroq
from agent.schemas import PlanSchema
from agent.prompts import agent_prompt
from langgraph.graph import StateGraph

llm = ChatGroq(model="openai/gpt-oss-20b", api_key=settings.GROQ_API_KEY)

user_prompt = "Create a Simple WEB Application"


def planner_agent(state: dict) -> dict:
    prompt = state["user_prompt"]
    response = llm.with_structured_output(PlanSchema).invoke(agent_prompt(prompt))
    return response


graph = StateGraph(dict)
graph.add_node("planner", planner_agent)
