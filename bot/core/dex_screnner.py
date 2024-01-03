from core.http_async import HttpAsync, ApiResponse
from schemas.dex_screnner import Tokens, Token


class DexScrenner(HttpAsync):
    def __init__(self) -> None:
        super().__init__(base_url="https://api.dexscreener.com")
        self.good_status_codes = [200, 304]

    async def tokens(self, ca: str) -> Tokens:
        raw_tokens = await self.request(
            method="GET",
            endpoint=f"/latest/dex/tokens/{ca}",
        )
        if raw_tokens.status_code in self.good_status_codes:
            token_list = []
            raw_pairs: list[dict] = raw_tokens.response.get("pairs")
            schema_version = raw_tokens.response.get("schemaVersion")
            if schema_version == "1.0.0":
                for pair in raw_pairs:
                    token_list.append(Token(**pair))
                return Tokens(
                    pairs=token_list,
                    schemaVersion=schema_version,
                )
