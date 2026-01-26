# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateAgentRuntimeInput(DaraModel):
    def __init__(
        self,
        agent_runtime_name: str = None,
        artifact_type: str = None,
        code_configuration: main_models.CodeConfiguration = None,
        container_configuration: main_models.ContainerConfiguration = None,
        cpu: float = None,
        credential_id: str = None,
        credential_name: str = None,
        description: str = None,
        environment_variables: Dict[str, str] = None,
        execution_role_arn: str = None,
        external_agent_endpoint_url: str = None,
        health_check_configuration: main_models.HealthCheckConfiguration = None,
        log_configuration: main_models.LogConfiguration = None,
        memory: int = None,
        nas_config: main_models.NASConfig = None,
        network_configuration: main_models.NetworkConfiguration = None,
        oss_mount_config: main_models.OSSMountConfig = None,
        port: int = None,
        protocol_configuration: main_models.ProtocolConfiguration = None,
        resource_group_id: str = None,
        session_concurrency_limit_per_instance: int = None,
        session_idle_timeout_seconds: int = None,
    ):
        # 智能体运行时的唯一标识名称，用于区分不同的智能体运行时实例
        # 
        # This parameter is required.
        self.agent_runtime_name = agent_runtime_name
        # 指定智能体运行时的部署类型，支持Code（代码模式）和Container（容器模式）
        # 
        # This parameter is required.
        self.artifact_type = artifact_type
        # 当artifactType为Code时的代码配置信息，包括代码源、入口文件等
        self.code_configuration = code_configuration
        # 当artifactType为Container时的容器配置信息，包括镜像地址、启动命令等
        self.container_configuration = container_configuration
        # 为智能体运行时分配的CPU资源，单位为核数
        # 
        # This parameter is required.
        self.cpu = cpu
        # 用于访问外部服务的凭证ID，智能体运行时将使用此凭证进行身份验证
        self.credential_id = credential_id
        # 用于访问智能体的凭证名称，访问智能体运行时将使用此凭证进行身份验证
        self.credential_name = credential_name
        # 智能体运行时的描述信息，用于说明该运行时的用途和功能
        self.description = description
        # 智能体运行时的环境变量配置，用于在运行时传递配置参数
        self.environment_variables = environment_variables
        # 为智能体运行时提供访问云服务权限的执行角色ARN
        self.execution_role_arn = execution_role_arn
        # 外部注册类型的智能体访问端点地址，用于连接已部署在外部的智能体服务
        self.external_agent_endpoint_url = external_agent_endpoint_url
        # 智能体运行时的健康检查配置，用于监控运行时实例的健康状态
        self.health_check_configuration = health_check_configuration
        # SLS（简单日志服务）配置
        self.log_configuration = log_configuration
        # 为智能体运行时分配的内存资源，单位为MB
        # 
        # This parameter is required.
        self.memory = memory
        # 文件存储NAS的配置信息，用于挂载NAS文件系统到智能体运行时
        self.nas_config = nas_config
        # 智能体运行时的网络配置，包括VPC、安全组等网络访问设置
        # 
        # This parameter is required.
        self.network_configuration = network_configuration
        # 对象存储OSS的挂载配置信息，用于挂载OSS存储桶到智能体运行时
        self.oss_mount_config = oss_mount_config
        # 智能体运行时监听的端口号，用于接收外部请求
        # 
        # This parameter is required.
        self.port = port
        # 智能体运行时的通信协议配置，定义运行时如何与外部系统交互
        self.protocol_configuration = protocol_configuration
        self.resource_group_id = resource_group_id
        # 每个运行时实例允许的最大并发会话数
        self.session_concurrency_limit_per_instance = session_concurrency_limit_per_instance
        # 会话的空闲超时时间，单位为秒。实例没有会话请求后处于空闲状态，空闲态为闲置计费模式，超过此超时时间后会话自动过期，不可继续使用
        self.session_idle_timeout_seconds = session_idle_timeout_seconds

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
        if self.agent_runtime_name is not None:
            result['agentRuntimeName'] = self.agent_runtime_name

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

        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables

        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn

        if self.external_agent_endpoint_url is not None:
            result['externalAgentEndpointUrl'] = self.external_agent_endpoint_url

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

        if self.session_concurrency_limit_per_instance is not None:
            result['sessionConcurrencyLimitPerInstance'] = self.session_concurrency_limit_per_instance

        if self.session_idle_timeout_seconds is not None:
            result['sessionIdleTimeoutSeconds'] = self.session_idle_timeout_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeName') is not None:
            self.agent_runtime_name = m.get('agentRuntimeName')

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

        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')

        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')

        if m.get('externalAgentEndpointUrl') is not None:
            self.external_agent_endpoint_url = m.get('externalAgentEndpointUrl')

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

        if m.get('sessionConcurrencyLimitPerInstance') is not None:
            self.session_concurrency_limit_per_instance = m.get('sessionConcurrencyLimitPerInstance')

        if m.get('sessionIdleTimeoutSeconds') is not None:
            self.session_idle_timeout_seconds = m.get('sessionIdleTimeoutSeconds')

        return self

