# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentResp(DaraModel):
    def __init__(
        self,
        activation_key: str = None,
        agent_endpoint: str = None,
        create_time: str = None,
        deploy_method: str = None,
        modify_time: str = None,
        name: str = None,
        owner: str = None,
        tags: str = None,
        tunnel_id: str = None,
        version: str = None,
    ):
        self.activation_key = activation_key
        self.agent_endpoint = agent_endpoint
        self.create_time = create_time
        self.deploy_method = deploy_method
        self.modify_time = modify_time
        self.name = name
        self.owner = owner
        self.tags = tags
        self.tunnel_id = tunnel_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activation_key is not None:
            result['ActivationKey'] = self.activation_key

        if self.agent_endpoint is not None:
            result['AgentEndpoint'] = self.agent_endpoint

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deploy_method is not None:
            result['DeployMethod'] = self.deploy_method

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivationKey') is not None:
            self.activation_key = m.get('ActivationKey')

        if m.get('AgentEndpoint') is not None:
            self.agent_endpoint = m.get('AgentEndpoint')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeployMethod') is not None:
            self.deploy_method = m.get('DeployMethod')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

