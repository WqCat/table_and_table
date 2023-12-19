"""
@Time: 2023/12/13 19:23
@Author: WQ
@File: crud_hero.py
@Des:
"""
from http.client import HTTPException
from typing import List

from fastapi import Response, status
from sqlalchemy import select, delete, update
from sqlalchemy.orm import selectinload
from sqlalchemy.util import greenlet_spawn


from king_of_Glory.api.deps import AnnotatedSession
from king_of_Glory.model import Hero, HeroSkin
from king_of_Glory.schema.hero_event import CreateHeroEvent


async def crud_add_hero(session: AnnotatedSession, data: CreateHeroEvent, response: Response):
    data = data.model_dump()
    db_data = Hero(**data)
    session.add(db_data)
    response.status_code = status.HTTP_204_NO_CONTENT
    await session.commit()
    await session.refresh(db_data)
    return db_data


# async def crud_add_heros(session: AnnotatedSession, datas: List[CreateHeroEvent], response: Response):
#
#     datas = datas.model_dump()
#     db_data = Hero(**datas)
#     session.bulk_insert_mappings(Hero, db_data)
#     response.status_code = status.HTTP_204_NO_CONTENT
#     await session.commit()
#     await session.refresh(db_data)
#     return db_data


async def crud_get_hero_by_id(session: AnnotatedSession, id: int):
    stmt = select(Hero).where(Hero.id == id).options(
        selectinload(Hero.hero_skins)
    )

    result = await session.execute(stmt)
    print(f"这是一个{type(result)}")
    org = result.scalars().all()
    print(f"下面的这是一个{type(org)}")

    if org is None:
        return "没有该数据"  # 或者根据你的需求返回合适的默认值

    return org[0]  # 返回结果的第一个元素，即Hero对象

async def crud_del_hero_by_ids(session: AnnotatedSession, ids: List):
    for id in ids:
        stmt = delete(Hero).where(Hero.id == id)
        await session.execute(stmt)
    await session.commit()
    return "删除成功"





async def crud_get_hero_skin_by_id(session: AnnotatedSession, id: int):
    stmt = select(Hero).where(HeroSkin.id == id)

    result = await session.execute(stmt)
    org = result.first()  # 这个方法通常用于期望查询结果只有一行记录的情况，例如使用主键作为条件进行查询时
    return org


async def crud_def_hero_by_id(session: AnnotatedSession, items: List[int]):
    stmt = delete(Hero).where(Hero.id.in_(items))
    await session.execute(stmt)
    await session.commit()


async def crud_update_hero_by_id(session: AnnotatedSession, id: int, data: CreateHeroEvent):
    data = data.model_dump()
    stmt = (update(Hero).where(Hero.id == id).values(**data)).execution_options(synchronize_session="fetch")

    await session.execute(stmt)
    await session.commit()
    hero = await crud_get_hero_by_id(session, id)
    return hero


async def crud_relationship_hero_by_addhero(session: AnnotatedSession, idzhu: int, idci: int) -> None:
    herozhu = await session.get(Hero, idzhu)
    heroci = await session.get(Hero, idci)
    if heroci and herozhu:
        herozhu.relate_hero_object.append(heroci)
        await session.add([herozhu, heroci])
        await session.commit()
    await session.refresh(herozhu)
    return herozhu


async def crud_relationship_hero_skin_id(session: AnnotatedSession, hero_id: int, skin_id: int):
    # 获取Hero和HeroSkin实例
    hero = await session.execute(select(Hero).where(Hero.id == hero_id)).scalar_one()
    hero = hero.scalar_one()
    skin = await session.execute(select(HeroSkin).where(HeroSkin.id == skin_id))
    skin = skin.scalar_one()
    if not hero or not skin:
        raise HTTPException(status_code=404, detail="Hero或HeroSkin不存在")
    print(hero.__dict__)
    print(skin.__dict__)
    hero.hero_skins.append(skin)
    print(hero.__dict__)
    await session.add(hero)
    # 提交更改
    session.commit()

    return {"message": "成功添加hero_skins关系属性"}


    # hero = await session.get(Hero, hero_id)
    # print(f"英雄类型为{type(hero)}")
    # skin = await session.get(HeroSkin, skin_id)
    # print(f"类型为{type(skin)}")
    # if hero and skin:
    #     hero.hero_skins.append(skin)
    #     await session.add([hero, skin])
    #     await session.commit()
    # await session.refresh(hero)
    # return hero


async def crud_page_hero(session: AnnotatedSession, page: int, page_size: int):
    offset = (page - 1) * page_size
    stmt = select(Hero).offset(offset).limit(page_size)
    result = await session.execute(stmt)
    orgs = result.scalars().all()
    return orgs


async def crud_add_foreignId(session: AnnotatedSession, skinId: int, id: int):
    hero_stmt = select(Hero).where(Hero.id == id)
    hero = await session.execute(hero_stmt)
    hero = hero.scalar_one()

    heroSkin_stmt = select(HeroSkin).where(HeroSkin.id == skinId)
    heroSkin = await session.execute(heroSkin_stmt)
    heroSkin = heroSkin.scalar_one()

    if hero and heroSkin:
        heroSkin.hero_id = id
        heroSkin.hero.append(hero)
        hero.hero_skins.append(heroSkin)
        await session.commit()
        await session.refresh(heroSkin)
    return heroSkin


async def crud_test(session: AnnotatedSession, id: int):
    hero_stmt = select(HeroSkin).where(HeroSkin.id == id)
    hero_skin = await session.execute(hero_stmt)
    print(hero_skin)
    hero = hero_skin.hero.name
    print(hero)
    return "success"
