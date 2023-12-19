"""
@Time: 2023/12/13 19:54
@Author: WQ
@File: hero_view.py
@Des:
"""
from typing import List

from fastapi import APIRouter, Response, Query

from king_of_Glory.api.deps import AnnotatedSession
from king_of_Glory.crud.crud_hero import crud_add_hero, crud_get_hero_by_id, crud_update_hero_by_id, crud_page_hero, \
    crud_add_foreignId, crud_test, crud_relationship_hero_by_addhero, crud_del_hero_by_ids, \
    crud_relationship_hero_skin_id
from king_of_Glory.schema.hero_event import CreateHeroEvent

hero_router = APIRouter()


@hero_router.post("/addHero", summary=["添加hero"])
async def add_hero(session: AnnotatedSession, data: CreateHeroEvent, response: Response):
    hero = await crud_add_hero(session, data, response)
    return hero


@hero_router.get("/getHero/{id}", summary=["id获取hero"])
async def get_hero_by_id(session: AnnotatedSession, id: int):
    hero = await crud_get_hero_by_id(session, id)
    return hero


@hero_router.delete("/delHero/{id}", summary=["id删除hero"])
async def del_hero_by_id(session: AnnotatedSession, items: List[int]):
    await crud_del_hero_by_ids(session, items)
    return "删除成功"


@hero_router.put("/updateHero", summary=["更新hero"])
async def update_hero_by_id(session: AnnotatedSession, id: int, data: CreateHeroEvent):
    hero = await crud_update_hero_by_id(session, id, data)
    return hero


@hero_router.get("/pagehero", summary=["分页获取hero"])
async def page_eval(
        session: AnnotatedSession,
        page: int = Query(1, ge=1, description="页码"),
        page_size: int = Query(3, ge=1, description="每页条数"),
):
    hero = await crud_page_hero(session, page, page_size)
    return hero


# @hero_router.post("/addHeros", summary=["添加多个hero"])
# async def add_hero(session: AnnotatedSession, datas: List[CreateHeroEvent], response: Response):
#     hero = await crud_add_heros(session, datas, response)
#     return hero

@hero_router.post("/addForeignID", summary=["添加多个hero外键"])
async def add_foreign_id(session: AnnotatedSession, skinId: int, id: int):
    hero = await crud_add_foreignId(session, skinId, id)
    return hero

@hero_router.get("/curdTest", summary=["测试crud"])
async def test(session: AnnotatedSession, id: int):
    result = await crud_test(session, id)
    return result

@hero_router.post("/addHeroRelationship", summary=["增加自关系"])
async def add_hero_relationship(session: AnnotatedSession, idzhu: int, idci: int):
    hero = await crud_relationship_hero_by_addhero(session, idzhu, idci)
    return hero


@hero_router.post("/addHeroAndSkinRelationship", summary=["增加英雄和皮肤关系"])
async def add_hero_skin_relationship(session: AnnotatedSession, hero_id: int, skin_id: int):
    hero = await crud_relationship_hero_skin_id(session, hero_id, skin_id)
    return hero













