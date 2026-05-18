# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAccessRuleRequest(DaraModel):
    def __init__(
        self,
        access_group_id: str = None,
        description: str = None,
        input_region_id: str = None,
        network_segment: str = None,
        priority: int = None,
        rwaccess_type: str = None,
    ):
        # This parameter is required.
        self.access_group_id = access_group_id
        self.description = description
        # This parameter is required.
        self.input_region_id = input_region_id
        # This parameter is required.
        self.network_segment = network_segment
        # This parameter is required.
        self.priority = priority
        # This parameter is required.
        self.rwaccess_type = rwaccess_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id

        if self.description is not None:
            result['Description'] = self.description

        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        if self.network_segment is not None:
            result['NetworkSegment'] = self.network_segment

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.rwaccess_type is not None:
            result['RWAccessType'] = self.rwaccess_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        if m.get('NetworkSegment') is not None:
            self.network_segment = m.get('NetworkSegment')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RWAccessType') is not None:
            self.rwaccess_type = m.get('RWAccessType')

        return self

