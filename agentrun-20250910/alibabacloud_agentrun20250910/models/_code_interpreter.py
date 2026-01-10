# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CodeInterpreter(DaraModel):
    def __init__(
        self,
        code_interpreter_id: str = None,
        code_interpreter_name: str = None,
        cpu: float = None,
        created_at: str = None,
        description: str = None,
        execution_role_arn: str = None,
        last_updated_at: str = None,
        memory: int = None,
        network_configuration: main_models.NetworkConfiguration = None,
        status: str = None,
        status_reason: str = None,
        tenant_id: str = None,
    ):
        # 代码解释器的唯一标识符
        self.code_interpreter_id = code_interpreter_id
        # 代码解释器的名称，用于标识和区分不同的代码解释器实例
        self.code_interpreter_name = code_interpreter_name
        self.cpu = cpu
        # 代码解释器的创建时间，采用ISO 8601格式
        self.created_at = created_at
        # 代码解释器的描述信息，说明该解释器的用途和功能
        self.description = description
        # 此代码解释器的执行角色
        self.execution_role_arn = execution_role_arn
        # 代码解释器的最后更新时间，采用ISO 8601格式
        self.last_updated_at = last_updated_at
        # 内存资源配置（单位：MB）
        self.memory = memory
        # 代码解释器的网络配置信息
        self.network_configuration = network_configuration
        # 代码解释器的当前状态，如READY（就绪）、TERMINATED（已终止）等
        self.status = status
        # 当前状态的原因说明（如适用）
        self.status_reason = status_reason
        self.tenant_id = tenant_id

    def validate(self):
        if self.network_configuration:
            self.network_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_interpreter_id is not None:
            result['codeInterpreterId'] = self.code_interpreter_id

        if self.code_interpreter_name is not None:
            result['codeInterpreterName'] = self.code_interpreter_name

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn

        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at

        if self.memory is not None:
            result['memory'] = self.memory

        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeInterpreterId') is not None:
            self.code_interpreter_id = m.get('codeInterpreterId')

        if m.get('codeInterpreterName') is not None:
            self.code_interpreter_name = m.get('codeInterpreterName')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')

        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('networkConfiguration') is not None:
            temp_model = main_models.NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m.get('networkConfiguration'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

