# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class AgentResource(DaraModel):
    def __init__(
        self,
        flow: main_models.Flow = None,
        latest_version: main_models.AgentResourceLatestVersion = None,
        resource_type: str = None,
        runtime: main_models.AgentRuntime = None,
    ):
        # 当 resourceType 为 Flow 时，此字段包含完整的工作流对象，包括所有配置和状态信息；当 resourceType 为 AgentRuntime 时，此字段为空
        self.flow = flow
        # 资源的最新发布版本摘要，包含版本号、描述和创建时间。如果资源没有已发布版本，则此字段为空
        self.latest_version = latest_version
        # 资源类型标识符，用于区分资源是智能体运行时（AgentRuntime）还是工作流（Flow）
        self.resource_type = resource_type
        # 当 resourceType 为 AgentRuntime 时，此字段包含完整的智能体运行时对象，包括所有配置和状态信息；当 resourceType 为 Flow 时，此字段为空
        self.runtime = runtime

    def validate(self):
        if self.flow:
            self.flow.validate()
        if self.latest_version:
            self.latest_version.validate()
        if self.runtime:
            self.runtime.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow is not None:
            result['flow'] = self.flow.to_map()

        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version.to_map()

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flow') is not None:
            temp_model = main_models.Flow()
            self.flow = temp_model.from_map(m.get('flow'))

        if m.get('latestVersion') is not None:
            temp_model = main_models.AgentResourceLatestVersion()
            self.latest_version = temp_model.from_map(m.get('latestVersion'))

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('runtime') is not None:
            temp_model = main_models.AgentRuntime()
            self.runtime = temp_model.from_map(m.get('runtime'))

        return self



class AgentResourceLatestVersion(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        publisher: str = None,
        version: str = None,
    ):
        # 版本发布时间，采用ISO 8601格式
        self.created_at = created_at
        # 该版本的描述信息
        self.description = description
        # 版本发布者（仅 AgentRuntime 类型资源返回）
        self.publisher = publisher
        # 最新发布的版本号
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.publisher is not None:
            result['publisher'] = self.publisher

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('publisher') is not None:
            self.publisher = m.get('publisher')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

