"""
@Time: 2023/11/24 14:39
@Author: WQ
@File: laji_test.py
@Des:
"""
from typing import Optional, List

from sqlalchemy import Integer, ForeignKey, Column
from sqlalchemy.orm import Mapped, relationship

from app.db.base import Base


class InboxObject(Base):
    __tablename__ = "inbox"

    id = Column(Integer, primary_key=True, index=True)
    relates_to_inbox_object_id = Column(
        Integer,
        ForeignKey("inbox.id"),
        nullable=True,
    )
    relates_to_inbox_object: Mapped[Optional[List["InboxObject"]]] = relationship(
        "InboxObject",
        foreign_keys=relates_to_inbox_object_id,
        remote_side=id,
        uselist=False,
    )

# 创建 InboxObject 对象
inbox_obj1 = InboxObject(id=1)
inbox_obj2 = InboxObject(id=2)
inbox_obj3 = InboxObject(id=3)
inbox_obj4 = InboxObject(id=4)
inbox_obj5 = InboxObject(id=5)
inbox_obj6 = InboxObject(id=6)

# 建立层级关系
inbox_obj2.relates_to_inbox_object = [inbox_obj1]
inbox_obj3.relates_to_inbox_object = [inbox_obj1]
inbox_obj4.relates_to_inbox_object = [inbox_obj2]
inbox_obj5.relates_to_inbox_object = [inbox_obj3]
inbox_obj6.relates_to_inbox_object = [inbox_obj4]

# 打印树状结构
def print_tree(obj, indent=0):
    print("  " * indent + f"InboxObject(id={obj.id})")
    if obj.relates_to_inbox_object:
        for child in obj.relates_to_inbox_object:
            print_tree(child, indent + 1)

print_tree(inbox_obj1)
