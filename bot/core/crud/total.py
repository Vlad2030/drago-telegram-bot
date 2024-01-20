from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from models.total_info import TotalInfoDatabase
from schemas.total_info import TotalInfo


class TotalInfoCRUD:
    def __init__(self, session: AsyncSession) -> None:
        self.session: AsyncSession = session


    async def get(self) -> TotalInfoDatabase | None:
        query = select(TotalInfoDatabase)
        result = await self.session.execute(query)

        return result.scalars().one_or_none()


    async def update(
            self,
            total: TotalInfo,
    ) -> bool:
        total_dict = total.model_dump()

        query = update(TotalInfoDatabase).values(**total_dict)

        result = await self.session.execute(query)

        await self.session.commit()

        return True if result else False
