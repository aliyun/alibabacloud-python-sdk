# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBNodePerformanceRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbnode_id: str = None,
        end_time: str = None,
        interval: str = None,
        key: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The ID of the node in the PolarDB cluster.
        # 
        # This parameter is required.
        self.dbnode_id = dbnode_id
        # The end of the time range to query. Specify the time in the `yyyy-MM-ddTHH:mmZ` format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The granularity of the performance data. Valid values:
        # 
        # - 5
        # 
        # - 30
        # 
        # - 60
        # 
        # - 600
        # 
        # - 1800
        # 
        # - 3600
        # 
        # - 86400
        self.interval = interval
        # The performance metrics to query. Separate multiple metrics with commas (,). For more information, see [Performance metrics](https://help.aliyun.com/document_detail/141787.html).
        # 
        # > - You can query a maximum of five performance metrics.
        # >
        # > - If your cluster has Serverless enabled for fixed specifications, querying PolarDBCPU or PolarDBMemory alone ignores the Interval parameter and returns performance metrics per second. To get data at your specified Interval, query multiple metrics.
        # 
        # This parameter is required.
        self.key = key
        # The beginning of the time range to query. Specify the time in the `yyyy-MM-ddTHH:mmZ` format. The time must be in Coordinated Universal Time (UTC).
        # 
        # This parameter is required.
        self.start_time = start_time
        # A special metric. Currently, only orca is supported.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.key is not None:
            result['Key'] = self.key

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

