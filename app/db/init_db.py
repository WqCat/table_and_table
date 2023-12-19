"""
@Time: 2023/12/6 16:48
@Author: WQ
@File: init_db.py
@Des:
"""
import asyncio

from app.db.base import Base
from app.db.session import async_engine
from app import model

async def async_main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(async_main())