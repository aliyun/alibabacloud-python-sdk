# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSwimmingLaneGroupRequest(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        logical_region_id: str = None,
    ):
        # The ID of the lane group.
        self.group_id = group_id
        # The ID of the namespace.
        # 
        # The ID of a custom namespace is in the region ID:namespace identifier format. Example: cn-beijing:test.<br>
        # The ID of the default namespace is in the region ID format. Example: cn-beijing.
        # 
        # This parameter is required.
        self.logical_region_id = logical_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.logical_region_id is not None:
            result['LogicalRegionId'] = self.logical_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('LogicalRegionId') is not None:
            self.logical_region_id = m.get('LogicalRegionId')

        return self

