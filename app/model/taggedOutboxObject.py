"""
@Time: 2023/12/6 15:21
@Author: WQ
@File: taggedOutboxObject.py
@Des:
"""
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.base import Base
from outboxObject import OutboxObject


class TaggedOutboxObject(Base):
    __tablename__ = "tagged_outbox_object"
    __table_args__ = (
        UniqueConstraint("outbox_object_id", "tag", name="uix_tagged_object"),
    )

    id = Column(Integer, primary_key=True, index=True)

    outbox_object_id = Column(Integer, ForeignKey("outbox.id"), nullable=False)
    outbox_object = relationship(OutboxObject, uselist=False)

    tag = Column(String, nullable=False, index=True)
