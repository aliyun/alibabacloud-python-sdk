# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgentConfigRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        config_name: str = None,
        content: str = None,
    ):
        # The ID of the component for the configuration. You can obtain the component ID from ListAgents.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The name of the configuration.
        # 
        # This parameter is required.
        self.config_name = config_name
        # The content of the configuration.
        # 
        # This parameter is required.
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.config_name is not None:
            result['configName'] = self.config_name

        if self.content is not None:
            result['content'] = self.content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('configName') is not None:
            self.config_name = m.get('configName')

        if m.get('content') is not None:
            self.content = m.get('content')

        return self

