# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIntervalAgentReportRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        end_time: int = None,
        instance_id: str = None,
        interval: str = None,
        media_type: str = None,
        start_time: int = None,
    ):
        # Agent ID.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # End time, formatted as a UNIX timestamp in milliseconds. This parameter is optional. The default value is the current time. If Interval is Daily, the maximum interval between StartTime and EndTime is 180 days. If Interval is Hourly, the maximum interval is 10 days. Time precision for statistics is at the hour level, rounded down to the next full hour, using an open interval. For example, if the start time is 11:12:20 and the end time is 11:45:50, the aligned input time range becomes [11:00:00, 12:00:00), meaning greater than or equal to 11:00:00 and less than 12:00:00.
        self.end_time = end_time
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Segment statistics type. Optional. Default value is Daily (aggregated by Day).
        self.interval = interval
        # Media type. The default value is Audio. Other valid values include Chat and Video.
        self.media_type = media_type
        # Start time, formatted as a UNIX timestamp in milliseconds. This parameter is optional. The default value is 00:00:00 of the current day. Time precision for statistics is at the hour level, rounded down to the previous full hour, using a closed interval.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

