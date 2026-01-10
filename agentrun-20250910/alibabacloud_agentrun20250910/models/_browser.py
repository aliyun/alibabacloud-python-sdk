# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class Browser(DaraModel):
    def __init__(
        self,
        browser_id: str = None,
        browser_name: str = None,
        cpu: float = None,
        created_at: str = None,
        credential_id: str = None,
        description: str = None,
        execution_role_arn: str = None,
        last_updated_at: str = None,
        memory: int = None,
        network_configuration: main_models.NetworkConfiguration = None,
        recording: main_models.BrowserRecordingConfiguration = None,
        status: str = None,
        status_reason: str = None,
        tenant_id: str = None,
    ):
        self.browser_id = browser_id
        self.browser_name = browser_name
        self.cpu = cpu
        self.created_at = created_at
        self.credential_id = credential_id
        self.description = description
        self.execution_role_arn = execution_role_arn
        self.last_updated_at = last_updated_at
        # 内存资源配置（单位：MB）
        self.memory = memory
        self.network_configuration = network_configuration
        self.recording = recording
        self.status = status
        # 当前状态的原因说明（如适用）
        self.status_reason = status_reason
        self.tenant_id = tenant_id

    def validate(self):
        if self.network_configuration:
            self.network_configuration.validate()
        if self.recording:
            self.recording.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_id is not None:
            result['browserId'] = self.browser_id

        if self.browser_name is not None:
            result['browserName'] = self.browser_name

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.credential_id is not None:
            result['credentialId'] = self.credential_id

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

        if self.recording is not None:
            result['recording'] = self.recording.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('browserId') is not None:
            self.browser_id = m.get('browserId')

        if m.get('browserName') is not None:
            self.browser_name = m.get('browserName')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('credentialId') is not None:
            self.credential_id = m.get('credentialId')

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

        if m.get('recording') is not None:
            temp_model = main_models.BrowserRecordingConfiguration()
            self.recording = temp_model.from_map(m.get('recording'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

