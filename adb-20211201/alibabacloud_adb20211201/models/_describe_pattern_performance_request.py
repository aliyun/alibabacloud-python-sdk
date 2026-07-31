# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePatternPerformanceRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        pattern_id: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the details of all clusters in a region, including their cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end of the time range to query. Specify the time in UTC in the *yyyy-MM-ddTHH:mm:ssZ* format.
        # 
        # > The end time must be later than the start time.
        self.end_time = end_time
        # The ID of the SQL pattern.
        # 
        # > You can call the [DescribeSQLPatterns](https://help.aliyun.com/document_detail/321868.html) operation to query information about all SQL patterns in a cluster within a specified time range, including the ID of each SQL pattern.
        self.pattern_id = pattern_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in UTC in the *yyyy-MM-ddTHH:mm:ssZ* format.
        # 
        # > - You can query data from the last 14 days. If you specify a start time earlier than this period, an empty value is returned. For example, if the current date is August 22, 2022 (China Standard Time), the earliest valid start time is 2022-08-08T16:00:00Z.
        # 
        # - The interval between the start time and the end time cannot exceed 24 hours.
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

        if self.pattern_id is not None:
            result['PatternId'] = self.pattern_id

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

        if m.get('PatternId') is not None:
            self.pattern_id = m.get('PatternId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

