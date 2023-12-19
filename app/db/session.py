"""
@Time: 2023/11/30 10:49
@Author: WQ
@File: session.py
@Des:
"""
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

async_engine = create_async_engine(
    url="postgresql+asyncpg://postgres:wq123@127.0.0.1/model_sql", future=True, echo=True,  connect_args={"timeout": 15}
)
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)



