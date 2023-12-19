"""
@Time: 2023/11/21 16:43
@Author: WQ
@File: permission.py
@Des:
"""

from app01.db.base import Base
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Permission(Base):
    __tablename__ = 'permission'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    parent_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String(100))
    roles: Mapped[list['Role']] = relationship(
        secondary='role_permission', back_populates='permissions'
    )

