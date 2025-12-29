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
        # The token that is used to retrieve the next page.
        self.next_token = next_token
        # The resource IDs. You can specify a maximum number of 50 resource IDs.
        self.resource_id_shrink = resource_id_shrink
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags. You can specify a maximum number of 20 tags.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.resource_id_shrink is not None:
            result['resourceId'] = self.resource_id_shrink

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('resourceId') is not None:
            self.resource_id_shrink = m.get('resourceId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')

        return self

