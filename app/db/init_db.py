"""
@Time: 2023/11/21 15:43
@Author: WQ
@File: init_db.py
@Des:
"""
import asyncio

from app.db.base import Base
from app.db.session import async_engine, sync_session, sync_engine
from app import models


async def async_main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


def create_db_and_tables():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)


if __name__ == "__main__":
    asyncio.run(async_main())
