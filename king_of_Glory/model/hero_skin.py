"""
@Time: 2023/12/13 11:04
@Author: WQ
@File: hero_skin.py
@Des:
"""
from typing import Optional, List

from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from king_of_Glory.db.base import Base


class HeroSkin(Base):
    __tablename__ = 'hero_skin'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    hero_id = Column(Integer, ForeignKey('hero.id'), nullable=True)
    hero = relationship("Hero", back_populates='hero_skins')
