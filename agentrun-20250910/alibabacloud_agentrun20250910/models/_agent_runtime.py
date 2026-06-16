# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class AgentRuntime(DaraModel):
    def __init__(
        self,
        agent_runtime_arn: str = None,
        agent_runtime_id: str = None,
        agent_runtime_name: str = None,
        agent_runtime_version: str = None,
        artifact_type: str = None,
        code_configuration: main_models.CodeConfiguration = None,
        container_configuration: main_models.ContainerConfiguration = None,
        cpu: float = None,
        created_at: str = None,
        credential_name: str = None,
        description: str = None,
        disable_ondemand: bool = None,
        disable_session_affinity: bool = None,
        disk_size: int = None,
        edition: str = None,
        enable_session_isolation: bool = None,
        environment_variables: Dict[str, str] = None,
        execution_role_arn: str = None,
        external_agent_endpoint_url: str = None,
        header_field_name: str = None,
        health_check_configuration: main_models.HealthCheckConfiguration = None,
        last_updated_at: str = None,
        log_configuration: main_models.LogConfiguration = None,
        memory: int = None,
        nas_config: main_models.NASConfig = None,
        network_configuration: main_models.NetworkConfiguration = None,
        oss_mount_config: main_models.OSSMountConfig = None,
        port: int = None,
        protocol_configuration: main_models.ProtocolConfiguration = None,
        resource_group_id: str = None,
        session_affinity_type: str = None,
        session_concurrency_limit_per_instance: int = None,
        session_idle_timeout_seconds: int = None,
        status: str = None,
        status_reason: str = None,
        system_tags: List[str] = None,
        workspace_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the agent runtime.
        self.agent_runtime_arn = agent_runtime_arn
        # The unique identifier of the agent runtime.
        self.agent_runtime_id = agent_runtime_id
        # The name of the agent runtime.
        self.agent_runtime_name = agent_runtime_name
        # The version number of the agent runtime.
        self.agent_runtime_version = agent_runtime_version
        # The deployment type of the agent runtime. Valid values: `Code` and `Container`.
        self.artifact_type = artifact_type
        # The code configuration details. This parameter is applicable when `artifactType` is set to `Code`.
        self.code_configuration = code_configuration
        # The container configuration details. This parameter is applicable when `artifactType` is set to `Container`.
        self.container_configuration = container_configuration
        # The amount of CPU allocated to the agent runtime, in vCPUs.
        self.cpu = cpu
        # The creation time of the agent runtime, in ISO 8601 format.
        self.created_at = created_at
        # The name of the credential used to authenticate requests to the agent runtime.
        self.credential_name = credential_name
        # The description of the agent runtime.
        self.description = description
        # Specifies whether to disable on-demand elasticity. Default: `false`.
        self.disable_ondemand = disable_ondemand
        # Specifies whether to disable session affinity. Default: `false`.
        self.disable_session_affinity = disable_session_affinity
        # The disk size.
        self.disk_size = disk_size
        # The edition of the agent runtime.
        self.edition = edition
        # Specifies whether to enable session isolation. If enabled, each session runs in an isolated environment.
        self.enable_session_isolation = enable_session_isolation
        # The environment variables for the agent runtime.
        self.environment_variables = environment_variables
        # The ARN of the execution role that grants the agent runtime permission to access cloud services.
        self.execution_role_arn = execution_role_arn
        # The endpoint URL of an externally deployed agent service.
        self.external_agent_endpoint_url = external_agent_endpoint_url
        # The name of the request header used for session affinity when `sessionAffinityType` is `HEADER_FIELD`.
        self.header_field_name = header_field_name
        # The health check configuration.
        self.health_check_configuration = health_check_configuration
        # The last update time of the agent runtime, in ISO 8601 format.
        self.last_updated_at = last_updated_at
        # The Log Service configuration.
        self.log_configuration = log_configuration
        # The amount of memory allocated to the agent runtime, in MB.
        self.memory = memory
        # The NAS file system configuration.
        self.nas_config = nas_config
        # The network configuration of the agent runtime.
        self.network_configuration = network_configuration
        # The OSS bucket mount configuration.
        self.oss_mount_config = oss_mount_config
        # The port on which the agent runtime listens.
        self.port = port
        # The communication protocol configuration for the agent runtime.
        self.protocol_configuration = protocol_configuration
        # The ID of the resource group to which the agent runtime belongs.
        self.resource_group_id = resource_group_id
        # The session affinity mode. Valid values: `NONE`, `HEADER_FIELD`, and `GENERATED_COOKIE`. `COOKIE` is a compatibility alias for `GENERATED_COOKIE`.
        self.session_affinity_type = session_affinity_type
        # The maximum number of concurrent sessions allowed per runtime instance.
        self.session_concurrency_limit_per_instance = session_concurrency_limit_per_instance
        # The idle timeout period for a session, in seconds. After this period of inactivity, the session expires and can no longer be used.
        self.session_idle_timeout_seconds = session_idle_timeout_seconds
        # The current status of the agent runtime. Possible values: `READY`, `CREATING`, and `FAILED`.
        self.status = status
        # The reason for the current status.
        self.status_reason = status_reason
        # The system tags for the agent runtime.
        self.system_tags = system_tags
        # The ID of the workspace for the agent runtime.
        self.workspace_id = workspace_id

    def validate(self):
        if self.code_configuration:
            self.code_configuration.validate()
        if self.container_configuration:
            self.container_configuration.validate()
        if self.health_check_configuration:
            self.health_check_configuration.validate()
        if self.log_configuration:
            self.log_configuration.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.network_configuration:
            self.network_configuration.validate()
        if self.oss_mount_config:
            self.oss_mount_config.validate()
        if self.protocol_configuration:
            self.protocol_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_runtime_arn is not None:
            result['agentRuntimeArn'] = self.agent_runtime_arn

        if self.agent_runtime_id is not None:
            result['agentRuntimeId'] = self.agent_runtime_id

        if self.agent_runtime_name is not None:
            result['agentRuntimeName'] = self.agent_runtime_name

        if self.agent_runtime_version is not None:
            result['agentRuntimeVersion'] = self.agent_runtime_version

        if self.artifact_type is not None:
            result['artifactType'] = self.artifact_type

        if self.code_configuration is not None:
            result['codeConfiguration'] = self.code_configuration.to_map()

        if self.container_configuration is not None:
            result['containerConfiguration'] = self.container_configuration.to_map()

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.credential_name is not None:
            result['credentialName'] = self.credential_name

        if self.description is not None:
            result['description'] = self.description

        if self.disable_ondemand is not None:
            result['disableOndemand'] = self.disable_ondemand

        if self.disable_session_affinity is not None:
            result['disableSessionAffinity'] = self.disable_session_affinity

        if self.disk_size is not None:
            result['diskSize'] = self.disk_size

        if self.edition is not None:
            result['edition'] = self.edition

        if self.enable_session_isolation is not None:
            result['enableSessionIsolation'] = self.enable_session_isolation

        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables

        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn

        if self.external_agent_endpoint_url is not None:
            result['externalAgentEndpointUrl'] = self.external_agent_endpoint_url

        if self.header_field_name is not None:
            result['headerFieldName'] = self.header_field_name

        if self.health_check_configuration is not None:
            result['healthCheckConfiguration'] = self.health_check_configuration.to_map()

        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at

        if self.log_configuration is not None:
            result['logConfiguration'] = self.log_configuration.to_map()

        if self.memory is not None:
            result['memory'] = self.memory

        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()

        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()

        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()

        if self.port is not None:
            result['port'] = self.port

        if self.protocol_configuration is not None:
            result['protocolConfiguration'] = self.protocol_configuration.to_map()

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.session_affinity_type is not None:
            result['sessionAffinityType'] = self.session_affinity_type

        if self.session_concurrency_limit_per_instance is not None:
            result['sessionConcurrencyLimitPerInstance'] = self.session_concurrency_limit_per_instance

        if self.session_idle_timeout_seconds is not None:
            result['sessionIdleTimeoutSeconds'] = self.session_idle_timeout_seconds

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        if self.system_tags is not None:
            result['systemTags'] = self.system_tags

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeArn') is not None:
            self.agent_runtime_arn = m.get('agentRuntimeArn')

        if m.get('agentRuntimeId') is not None:
            self.agent_runtime_id = m.get('agentRuntimeId')

        if m.get('agentRuntimeName') is not None:
            self.agent_runtime_name = m.get('agentRuntimeName')

        if m.get('agentRuntimeVersion') is not None:
            self.agent_runtime_version = m.get('agentRuntimeVersion')

        if m.get('artifactType') is not None:
            self.artifact_type = m.get('artifactType')

        if m.get('codeConfiguration') is not None:
            temp_model = main_models.CodeConfiguration()
            self.code_configuration = temp_model.from_map(m.get('codeConfiguration'))

        if m.get('containerConfiguration') is not None:
            temp_model = main_models.ContainerConfiguration()
            self.container_configuration = temp_model.from_map(m.get('containerConfiguration'))

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('credentialName') is not None:
            self.credential_name = m.get('credentialName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('disableOndemand') is not None:
            self.disable_ondemand = m.get('disableOndemand')

        if m.get('disableSessionAffinity') is not None:
            self.disable_session_affinity = m.get('disableSessionAffinity')

        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')

        if m.get('edition') is not None:
            self.edition = m.get('edition')

        if m.get('enableSessionIsolation') is not None:
            self.enable_session_isolation = m.get('enableSessionIsolation')

        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')

        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')

        if m.get('externalAgentEndpointUrl') is not None:
            self.external_agent_endpoint_url = m.get('externalAgentEndpointUrl')

        if m.get('headerFieldName') is not None:
            self.header_field_name = m.get('headerFieldName')

        if m.get('healthCheckConfiguration') is not None:
            temp_model = main_models.HealthCheckConfiguration()
            self.health_check_configuration = temp_model.from_map(m.get('healthCheckConfiguration'))

        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')

        if m.get('logConfiguration') is not None:
            temp_model = main_models.LogConfiguration()
            self.log_configuration = temp_model.from_map(m.get('logConfiguration'))

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('nasConfig') is not None:
            temp_model = main_models.NASConfig()
            self.nas_config = temp_model.from_map(m.get('nasConfig'))

        if m.get('networkConfiguration') is not None:
            temp_model = main_models.NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m.get('networkConfiguration'))

        if m.get('ossMountConfig') is not None:
            temp_model = main_models.OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m.get('ossMountConfig'))

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocolConfiguration') is not None:
            temp_model = main_models.ProtocolConfiguration()
            self.protocol_configuration = temp_model.from_map(m.get('protocolConfiguration'))

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('sessionAffinityType') is not None:
            self.session_affinity_type = m.get('sessionAffinityType')

        if m.get('sessionConcurrencyLimitPerInstance') is not None:
            self.session_concurrency_limit_per_instance = m.get('sessionConcurrencyLimitPerInstance')

        if m.get('sessionIdleTimeoutSeconds') is not None:
            self.session_idle_timeout_seconds = m.get('sessionIdleTimeoutSeconds')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        if m.get('systemTags') is not None:
            self.system_tags = m.get('systemTags')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

