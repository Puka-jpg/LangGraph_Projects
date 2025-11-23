from langgraph.graph import StateGraph, START, END

from basics.first.schemas import PortfolioState


def calc_total(state: PortfolioState) -> PortfolioState:
    state["total_usd"] = state["amount_usd"] * 1.8
    return state


def convert_to_npr(state: PortfolioState) -> PortfolioState:
    state["total_npr"] = state["total_usd"] * 150
    return state


builder = StateGraph(PortfolioState)

builder.add_node(calc_total, "cal_total")
builder.add_node(convert_to_npr, "convert_to_npr")


builder.add_edge(START, "calc_total")
builder.add_edge("calc_total", "convert_to_npr")
builder.add_edge("convert_to_npr", END)

graph = builder.compile()

final_state = graph.invoke({"amount_usd": 1000})
print(final_state)
