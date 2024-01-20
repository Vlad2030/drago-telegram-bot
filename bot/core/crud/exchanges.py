from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from models.exchanges_info import ExchangesInfoDatabase
from schemas.exchange_info import ExchangesInfo


class ExchangesInfoCRUD:
    def __init__(self, session: AsyncSession) -> None:
        self.session: AsyncSession = session


    async def get_all(self) -> list[ExchangesInfoDatabase]:
        query = select(ExchangesInfoDatabase)
        result = await self.session.execute(query)

        return result.scalars().all()


    async def get_one_by_exchange_name(
            self,
            exchange_name: str,
    ) -> ExchangesInfoDatabase | None:
        query = (select(ExchangesInfoDatabase)
                 .where(ExchangesInfoDatabase.name == exchange_name))
        result = await self.session.execute(query)

        return result.scalars().one_or_none()


    async def update(
            self,
            exchange: ExchangesInfo,
    ) -> bool:
        _exchange = await self.get_one_by_exchange_name(exchange.name)

        if _exchange is None:
            return False

        exchange_dict = exchange.model_dump()

        query = (update(ExchangesInfoDatabase)
                 .where(ExchangesInfoDatabase.name == exchange.name)
                 .values(**exchange_dict))

        result = await self.session.execute(query)

        await self.session.commit()

        return True if result else False
