# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScriptTrendingReportRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        script_id: str = None,
        start_time: int = None,
        time_interval: str = None,
    ):
        # The end time of the statistics. The parameter value must be a UNIX timestamp in milliseconds. It indicates the number of milliseconds that have elapsed since 00:00:00 UTC on January 1, 1970. The following limits apply:
        # 
        # 1. Time range: You can query data by hour for up to 7 days or by day for up to 180 days.
        # 
        # 2. Alignment with time granularity: If you query data by hour, the minutes, seconds, and milliseconds must be 0. If you query data by day, the hours, minutes, seconds, and milliseconds must be 0. If the specified timestamp is not aligned with the time granularity, the system automatically rounds it up to the next valid time.
        self.end_time = end_time
        # The instance ID.
        self.instance_id = instance_id
        # The scenario ID.
        self.script_id = script_id
        # The start time of the statistics. The parameter value is a UNIX timestamp in milliseconds. It indicates the number of milliseconds that have elapsed since 00:00:00 UTC on January 1, 1970. The following limits apply:
        # 
        # 1. Valid start time: You can query data collected within the last 365 days from the current date.
        # 
        # 2. Alignment with time granularity: If you query data by hour, the minutes, seconds, and milliseconds must be 0. If you query data by day, the hours, minutes, seconds, and milliseconds must be 0.
        # 
        # 3. If the specified timestamp is not aligned with the time granularity, the system automatically rounds it up to the next valid time.
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

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

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

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')

        return self

