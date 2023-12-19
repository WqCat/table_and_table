"""
@Time: 2023/11/30 10:56
@Author: WQ
@File: Base_class.py
@Des:
"""
from typing import Any

from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

Base: Any = declarative_base()

metadata_obj = MetaData()
