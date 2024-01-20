from core.http_async import HttpAsync
from schemas.mexc import PairInfo


class MEXC(HttpAsync):
    def __init__(self) -> None:
        super().__init__(base_url="https://api.mexc.com")

    async def ticker_24h(self, pair: str = "DRAGOUSDT") -> PairInfo:
        raw_ticker_24h = await self.request(
            method="GET",
            endpoint=f"api/v3/ticker/24hr/",
            params={"symbol": pair.upper()},
        )
        if raw_ticker_24h.status_code == 200:
            ticker_24h = raw_ticker_24h.response
            return PairInfo(
                symbol=ticker_24h.get("symbol"),
                price_change=float(ticker_24h.get("priceChange")),
                price_change_percent=float(ticker_24h.get("priceChangePercent")),
                prev_close_price=float(ticker_24h.get("prevClosePrice")),
                last_price=float(ticker_24h.get("lastPrice")),
                bid_price=float(ticker_24h.get("bidPrice")),
                bid_qty=float(ticker_24h.get("bidQty")),
                ask_price=float(ticker_24h.get("askPrice")),
                ask_qty=float(ticker_24h.get("askQty")),
                open_price=float(ticker_24h.get("openPrice")),
                high_price=float(ticker_24h.get("highPrice")),
                low_price=float(ticker_24h.get("lowPrice")),
                volume=float(ticker_24h.get("volume")),
                quote_volume=float(ticker_24h.get("quoteVolume")),
                open_time=ticker_24h.get("openTime"),
                close_time=ticker_24h.get("closeTime"),
                count=ticker_24h.get("count"),
            )
