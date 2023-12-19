"""
@Time: 2023/11/21 15:54
@Author: WQ
@File: user.py
@Des:
"""

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app01.db.base import Base


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    state: Mapped[int] = mapped_column(default=0)
    name: Mapped[str] = mapped_column(String(256), default='')
    mobile: Mapped[str] = mapped_column(String(12), default='')
    head_img_url: Mapped[str] = mapped_column(String(256), default='')

    roles: Mapped[list['Role']] = relationship(
        secondary='user_role', back_populates='users'
    )

    accounts: Mapped[list['Account']] = relationship(back_populates='user')

    user_groups: Mapped[list['UserGroup']] = relationship(
        secondary='user_group_user',back_populates='users'
    )
