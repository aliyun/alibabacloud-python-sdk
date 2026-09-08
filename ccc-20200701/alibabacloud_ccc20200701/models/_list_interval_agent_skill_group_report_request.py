# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIntervalAgentSkillGroupReportRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        end_time: int = None,
        instance_id: str = None,
        interval: str = None,
        skill_group_id: str = None,
        start_time: int = None,
    ):
        # The agent ID.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The end time. This is a UNIX timestamp in milliseconds. This parameter is not required. The default value is the current time. If Interval is set to Daily, the maximum interval between StartTime and EndTime is 180 days. If Interval is set to Hourly, the maximum interval is 10 days. The statistics are measured in hours and rounded up to the nearest hour. This is an open interval. For example, if the start time is 11:12:20 and the end time is 11:45:50, the aligned time range for the input parameters is [11:00:00, 12:00:00), which means greater than or equal to 11:00 and less than 12:00.
        self.end_time = end_time
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of interval-based statistics. This parameter is not required. The default value is Daily (summarized by day).
        self.interval = interval
        # The skill group ID.
        # 
        # This parameter is required.
        self.skill_group_id = skill_group_id
        # The start timestamp. The default value is 00:00 on the current day. The statistics are measured in hours and rounded down to the nearest hour. This is a closed interval.
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

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

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

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

