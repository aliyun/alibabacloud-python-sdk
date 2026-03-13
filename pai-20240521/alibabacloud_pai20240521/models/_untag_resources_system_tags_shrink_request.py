# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UntagResourcesSystemTagsShrinkRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id_shrink: str = None,
        resource_type: str = None,
        tag_key_shrink: str = None,
        tag_owner_uid: int = None,
    ):
        self.all = all
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.resource_id_shrink = resource_id_shrink
        # This parameter is required.
        self.resource_type = resource_type
        self.tag_key_shrink = tag_key_shrink
        # This parameter is required.
        self.tag_owner_uid = tag_owner_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id_shrink is not None:
            result['ResourceId'] = self.resource_id_shrink

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_key_shrink is not None:
            result['TagKey'] = self.tag_key_shrink

        if self.tag_owner_uid is not None:
            result['TagOwnerUid'] = self.tag_owner_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id_shrink = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key_shrink = m.get('TagKey')

        if m.get('TagOwnerUid') is not None:
            self.tag_owner_uid = m.get('TagOwnerUid')

        return self

