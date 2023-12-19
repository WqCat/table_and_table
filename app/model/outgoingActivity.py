"""
@Time: 2023/12/6 15:15
@Author: WQ
@File: outgoingActivity.py
@Des:
"""
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.util.datetimeUtil import now

from outboxObject import OutboxObject
from inboxObject import InboxObject



class OutgoingActivity(Base):
    __tablename__ = "outgoing_activity"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=now)

    recipient = Column(String, nullable=False)

    outbox_object_id = Column(Integer, ForeignKey("outbox.id"), nullable=True)
    outbox_object = relationship(OutboxObject, uselist=False)

    # Can also reference an inbox object if it needds to be forwarded
    inbox_object_id = Column(Integer, ForeignKey("inbox.id"), nullable=True)
    inbox_object = relationship(InboxObject, uselist=False)

    # The source will be the outbox object URL
    webmention_target = Column(String, nullable=True)

    tries = Column(Integer, nullable=False, default=0)
    next_try = Column(DateTime(timezone=True), nullable=True, default=now)

    last_try = Column(DateTime(timezone=True), nullable=True)
    last_status_code = Column(Integer, nullable=True)
    last_response = Column(String, nullable=True)

    is_sent = Column(Boolean, nullable=False, default=False)
    is_errored = Column(Boolean, nullable=False, default=False)
    error = Column(String, nullable=True)

    @property
    def anybox_object(self) -> OutboxObject | InboxObject:
        if self.outbox_object_id:
            return self.outbox_object  # type: ignore
        elif self.inbox_object_id:
            return self.inbox_object  # type: ignore
        else:
            raise ValueError("Should never happen")
