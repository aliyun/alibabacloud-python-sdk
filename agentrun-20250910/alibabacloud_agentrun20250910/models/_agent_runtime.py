# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

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
        environment_variables: Dict[str, str] = None,
        execution_role_arn: str = None,
        health_check_configuration: main_models.HealthCheckConfiguration = None,
        last_updated_at: str = None,
        log_configuration: main_models.LogConfiguration = None,
        memory: int = None,
        network_configuration: main_models.NetworkConfiguration = None,
        port: int = None,
        protocol_configuration: main_models.ProtocolConfiguration = None,
        resource_group_id: str = None,
        session_concurrency_limit_per_instance: int = None,
        session_idle_timeout_seconds: int = None,
        status: str = None,
        status_reason: str = None,
    ):
        # 智能体运行时的全局唯一资源名称
        self.agent_runtime_arn = agent_runtime_arn
        # 智能体运行时的唯一标识符
        self.agent_runtime_id = agent_runtime_id
        # 智能体运行时的名称，用于标识和区分不同的运行时实例
        self.agent_runtime_name = agent_runtime_name
        # 智能体运行时的版本号，用于版本管理和回滚
        self.agent_runtime_version = agent_runtime_version
        # 智能体运行时的部署类型，支持Code（代码模式）和Container（容器模式）
        self.artifact_type = artifact_type
        # 当artifactType为Code时的代码配置信息
        self.code_configuration = code_configuration
        # 当artifactType为Container时的容器配置信息
        self.container_configuration = container_configuration
        # 智能体运行时分配的CPU资源，单位为核数
        self.cpu = cpu
        # 智能体运行时的创建时间，采用ISO 8601格式
        self.created_at = created_at
        # 用于访问智能体的凭证名称，访问智能体运行时将使用此凭证进行身份验证
        self.credential_name = credential_name
        # 智能体运行时的描述信息，说明该运行时的用途和功能
        self.description = description
        # 智能体运行时的环境变量配置
        self.environment_variables = environment_variables
        # 为智能体运行时提供访问云服务权限的执行角色ARN
        self.execution_role_arn = execution_role_arn
        # 智能体运行时的健康检查配置，用于监控运行时实例的健康状态
        self.health_check_configuration = health_check_configuration
        # 智能体运行时最后一次更新的时间，采用ISO 8601格式
        self.last_updated_at = last_updated_at
        # SLS（简单日志服务）配置
        self.log_configuration = log_configuration
        # 智能体运行时分配的内存资源，单位为MB
        self.memory = memory
        # 智能体运行时的网络配置信息
        self.network_configuration = network_configuration
        # 智能体运行时监听的端口号
        self.port = port
        # 智能体运行时的通信协议配置
        self.protocol_configuration = protocol_configuration
        self.resource_group_id = resource_group_id
        # 每个运行时实例允许的最大并发会话数
        self.session_concurrency_limit_per_instance = session_concurrency_limit_per_instance
        # 会话的空闲超时时间，单位为秒。实例没有会话请求后处于空闲状态，空闲态为闲置计费模式，超过此超时时间后会话自动过期，不可继续使用
        self.session_idle_timeout_seconds = session_idle_timeout_seconds
        # 智能体运行时的当前状态，如READY（就绪）、CREATING（创建中）、FAILED（失败）等
        self.status = status
        # 当前状态的原因说明（如适用）
        self.status_reason = status_reason

    def validate(self):
        if self.code_configuration:
            self.code_configuration.validate()
        if self.container_configuration:
            self.container_configuration.validate()
        if self.health_check_configuration:
            self.health_check_configuration.validate()
        if self.log_configuration:
            self.log_configuration.validate()
        if self.network_configuration:
            self.network_configuration.validate()
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

        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables

        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn

        if self.health_check_configuration is not None:
            result['healthCheckConfiguration'] = self.health_check_configuration.to_map()

        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at

        if self.log_configuration is not None:
            result['logConfiguration'] = self.log_configuration.to_map()

        if self.memory is not None:
            result['memory'] = self.memory

        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()

        if self.port is not None:
            result['port'] = self.port

        if self.protocol_configuration is not None:
            result['protocolConfiguration'] = self.protocol_configuration.to_map()

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.session_concurrency_limit_per_instance is not None:
            result['sessionConcurrencyLimitPerInstance'] = self.session_concurrency_limit_per_instance

        if self.session_idle_timeout_seconds is not None:
            result['sessionIdleTimeoutSeconds'] = self.session_idle_timeout_seconds

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

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

        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')

        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')

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

        if m.get('networkConfiguration') is not None:
            temp_model = main_models.NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m.get('networkConfiguration'))

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocolConfiguration') is not None:
            temp_model = main_models.ProtocolConfiguration()
            self.protocol_configuration = temp_model.from_map(m.get('protocolConfiguration'))

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('sessionConcurrencyLimitPerInstance') is not None:
            self.session_concurrency_limit_per_instance = m.get('sessionConcurrencyLimitPerInstance')

        if m.get('sessionIdleTimeoutSeconds') is not None:
            self.session_idle_timeout_seconds = m.get('sessionIdleTimeoutSeconds')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        return self

