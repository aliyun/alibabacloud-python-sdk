# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolarFsPerformanceRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        interval: str = None,
        key: str = None,
        polar_fs_instance_id: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The cluster ID.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the IDs of all Data Warehouse Edition clusters in the specified region.
        self.dbcluster_id = dbcluster_id
        # The end time of the query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format. The time must be in UTC and must not be earlier than the start time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The sampling granularity of performance data, in seconds. The value must be a multiple of 60 and greater than 0. Default value: 60.
        self.interval = interval
        # The monitoring metric group. Valid values: Capacity (capacity), Inode (file nodes), Iops (read and write operations per second), Latency (read and write latency), QpsMeta (metadata operation requests), and Throughput (read and write throughput).
        # 
        # This parameter is required.
        self.key = key
        # The PolarFS instance ID.
        # 
        # This parameter is required.
        self.polar_fs_instance_id = polar_fs_instance_id
        # The region ID.
        self.region_id = region_id
        # The start time of the query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
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

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.key is not None:
            result['Key'] = self.key

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

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

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

