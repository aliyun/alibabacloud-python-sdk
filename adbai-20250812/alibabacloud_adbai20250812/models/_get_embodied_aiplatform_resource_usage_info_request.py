# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEmbodiedAIPlatformResourceUsageInfoRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        platform_name: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The instance cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end of the time range for querying network resource usage. Format: yyyy-MM-ddTHH:mmZ.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.end_time = end_time
        # The name of the embodied intelligence platform.
        self.platform_name = platform_name
        # The region ID of the instance.
        # 
        # > You can call the DescribeRegions operation to query the region ID of a specified Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The start of the time range for querying network resource usage. Format: yyyy-MM-ddTHH:mmZ.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.platform_name is not None:
            result['PlatformName'] = self.platform_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PlatformName') is not None:
            self.platform_name = m.get('PlatformName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

