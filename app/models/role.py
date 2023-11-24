"""
@Time: 2023/11/21 16:29
@Author: WQ
@File: role.py
@Des:
"""

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.db.base import Base


class Role(Base):
    __tablename__ = 'role'
    id: Mapped[int] = mapped_column(primary_key=True)
    parents_id: Mapped[int] = mapped_column(nullable=True)
    code: Mapped[str] = mapped_column(String(256), nullable=True)
    name: Mapped[str] = mapped_column(String(256), nullable=True)
    permissions: Mapped[list['Permission']] = relationship(
        secondary='role_permission', back_populates='roles'
    )
    users: Mapped[list['User']] = relationship(
        secondary='role_user', back_populates='roles'
    )
    user_groups: Mapped[list['UserGroup']] = relationship(
        secondary='user_group_role', back_populates='roles'
    )


