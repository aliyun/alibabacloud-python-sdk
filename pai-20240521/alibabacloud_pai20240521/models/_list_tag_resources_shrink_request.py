# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagResourcesShrinkRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        next_token: str = None,
        region_id: str = None,
        resource_id_shrink: str = None,
        resource_type: str = None,
        scope: str = None,
        tag_shrink: str = None,
        tag_owner_uid: int = None,
    ):
        self.category = category
        self.next_token = next_token
        # This parameter is required.
        self.region_id = region_id
        self.resource_id_shrink = resource_id_shrink
        # This parameter is required.
        self.resource_type = resource_type
        self.scope = scope
        self.tag_shrink = tag_shrink
        # This parameter is required.
        self.tag_owner_uid = tag_owner_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id_shrink is not None:
            result['ResourceId'] = self.resource_id_shrink

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        if self.tag_owner_uid is not None:
            result['TagOwnerUid'] = self.tag_owner_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id_shrink = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        if m.get('TagOwnerUid') is not None:
            self.tag_owner_uid = m.get('TagOwnerUid')

        return self

