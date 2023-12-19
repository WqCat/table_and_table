"""
@Time: 2023/11/30 10:49
@Author: WQ
@File: test_model.py
@Des:
"""
import asyncio

from Base_class import Base
from session import async_engine
from test_model import models



async def async_main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    asyncio.run(async_main())
