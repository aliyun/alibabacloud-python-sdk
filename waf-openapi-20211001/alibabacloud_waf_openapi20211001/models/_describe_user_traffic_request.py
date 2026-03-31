# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserTrafficRequest(DaraModel):
    def __init__(
        self,
        end_timestamp: int = None,
        instance_id: str = None,
        interval: int = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        start_timestamp: int = None,
        type: str = None,
    ):
        self.end_timestamp = end_timestamp
        # This parameter is required.
        self.instance_id = instance_id
        self.interval = interval
        self.region_id = region_id
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        self.start_timestamp = start_timestamp
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

