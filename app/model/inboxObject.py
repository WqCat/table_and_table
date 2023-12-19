"""
@Time: 2023/12/6 14:56
@Author: WQ
@File: inboxObject.py
@Des:
"""
from typing import Any, Optional, Union

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, JSON, Enum
from sqlalchemy.orm import Mapped, relationship

from app.core import acticitypub as ap

from app.db.base import Base
from app.db.baseObject import BaseObject
from app.util.datetimeUtil import now
from actor import Actor


class InboxObject(Base, BaseObject):
    __tablename__ = "inbox"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=now)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=now)

    actor_id = Column(Integer, ForeignKey("actor.id"), nullable=False)
    actor: Mapped[Actor] = relationship(Actor, uselist=False)
    # 使用uselist = False的情况适用于一对一或多对一的关系，其中一个对象只能与一个相关对象相关联。
    # 如果关系是一对多或多对多的，uselist默认为True，并且返回一个对象列表

    server = Column(String, nullable=False)

    is_hidden_from_stream = Column(Boolean, nullable=False, default=False)

    ap_actor_id = Column(String, nullable=False)
    ap_type = Column(String, nullable=False, index=True)
    ap_id: Mapped[str] = Column(String, nullable=False, unique=True, index=True)
    ap_context = Column(String, nullable=True)
    ap_published_at = Column(DateTime(timezone=True), nullable=False)
    ap_object: Mapped[ap.RawObject] = Column(JSON, nullable=False)

    # Only set for activities
    activity_object_ap_id = Column(String, nullable=True, index=True)

    visibility = Column(Enum(ap.VisibilityEnum), nullable=False)
    conversation = Column(String, nullable=True)

    has_local_mention = Column(
        Boolean, nullable=False, default=False, server_default="0"
    )

    # Used for Like, Announce and Undo activities
    relates_to_inbox_object_id = Column(
        Integer,
        ForeignKey("inbox.id"),
        nullable=True,
    )
    relates_to_inbox_object: Mapped[Optional["InboxObject"]] = relationship(
        "InboxObject",
        foreign_keys=relates_to_inbox_object_id,
        remote_side=id,  # 会使用 Employee 表的 id 字段与当前模型的关联字段进行匹配
        uselist=False,
    )
    relates_to_outbox_object_id = Column(
        Integer,
        ForeignKey("outbox.id"),
        nullable=True,
    )
    relates_to_outbox_object: Mapped[Optional["OutboxObject"]] = relationship(
        "OutboxObject",
        foreign_keys=[relates_to_outbox_object_id],
        uselist=False,
    )
    undone_by_inbox_object_id = Column(Integer, ForeignKey("inbox.id"), nullable=True)

    # Link the oubox AP ID to allow undo without any extra query
    liked_via_outbox_object_ap_id = Column(String, nullable=True)
    announced_via_outbox_object_ap_id = Column(String, nullable=True)
    voted_for_answers: Mapped[list[str] | None] = Column(JSON, nullable=True)

    is_bookmarked = Column(Boolean, nullable=False, default=False)

    # Used to mark deleted objects, but also activities that were undone
    is_deleted = Column(Boolean, nullable=False, default=False)
    is_transient = Column(Boolean, nullable=False, default=False, server_default="0")

    replies_count: Mapped[int] = Column(Integer, nullable=False, default=0)

    og_meta: Mapped[list[dict[str, Any]] | None] = Column(JSON, nullable=True)

    @property
    def relates_to_anybox_object(self) -> Union["InboxObject", "OutboxObject"] | None:
        if self.relates_to_inbox_object_id:
            return self.relates_to_inbox_object
        elif self.relates_to_outbox_object_id:
            return self.relates_to_outbox_object
        else:
            return None

    @property
    def is_from_db(self) -> bool:
        return True

    @property
    def is_from_inbox(self) -> bool:
        return True
