# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ResetWorkflowNodeConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        can_edit: bool = None,
        code: str = None,
        config_version: int = None,
        default_executor: main_models.ResetWorkflowNodeConfigurationResponseBodyDefaultExecutor = None,
        default_model: str = None,
        default_responsible_user_ids: List[str] = None,
        effective_executor: main_models.ResetWorkflowNodeConfigurationResponseBodyEffectiveExecutor = None,
        effective_model: str = None,
        effective_responsible_user_ids: List[str] = None,
        instance_id: str = None,
        message: str = None,
        node_id: str = None,
        overrides: main_models.ResetWorkflowNodeConfigurationResponseBodyOverrides = None,
        request_id: str = None,
        state_version: int = None,
        updated_at: str = None,
        updated_by: int = None,
    ):
        # 当前用户是否可编辑此节点
        self.can_edit = can_edit
        # 公共业务状态码
        self.code = code
        # 配置版本；更新或恢复时作为expectedVersion
        self.config_version = config_version
        # 模板默认执行主体
        self.default_executor = default_executor
        # 模板默认模型运行档
        self.default_model = default_model
        # 模板默认负责人用户ID列表
        self.default_responsible_user_ids = default_responsible_user_ids
        # 当前生效的执行主体
        self.effective_executor = effective_executor
        # 当前生效的模型运行档
        self.effective_model = effective_model
        # 当前生效的负责人用户ID列表
        self.effective_responsible_user_ids = effective_responsible_user_ids
        # 当前物理计划ID
        self.instance_id = instance_id
        # 公共错误描述
        self.message = message
        # 业务节点key
        self.node_id = node_id
        # 实例覆盖值；字段为null时使用模板默认值
        self.overrides = overrides
        # 请求追踪ID
        self.request_id = request_id
        # 状态刷新游标，不能作为配置版本
        self.state_version = state_version
        # 最后配置更新时间ISO8601；从未更新时为空
        self.updated_at = updated_at
        # 最后更新配置的平台用户ID；从未更新时为空
        self.updated_by = updated_by

    def validate(self):
        if self.default_executor:
            self.default_executor.validate()
        if self.effective_executor:
            self.effective_executor.validate()
        if self.overrides:
            self.overrides.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_edit is not None:
            result['canEdit'] = self.can_edit

        if self.code is not None:
            result['code'] = self.code

        if self.config_version is not None:
            result['configVersion'] = self.config_version

        if self.default_executor is not None:
            result['defaultExecutor'] = self.default_executor.to_map()

        if self.default_model is not None:
            result['defaultModel'] = self.default_model

        if self.default_responsible_user_ids is not None:
            result['defaultResponsibleUserIds'] = self.default_responsible_user_ids

        if self.effective_executor is not None:
            result['effectiveExecutor'] = self.effective_executor.to_map()

        if self.effective_model is not None:
            result['effectiveModel'] = self.effective_model

        if self.effective_responsible_user_ids is not None:
            result['effectiveResponsibleUserIds'] = self.effective_responsible_user_ids

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.message is not None:
            result['message'] = self.message

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.overrides is not None:
            result['overrides'] = self.overrides.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.state_version is not None:
            result['stateVersion'] = self.state_version

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('canEdit') is not None:
            self.can_edit = m.get('canEdit')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('configVersion') is not None:
            self.config_version = m.get('configVersion')

        if m.get('defaultExecutor') is not None:
            temp_model = main_models.ResetWorkflowNodeConfigurationResponseBodyDefaultExecutor()
            self.default_executor = temp_model.from_map(m.get('defaultExecutor'))

        if m.get('defaultModel') is not None:
            self.default_model = m.get('defaultModel')

        if m.get('defaultResponsibleUserIds') is not None:
            self.default_responsible_user_ids = m.get('defaultResponsibleUserIds')

        if m.get('effectiveExecutor') is not None:
            temp_model = main_models.ResetWorkflowNodeConfigurationResponseBodyEffectiveExecutor()
            self.effective_executor = temp_model.from_map(m.get('effectiveExecutor'))

        if m.get('effectiveModel') is not None:
            self.effective_model = m.get('effectiveModel')

        if m.get('effectiveResponsibleUserIds') is not None:
            self.effective_responsible_user_ids = m.get('effectiveResponsibleUserIds')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('overrides') is not None:
            temp_model = main_models.ResetWorkflowNodeConfigurationResponseBodyOverrides()
            self.overrides = temp_model.from_map(m.get('overrides'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('stateVersion') is not None:
            self.state_version = m.get('stateVersion')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')

        return self

class ResetWorkflowNodeConfigurationResponseBodyOverrides(DaraModel):
    def __init__(
        self,
        executor: main_models.ResetWorkflowNodeConfigurationResponseBodyOverridesExecutor = None,
        model: str = None,
        responsible_user_ids: List[int] = None,
    ):
        # 覆盖执行主体；null为默认
        self.executor = executor
        # 覆盖模型运行档；null为默认
        self.model = model
        # 覆盖负责人ID列表；null为默认
        self.responsible_user_ids = responsible_user_ids

    def validate(self):
        if self.executor:
            self.executor.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.executor is not None:
            result['executor'] = self.executor.to_map()

        if self.model is not None:
            result['model'] = self.model

        if self.responsible_user_ids is not None:
            result['responsibleUserIds'] = self.responsible_user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('executor') is not None:
            temp_model = main_models.ResetWorkflowNodeConfigurationResponseBodyOverridesExecutor()
            self.executor = temp_model.from_map(m.get('executor'))

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('responsibleUserIds') is not None:
            self.responsible_user_ids = m.get('responsibleUserIds')

        return self

class ResetWorkflowNodeConfigurationResponseBodyOverridesExecutor(DaraModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        # USER 为正整数平台用户ID字符串；AGENT 为空间数字员工技术名称
        self.id = id
        # USER 真人、AGENT 数字员工或历史 SYSTEM 系统执行人；SYSTEM仅用于响应
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ResetWorkflowNodeConfigurationResponseBodyEffectiveExecutor(DaraModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        # USER 为正整数平台用户ID字符串；AGENT 为空间数字员工技术名称
        self.id = id
        # USER 真人、AGENT 数字员工或历史 SYSTEM 系统执行人；SYSTEM仅用于响应
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ResetWorkflowNodeConfigurationResponseBodyDefaultExecutor(DaraModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        # USER 为正整数平台用户ID字符串；AGENT 为空间数字员工技术名称
        self.id = id
        # USER 真人、AGENT 数字员工或历史 SYSTEM 系统执行人；SYSTEM仅用于响应
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

