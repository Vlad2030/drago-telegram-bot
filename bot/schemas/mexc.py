from pydantic import BaseModel


class PairInfo(BaseModel):
    price: float
    price_change_percent: float
    high_price: float
    low_price: float
    volume: float
    quote_volume: float
