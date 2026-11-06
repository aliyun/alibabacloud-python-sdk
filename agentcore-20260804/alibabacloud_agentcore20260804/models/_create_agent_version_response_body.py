# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateAgentVersionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateAgentVersionResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务状态码，请求成功时为 SUCCESS，失败时为错误码。
        self.code = code
        # 已保存的智能体固定版本详情；重复提交命中已有版本时返回该已有版本。
        self.data = data
        # HTTP 状态码。
        self.http_status_code = http_status_code
        # 响应消息，请求成功时为 success，失败时为错误信息。
        self.message = message
        # 请求 ID，用于定位和排查请求。
        self.request_id = request_id
        # 请求是否成功。
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.CreateAgentVersionResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreateAgentVersionResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_version: str = None,
        artifact_status: str = None,
        configuration: Dict[str, Any] = None,
        created_at: str = None,
        created_by: str = None,
        description: str = None,
        target_spec_version: int = None,
        version_name: str = None,
        workspace_id: str = None,
    ):
        # 版本所属的托管智能体或自定义智能体 ID。
        self.agent_id = agent_id
        # 系统按 Agent 递增生成的版本号，例如 v1、v2。查询、删除版本及服务端点引用版本时使用。
        self.agent_version = agent_version
        # 仅表示版本模板与制品归档是否完整，不代表部署或运行状态。READY 为完整，INVALID 为归档缺失或不一致。
        self.artifact_status = artifact_status
        # 托管智能体与 GetManagedAgent 的 data 结构一致，自定义智能体与 GetCustomAgent 的 data 结构一致，脱敏规则相同。
        self.configuration = configuration
        # 版本保存的时间，采用 ISO 8601 UTC 格式。
        self.created_at = created_at
        # 保存该版本的调用者阿里云账号 UID；RAM 用户调用时为其所属阿里云主账号 UID。
        self.created_by = created_by
        # 保存版本时填写的版本描述，最多 1024 个字符；保存时未填写则为空。
        self.description = description
        # 保存版本时 Agent 已生效的发布流水号，即当时的 effectiveSpecVersion。版本保存后该值不再变化。
        self.target_spec_version = target_spec_version
        # 保存版本时用户指定的展示名称。早期保存且未记录名称的版本返回 agentVersion。
        self.version_name = version_name
        # 版本所属智能体所在的 AgentCore 工作空间 ID。
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.agent_version is not None:
            result['agentVersion'] = self.agent_version

        if self.artifact_status is not None:
            result['artifactStatus'] = self.artifact_status

        if self.configuration is not None:
            result['configuration'] = self.configuration

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.description is not None:
            result['description'] = self.description

        if self.target_spec_version is not None:
            result['targetSpecVersion'] = self.target_spec_version

        if self.version_name is not None:
            result['versionName'] = self.version_name

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('agentVersion') is not None:
            self.agent_version = m.get('agentVersion')

        if m.get('artifactStatus') is not None:
            self.artifact_status = m.get('artifactStatus')

        if m.get('configuration') is not None:
            self.configuration = m.get('configuration')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('targetSpecVersion') is not None:
            self.target_spec_version = m.get('targetSpecVersion')

        if m.get('versionName') is not None:
            self.version_name = m.get('versionName')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

