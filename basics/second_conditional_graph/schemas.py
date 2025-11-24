from typing import TypedDict, Literal


class PortfolioSchema(TypedDict):
    usd_amount: float
    total_usd: float
    currency_type: Literal["NPR", "INR"]
    total_amount: float
