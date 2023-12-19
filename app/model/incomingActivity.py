"""
@Time: 2023/12/6 15:14
@Author: WQ
@File: incomingActivity.py
@Des:
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean, JSON
from sqlalchemy.orm import Mapped

from app.core import acticitypub as ap
from app.db.base import Base
from app.util.datetimeUtil import now


class IncomingActivity(Base):
    __tablename__ = "incoming_activity"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=now)

    # An incoming activity can be a webmention
    webmention_source = Column(String, nullable=True)
    # or an AP object
    sent_by_ap_actor_id = Column(String, nullable=True)
    ap_id = Column(String, nullable=True, index=True)
    ap_object: Mapped[ap.RawObject] = Column(JSON, nullable=True)

    tries: Mapped[int] = Column(Integer, nullable=False, default=0)
    next_try = Column(DateTime(timezone=True), nullable=True, default=now)

    last_try = Column(DateTime(timezone=True), nullable=True)

    is_processed = Column(Boolean, nullable=False, default=False)
    is_errored = Column(Boolean, nullable=False, default=False)
    error = Column(String, nullable=True)
