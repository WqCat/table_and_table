"""
@Time: 2023/11/21 15:45
@Author: WQ
@File: session.py
@Des:
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
# 异步
async_engine = create_async_engine(url="postgresql+asyncpg://postgres:wq123@127.0.0.1/test", echo=True)

async_session = sessionmaker(
    async_engine,
    class_=AsyncSession,
)


# 同步
sync_engine = create_engine(url="postgresql://postgres:wq123@127.0.0.1/auth_test", echo=True)
sync_session = sessionmaker(sync_engine)


async def get_db() -> AsyncSession:
    async with async_session() as session_:
        try:
            yield session_
        finally:
            await session_.close()




