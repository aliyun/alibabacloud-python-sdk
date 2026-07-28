# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEapDeviceResourceAllocationRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        device_count: int = None,
        region_id: str = None,
    ):
        # Instance cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Total number of devices
        self.device_count = device_count
        # Region ID where the instance is located.
        # 
        # > You can invoke the DescribeRegions API to view the region ID of a specified Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.device_count is not None:
            result['DeviceCount'] = self.device_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

