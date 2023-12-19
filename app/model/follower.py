"""
@Time: 2023/12/6 15:13
@Author: WQ
@File: follower.py
@Des:
"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, relationship

from actor import Actor
from app.db.base import Base
from app.util.datetimeUtil import now
from inboxObject import InboxObject

class Follower(Base):
    __tablename__ = "follower"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=now)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=now)

    actor_id = Column(Integer, ForeignKey("actor.id"), nullable=False, unique=True)
    actor: Mapped[Actor] = relationship(Actor, uselist=False)

    inbox_object_id = Column(Integer, ForeignKey("inbox.id"), nullable=False)
    inbox_object = relationship(InboxObject, uselist=False)

    ap_actor_id = Column(String, nullable=False, unique=True)
