from data.config import DatabaseConfig
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import (AsyncEngine, AsyncSession,
                                    create_async_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = (f"postgresql+asyncpg://"
                f"{DatabaseConfig.DATABASE_USER}:{DatabaseConfig.DATABASE_PASSWORD}"
                f"@{DatabaseConfig.DATABASE_HOST}:{DatabaseConfig.DATABASE_PORT}"
                f"/{DatabaseConfig.DATABASE_DB}")

Base = declarative_base()
metadata = MetaData()
engine = create_async_engine(url=DATABASE_URL, echo=False)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def async_create_all() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session
