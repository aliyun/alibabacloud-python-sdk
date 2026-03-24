# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBotSessionDataRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        start_time: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.robot_instance_id = robot_instance_id
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

