import asyncio

from core.crud.exchanges import ExchangesInfoCRUD
from core.crud.total import TotalInfoCRUD
from core.data.config import BotConfig
from core.database import get_async_session
from core.dex_screnner import DexScrenner
from core.mexc import MEXC
from schemas.exchange_info import ExchangesInfo
from schemas.total_info import TotalInfo


async def update_prices() -> None:
    async_session = await get_async_session()
    exchanges_info = ExchangesInfoCRUD(async_session)
    total_info = TotalInfoCRUD(async_session)

    dex_screnner = DexScrenner()
    mexc = MEXC()

    while True:
        dex_screnner_info = await dex_screnner.tokens(BotConfig.DRAGO_CONTRACT_ADDRESS)

        dex_price = float(dex_screnner_info.pairs[0].priceUsd)
        dex_h24_volume = dex_screnner_info.pairs[0].volume.h24 / dex_price

        await exchanges_info.update(
            exchange=ExchangesInfo(
                name="DEX Screener",
                link="https://dexscreener.com/solana/gd6scpwtmhmcphzkza1a7jlncqer3tubny3jqshzl6v2",
                price=dex_price,
                price_change=dex_screnner_info.pairs[0].priceChange.h6,
                price_h24_high=None,
                price_h24_low=None,
                h24_volume=dex_h24_volume,
                h24_volume_quote=dex_screnner_info.pairs[0].volume.h24,
            ),
        )

        mexc_info = await mexc.ticker("DRAGO_USDT")
        price_change_percent = mexc_info.price_change_percent * 100

        await exchanges_info.update(
            exchange=ExchangesInfo(
                name="MEXC",
                link="https://www.mexc.com/exchange/DRAGO_USDT",
                price=mexc_info.price,
                price_change=price_change_percent,
                price_h24_high=mexc_info.high_price,
                price_h24_low=mexc_info.low_price,
                h24_volume=mexc_info.volume,
                h24_volume_quote=mexc_info.quote_volume,
            ),
        )

        total_h24_volume = dex_h24_volume + mexc_info.volume
        total_h24_volume_quote = dex_screnner_info.pairs[0].volume.h24 + mexc_info.quote_volume
        best_price = mexc_info.price if mexc_info.price > dex_price else dex_price
        worst_price = mexc_info.price if mexc_info.price < dex_price else dex_price

        total_info_old = await total_info.get()
        total_ath = best_price if best_price > total_info_old.total_ath else total_info_old.total_ath
        total_atl = worst_price if worst_price < total_info_old.total_atl else total_info_old.total_atl

        await total_info.update(
            total=TotalInfo(
                price=best_price,
                price_change=price_change_percent,
                total_h24_volume=total_h24_volume,
                total_h24_volume_quote=total_h24_volume_quote,
                total_h24_high=mexc_info.high_price,
                total_h24_low=mexc_info.low_price,
                total_ath=total_ath,
                total_atl=total_atl,
            )
        )

        await asyncio.sleep(0.20)
