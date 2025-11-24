from langchain_groq import ChatGroq
from langgraph.graph.message import add_messages
from basics.third_chatbot.schemas import ChatState
from langgraph.graph import StateGraph, START, END

from settings import settings


llm = ChatGroq(model="llama-3.1-8b-instant",api_key=settings.GROQ_API_KEY )

def chatbot(state: ChatState) -> ChatState:
    return {"messages":[llm.invoke(state["messages"])]}


builder = StateGraph(ChatState)
builder.add_node("chatbot_node", chatbot)

builder.add_edge(START, "chatbot_node")
builder.add_edge("chatbot_node",END)

bot = builder.compile()

