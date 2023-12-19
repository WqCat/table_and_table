"""
@Time: 2023/12/13 19:52
@Author: WQ
@File: api.py
@Des:
"""
from fastapi import APIRouter

from king_of_Glory.api.endpoints.operate.hero_view import hero_router

api_router = APIRouter()

api_router.include_router(hero_router, prefix="/hero", tags=["hero operate"])
