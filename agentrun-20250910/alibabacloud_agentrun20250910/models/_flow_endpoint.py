# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class FlowEndpoint(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        flow_endpoint_arn: str = None,
        flow_endpoint_id: str = None,
        flow_endpoint_name: str = None,
        flow_id: str = None,
        last_updated_at: str = None,
        routing_configuration: List[main_models.FlowEndpointRoutingConfig] = None,
        target_version: str = None,
    ):
        # 工作流端点的创建时间，采用ISO 8601格式
        self.created_at = created_at
        # 工作流端点的描述信息
        self.description = description
        # 工作流端点的全局唯一资源名称
        self.flow_endpoint_arn = flow_endpoint_arn
        # 工作流端点的唯一标识符
        self.flow_endpoint_id = flow_endpoint_id
        # 工作流端点的名称
        self.flow_endpoint_name = flow_endpoint_name
        # 工作流的唯一标识符
        self.flow_id = flow_id
        # 工作流端点最后一次更新的时间，采用ISO 8601格式
        self.last_updated_at = last_updated_at
        # 工作流端点的版本路由配置
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
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.flow_endpoint_arn is not None:
            result['flowEndpointArn'] = self.flow_endpoint_arn

        if self.flow_endpoint_id is not None:
            result['flowEndpointId'] = self.flow_endpoint_id

        if self.flow_endpoint_name is not None:
            result['flowEndpointName'] = self.flow_endpoint_name

        if self.flow_id is not None:
            result['flowId'] = self.flow_id

        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at

        result['routingConfiguration'] = []
        if self.routing_configuration is not None:
            for k1 in self.routing_configuration:
                result['routingConfiguration'].append(k1.to_map() if k1 else None)

        if self.target_version is not None:
            result['targetVersion'] = self.target_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('flowEndpointArn') is not None:
            self.flow_endpoint_arn = m.get('flowEndpointArn')

        if m.get('flowEndpointId') is not None:
            self.flow_endpoint_id = m.get('flowEndpointId')

        if m.get('flowEndpointName') is not None:
            self.flow_endpoint_name = m.get('flowEndpointName')

        if m.get('flowId') is not None:
            self.flow_id = m.get('flowId')

        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')

        self.routing_configuration = []
        if m.get('routingConfiguration') is not None:
            for k1 in m.get('routingConfiguration'):
                temp_model = main_models.FlowEndpointRoutingConfig()
                self.routing_configuration.append(temp_model.from_map(k1))

        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')

        return self

