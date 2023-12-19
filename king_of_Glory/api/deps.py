"""
@Time: 2023/12/13 19:51
@Author: WQ
@File: deps.py
@Des:
"""
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from king_of_Glory.db.session import get_db

AnnotatedSession = Annotated[AsyncSession, Depends(get_db)]
