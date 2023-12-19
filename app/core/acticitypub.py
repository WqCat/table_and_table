"""
@Time: 2023/12/4 11:17
@Author: WQ
@File: acticitypub.py
@Des:
"""
from typing import TYPE_CHECKING, Any
import httpx
import enum

if TYPE_CHECKING:
    from test_model.actor import Actor

RawObject = dict[str, Any]
AS_CTX = "https://www.w3.org/ns/activitystreams"
AS_PUBLIC = "https://www.w3.org/ns/activitystreams#Public"

ACTOR_TYPES = ["Application", "Group", "Organization", "Person", "Service"]

AS_EXTENDED_CTX = [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {
        # AS ext
        "Hashtag": "as:Hashtag",
        "sensitive": "as:sensitive",
        "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
        "alsoKnownAs": {"@id": "as:alsoKnownAs", "@type": "@id"},
        "movedTo": {"@id": "as:movedTo", "@type": "@id"},
        # toot
        "toot": "http://joinmastodon.org/ns#",
        "featured": {"@id": "toot:featured", "@type": "@id"},
        "Emoji": "toot:Emoji",
        "blurhash": "toot:blurhash",
        "votersCount": "toot:votersCount",
        # schema
        "schema": "http://schema.org#",
        "PropertyValue": "schema:PropertyValue",
        "value": "schema:value",
        # ostatus
        "ostatus": "http://ostatus.org#",
        "conversation": "ostatus:conversation",
    },
]


class FetchError(Exception):
    def __init__(self, url: str, resp: httpx.Response | None = None) -> None:
        resp_part = ""
        if resp:
            resp_part = f", got HTTP {resp.status_code}: {resp.text}"
        message = f"Failed to fetch {url}{resp_part}"
        super().__init__(message)
        self.resp = resp
        self.url = url


class ObjectIsGoneError(FetchError):
    pass


class ObjectNotFoundError(FetchError):
    pass


class ObjectUnavailableError(FetchError):
    pass


class FetchErrorTypeEnum(str, enum.Enum):
    TIMEOUT = "TIMEOUT"
    NOT_FOUND = "NOT_FOUND"
    UNAUHTORIZED = "UNAUTHORIZED"

    INTERNAL_ERROR = "INTERNAL_ERROR"


class VisibilityEnum(str, enum.Enum):
    PUBLIC = "public"
    UNLISTED = "unlisted"
    FOLLOWERS_ONLY = "followers-only"
    DIRECT = "direct"

    @staticmethod
    def get_display_name(key: "VisibilityEnum") -> str:
        return {
            VisibilityEnum.PUBLIC: "Public - sent to followers and visible on the homepage",  # noqa: E501
            VisibilityEnum.UNLISTED: "Unlisted - like public, but hidden from the homepage",  # noqa: E501,
            VisibilityEnum.FOLLOWERS_ONLY: "Followers only",
            VisibilityEnum.DIRECT: "Direct - only visible for mentioned actors",
        }[key]