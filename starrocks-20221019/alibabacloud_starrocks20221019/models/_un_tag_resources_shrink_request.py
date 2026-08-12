# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnTagResourcesShrinkRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id_shrink: str = None,
        resource_type: str = None,
        tag_key_shrink: str = None,
    ):
        # Specifies whether to remove all tags from the resources. This parameter is valid only when the TagKey parameter is left empty. The default value is false.
        self.all = all
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # A list of resource IDs. The list can contain up to 50 resource IDs.
        # 
        # This parameter is required.
        self.resource_id_shrink = resource_id_shrink
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # A list of tag keys to remove. The list can contain up to 20 tag keys.
        self.tag_key_shrink = tag_key_shrink

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

        return self

