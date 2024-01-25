from pydantic import BaseModel


class TotalInfo(BaseModel):
    price: float
    price_change: float
    total_h24_volume: float
    total_h24_volume_quote: float
    total_h24_high: float
    total_h24_low: float
    total_ath: float
    total_atl: float
