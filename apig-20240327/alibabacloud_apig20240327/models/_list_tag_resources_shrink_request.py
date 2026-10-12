# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagResourcesShrinkRequest(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        resource_id_shrink: str = None,
        resource_type: str = None,
        tag_shrink: str = None,
    ):
        # The token used to start the next query.
        self.next_token = next_token
        # The resource IDs. You can specify up to 50 resource IDs. You must specify at least one of ResourceId and Tag. If both are empty, the API returns InvalidParameter.BothEmpty(400).
        self.resource_id_shrink = resource_id_shrink
        # The resource type. Note: Although the documentation indicates a default value of Gateway, you must explicitly specify this parameter when you call the API. Otherwise, the API returns InvalidParameter.UnsupportedTagResourceType(400). Valid values: Gateway.
        self.resource_type = resource_type
        # The list of tags. You can specify up to 20 tags. You must specify at least one of ResourceId and Tag. If both are empty, the API returns InvalidParameter.BothEmpty(400).
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_id_shrink is not None:
            result['ResourceId'] = self.resource_id_shrink

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceId') is not None:
            self.resource_id_shrink = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self

