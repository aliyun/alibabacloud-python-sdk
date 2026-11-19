# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublishAppConfigRequest(DaraModel):
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
        # The agent ID. This parameter must be the AgentId returned by the AddAppAgent operation after the agent is added.
        self.agent_id = agent_id
        # The agent name.
        self.agent_name = agent_name
        # The application ID. This parameter must be the AppId returned by the AddAppConfig operation after the application is created.
        self.app_id = app_id
        # The configuration details. The value is a JSON string. The outer object contains the agentItemConfigs field, and its value is a re-serialized JSON array string (a double-nested structure) represented as a sequence of characters. Each array element in agentItemConfigs is an agent configuration object. Supported fields include agentId (string, the agent ID. Use the actual value returned by AddAppAgent or a clear placeholder such as <your-agent-id>), name (string, the agent name), and enable (boolean, specifies whether to enable the agent). Differences and connections with the Config parameter of ModifyAppAgent: The Config parameter of ModifyAppAgent describes the runtime configuration of a single agent (model, scene, or labelConfig), and you must first configure the agent by calling ModifyAppAgent. The Config parameter of this operation aggregates all agent entries (agentItemConfigs) under the application for overall publishing.
        self.config = config
        # Specifies whether to enable the agent. Valid values:
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.enable = enable
        # The region ID.
        self.region_id = region_id
        # The resource type.
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

