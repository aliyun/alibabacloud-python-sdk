# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        robot_type: str = None,
        sandbox: bool = None,
    ):
        self.agent_key = agent_key
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.robot_type = robot_type
        self.sandbox = sandbox

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.robot_type is not None:
            result['RobotType'] = self.robot_type

        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')

        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')

        return self

