"""
@Time: 2023/12/13 10:51
@Author: WQ
@File: init_db.py
@Des:
"""
import asyncio

from king_of_Glory.db.base import Base
from session import async_engine
from king_of_Glory import model


async def async_main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    asyncio.run(async_main())








