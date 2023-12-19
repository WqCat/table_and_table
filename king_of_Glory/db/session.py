"""
@Time: 2023/12/13 10:51
@Author: WQ
@File: session.py
@Des:
"""
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

async_engine = create_async_engine(
    url="postgresql+asyncpg://postgres:wq123@localhost/king_hero", echo=True,
)

async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session

