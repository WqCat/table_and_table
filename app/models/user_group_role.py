"""
@Time: 2023/11/23 18:31
@Author: WQ
@File: user_group_role.py
@Des:
"""
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from app.db.base import Base


class UserGroupRole(Base):
    __tablename__ = 'user_group_role'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_group_id: Mapped[int] = mapped_column(ForeignKey('user_group.id'),index=True, nullable=True)
    role_id: Mapped[int] = mapped_column(ForeignKey('role.id'),index=True, nullable=True)
