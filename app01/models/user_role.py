"""
@Time: 2023/11/21 16:38
@Author: WQ
@File: user_role.py
@Des:
"""
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app01.db.base import Base


class UserRole(Base):
    __tablename__ = 'user_role'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=True)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('role.id'), nullable=True)




