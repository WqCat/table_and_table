"""
@Time: 2023/12/6 14:18
@Author: WQ
@File: ap_object.py
@Des:
"""
from datetime import datetime
from functools import cached_property
from test_model import acticitypub as ap
from test_model.datetimeUtil import parse_isoformat
from bs4 import BeautifulSoup

class Object:
    @property
    def is_from_db(self) -> bool:
        return False

    @property
    def is_from_outbox(self) -> bool:
        return False

    @property
    def is_from_inbox(self) -> bool:
        return False

    @cached_property
    def ap_type(self) -> str:
        return ap.as_list(self.ap_object["type"])[0]

    @property
    def ap_object(self) -> ap.RawObject:
        raise NotImplementedError

    @property
    def ap_id(self) -> str:
        return ap.get_id(self.ap_object["id"])

    @property
    def ap_actor_id(self) -> str:
        return ap.get_actor_id(self.ap_object)

    @cached_property
    def ap_published_at(self) -> datetime | None:
        # TODO: default to None? or now()?
        if "published" in self.ap_object:
            return parse_isoformat(self.ap_object["published"])
        elif "created" in self.ap_object:
            return parse_isoformat(self.ap_object["created"])
        return None

    @property
    def actor(self) -> Actor:
        raise NotImplementedError()

    # @cached_property
    # def visibility(self) -> ap.VisibilityEnum:
    #     return ap.object_visibility(self.ap_object, self.actor)

    @property
    def ap_context(self) -> str | None:
        return self.ap_object.get("context") or self.ap_object.get("conversation")

    @property
    def sensitive(self) -> bool:
        return self.ap_object.get("sensitive", False)

    @property
    def tags(self) -> list[ap.RawObject]:
        return ap.as_list(self.ap_object.get("tag", []))

    @cached_property
    def inlined_images(self) -> set[str]:
        image_urls: set[str] = set()
        if not self.content:
            return image_urls

        soup = BeautifulSoup(self.content, "html5lib")
        imgs = soup.find_all("img")

        for img in imgs:
            if not img.attrs.get("src"):
                continue

            image_urls.add(img.attrs["src"])

        return image_urls
