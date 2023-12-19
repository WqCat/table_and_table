"""
@Time: 2023/11/21 17:13
@Author: WQ
@File: role_permission.py
@Des:
"""
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app01.db.base import Base


class RolePermission(Base):
    __tablename__ = 'role_permission'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('role.id'), nullable=True)
    permission_id: Mapped[int] = mapped_column(Integer, ForeignKey('permission.id'), nullable=True)
