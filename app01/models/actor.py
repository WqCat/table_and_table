"""
@Time: 2023/12/6 14:41
@Author: WQ
@File: actor.py
@Des:
"""
from sqlalchemy import Column, Integer, String, DateTime, Boolean, JSON
from sqlalchemy.orm import Mapped

from app.core import acticitypub as ap
from app.db.base import Base
from app.util.datetimeUtil import now

from app.db.baseActor import BaseActor


class Actor(Base, BaseActor):
    __tablename__ = "actor"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=now)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=now)

    ap_id: Mapped[str] = Column(String, unique=True, nullable=False, index=True)
    ap_actor: Mapped[ap.RawObject] = Column(JSON, nullable=False)
    ap_type = Column(String, nullable=False)

    handle = Column(String, nullable=True, index=True)

    is_blocked = Column(Boolean, nullable=False, default=False, server_default="0")
    is_deleted = Column(Boolean, nullable=False, default=False, server_default="0")

    are_announces_hidden_from_stream = Column(
        Boolean, nullable=False, default=False, server_default="0"
    )

    @property
    def is_from_db(self) -> bool:
        return True
