# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        category: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
        tag_keys: List[str] = None,
        tag_owner_uid: int = None,
    ):
        self.region_id = region_id
        self.category = category
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.tag_keys = tag_keys
        self.tag_owner_uid = tag_owner_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.category is not None:
            result['category'] = self.category

        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.tag_keys is not None:
            result['tagKeys'] = self.tag_keys

        if self.tag_owner_uid is not None:
            result['tagOwnerUid'] = self.tag_owner_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('tagKeys') is not None:
            self.tag_keys = m.get('tagKeys')

        if m.get('tagOwnerUid') is not None:
            self.tag_owner_uid = m.get('tagOwnerUid')

        return self

