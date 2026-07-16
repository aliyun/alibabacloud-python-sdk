# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWorkerShrinkRequest(DaraModel):
    def __init__(
        self,
        agents: str = None,
        channels_shrink: str = None,
        client_token: str = None,
        credentials_shrink: str = None,
        instance_id: str = None,
        limit_config_shrink: str = None,
        mcp_servers_shrink: str = None,
        model_shrink: str = None,
        name: str = None,
        skills_shrink: str = None,
        soul: str = None,
        template_shrink: str = None,
        version_code: str = None,
    ):
        self.agents = agents
        self.channels_shrink = channels_shrink
        self.client_token = client_token
        self.credentials_shrink = credentials_shrink
        # This parameter is required.
        self.instance_id = instance_id
        self.limit_config_shrink = limit_config_shrink
        self.mcp_servers_shrink = mcp_servers_shrink
        self.model_shrink = model_shrink
        # This parameter is required.
        self.name = name
        self.skills_shrink = skills_shrink
        self.soul = soul
        self.template_shrink = template_shrink
        self.version_code = version_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agents is not None:
            result['Agents'] = self.agents

        if self.channels_shrink is not None:
            result['Channels'] = self.channels_shrink

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.credentials_shrink is not None:
            result['Credentials'] = self.credentials_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.limit_config_shrink is not None:
            result['LimitConfig'] = self.limit_config_shrink

        if self.mcp_servers_shrink is not None:
            result['McpServers'] = self.mcp_servers_shrink

        if self.model_shrink is not None:
            result['Model'] = self.model_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.skills_shrink is not None:
            result['Skills'] = self.skills_shrink

        if self.soul is not None:
            result['Soul'] = self.soul

        if self.template_shrink is not None:
            result['Template'] = self.template_shrink

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agents') is not None:
            self.agents = m.get('Agents')

        if m.get('Channels') is not None:
            self.channels_shrink = m.get('Channels')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Credentials') is not None:
            self.credentials_shrink = m.get('Credentials')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LimitConfig') is not None:
            self.limit_config_shrink = m.get('LimitConfig')

        if m.get('McpServers') is not None:
            self.mcp_servers_shrink = m.get('McpServers')

        if m.get('Model') is not None:
            self.model_shrink = m.get('Model')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Skills') is not None:
            self.skills_shrink = m.get('Skills')

        if m.get('Soul') is not None:
            self.soul = m.get('Soul')

        if m.get('Template') is not None:
            self.template_shrink = m.get('Template')

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        return self

