# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSqlPatternCompareReportRequest(DaraModel):
    def __init__(
        self,
        compare_end_time: str = None,
        compare_start_time: str = None,
        dbcluster_id: str = None,
        end_time: str = None,
        pattern_type: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The end time of time window 2. Specify the time in UTC in the yyyy-MM-ddTHH:mmZ or yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is required.
        self.compare_end_time = compare_end_time
        # The start time of time window 2. Specify the time in UTC in the yyyy-MM-ddTHH:mmZ or yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is required.
        self.compare_start_time = compare_start_time
        # The ID of the AnalyticDB for MySQL cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end time of time window 1. Specify the time in UTC in the yyyy-MM-ddTHH:mmZ or yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The report type. Valid values:
        # 
        # - `NEW`: Patterns that are new in time window 2.
        # - `CHANGED`: Patterns that exist in both time windows and have an increased average value in at least one metric.
        # 
        # This parameter is required.
        self.pattern_type = pattern_type
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The start time of time window 1. Specify the time in UTC in the yyyy-MM-ddTHH:mmZ or yyyy-MM-ddTHH:mm:ssZ format.
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
        if self.compare_end_time is not None:
            result['CompareEndTime'] = self.compare_end_time

        if self.compare_start_time is not None:
            result['CompareStartTime'] = self.compare_start_time

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.pattern_type is not None:
            result['PatternType'] = self.pattern_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompareEndTime') is not None:
            self.compare_end_time = m.get('CompareEndTime')

        if m.get('CompareStartTime') is not None:
            self.compare_start_time = m.get('CompareStartTime')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PatternType') is not None:
            self.pattern_type = m.get('PatternType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

