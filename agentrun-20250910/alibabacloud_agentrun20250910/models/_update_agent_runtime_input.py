# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class UpdateAgentRuntimeInput(DaraModel):
    def __init__(
        self,
        agent_runtime_name: str = None,
        arms_configuration: main_models.ArmsConfiguration = None,
        artifact_type: str = None,
        code_configuration: main_models.CodeConfiguration = None,
        container_configuration: main_models.ContainerConfiguration = None,
        cpu: float = None,
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
        force_evict_instances: bool = None,
        header_field_name: str = None,
        health_check_configuration: main_models.HealthCheckConfiguration = None,
        log_configuration: main_models.LogConfiguration = None,
        memory: int = None,
        nas_config: main_models.NASConfig = None,
        network_configuration: main_models.NetworkConfiguration = None,
        oss_mount_config: main_models.OSSMountConfig = None,
        port: int = None,
        protocol_configuration: main_models.ProtocolConfiguration = None,
        session_affinity_type: str = None,
        session_concurrency_limit_per_instance: int = None,
        session_idle_timeout_seconds: int = None,
        system_tags: List[str] = None,
        workspace_id: str = None,
    ):
        # The name of the agent runtime.
        self.agent_runtime_name = agent_runtime_name
        # 应用实时监控服务（ARMS）的配置信息
        self.arms_configuration = arms_configuration
        # The artifact type.
        self.artifact_type = artifact_type
        # The code configuration.
        self.code_configuration = code_configuration
        # The container configuration.
        self.container_configuration = container_configuration
        # The number of CPU cores.
        # 
        # This parameter is required.
        self.cpu = cpu
        # The name of the credential that the agent runtime uses to authenticate requests.
        self.credential_name = credential_name
        # The description of the agent runtime.
        self.description = description
        # Specifies whether to disable on-demand elasticity. Set to true to disable. Default: false.
        self.disable_ondemand = disable_ondemand
        # Specifies whether to disable session affinity. Set to true to disable. Default: false.
        self.disable_session_affinity = disable_session_affinity
        # The disk size in gigabytes (GB).
        self.disk_size = disk_size
        self.edition = edition
        # Specifies whether to enable session isolation. If enabled, each session runs in an isolated environment.
        self.enable_session_isolation = enable_session_isolation
        # Environment variables for the agent runtime.
        self.environment_variables = environment_variables
        # The execution role ARN that grants the agent runtime permissions to access cloud services.
        self.execution_role_arn = execution_role_arn
        # The endpoint URL for an externally registered agent. The platform uses this URL to connect to an agent service deployed outside the platform.
        self.external_agent_endpoint_url = external_agent_endpoint_url
        # Specifies whether to perform a best-effort eviction of active Function Compute (FC) sessions when the configuration is updated. This helps the new settings take effect faster.
        self.force_evict_instances = force_evict_instances
        # The name of the request header used for session affinity when sessionAffinityType is set to "HEADER_FIELD".
        self.header_field_name = header_field_name
        # The health check configuration for monitoring the health of agent runtime instances.
        self.health_check_configuration = health_check_configuration
        # The configuration for Simple Log Service (SLS).
        self.log_configuration = log_configuration
        # The amount of memory in megabytes (MB).
        self.memory = memory
        # Configuration for mounting a NAS file system to the agent runtime.
        self.nas_config = nas_config
        # The network configuration.
        self.network_configuration = network_configuration
        # Configuration for mounting an OSS bucket to the agent runtime.
        self.oss_mount_config = oss_mount_config
        # The port on which the agent service listens.
        self.port = port
        # The protocol configuration.
        self.protocol_configuration = protocol_configuration
        # The session affinity mode. Valid values: NONE (disables session affinity), HEADER_FIELD (routes requests based on a request header), and GENERATED_COOKIE (routes requests using a cookie generated by Function Compute (FC)). The value COOKIE is an alias for GENERATED_COOKIE.
        self.session_affinity_type = session_affinity_type
        # The maximum number of concurrent sessions allowed per runtime instance.
        self.session_concurrency_limit_per_instance = session_concurrency_limit_per_instance
        # The idle timeout for a session, in seconds. If an instance remains idle longer than this timeout after receiving no requests, the session expires.
        self.session_idle_timeout_seconds = session_idle_timeout_seconds
        # The system tags for the agent runtime, used for resource classification and management.
        self.system_tags = system_tags
        # The ID of the workspace.
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

        if self.force_evict_instances is not None:
            result['forceEvictInstances'] = self.force_evict_instances

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

        if m.get('forceEvictInstances') is not None:
            self.force_evict_instances = m.get('forceEvictInstances')

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

