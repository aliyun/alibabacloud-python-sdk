# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IMBotMetadata(DaraModel):
    def __init__(
        self,
        agent_runtime_endpoint_id: str = None,
        agent_runtime_endpoint_url: str = None,
        agent_runtime_id: str = None,
        custom_function_meta: str = None,
        protocol_type: str = None,
        role: str = None,
    ):
        # 可选
        self.agent_runtime_endpoint_id = agent_runtime_endpoint_id
        # 标准模式下必填：下游 Agent 可调用的 URL；custom 模式可省略
        self.agent_runtime_endpoint_url = agent_runtime_endpoint_url
        # 绑定的 Agent Runtime UUID
        self.agent_runtime_id = agent_runtime_id
        # 自定义函数元信息；可选；与后端 IMBotMetadata 持久化字段一致
        self.custom_function_meta = custom_function_meta
        # 标准模式下必填，与 ValidateAgentRuntimeProtocolTypeValue 一致（大小写敏感）；custom 模式可省略
        self.protocol_type = protocol_type
        # 不写入单 Bot 持久化 JSON；用于首次/更新时设置租户级 FC RAM 执行角色 ARN（acs:ram::...）；FC 启用且非 custom 时按服务逻辑校验
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_runtime_endpoint_id is not None:
            result['agentRuntimeEndpointId'] = self.agent_runtime_endpoint_id

        if self.agent_runtime_endpoint_url is not None:
            result['agentRuntimeEndpointUrl'] = self.agent_runtime_endpoint_url

        if self.agent_runtime_id is not None:
            result['agentRuntimeId'] = self.agent_runtime_id

        if self.custom_function_meta is not None:
            result['customFunctionMeta'] = self.custom_function_meta

        if self.protocol_type is not None:
            result['protocolType'] = self.protocol_type

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeEndpointId') is not None:
            self.agent_runtime_endpoint_id = m.get('agentRuntimeEndpointId')

        if m.get('agentRuntimeEndpointUrl') is not None:
            self.agent_runtime_endpoint_url = m.get('agentRuntimeEndpointUrl')

        if m.get('agentRuntimeId') is not None:
            self.agent_runtime_id = m.get('agentRuntimeId')

        if m.get('customFunctionMeta') is not None:
            self.custom_function_meta = m.get('customFunctionMeta')

        if m.get('protocolType') is not None:
            self.protocol_type = m.get('protocolType')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

