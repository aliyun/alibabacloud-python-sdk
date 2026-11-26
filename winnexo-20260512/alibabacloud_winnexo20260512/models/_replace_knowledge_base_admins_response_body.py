# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ReplaceKnowledgeBaseAdminsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        creator: main_models.ReplaceKnowledgeBaseAdminsResponseBodyCreator = None,
        directory_id: str = None,
        effective_approvers: List[main_models.ReplaceKnowledgeBaseAdminsResponseBodyEffectiveApprovers] = None,
        message: str = None,
        principals: List[main_models.ReplaceKnowledgeBaseAdminsResponseBodyPrincipals] = None,
        request_id: str = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码
        self.code = code
        # 知识库创建者
        self.creator = creator
        # 已配置的知识库根目录业务 ID
        self.directory_id = directory_id
        # 用户组展开和去重后的有效审批人
        self.effective_approvers = effective_approvers
        # 错误描述，成功时为空
        self.message = message
        # 配置完成后的管理员主体列表，包含创建者
        self.principals = principals
        # 请求追踪 ID
        self.request_id = request_id

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.effective_approvers:
            for v1 in self.effective_approvers:
                 if v1:
                    v1.validate()
        if self.principals:
            for v1 in self.principals:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.creator is not None:
            result['creator'] = self.creator.to_map()

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        result['effectiveApprovers'] = []
        if self.effective_approvers is not None:
            for k1 in self.effective_approvers:
                result['effectiveApprovers'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        result['principals'] = []
        if self.principals is not None:
            for k1 in self.principals:
                result['principals'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('creator') is not None:
            temp_model = main_models.ReplaceKnowledgeBaseAdminsResponseBodyCreator()
            self.creator = temp_model.from_map(m.get('creator'))

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        self.effective_approvers = []
        if m.get('effectiveApprovers') is not None:
            for k1 in m.get('effectiveApprovers'):
                temp_model = main_models.ReplaceKnowledgeBaseAdminsResponseBodyEffectiveApprovers()
                self.effective_approvers.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        self.principals = []
        if m.get('principals') is not None:
            for k1 in m.get('principals'):
                temp_model = main_models.ReplaceKnowledgeBaseAdminsResponseBodyPrincipals()
                self.principals.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ReplaceKnowledgeBaseAdminsResponseBodyPrincipals(DaraModel):
    def __init__(
        self,
        immutable: bool = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        source: str = None,
    ):
        # 是否为不可移除的创建者
        self.immutable = immutable
        # 用户 ID 或用户组 ID
        self.principal_id = principal_id
        # 主体显示名称，无法解析时为空
        self.principal_name = principal_name
        # 主体类型：USER 或 USER_GROUP
        self.principal_type = principal_type
        # 权限来源：CREATOR 或 DIRECT
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.immutable is not None:
            result['immutable'] = self.immutable

        if self.principal_id is not None:
            result['principalId'] = self.principal_id

        if self.principal_name is not None:
            result['principalName'] = self.principal_name

        if self.principal_type is not None:
            result['principalType'] = self.principal_type

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')

        if m.get('principalId') is not None:
            self.principal_id = m.get('principalId')

        if m.get('principalName') is not None:
            self.principal_name = m.get('principalName')

        if m.get('principalType') is not None:
            self.principal_type = m.get('principalType')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

class ReplaceKnowledgeBaseAdminsResponseBodyEffectiveApprovers(DaraModel):
    def __init__(
        self,
        source_principal_ids: List[str] = None,
        user_id: int = None,
        user_name: str = None,
    ):
        # 产生该审批权限的主体 ID 列表
        self.source_principal_ids = source_principal_ids
        # 有效审批用户 ID
        self.user_id = user_id
        # 租户内显示名称，无法解析时为空
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_principal_ids is not None:
            result['sourcePrincipalIds'] = self.source_principal_ids

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourcePrincipalIds') is not None:
            self.source_principal_ids = m.get('sourcePrincipalIds')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

class ReplaceKnowledgeBaseAdminsResponseBodyCreator(DaraModel):
    def __init__(
        self,
        immutable: bool = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        source: str = None,
    ):
        # 是否为不可移除的创建者
        self.immutable = immutable
        # 用户 ID 或用户组 ID
        self.principal_id = principal_id
        # 主体显示名称，无法解析时为空
        self.principal_name = principal_name
        # 主体类型：USER 或 USER_GROUP
        self.principal_type = principal_type
        # 权限来源：CREATOR 或 DIRECT
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.immutable is not None:
            result['immutable'] = self.immutable

        if self.principal_id is not None:
            result['principalId'] = self.principal_id

        if self.principal_name is not None:
            result['principalName'] = self.principal_name

        if self.principal_type is not None:
            result['principalType'] = self.principal_type

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')

        if m.get('principalId') is not None:
            self.principal_id = m.get('principalId')

        if m.get('principalName') is not None:
            self.principal_name = m.get('principalName')

        if m.get('principalType') is not None:
            self.principal_type = m.get('principalType')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

