from pydantic import BaseModel


class PairInfo(BaseModel):
    symbol: str
    price_change: float
    price_change_percent: float
    prev_close_price: float
    last_price: float
    bid_price: float
    bid_qty: float
    ask_price: float
    ask_qty: float
    open_price: float
    high_price: float
    low_price: float
    volume: float
    quote_volume: float
    open_time: int
    close_time: int
    count: int | None
