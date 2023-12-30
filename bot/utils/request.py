import orjson
import aiohttp
from core.data.config import BotConfig
from pydantic import BaseModel


class ApiResponse(BaseModel):
    response: dict
    status_code: int


async def request(
        method: str,
        endpoint: str,
        params: dict = None,
        json: dict = None,
) -> ApiResponse:
    async with aiohttp.ClientSession(
        base_url=f"http://{BotConfig.BACKEND_HOST}:{BotConfig.BACKEND_PORT}",
        json_serialize=lambda x: orjson.dumps(x).decode(),
    ) as _session:
        async with _session.request(
            method=method,
            url=endpoint,
            params=params,
            json=json,
        ) as _response:
            return ApiResponse(
                response=await _response.json(),
                status_code=_response.status
            )
