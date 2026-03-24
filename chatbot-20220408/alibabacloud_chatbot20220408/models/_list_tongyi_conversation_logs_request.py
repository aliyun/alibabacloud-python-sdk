# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTongyiConversationLogsRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        robot_instance_id: str = None,
        session_id: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.robot_instance_id = robot_instance_id
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

