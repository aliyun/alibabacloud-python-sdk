# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateAgentRuntimeInput(DaraModel):
    def __init__(
        self,
        agent_runtime_name: str = None,
        arms_configuration: main_models.ArmsConfiguration = None,
        artifact_type: str = None,
        code_configuration: main_models.CodeConfiguration = None,
        container_configuration: main_models.ContainerConfiguration = None,
        cpu: float = None,
        credential_id: str = None,
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
        system_tags: List[str] = None,
        workspace_id: str = None,
    ):
        # A unique name for the agent runtime.
        # 
        # This parameter is required.
        self.agent_runtime_name = agent_runtime_name
        self.arms_configuration = arms_configuration
        # The deployment type for the agent runtime. Valid values: Code and Container.
        # 
        # This parameter is required.
        self.artifact_type = artifact_type
        # The code configuration, including the code source and entrypoint. This parameter is required when artifactType is Code.
        self.code_configuration = code_configuration
        # The container configuration, including the image URL and startup command. This parameter is required when artifactType is Container.
        self.container_configuration = container_configuration
        # The amount of CPU allocated to the agent runtime, in cores.
        # 
        # This parameter is required.
        self.cpu = cpu
        # The ID of the credential used to authenticate with external services.
        self.credential_id = credential_id
        # The name of the credential used to access the agent runtime.
        self.credential_name = credential_name
        # A description of the agent runtime.
        self.description = description
        # Specifies whether to disable on-demand elasticity. By default, on-demand elasticity is enabled.
        self.disable_ondemand = disable_ondemand
        # Specifies whether to disable session affinity. By default, session affinity is enabled.
        self.disable_session_affinity = disable_session_affinity
        # The disk size allocated to the agent runtime.
        self.disk_size = disk_size
        # The edition of the agent runtime.
        self.edition = edition
        # Specifies whether to enable session isolation. If enabled, each session runs in an isolated environment.
        self.enable_session_isolation = enable_session_isolation
        # A key-value map of environment variables to set for the agent runtime.
        self.environment_variables = environment_variables
        # The ARN of the execution role that the agent runtime uses to access cloud services.
        self.execution_role_arn = execution_role_arn
        # The endpoint URL of an external agent service.
        self.external_agent_endpoint_url = external_agent_endpoint_url
        # The name of the request header used for session affinity when sessionAffinityType is HEADER_FIELD.
        self.header_field_name = header_field_name
        # The health check configuration for the agent runtime, used to monitor the health of its instances.
        self.health_check_configuration = health_check_configuration
        # The Log Service configuration.
        self.log_configuration = log_configuration
        # The amount of memory allocated to the agent runtime, in MB.
        # 
        # This parameter is required.
        self.memory = memory
        # The configuration for mounting a NAS file system to the agent runtime.
        self.nas_config = nas_config
        # The network configuration for the agent runtime, including VPC and security group settings.
        # 
        # This parameter is required.
        self.network_configuration = network_configuration
        # The configuration for mounting an OSS bucket to the agent runtime.
        self.oss_mount_config = oss_mount_config
        # The port on which the agent runtime listens for external requests.
        # 
        # This parameter is required.
        self.port = port
        # The communication protocol configuration for the agent runtime.
        self.protocol_configuration = protocol_configuration
        # The ID of the resource group for the agent runtime.
        self.resource_group_id = resource_group_id
        # The session affinity mode. NONE disables session affinity. HEADER_FIELD enables session affinity based on a request header. GENERATED_COOKIE uses a service-generated cookie to maintain session affinity. COOKIE is a compatibility alias that the server normalizes to GENERATED_COOKIE.
        self.session_affinity_type = session_affinity_type
        # The maximum number of concurrent sessions allowed per runtime instance.
        self.session_concurrency_limit_per_instance = session_concurrency_limit_per_instance
        # The time in seconds that a session can remain idle before it expires and is terminated.
        self.session_idle_timeout_seconds = session_idle_timeout_seconds
        # The system tags for the agent runtime, used for system-level resource classification and management.
        self.system_tags = system_tags
        # The ID of the workspace for the agent runtime, used for resource isolation and access control.
        self.workspace_id = workspace_id

    def validate(self):
        if self.arms_configuration:
            self.arms_configuration.validate()
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
        if self.agent_runtime_name is not None:
            result['agentRuntimeName'] = self.agent_runtime_name

        if self.arms_configuration is not None:
            result['armsConfiguration'] = self.arms_configuration.to_map()

        if self.artifact_type is not None:
            result['artifactType'] = self.artifact_type

        if self.code_configuration is not None:
            result['codeConfiguration'] = self.code_configuration.to_map()

        if self.container_configuration is not None:
            result['containerConfiguration'] = self.container_configuration.to_map()

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.credential_id is not None:
            result['credentialId'] = self.credential_id

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

        if self.system_tags is not None:
            result['systemTags'] = self.system_tags

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeName') is not None:
            self.agent_runtime_name = m.get('agentRuntimeName')

        if m.get('armsConfiguration') is not None:
            temp_model = main_models.ArmsConfiguration()
            self.arms_configuration = temp_model.from_map(m.get('armsConfiguration'))

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

        if m.get('credentialId') is not None:
            self.credential_id = m.get('credentialId')

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

        if m.get('systemTags') is not None:
            self.system_tags = m.get('systemTags')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

