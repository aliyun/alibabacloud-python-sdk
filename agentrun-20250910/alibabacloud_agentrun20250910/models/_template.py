# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List, Any

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class Template(DaraModel):
    def __init__(
        self,
        allow_anonymous_manage: bool = None,
        container_configuration: main_models.ContainerConfiguration = None,
        cpu: float = None,
        created_at: str = None,
        credential_configuration: main_models.CredentialConfiguration = None,
        description: str = None,
        disk_size: int = None,
        environment_variables: Dict[str, str] = None,
        execution_role_arn: str = None,
        last_updated_at: str = None,
        log_configuration: main_models.LogConfiguration = None,
        mcp_options: main_models.TemplateMcpOptions = None,
        mcp_state: main_models.TemplateMcpState = None,
        memory: int = None,
        network_configuration: main_models.NetworkConfiguration = None,
        oss_configuration: List[main_models.OssConfiguration] = None,
        resource_name: str = None,
        sandbox_idle_timeout_in_seconds: str = None,
        sandbox_ttlin_seconds: str = None,
        status: str = None,
        status_reason: str = None,
        template_arn: str = None,
        template_configuration: Dict[str, Any] = None,
        template_id: str = None,
        template_name: str = None,
        template_type: str = None,
        template_version: str = None,
    ):
        self.allow_anonymous_manage = allow_anonymous_manage
        self.container_configuration = container_configuration
        # This parameter is required.
        self.cpu = cpu
        self.created_at = created_at
        self.credential_configuration = credential_configuration
        self.description = description
        self.disk_size = disk_size
        self.environment_variables = environment_variables
        self.execution_role_arn = execution_role_arn
        self.last_updated_at = last_updated_at
        self.log_configuration = log_configuration
        self.mcp_options = mcp_options
        self.mcp_state = mcp_state
        # This parameter is required.
        self.memory = memory
        self.network_configuration = network_configuration
        self.oss_configuration = oss_configuration
        self.resource_name = resource_name
        self.sandbox_idle_timeout_in_seconds = sandbox_idle_timeout_in_seconds
        self.sandbox_ttlin_seconds = sandbox_ttlin_seconds
        self.status = status
        self.status_reason = status_reason
        self.template_arn = template_arn
        self.template_configuration = template_configuration
        # This parameter is required.
        self.template_id = template_id
        # This parameter is required.
        self.template_name = template_name
        self.template_type = template_type
        self.template_version = template_version

    def validate(self):
        if self.container_configuration:
            self.container_configuration.validate()
        if self.credential_configuration:
            self.credential_configuration.validate()
        if self.log_configuration:
            self.log_configuration.validate()
        if self.mcp_options:
            self.mcp_options.validate()
        if self.mcp_state:
            self.mcp_state.validate()
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

        if self.container_configuration is not None:
            result['containerConfiguration'] = self.container_configuration.to_map()

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.credential_configuration is not None:
            result['credentialConfiguration'] = self.credential_configuration.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.disk_size is not None:
            result['diskSize'] = self.disk_size

        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables

        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn

        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at

        if self.log_configuration is not None:
            result['logConfiguration'] = self.log_configuration.to_map()

        if self.mcp_options is not None:
            result['mcpOptions'] = self.mcp_options.to_map()

        if self.mcp_state is not None:
            result['mcpState'] = self.mcp_state.to_map()

        if self.memory is not None:
            result['memory'] = self.memory

        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()

        result['ossConfiguration'] = []
        if self.oss_configuration is not None:
            for k1 in self.oss_configuration:
                result['ossConfiguration'].append(k1.to_map() if k1 else None)

        if self.resource_name is not None:
            result['resourceName'] = self.resource_name

        if self.sandbox_idle_timeout_in_seconds is not None:
            result['sandboxIdleTimeoutInSeconds'] = self.sandbox_idle_timeout_in_seconds

        if self.sandbox_ttlin_seconds is not None:
            result['sandboxTTLInSeconds'] = self.sandbox_ttlin_seconds

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        if self.template_arn is not None:
            result['templateArn'] = self.template_arn

        if self.template_configuration is not None:
            result['templateConfiguration'] = self.template_configuration

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.template_type is not None:
            result['templateType'] = self.template_type

        if self.template_version is not None:
            result['templateVersion'] = self.template_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowAnonymousManage') is not None:
            self.allow_anonymous_manage = m.get('allowAnonymousManage')

        if m.get('containerConfiguration') is not None:
            temp_model = main_models.ContainerConfiguration()
            self.container_configuration = temp_model.from_map(m.get('containerConfiguration'))

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('credentialConfiguration') is not None:
            temp_model = main_models.CredentialConfiguration()
            self.credential_configuration = temp_model.from_map(m.get('credentialConfiguration'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')

        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')

        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')

        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')

        if m.get('logConfiguration') is not None:
            temp_model = main_models.LogConfiguration()
            self.log_configuration = temp_model.from_map(m.get('logConfiguration'))

        if m.get('mcpOptions') is not None:
            temp_model = main_models.TemplateMcpOptions()
            self.mcp_options = temp_model.from_map(m.get('mcpOptions'))

        if m.get('mcpState') is not None:
            temp_model = main_models.TemplateMcpState()
            self.mcp_state = temp_model.from_map(m.get('mcpState'))

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

        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')

        if m.get('sandboxIdleTimeoutInSeconds') is not None:
            self.sandbox_idle_timeout_in_seconds = m.get('sandboxIdleTimeoutInSeconds')

        if m.get('sandboxTTLInSeconds') is not None:
            self.sandbox_ttlin_seconds = m.get('sandboxTTLInSeconds')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        if m.get('templateArn') is not None:
            self.template_arn = m.get('templateArn')

        if m.get('templateConfiguration') is not None:
            self.template_configuration = m.get('templateConfiguration')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('templateType') is not None:
            self.template_type = m.get('templateType')

        if m.get('templateVersion') is not None:
            self.template_version = m.get('templateVersion')

        return self

class TemplateMcpState(DaraModel):
    def __init__(
        self,
        access_endpoint: str = None,
        status: str = None,
        status_reason: str = None,
    ):
        self.access_endpoint = access_endpoint
        self.status = status
        self.status_reason = status_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_endpoint is not None:
            result['accessEndpoint'] = self.access_endpoint

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessEndpoint') is not None:
            self.access_endpoint = m.get('accessEndpoint')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        return self

class TemplateMcpOptions(DaraModel):
    def __init__(
        self,
        enabled_tools: List[str] = None,
        transport: str = None,
    ):
        self.enabled_tools = enabled_tools
        self.transport = transport

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled_tools is not None:
            result['enabledTools'] = self.enabled_tools

        if self.transport is not None:
            result['transport'] = self.transport

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabledTools') is not None:
            self.enabled_tools = m.get('enabledTools')

        if m.get('transport') is not None:
            self.transport = m.get('transport')

        return self

