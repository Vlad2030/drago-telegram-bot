from pydantic import BaseModel


class ExchangesInfo(BaseModel):
    name: str
    link: str
    price: float
    price_change: float
    price_h24_high: float | None
    price_h24_low: float | None
    h24_volume: float | None
    h24_volume_quote: float | None
