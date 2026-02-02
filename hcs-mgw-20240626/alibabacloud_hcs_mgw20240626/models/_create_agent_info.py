# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgentInfo(DaraModel):
    def __init__(
        self,
        agent_endpoint: str = None,
        deploy_method: str = None,
        name: str = None,
        tags: str = None,
        tunnel_id: str = None,
    ):
        # This parameter is required.
        self.agent_endpoint = agent_endpoint
        # This parameter is required.
        self.deploy_method = deploy_method
        # This parameter is required.
        self.name = name
        self.tags = tags
        # This parameter is required.
        self.tunnel_id = tunnel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_endpoint is not None:
            result['AgentEndpoint'] = self.agent_endpoint

        if self.deploy_method is not None:
            result['DeployMethod'] = self.deploy_method

        if self.name is not None:
            result['Name'] = self.name

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentEndpoint') is not None:
            self.agent_endpoint = m.get('AgentEndpoint')

        if m.get('DeployMethod') is not None:
            self.deploy_method = m.get('DeployMethod')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')

        return self

