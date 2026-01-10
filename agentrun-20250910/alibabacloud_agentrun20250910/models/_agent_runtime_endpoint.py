# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class AgentRuntimeEndpoint(DaraModel):
    def __init__(
        self,
        agent_runtime_endpoint_arn: str = None,
        agent_runtime_endpoint_id: str = None,
        agent_runtime_endpoint_name: str = None,
        agent_runtime_id: str = None,
        description: str = None,
        endpoint_public_url: str = None,
        routing_configuration: main_models.RoutingConfiguration = None,
        status: str = None,
        status_reason: str = None,
        target_version: str = None,
    ):
        self.agent_runtime_endpoint_arn = agent_runtime_endpoint_arn
        self.agent_runtime_endpoint_id = agent_runtime_endpoint_id
        self.agent_runtime_endpoint_name = agent_runtime_endpoint_name
        self.agent_runtime_id = agent_runtime_id
        self.description = description
        # 智能体运行时端点的公网访问地址
        self.endpoint_public_url = endpoint_public_url
        # 智能体运行时端点的路由配置，支持多版本权重分配
        self.routing_configuration = routing_configuration
        self.status = status
        self.status_reason = status_reason
        self.target_version = target_version

    def validate(self):
        if self.routing_configuration:
            self.routing_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_runtime_endpoint_arn is not None:
            result['agentRuntimeEndpointArn'] = self.agent_runtime_endpoint_arn

        if self.agent_runtime_endpoint_id is not None:
            result['agentRuntimeEndpointId'] = self.agent_runtime_endpoint_id

        if self.agent_runtime_endpoint_name is not None:
            result['agentRuntimeEndpointName'] = self.agent_runtime_endpoint_name

        if self.agent_runtime_id is not None:
            result['agentRuntimeId'] = self.agent_runtime_id

        if self.description is not None:
            result['description'] = self.description

        if self.endpoint_public_url is not None:
            result['endpointPublicUrl'] = self.endpoint_public_url

        if self.routing_configuration is not None:
            result['routingConfiguration'] = self.routing_configuration.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        if self.target_version is not None:
            result['targetVersion'] = self.target_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeEndpointArn') is not None:
            self.agent_runtime_endpoint_arn = m.get('agentRuntimeEndpointArn')

        if m.get('agentRuntimeEndpointId') is not None:
            self.agent_runtime_endpoint_id = m.get('agentRuntimeEndpointId')

        if m.get('agentRuntimeEndpointName') is not None:
            self.agent_runtime_endpoint_name = m.get('agentRuntimeEndpointName')

        if m.get('agentRuntimeId') is not None:
            self.agent_runtime_id = m.get('agentRuntimeId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('endpointPublicUrl') is not None:
            self.endpoint_public_url = m.get('endpointPublicUrl')

        if m.get('routingConfiguration') is not None:
            temp_model = main_models.RoutingConfiguration()
            self.routing_configuration = temp_model.from_map(m.get('routingConfiguration'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')

        return self

