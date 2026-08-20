# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class AgentInfo(DaraModel):
    def __init__(
        self,
        agent_access: main_models.AgentInfoAgentAccess = None,
        agent_id: str = None,
        agent_type: str = None,
        allowed_capabilities: List[str] = None,
        create_timestamp: int = None,
        description: str = None,
        gateway_id: str = None,
        model_access: main_models.AgentInfoModelAccess = None,
        name: str = None,
        resource_group_id: str = None,
        status: str = None,
        update_timestamp: int = None,
    ):
        # The associated resource information for the Agent access capability. Returns null if the Agent access capability is not configured.
        self.agent_access = agent_access
        # Agent ID。
        self.agent_id = agent_id
        # The Agent type. DashScope (Bailian) allows only Agent access. Dify allows both Agent access and model access. ClaudeCode allows only model access. Custom allows both Agent access and model access.
        self.agent_type = agent_type
        # The list of capabilities that the current Agent type allows to be configured. This field does not indicate that the capabilities are already configured. To determine whether a capability is configured, check whether agentAccess or modelAccess is null.
        self.allowed_capabilities = allowed_capabilities
        # The Agent creation time, in Unix millisecond timestamp.
        self.create_timestamp = create_timestamp
        # The Agent description.
        self.description = description
        # The gateway ID to which the Agent belongs. When reading the associated API deployment configuration, select the configuration whose gatewayId matches this value.
        self.gateway_id = gateway_id
        # The associated resource information for the model access capability. Returns null if the model access capability is not configured.
        self.model_access = model_access
        # The Agent name.
        self.name = name
        # The resource group ID in which the Agent is saved.
        self.resource_group_id = resource_group_id
        # The Agent status. An Agent that is successfully created and queryable always returns Ready. Internal creation or compensation states are not returned externally.
        self.status = status
        # The Agent last update time, in Unix millisecond timestamp.
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.agent_access:
            self.agent_access.validate()
        if self.model_access:
            self.model_access.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_access is not None:
            result['agentAccess'] = self.agent_access.to_map()

        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.agent_type is not None:
            result['agentType'] = self.agent_type

        if self.allowed_capabilities is not None:
            result['allowedCapabilities'] = self.allowed_capabilities

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.description is not None:
            result['description'] = self.description

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.model_access is not None:
            result['modelAccess'] = self.model_access.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['status'] = self.status

        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentAccess') is not None:
            temp_model = main_models.AgentInfoAgentAccess()
            self.agent_access = temp_model.from_map(m.get('agentAccess'))

        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('agentType') is not None:
            self.agent_type = m.get('agentType')

        if m.get('allowedCapabilities') is not None:
            self.allowed_capabilities = m.get('allowedCapabilities')

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('modelAccess') is not None:
            temp_model = main_models.AgentInfoModelAccess()
            self.model_access = temp_model.from_map(m.get('modelAccess'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        return self

class AgentInfoModelAccess(DaraModel):
    def __init__(
        self,
        consumer_ids: List[str] = None,
        model_api_id: str = None,
    ):
        # The list of consumer identity bindings maintained by the Agent domain. The Model API ID and the consumer IDs in this list together identify the Agent identity and take effect on all routes of the Model API. Consumer details and their Model API authorization details can be obtained through existing Consumer API and consumer authorization query interfaces.
        self.consumer_ids = consumer_ids
        # The Model API ID associated with the model access capability. Model Access does not distinguish routes. The frontend uses this ID to query the Model API basic information and all routes.
        self.model_api_id = model_api_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_ids is not None:
            result['consumerIds'] = self.consumer_ids

        if self.model_api_id is not None:
            result['modelApiId'] = self.model_api_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerIds') is not None:
            self.consumer_ids = m.get('consumerIds')

        if m.get('modelApiId') is not None:
            self.model_api_id = m.get('modelApiId')

        return self

class AgentInfoAgentAccess(DaraModel):
    def __init__(
        self,
        http_api_id: str = None,
    ):
        # The HTTP API ID associated with the Agent access capability. The frontend uses this ID to call existing HTTP API, route, consumer authorization, policy, and plugin query interfaces.
        self.http_api_id = http_api_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_api_id is not None:
            result['httpApiId'] = self.http_api_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('httpApiId') is not None:
            self.http_api_id = m.get('httpApiId')

        return self

