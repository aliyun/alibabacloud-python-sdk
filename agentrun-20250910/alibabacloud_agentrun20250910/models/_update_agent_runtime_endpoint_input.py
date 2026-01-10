# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class UpdateAgentRuntimeEndpointInput(DaraModel):
    def __init__(
        self,
        agent_runtime_endpoint_name: str = None,
        description: str = None,
        routing_configuration: main_models.RoutingConfiguration = None,
        target_version: str = None,
    ):
        self.agent_runtime_endpoint_name = agent_runtime_endpoint_name
        self.description = description
        # 智能体运行时端点的路由配置，支持多版本权重分配
        self.routing_configuration = routing_configuration
        # 智能体运行时的目标版本
        self.target_version = target_version

    def validate(self):
        if self.routing_configuration:
            self.routing_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_runtime_endpoint_name is not None:
            result['agentRuntimeEndpointName'] = self.agent_runtime_endpoint_name

        if self.description is not None:
            result['description'] = self.description

        if self.routing_configuration is not None:
            result['routingConfiguration'] = self.routing_configuration.to_map()

        if self.target_version is not None:
            result['targetVersion'] = self.target_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeEndpointName') is not None:
            self.agent_runtime_endpoint_name = m.get('agentRuntimeEndpointName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('routingConfiguration') is not None:
            temp_model = main_models.RoutingConfiguration()
            self.routing_configuration = temp_model.from_map(m.get('routingConfiguration'))

        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')

        return self

