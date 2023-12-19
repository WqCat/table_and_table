"""
@Time: 2023/12/13 19:11
@Author: WQ
@File: hero_event.py
@Des:
"""
from pydantic import BaseModel


class CreateHeroEvent(BaseModel):
    name: str
    price: int
    level: int

    class Config:
        from_attributes = True


