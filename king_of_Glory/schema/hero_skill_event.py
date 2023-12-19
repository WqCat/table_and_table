"""
@Time: 2023/12/13 19:16
@Author: WQ
@File: hero_skill_event.py
@Des:
"""
from pydantic import BaseModel


class HeroSkillEvent(BaseModel):
    name: str
    class Config:
        orm_mode = True
