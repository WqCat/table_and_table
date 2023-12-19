"""
@Time: 2023/12/4 11:17
@Author: WQ
@File: acticitypub.py
@Des:
"""
from typing import TYPE_CHECKING, Any

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