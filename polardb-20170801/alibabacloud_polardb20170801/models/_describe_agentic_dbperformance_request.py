# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAgenticDBPerformanceRequest(DaraModel):
    def __init__(
        self,
        aggregate: bool = None,
        branch_id: str = None,
        dbcluster_id: str = None,
        end_time: str = None,
        interval: str = None,
        key: str = None,
        start_time: str = None,
    ):
        # The statistical method for alerts. Valid values for different monitoring items:
        # 
        # - Value: the value of the HTTP status code.
        # - Average: the average HTTP wait time.
        # - Value: the value of the TELNET status code.
        # - TelnetLatency: the average TELNET wait time.
        # - Average: the average PING packet loss rate.
        self.aggregate = aggregate
        # The ID of the anchor branch. If you do not specify this parameter, the main branch of the project is used by default.
        self.branch_id = branch_id
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end time of the query. Specify the time in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The granularity of performance data. Valid values:
        # 
        # - 5
        # - 30
        # - 60
        # - 600
        # - 1800
        # - 3600
        # - 86400
        self.interval = interval
        # The performance metrics to query. Separate multiple values with commas (,).
        # Note
        # You can specify up to 5 performance metrics.
        # 
        # This parameter is required.
        self.key = key
        # The start time of the query. Specify the time in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
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
        if self.aggregate is not None:
            result['Aggregate'] = self.aggregate

        if self.branch_id is not None:
            result['BranchId'] = self.branch_id

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
        if m.get('Aggregate') is not None:
            self.aggregate = m.get('Aggregate')

        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

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

