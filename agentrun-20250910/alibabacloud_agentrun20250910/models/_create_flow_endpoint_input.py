# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateFlowEndpointInput(DaraModel):
    def __init__(
        self,
        description: str = None,
        flow_endpoint_name: str = None,
        routing_configuration: List[main_models.FlowEndpointRoutingConfig] = None,
        target_version: str = None,
    ):
        # 工作流端点的描述信息
        self.description = description
        # 工作流端点的唯一标识名称
        # 
        # This parameter is required.
        self.flow_endpoint_name = flow_endpoint_name
        # 工作流端点的版本路由配置，用于流量分配
        self.routing_configuration = routing_configuration
        # 工作流端点指向的目标版本号
        self.target_version = target_version

    def validate(self):
        if self.routing_configuration:
            for v1 in self.routing_configuration:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.flow_endpoint_name is not None:
            result['flowEndpointName'] = self.flow_endpoint_name

        result['routingConfiguration'] = []
        if self.routing_configuration is not None:
            for k1 in self.routing_configuration:
                result['routingConfiguration'].append(k1.to_map() if k1 else None)

        if self.target_version is not None:
            result['targetVersion'] = self.target_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('flowEndpointName') is not None:
            self.flow_endpoint_name = m.get('flowEndpointName')

        self.routing_configuration = []
        if m.get('routingConfiguration') is not None:
            for k1 in m.get('routingConfiguration'):
                temp_model = main_models.FlowEndpointRoutingConfig()
                self.routing_configuration.append(temp_model.from_map(k1))

        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')

        return self

