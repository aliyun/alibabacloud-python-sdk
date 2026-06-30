# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolarClawAgentToolsRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        include_plugins: bool = None,
    ):
        # Agent ID
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # Specifies whether to include plugin tools.
        self.include_plugins = include_plugins

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.include_plugins is not None:
            result['IncludePlugins'] = self.include_plugins

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('IncludePlugins') is not None:
            self.include_plugins = m.get('IncludePlugins')

        return self

