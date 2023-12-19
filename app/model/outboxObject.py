"""
@Time: 2023/12/6 15:11
@Author: WQ
@File: outboxObject.py
@Des:
"""
from enum import Enum
from typing import Any, Optional, Union

from sqlalchemy import Column, Integer, String, DateTime, Boolean, JSON, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from app.core import acticitypub as ap
from app.db.base import Base
from app.db.baseObject import BaseObject
from app.util.datetimeUtil import now


class OutboxObject(Base, BaseObject):
    __tablename__ = "outbox"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=now)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=now)

    is_hidden_from_homepage = Column(Boolean, nullable=False, default=False)

    public_id = Column(String, nullable=False, index=True)
    slug = Column(String, nullable=True, index=True)

    ap_type = Column(String, nullable=False, index=True)
    ap_id: Mapped[str] = Column(String, nullable=False, unique=True, index=True)
    ap_context = Column(String, nullable=True)
    ap_object: Mapped[ap.RawObject] = Column(JSON, nullable=False)

    activity_object_ap_id = Column(String, nullable=True, index=True)

    # Source content for activities (like Notes)
    source = Column(String, nullable=True)
    revisions: Mapped[list[dict[str, Any]] | None] = Column(JSON, nullable=True)

    ap_published_at = Column(DateTime(timezone=True), nullable=False, default=now)
    visibility = Column(Enum(ap.VisibilityEnum), nullable=False)
    conversation = Column(String, nullable=True)

    likes_count = Column(Integer, nullable=False, default=0)
    announces_count = Column(Integer, nullable=False, default=0)
    replies_count: Mapped[int] = Column(Integer, nullable=False, default=0)
    webmentions_count: Mapped[int] = Column(
        Integer, nullable=False, default=0, server_default="0"
    )
    # reactions: Mapped[list[dict[str, Any]] | None] = Column(JSON, nullable=True)

    og_meta: Mapped[list[dict[str, Any]] | None] = Column(JSON, nullable=True)

    # For the featured collection
    is_pinned = Column(Boolean, nullable=False, default=False)
    is_transient = Column(Boolean, nullable=False, default=False, server_default="0")

    # Never actually delete from the outbox
    is_deleted = Column(Boolean, nullable=False, default=False)
    # Used for Create, Like, Announce and Undo activities
    relates_to_inbox_object_id = Column(
        Integer,
        ForeignKey("inbox.id"),
        nullable=True,
    )
    relates_to_inbox_object: Mapped[Optional["InboxObject"]] = relationship(
        "InboxObject",
        foreign_keys=[relates_to_inbox_object_id],
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
        remote_side=id,
        uselist=False,
    )
    # For Follow activies
    relates_to_actor_id = Column(
        Integer,
        ForeignKey("actor.id"),
        nullable=True,
    )
    relates_to_actor: Mapped[Optional["Actor"]] = relationship(
        "Actor",
        foreign_keys=[relates_to_actor_id],
        uselist=False,
    )

    undone_by_outbox_object_id = Column(Integer, ForeignKey("outbox.id"), nullable=True)

    # @property
    # def actor(self) -> BaseActor:
    #     return LOCAL_ACTOR

    outbox_object_attachments: Mapped[list["OutboxObjectAttachment"]] = relationship(
        "OutboxObjectAttachment", uselist=True, backref="outbox_object"
    )

    # @property
    # def attachments(self) -> list[Attachment]:
    #     out = []
    #     for attachment in self.outbox_object_attachments:
    #         url = (
    #                 BASE_URL
    #                 + f"/attachments/{attachment.upload.content_hash}/{attachment.filename}"
    #         )
    #         out.append(
    #             Attachment.parse_obj(
    #                 {
    #                     "type": "Document",
    #                     "mediaType": attachment.upload.content_type,
    #                     "name": attachment.alt or attachment.filename,
    #                     "url": url,
    #                     "width": attachment.upload.width,
    #                     "height": attachment.upload.height,
    #                     "proxiedUrl": url,
    #                     "resizedUrl": BASE_URL
    #                                   + (
    #                                       "/attachments/thumbnails/"
    #                                       f"{attachment.upload.content_hash}"
    #                                       f"/{attachment.filename}"
    #                                   )
    #                     if attachment.upload.has_thumbnail
    #                     else None,
    #                 }
    #             )
    #         )
    #     return out

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
    def is_from_outbox(self) -> bool:
        return True

    # @property
    # def url(self) -> str | None:
    #     # XXX: rewrite old URL here for compat
    #     if self.ap_type == "Article" and self.slug and self.public_id:
    #         return f"{BASE_URL}/articles/{self.public_id[:7]}/{self.slug}"
    #     return super().url
