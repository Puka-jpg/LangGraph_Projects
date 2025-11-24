from basics.forth_toolcall.schemas import ChatState
from langchain_groq import ChatGroq
from settings import settings
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool


llm = ChatGroq(model="llama-3.1-8b-instant", api_key=settings.GROQ_API_KEY)


@tool
def weather_tool(city: str) -> str:
    """Return the current temperature of a city given the city name
    Args: city name
    Return: current temperature of the city
    """
    city = city.strip().lower()

    return {
        "kathmandu": "19 degree Celcius",
        "pokhara": "12 degree Celcius",
        "tanahun": "24 degree Celcius",
    }.get(city, f"No data for {city}")


tools = [weather_tool]
llm_with_tools = llm.bind_tools(tools)


def chatbot(state: ChatState) -> ChatState:
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


builder = StateGraph(ChatState)
builder.add_node("chatbot", chatbot)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "chatbot")
builder.add_conditional_edges("chatbot", tools_condition)
builder.add_edge("tools", "chatbot")
builder.add_edge("chatbot", END)

bot = builder.compile()
state = {
    "messages": [
        {
            "role": "user",
            "content": "What is current  temperature of both kathmandu and pokhara?",
        }
    ]
}
response = bot.invoke(state)
print(response["messages"][-1].content)
# print(response)
