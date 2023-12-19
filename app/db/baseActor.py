"""
@Time: 2023/12/6 15:04
@Author: WQ
@File: baseActor.py
@Des:
"""

from functools import cached_property

from test_model import acticitypub as ap

class BaseActor:
    @property
    def ap_actor(self) -> ap.RawObject:
        raise NotImplementedError()

    @property
    def ap_id(self) -> str:
        return ap.get_id(self.ap_actor["id"])

    @property
    def name(self) -> str | None:
        return self.ap_actor.get("name")

    @property
    def summary(self) -> str | None:
        return self.ap_actor.get("summary")

    @property
    def url(self) -> str | None:
        return self.ap_actor.get("url") or self.ap_actor["id"]

    @property
    def preferred_username(self) -> str:
        return self.ap_actor["preferredUsername"]

    @property
    def display_name(self) -> str:
        if self.name:
            return self.name
        return self.preferred_username

    # @cached_property
    # def handle(self) -> str:
    #     return _handle(self.ap_actor)

    @property
    def ap_type(self) -> str:
        raise NotImplementedError()

    @property
    def inbox_url(self) -> str:
        return self.ap_actor["inbox"]

    @property
    def outbox_url(self) -> str:
        return self.ap_actor["outbox"]

    @property
    def shared_inbox_url(self) -> str:
        return self.ap_actor.get("endpoints", {}).get("sharedInbox") or self.inbox_url

    @property
    def icon_url(self) -> str | None:
        if icon := self.ap_actor.get("icon"):
            return icon.get("url")
        return None

    @property
    def icon_media_type(self) -> str | None:
        if icon := self.ap_actor.get("icon"):
            return icon.get("mediaType")
        return None

    @property
    def image_url(self) -> str | None:
        if image := self.ap_actor.get("image"):
            return image.get("url")
        return None

    @property
    def public_key_as_pem(self) -> str:
        return self.ap_actor["publicKey"]["publicKeyPem"]

    @property
    def public_key_id(self) -> str:
        return self.ap_actor["publicKey"]["id"]

    # @property
    # def proxied_icon_url(self) -> str:
    #     if self.icon_url:
    #         return media.proxied_media_url(self.icon_url)
    #     else:
    #         return BASE_URL + "/static/nopic.png"

    # @property
    # def resized_icon_url(self) -> str:
    #     if self.icon_url:
    #         return media.resized_media_url(self.icon_url, 50)
    #     else:
    #         return BASE_URL + "/static/nopic.png"

    @property
    def tags(self) -> list[ap.RawObject]:
        return ap.as_list(self.ap_actor.get("tag", []))

    @property
    def followers_collection_id(self) -> str | None:
        return self.ap_actor.get("followers")

    @cached_property
    def attachments(self) -> list[ap.RawObject]:
        return ap.as_list(self.ap_actor.get("attachment", []))

    @cached_property
    def moved_to(self) -> str | None:
        return self.ap_actor.get("movedTo")

    @cached_property
    def server(self) -> str:
        return urlparse(self.ap_id).hostname  # type: ignore

