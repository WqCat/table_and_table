"""
@Time: 2023/12/13 18:44
@Author: WQ
@File: skill.py
@Des:
"""
from typing import List

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped

from king_of_Glory.db.base import Base
from king_of_Glory.model.hero_skill import HeroSkillLink


class Skill(Base):
    __tablename__ ='skill'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    level = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    heros= relationship("Hero", secondary="hero_skill_link", overlaps="skills")




