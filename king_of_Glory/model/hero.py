"""
@Time: 2023/12/13 11:01
@Author: WQ
@File: hero.py
@Des:
"""
from typing import Optional, List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from king_of_Glory.db.base import Base
from king_of_Glory.model.hero_skill import HeroSkillLink


class Hero(Base):
    __tablename__ = 'hero'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    level = Column(Integer, nullable=False)
    hero_skins = relationship("HeroSkin", back_populates="hero")
    skills = relationship("Skill", secondary="hero_skill_link", overlaps="heros")

    relate_hero_id = Column(
        Integer,
        ForeignKey("hero.id"),
        nullable=True
    )

    relate_hero_object: Mapped[Optional["Hero"]] = relationship(
        "Hero",
        foreign_keys=relate_hero_id,
        remote_side=id,
        uselist=True
    )




