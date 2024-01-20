import asyncio

from core.tasks import update_prices

if __name__ == "__main__":
    asyncio.run(update_prices())
