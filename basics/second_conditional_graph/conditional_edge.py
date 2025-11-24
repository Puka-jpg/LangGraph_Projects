from basics.second_conditional_graph.schemas import PortfolioSchema
from langgraph.graph import StateGraph, START, END


def calc_total_usd(state: PortfolioSchema) -> PortfolioSchema:
    state["total_usd"] = state["usd_amount"] * 2
    return state


def choose_currency(state: PortfolioSchema) -> str:
    return state["currency_type"]


def convert_to_npr(state: PortfolioSchema) -> PortfolioSchema:
    state["total_amount"] = state["total_usd"] * 150
    return state


def convert_to_inr(state: PortfolioSchema) -> PortfolioSchema:
    state["total_amount"] = state["total_usd"] * 80
    return state


graph = StateGraph(PortfolioSchema)
graph.add_node(calc_total_usd, "total_usd")
graph.add_node(convert_to_inr, "convert_to_inr")
graph.add_node(convert_to_npr, "convert_to_npr")

graph.add_edge(START, "calc_total_usd")
graph.add_conditional_edges(
    "calc_total_usd",
    choose_currency,
    {"INR": "convert_to_inr", "NPR": "convert_to_npr"},
)
graph.add_edge("convert_to_inr", END)
graph.add_edge("convert_to_npr", END)

bot = graph.compile()
final_output = bot.invoke({"usd_amount": 1000, "currency_type": "INR"})
print(final_output)
