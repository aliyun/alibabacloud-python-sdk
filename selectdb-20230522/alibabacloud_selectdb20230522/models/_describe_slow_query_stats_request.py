# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSlowQueryStatsRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        region_id: str = None,
        start_time: str = None,
        threshold_ms: int = None,
        top_n: int = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The end time. Must be later than the start time. Defaults to the current time.
        self.end_time = end_time
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The start time. Defaults to 24 hours before the current time.
        self.start_time = start_time
        # The slow query threshold, in milliseconds. The default value is 5000.
        self.threshold_ms = threshold_ms
        # The number of top slow queries to return. The default value is 10.
        self.top_n = top_n

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.threshold_ms is not None:
            result['ThresholdMs'] = self.threshold_ms

        if self.top_n is not None:
            result['TopN'] = self.top_n

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('ThresholdMs') is not None:
            self.threshold_ms = m.get('ThresholdMs')

        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')

        return self

