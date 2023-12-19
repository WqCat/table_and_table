"""
@Time: 2023/11/21 15:54
@Author: WQ
@File: account.py
@Des:
"""

from sqlalchemy import Integer, ForeignKey, String, BigInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app01.db.base import Base


class Account(Base):
    __tablename__ = 'account'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=True)
    open_code: Mapped[str] = mapped_column(String(256), nullable=False)
    category: Mapped[int] = mapped_column(Integer, nullable=False)

    user: Mapped['User'] = relationship(back_populates='accounts')
