# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAppAgentRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        app_id: str = None,
        config: str = None,
        enable: bool = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        # The agent ID, which is the unique identifier of the agent and is returned in the response of the AddAppAgent operation.
        self.agent_id = agent_id
        # The name of the agent.
        self.agent_name = agent_name
        # The app ID, which is the unique identifier of the application and is returned in the response of the AddAppConfig operation. Note: This parameter is actually required. If it is not provided, the API returns a 400 error with the message "appId may not be empty".
        self.app_id = app_id
        # The configuration details.
        self.config = config
        # Specifies whether to enable the agent. Valid values:
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.enable = enable
        # The region ID.
        self.region_id = region_id
        # The resource type. Note: This parameter is actually required. If it is not provided, the API returns a 400 error with the message "resourceType may not be empty".
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.config is not None:
            result['Config'] = self.config

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

