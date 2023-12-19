"""
@Time: 2023/12/6 15:22
@Author: WQ
@File: upload.py
@Des:
"""
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import Mapped

from app.db.base import Base
from app.util.datetimeUtil import now


class Upload(Base):
    __tablename__ = "upload"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=now)

    content_type: Mapped[str] = Column(String, nullable=False)
    content_hash = Column(String, nullable=False, unique=True)

    has_thumbnail = Column(Boolean, nullable=False)

    # Only set for images
    blurhash = Column(String, nullable=True)
    width = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)

    @property
    def is_image(self) -> bool:
        return self.content_type.startswith("image")
