# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List, Any

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class UpdateTemplateInput(DaraModel):
    def __init__(
        self,
        allow_anonymous_manage: bool = None,
        arms_configuration: main_models.ArmsConfiguration = None,
        container_configuration: main_models.ContainerConfiguration = None,
        cpu: float = None,
        credential_configuration: main_models.CredentialConfiguration = None,
        description: str = None,
        environment_variables: Dict[str, str] = None,
        execution_role_arn: str = None,
        log_configuration: main_models.LogConfiguration = None,
        memory: int = None,
        network_configuration: main_models.NetworkConfiguration = None,
        oss_configuration: List[main_models.OssConfiguration] = None,
        sandbox_idle_timeout_in_seconds: int = None,
        sandbox_ttlin_seconds: int = None,
        template_configuration: Dict[str, Any] = None,
    ):
        self.allow_anonymous_manage = allow_anonymous_manage
        self.arms_configuration = arms_configuration
        # 容器配置（内置的不可改）
        self.container_configuration = container_configuration
        # CPU资源配置（单位：核心）
        self.cpu = cpu
        self.credential_configuration = credential_configuration
        self.description = description
        self.environment_variables = environment_variables
        self.execution_role_arn = execution_role_arn
        self.log_configuration = log_configuration
        # 内存资源配置（单位：MB）
        self.memory = memory
        self.network_configuration = network_configuration
        self.oss_configuration = oss_configuration
        # 沙箱空闲超时时间（秒）
        self.sandbox_idle_timeout_in_seconds = sandbox_idle_timeout_in_seconds
        # 沙箱存活时间（秒）
        self.sandbox_ttlin_seconds = sandbox_ttlin_seconds
        # 模板配置（灵活的对象结构，根据 templateType 不同而不同）
        self.template_configuration = template_configuration

    def validate(self):
        if self.arms_configuration:
            self.arms_configuration.validate()
        if self.container_configuration:
            self.container_configuration.validate()
        if self.credential_configuration:
            self.credential_configuration.validate()
        if self.log_configuration:
            self.log_configuration.validate()
        if self.network_configuration:
            self.network_configuration.validate()
        if self.oss_configuration:
            for v1 in self.oss_configuration:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_anonymous_manage is not None:
            result['allowAnonymousManage'] = self.allow_anonymous_manage

        if self.arms_configuration is not None:
            result['armsConfiguration'] = self.arms_configuration.to_map()

        if self.container_configuration is not None:
            result['containerConfiguration'] = self.container_configuration.to_map()

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.credential_configuration is not None:
            result['credentialConfiguration'] = self.credential_configuration.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables

        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn

        if self.log_configuration is not None:
            result['logConfiguration'] = self.log_configuration.to_map()

        if self.memory is not None:
            result['memory'] = self.memory

        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()

        result['ossConfiguration'] = []
        if self.oss_configuration is not None:
            for k1 in self.oss_configuration:
                result['ossConfiguration'].append(k1.to_map() if k1 else None)

        if self.sandbox_idle_timeout_in_seconds is not None:
            result['sandboxIdleTimeoutInSeconds'] = self.sandbox_idle_timeout_in_seconds

        if self.sandbox_ttlin_seconds is not None:
            result['sandboxTTLInSeconds'] = self.sandbox_ttlin_seconds

        if self.template_configuration is not None:
            result['templateConfiguration'] = self.template_configuration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowAnonymousManage') is not None:
            self.allow_anonymous_manage = m.get('allowAnonymousManage')

        if m.get('armsConfiguration') is not None:
            temp_model = main_models.ArmsConfiguration()
            self.arms_configuration = temp_model.from_map(m.get('armsConfiguration'))

        if m.get('containerConfiguration') is not None:
            temp_model = main_models.ContainerConfiguration()
            self.container_configuration = temp_model.from_map(m.get('containerConfiguration'))

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('credentialConfiguration') is not None:
            temp_model = main_models.CredentialConfiguration()
            self.credential_configuration = temp_model.from_map(m.get('credentialConfiguration'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')

        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')

        if m.get('logConfiguration') is not None:
            temp_model = main_models.LogConfiguration()
            self.log_configuration = temp_model.from_map(m.get('logConfiguration'))

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('networkConfiguration') is not None:
            temp_model = main_models.NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m.get('networkConfiguration'))

        self.oss_configuration = []
        if m.get('ossConfiguration') is not None:
            for k1 in m.get('ossConfiguration'):
                temp_model = main_models.OssConfiguration()
                self.oss_configuration.append(temp_model.from_map(k1))

        if m.get('sandboxIdleTimeoutInSeconds') is not None:
            self.sandbox_idle_timeout_in_seconds = m.get('sandboxIdleTimeoutInSeconds')

        if m.get('sandboxTTLInSeconds') is not None:
            self.sandbox_ttlin_seconds = m.get('sandboxTTLInSeconds')

        if m.get('templateConfiguration') is not None:
            self.template_configuration = m.get('templateConfiguration')

        return self

