# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateCodeInterpreterInput(DaraModel):
    def __init__(
        self,
        code_interpreter_name: str = None,
        cpu: float = None,
        credential_id: str = None,
        description: str = None,
        execution_role_arn: str = None,
        memory: int = None,
        network_configuration: main_models.NetworkConfiguration = None,
        session_idle_timeout_seconds: int = None,
    ):
        # The name of the code interpreter. Use this to identify and distinguish code interpreter instances.
        # 
        # This parameter is required.
        self.code_interpreter_name = code_interpreter_name
        # The amount of CPU to allocate, in cores.
        # 
        # This parameter is required.
        self.cpu = cpu
        # The credential ID used for authentication.
        self.credential_id = credential_id
        # A description of the code interpreter.
        self.description = description
        # The Alibaba Cloud Resource Name (ARN) of the execution role for the code interpreter.
        self.execution_role_arn = execution_role_arn
        # The amount of memory to allocate, in megabytes (MB).
        # 
        # This parameter is required.
        self.memory = memory
        # Specifies the network configuration for the code interpreter, including VPC and security group settings.
        # 
        # This parameter is required.
        self.network_configuration = network_configuration
        # The idle timeout for a session, in seconds. If an instance has no new requests for this duration, its session expires and cannot be reused.
        self.session_idle_timeout_seconds = session_idle_timeout_seconds

    def validate(self):
        if self.network_configuration:
            self.network_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_interpreter_name is not None:
            result['codeInterpreterName'] = self.code_interpreter_name

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
        if m.get('codeInterpreterName') is not None:
            self.code_interpreter_name = m.get('codeInterpreterName')

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

