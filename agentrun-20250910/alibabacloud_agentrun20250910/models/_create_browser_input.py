# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateBrowserInput(DaraModel):
    def __init__(
        self,
        browser_name: str = None,
        cpu: float = None,
        credential_id: str = None,
        description: str = None,
        execution_role_arn: str = None,
        memory: int = None,
        network_configuration: main_models.NetworkConfiguration = None,
        session_idle_timeout_seconds: int = None,
    ):
        # This parameter is required.
        self.browser_name = browser_name
        # CPU资源配置（单位：核）
        # 
        # This parameter is required.
        self.cpu = cpu
        self.credential_id = credential_id
        self.description = description
        self.execution_role_arn = execution_role_arn
        # 内存资源配置（单位：MB）
        # 
        # This parameter is required.
        self.memory = memory
        # This parameter is required.
        self.network_configuration = network_configuration
        # 会话的空闲超时时间，单位为秒。实例没有会话请求后处于空闲状态，空闲态为闲置计费模式，超过此超时时间后会话自动过期，不可继续使用
        self.session_idle_timeout_seconds = session_idle_timeout_seconds

    def validate(self):
        if self.network_configuration:
            self.network_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_name is not None:
            result['browserName'] = self.browser_name

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.credential_id is not None:
            result['credentialId'] = self.credential_id

        if self.description is not None:
            result['description'] = self.description

        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn

        if self.memory is not None:
            result['memory'] = self.memory

        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()

        if self.session_idle_timeout_seconds is not None:
            result['sessionIdleTimeoutSeconds'] = self.session_idle_timeout_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('browserName') is not None:
            self.browser_name = m.get('browserName')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('credentialId') is not None:
            self.credential_id = m.get('credentialId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('networkConfiguration') is not None:
            temp_model = main_models.NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m.get('networkConfiguration'))

        if m.get('sessionIdleTimeoutSeconds') is not None:
            self.session_idle_timeout_seconds = m.get('sessionIdleTimeoutSeconds')

        return self

