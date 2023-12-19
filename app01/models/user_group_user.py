"""
@Time: 2023/11/23 17:11
@Author: WQ
@File: user_group_user.py
@Des:
"""
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app01.db.base import Base


class UserGroupUser(Base):
    __tablename__ = 'user_group_user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), index=True, nullable=True)
    user_group_id: Mapped[int] = mapped_column(Integer, ForeignKey('user_group.id'), index=True, nullable=True)
