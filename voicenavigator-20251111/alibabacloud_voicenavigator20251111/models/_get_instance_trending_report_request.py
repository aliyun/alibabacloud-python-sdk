# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceTrendingReportRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        start_time: int = None,
        time_interval: str = None,
    ):
        # The end time of the statistical period. The value is a millisecond-level UNIX timestamp that represents the number of milliseconds elapsed since 1970-01-01 00:00:00 UTC. The following constraints apply:
        # 
        # Time range constraint: The maximum time range is 7 days for hourly queries and 180 days for daily queries.
        # Time granularity alignment: For hourly queries, the minutes, seconds, and milliseconds must be 0. For daily queries, the hours, minutes, seconds, and milliseconds must be 0.
        # If the specified timestamp is not aligned with the corresponding granularity, the server automatically rounds it up.
        self.end_time = end_time
        # The instance ID.
        self.instance_id = instance_id
        # The start time of the statistical period. The value is a millisecond-level UNIX timestamp that represents the number of milliseconds elapsed since 1970-01-01 00:00:00 UTC. The following constraints apply:
        # 1. Earliest boundary: The start time can trace back to 00:00:00 of the date 365 calendar days before the current date.
        # 2. Time granularity alignment: For hourly queries, the minutes, seconds, and milliseconds must be 0. For daily queries, the hours, minutes, seconds, and milliseconds must be 0.
        # 3. If the specified timestamp is not aligned with the corresponding granularity, the server automatically rounds it up.
        self.start_time = start_time
        # The time interval.
        self.time_interval = time_interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')

        return self

