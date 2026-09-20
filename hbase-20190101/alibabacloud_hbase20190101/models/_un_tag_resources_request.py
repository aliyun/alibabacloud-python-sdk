# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UnTagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to delete all tags. If TagKey is specified, tags are deleted only by TagKey. Valid values: true and false. If this parameter is set to true and TagKey is not specified, all tags are deleted.
        self.all = all
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of resource N to untag. The resource ID is the cluster ID. You can specify multiple resource IDs, such as ResourceId.2 and ResourceId.3. N is a positive integer.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The key of tag N to delete. You can specify multiple tag keys, such as TagKey.2 and TagKey.3. N is a positive integer.
        self.tag_key = tag_key

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

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

