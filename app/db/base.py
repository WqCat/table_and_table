"""
@Time: 2023/11/21 15:22
@Author: WQ
@File: base.py
@Des:
"""
from datetime import datetime, date

from sqlalchemy import MetaData, Integer, DateTime, func, String
from sqlalchemy.orm import DeclarativeBase, declared_attr, as_declarative, Mapped, mapped_column

# NAMING_CONVENTION = {
#     "ix": "%(column_0_label)s_idx",
#     "uq": "%(table_name)s_%(column_0_name)s_key",
#     "ck": "%(table_name)s_%(constraint_name)s_check",
#     "fk": "%(table_name)s_%(column_0_name)s_fkey",
#     "pk": "%(table_name)s_pkey",
# }
# metadata = MetaData(naming_convention=NAMING_CONVENTION, schema="public")



class Base(DeclarativeBase):
    NAMING_CONVENTION = {
        "ix": "%(column_0_label)s_idx",
        "uq": "%(table_name)s_%(column_0_name)s_key",
        "ck": "%(table_name)s_%(constraint_name)s_check",
        "fk": "%(table_name)s_%(column_0_name)s_fkey",
        "pk": "%(table_name)s_pkey",
    }
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    creator: Mapped[str] = mapped_column(String(36), nullable=True)
    edited: Mapped[date] = mapped_column(default=func.now(), onupdate=func.now())
    ediotor: Mapped[str] = mapped_column(String(36), nullable=True)
    deleted: Mapped[bool] = mapped_column(default=False)
