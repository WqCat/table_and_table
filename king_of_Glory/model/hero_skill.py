"""
@Time: 2023/12/18 15:55
@Author: WQ
@File: hero_skill.py
@Des:
"""
from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship, Mapped

from king_of_Glory.db.base import Base
class HeroSkillLink(Base):
    __tablename__ = 'hero_skill_link'
    id = Column(Integer, primary_key=True)

    hero_id = Column(Integer, ForeignKey('hero.id'), primary_key=True)
    skill_id = Column(Integer, ForeignKey('skill.id'), primary_key=True)

