# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAIDBClusterPerformanceRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        interval: str = None,
        key: str = None,
        start_time: str = None,
    ):
        # The cluster ID.
        # 
        # > Call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the details of all clusters under your account, including the cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the `YYYY-MM-DDThh:mmZ` format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The time granularity of the data to retrieve. Valid values: **60** (minutes) and **3600** (hours).
        # 
        # - If you set **Interval** to **60**, you can query data from the last month. The maximum time range for a single query is 7 days.
        # - If you set **Interval** to **3600**, you can query data from the last month. The maximum time range for a single query is 7 days.
        self.interval = interval
        # The name of the metric.
        # 
        # This parameter is required.
        self.key = key
        # The beginning of the time range to query. Specify the time in the `YYYY-MM-DDThh:mmZ` format. The time must be in UTC.
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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

