# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PathConfig(DaraModel):
    def __init__(
        self,
        agent_runtime_endpoint_name: str = None,
        methods: List[str] = None,
        path: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # agent runtime 版本（仅当 resourceType 为 runtime 时有效）
        self.agent_runtime_endpoint_name = agent_runtime_endpoint_name
        # 支持的方法有：HEAD, GET, POST, PUT, DELETE, PATCH, OPTIONS
        self.methods = methods
        # 此条路由规则对应的请求路径。
        self.path = path
        # 资源名称
        self.resource_name = resource_name
        # 资源类型（和凭证关联资源类型一致）
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_runtime_endpoint_name is not None:
            result['agentRuntimeEndpointName'] = self.agent_runtime_endpoint_name

        if self.methods is not None:
            result['methods'] = self.methods

        if self.path is not None:
            result['path'] = self.path

        if self.resource_name is not None:
            result['resourceName'] = self.resource_name

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeEndpointName') is not None:
            self.agent_runtime_endpoint_name = m.get('agentRuntimeEndpointName')

        if m.get('methods') is not None:
            self.methods = m.get('methods')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

