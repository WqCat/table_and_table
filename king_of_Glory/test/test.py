"""
@Time: 2023/12/13 16:10
@Author: WQ
@File: test.py
@Des:
"""
import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from king_of_Glory.model import Hero, HeroSkin
from sqlalchemy import select


async def test():
    async_engine = create_async_engine(
        url="postgresql+asyncpg://postgres:wq123@localhost/king_hero", echo=True,
    )

    async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
    session = async_session()

    hero_stmt = select(HeroSkin).where(HeroSkin.id == 2)
    hero_skin = await session.execute(hero_stmt)
    print(hero_skin)
    hero = hero_skin.hero.name
    print(hero)
    return "success"

if __name__ == '__main__':
    asyncio.run(test())










