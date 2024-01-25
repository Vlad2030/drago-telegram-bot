from core.http_async import HttpAsync
from schemas.mexc import PairInfo


class MEXC(HttpAsync):
    def __init__(self) -> None:
        super().__init__(base_url="https://mexc.com")

    async def ticker(self, pair: str = "DRAGO_USDT") -> PairInfo:
        raw_ticker = await self.request(
            method="GET",
            endpoint="/api/platform/spot/market-v2/web/symbol/ticker",
            params={"symbol": pair.upper()},
        )
        if raw_ticker.status_code == 200:
            ticker: dict = raw_ticker.response.get("data")
            return PairInfo(
                price=float(ticker.get("c")),
                price_change_percent=float(ticker.get("r8")),
                high_price=float(ticker.get("h")),
                low_price=float(ticker.get("l")),
                volume=float(ticker.get("a")),
                quote_volume=float(ticker.get("q")),
            )
