"""
@Time: 2023/11/23 17:08
@Author: WQ
@File: user_group.py
@Des:
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app01.db.base import Base


class UserGroup(Base):
    __tablename__ = 'user_group'
    id: Mapped[int] = mapped_column(primary_key=True)
    parents_id: Mapped[int] = mapped_column(index=True)
    code: Mapped[str] = mapped_column(index=True)
    name: Mapped[str] = mapped_column(String(255))

    users: Mapped[list['User']] = relationship(
        secondary='user_group_user', back_populates='user_groups'
    )

    roles: Mapped[list['UserGroup']] = relationship(
        secondary='user_group_role', back_populates='user_groups'
    )
