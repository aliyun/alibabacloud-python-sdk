# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMobileAgentTaskRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        input_param: str = None,
        name: str = None,
        node_ids: str = None,
        session_id: str = None,
        type: str = None,
    ):
        # The agent ID.
        self.agent_id = agent_id
        # The task input.
        self.input_param = input_param
        # The task name.
        self.name = name
        # The list of node IDs.
        self.node_ids = node_ids
        # The session ID. Tasks with the same session ID share the same context.
        self.session_id = session_id
        # The task type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.input_param is not None:
            result['InputParam'] = self.input_param

        if self.name is not None:
            result['Name'] = self.name

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('InputParam') is not None:
            self.input_param = m.get('InputParam')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

