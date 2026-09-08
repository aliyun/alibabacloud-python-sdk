# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentStateLogsRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        end_time: int = None,
        instance_id: str = None,
        start_time: int = None,
    ):
        # Agent ID.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # End UNIX timestamp. The default value is the current time. The time difference between EndTime and StartTime must not exceed 7 days. The format is a Unix timestamp in milliseconds.
        self.end_time = end_time
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Start UNIX timestamp. The default value is the start time of the current day. The earliest allowed value is 180 days before the current date. The format is a Unix timestamp in milliseconds.
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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

