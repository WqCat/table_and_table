"""
@Time: 2023/12/6 15:14
@Author: WQ
@File: following.py
@Des:
"""
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from actor import Actor
from app.db.base import Base
from outboxObject import OutboxObject
from app.util.datetimeUtil import now


class Following(Base):
    __tablename__ = "following"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=now)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=now)

    actor_id = Column(Integer, ForeignKey("actor.id"), nullable=False, unique=True)
    actor = relationship(Actor, uselist=False)

    outbox_object_id = Column(Integer, ForeignKey("outbox.id"), nullable=False)
    outbox_object = relationship(OutboxObject, uselist=False)

    ap_actor_id = Column(String, nullable=False, unique=True)
