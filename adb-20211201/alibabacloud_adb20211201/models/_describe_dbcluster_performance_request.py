# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBClusterPerformanceRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        key: str = None,
        region_id: str = None,
        resource_pools: str = None,
        start_time: str = None,
    ):
        # <props="china">The ID of the Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # <props="intl">The ID of the Data Lakehouse Edition cluster.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/612397.html) operation to query the IDs of all clusters in a specified region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end time of the query. Specify the time in UTC in the <i>yyyy-MM-ddTHH:mmZ</i> format.
        # 
        # > The end time must be later than the start time, and the time span between the start time and the end time cannot exceed two days.
        self.end_time = end_time
        # The names of the performance metrics to query, which are the keys of the monitored items. Separate multiple values with commas (,). For more information about the supported metrics, refer to [Overview of monitoring metrics](https://help.aliyun.com/document_detail/2863211.html).
        self.key = key
        # The region ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/612393.html) operation to query the regions and zones supported by AnalyticDB for MySQL, including region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group.
        self.resource_pools = resource_pools
        # The start time of the query. Specify the time in UTC in the <i>yyyy-MM-ddTHH:mmZ</i> format.
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

        if self.key is not None:
            result['Key'] = self.key

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_pools is not None:
            result['ResourcePools'] = self.resource_pools

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourcePools') is not None:
            self.resource_pools = m.get('ResourcePools')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

