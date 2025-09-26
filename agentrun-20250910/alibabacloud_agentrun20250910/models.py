# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class CodeConfiguration(TeaModel):
    def __init__(
        self,
        checksum: str = None,
        command: List[str] = None,
        language: str = None,
        zip_file: str = None,
    ):
        # 代码包的CRC-64校验值。如果提供了checksum，则函数计算会校验代码包的checksum是否和提供的一致
        self.checksum = checksum
        # 在运行时中运行的命令（例如：[\"python\"]）
        self.command = command
        # 代码运行时的编程语言，如 python3、nodejs 等
        self.language = language
        # 智能体代码ZIP包的Base64编码
        self.zip_file = zip_file

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checksum is not None:
            result['checksum'] = self.checksum
        if self.command is not None:
            result['command'] = self.command
        if self.language is not None:
            result['language'] = self.language
        if self.zip_file is not None:
            result['zipFile'] = self.zip_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checksum') is not None:
            self.checksum = m.get('checksum')
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('zipFile') is not None:
            self.zip_file = m.get('zipFile')
        return self


class ContainerConfiguration(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
        image: str = None,
    ):
        # 在容器中运行的命令（例如：[\"python3\", \"app.py\"]）
        self.command = command
        self.image = image

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['command'] = self.command
        if self.image is not None:
            result['image'] = self.image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('image') is not None:
            self.image = m.get('image')
        return self


class HealthCheckConfiguration(TeaModel):
    def __init__(
        self,
        failure_threshold: int = None,
        http_get_url: str = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        timeout_seconds: int = None,
    ):
        # 在将容器视为不健康之前，连续失败的健康检查次数
        self.failure_threshold = failure_threshold
        # 用于健康检查的HTTP GET请求的URL地址
        self.http_get_url = http_get_url
        # 在容器启动后，首次执行健康检查前的延迟时间（秒）
        self.initial_delay_seconds = initial_delay_seconds
        # 执行健康检查的时间间隔（秒）
        self.period_seconds = period_seconds
        # 在将容器视为健康之前，连续成功的健康检查次数
        self.success_threshold = success_threshold
        # 健康检查的超时时间（秒）
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failure_threshold is not None:
            result['failureThreshold'] = self.failure_threshold
        if self.http_get_url is not None:
            result['httpGetUrl'] = self.http_get_url
        if self.initial_delay_seconds is not None:
            result['initialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['periodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['successThreshold'] = self.success_threshold
        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failureThreshold') is not None:
            self.failure_threshold = m.get('failureThreshold')
        if m.get('httpGetUrl') is not None:
            self.http_get_url = m.get('httpGetUrl')
        if m.get('initialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('initialDelaySeconds')
        if m.get('periodSeconds') is not None:
            self.period_seconds = m.get('periodSeconds')
        if m.get('successThreshold') is not None:
            self.success_threshold = m.get('successThreshold')
        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')
        return self


class LogConfiguration(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
    ):
        # SLS日志库名称
        self.logstore = logstore
        # SLS项目名称
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class NetworkConfiguration(TeaModel):
    def __init__(
        self,
        network_mode: str = None,
        security_group_id: str = None,
        vpc_id: str = None,
        vswitch_ids: List[str] = None,
    ):
        self.network_mode = network_mode
        self.security_group_id = security_group_id
        self.vpc_id = vpc_id
        self.vswitch_ids = vswitch_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_mode is not None:
            result['networkMode'] = self.network_mode
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vswitch_ids is not None:
            result['vswitchIds'] = self.vswitch_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('networkMode') is not None:
            self.network_mode = m.get('networkMode')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vswitchIds') is not None:
            self.vswitch_ids = m.get('vswitchIds')
        return self


class ProtocolConfiguration(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AgentRuntime(TeaModel):
    def __init__(
        self,
        agent_runtime_arn: str = None,
        agent_runtime_id: str = None,
        agent_runtime_name: str = None,
        agent_runtime_version: str = None,
        artifact_type: str = None,
        code_configuration: CodeConfiguration = None,
        container_configuration: ContainerConfiguration = None,
        cpu: float = None,
        created_at: str = None,
        description: str = None,
        environment_variables: Dict[str, str] = None,
        execution_role_arn: str = None,
        health_check_configuration: HealthCheckConfiguration = None,
        last_updated_at: str = None,
        log_configuration: LogConfiguration = None,
        memory: int = None,
        network_configuration: NetworkConfiguration = None,
        port: int = None,
        protocol_configuration: ProtocolConfiguration = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CodeConfiguration()
            self.code_configuration = temp_model.from_map(m['codeConfiguration'])
        if m.get('containerConfiguration') is not None:
            temp_model = ContainerConfiguration()
            self.container_configuration = temp_model.from_map(m['containerConfiguration'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')
        if m.get('healthCheckConfiguration') is not None:
            temp_model = HealthCheckConfiguration()
            self.health_check_configuration = temp_model.from_map(m['healthCheckConfiguration'])
        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')
        if m.get('logConfiguration') is not None:
            temp_model = LogConfiguration()
            self.log_configuration = temp_model.from_map(m['logConfiguration'])
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('networkConfiguration') is not None:
            temp_model = NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m['networkConfiguration'])
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocolConfiguration') is not None:
            temp_model = ProtocolConfiguration()
            self.protocol_configuration = temp_model.from_map(m['protocolConfiguration'])
        if m.get('sessionConcurrencyLimitPerInstance') is not None:
            self.session_concurrency_limit_per_instance = m.get('sessionConcurrencyLimitPerInstance')
        if m.get('sessionIdleTimeoutSeconds') is not None:
            self.session_idle_timeout_seconds = m.get('sessionIdleTimeoutSeconds')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')
        return self


class VersionWeight(TeaModel):
    def __init__(
        self,
        version: str = None,
        weight: float = None,
    ):
        # 智能体运行时版本号
        self.version = version
        # 流量权重比例（0.0-1.0）
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['version'] = self.version
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class RoutingConfiguration(TeaModel):
    def __init__(
        self,
        version_weights: List[VersionWeight] = None,
    ):
        # 不同版本的流量权重配置
        self.version_weights = version_weights

    def validate(self):
        if self.version_weights:
            for k in self.version_weights:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['versionWeights'] = []
        if self.version_weights is not None:
            for k in self.version_weights:
                result['versionWeights'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.version_weights = []
        if m.get('versionWeights') is not None:
            for k in m.get('versionWeights'):
                temp_model = VersionWeight()
                self.version_weights.append(temp_model.from_map(k))
        return self


class AgentRuntimeEndpoint(TeaModel):
    def __init__(
        self,
        agent_runtime_endpoint_arn: str = None,
        agent_runtime_endpoint_id: str = None,
        agent_runtime_endpoint_name: str = None,
        agent_runtime_id: str = None,
        description: str = None,
        endpoint_public_url: str = None,
        routing_configuration: RoutingConfiguration = None,
        status: str = None,
        status_reason: str = None,
        target_version: str = None,
    ):
        self.agent_runtime_endpoint_arn = agent_runtime_endpoint_arn
        self.agent_runtime_endpoint_id = agent_runtime_endpoint_id
        self.agent_runtime_endpoint_name = agent_runtime_endpoint_name
        self.agent_runtime_id = agent_runtime_id
        self.description = description
        # 智能体运行时端点的公网访问地址
        self.endpoint_public_url = endpoint_public_url
        # 智能体运行时端点的路由配置，支持多版本权重分配
        self.routing_configuration = routing_configuration
        self.status = status
        self.status_reason = status_reason
        self.target_version = target_version

    def validate(self):
        if self.routing_configuration:
            self.routing_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_runtime_endpoint_arn is not None:
            result['agentRuntimeEndpointArn'] = self.agent_runtime_endpoint_arn
        if self.agent_runtime_endpoint_id is not None:
            result['agentRuntimeEndpointId'] = self.agent_runtime_endpoint_id
        if self.agent_runtime_endpoint_name is not None:
            result['agentRuntimeEndpointName'] = self.agent_runtime_endpoint_name
        if self.agent_runtime_id is not None:
            result['agentRuntimeId'] = self.agent_runtime_id
        if self.description is not None:
            result['description'] = self.description
        if self.endpoint_public_url is not None:
            result['endpointPublicUrl'] = self.endpoint_public_url
        if self.routing_configuration is not None:
            result['routingConfiguration'] = self.routing_configuration.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.status_reason is not None:
            result['statusReason'] = self.status_reason
        if self.target_version is not None:
            result['targetVersion'] = self.target_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeEndpointArn') is not None:
            self.agent_runtime_endpoint_arn = m.get('agentRuntimeEndpointArn')
        if m.get('agentRuntimeEndpointId') is not None:
            self.agent_runtime_endpoint_id = m.get('agentRuntimeEndpointId')
        if m.get('agentRuntimeEndpointName') is not None:
            self.agent_runtime_endpoint_name = m.get('agentRuntimeEndpointName')
        if m.get('agentRuntimeId') is not None:
            self.agent_runtime_id = m.get('agentRuntimeId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('endpointPublicUrl') is not None:
            self.endpoint_public_url = m.get('endpointPublicUrl')
        if m.get('routingConfiguration') is not None:
            temp_model = RoutingConfiguration()
            self.routing_configuration = temp_model.from_map(m['routingConfiguration'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')
        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')
        return self


class AgentRuntimeEndpointResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AgentRuntimeEndpoint = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        # 智能体运行时端点的详细信息
        self.data = data
        # 唯一的请求标识符，用于问题追踪
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = AgentRuntimeEndpoint()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AgentRuntimeResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AgentRuntime = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        # 智能体运行时的详细信息
        self.data = data
        # 唯一的请求标识符，用于问题追踪
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = AgentRuntime()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AgentRuntimeVersion(TeaModel):
    def __init__(
        self,
        agent_runtime_arn: str = None,
        agent_runtime_id: str = None,
        agent_runtime_name: str = None,
        agent_runtime_version: str = None,
        description: str = None,
        last_updated_at: str = None,
    ):
        # 智能体运行时的ARN
        self.agent_runtime_arn = agent_runtime_arn
        # 智能体运行时的ID
        self.agent_runtime_id = agent_runtime_id
        # 智能体运行时的名称
        self.agent_runtime_name = agent_runtime_name
        # 已发布版本的版本号
        self.agent_runtime_version = agent_runtime_version
        # 此版本的描述
        self.description = description
        # 最后更新的时间戳
        self.last_updated_at = last_updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_runtime_arn is not None:
            result['agentRuntimeArn'] = self.agent_runtime_arn
        if self.agent_runtime_id is not None:
            result['agentRuntimeId'] = self.agent_runtime_id
        if self.agent_runtime_name is not None:
            result['agentRuntimeName'] = self.agent_runtime_name
        if self.agent_runtime_version is not None:
            result['agentRuntimeVersion'] = self.agent_runtime_version
        if self.description is not None:
            result['description'] = self.description
        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at
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
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')
        return self


class AgentRuntimeVersionResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AgentRuntimeVersion = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        # 智能体运行时版本的详细信息
        self.data = data
        # 唯一的请求标识符，用于问题追踪
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = AgentRuntimeVersion()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AiFallbackServiceConfig(TeaModel):
    def __init__(
        self,
        pass_through_model_name: bool = None,
        service_id: str = None,
        target_model_name: str = None,
    ):
        self.pass_through_model_name = pass_through_model_name
        self.service_id = service_id
        self.target_model_name = target_model_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pass_through_model_name is not None:
            result['passThroughModelName'] = self.pass_through_model_name
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.target_model_name is not None:
            result['targetModelName'] = self.target_model_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passThroughModelName') is not None:
            self.pass_through_model_name = m.get('passThroughModelName')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('targetModelName') is not None:
            self.target_model_name = m.get('targetModelName')
        return self


class AiFallbackConfig(TeaModel):
    def __init__(
        self,
        service_configs: List[AiFallbackServiceConfig] = None,
    ):
        self.service_configs = service_configs

    def validate(self):
        if self.service_configs:
            for k in self.service_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k in self.service_configs:
                result['serviceConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k in m.get('serviceConfigs'):
                temp_model = AiFallbackServiceConfig()
                self.service_configs.append(temp_model.from_map(k))
        return self


class AiServiceConfig(TeaModel):
    def __init__(
        self,
        address: str = None,
        api_keys: List[str] = None,
        enable_health_check: bool = None,
        protocols: List[str] = None,
        provider: str = None,
    ):
        self.address = address
        self.api_keys = api_keys
        self.enable_health_check = enable_health_check
        self.protocols = protocols
        self.provider = provider

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.api_keys is not None:
            result['apiKeys'] = self.api_keys
        if self.enable_health_check is not None:
            result['enableHealthCheck'] = self.enable_health_check
        if self.protocols is not None:
            result['protocols'] = self.protocols
        if self.provider is not None:
            result['provider'] = self.provider
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('apiKeys') is not None:
            self.api_keys = m.get('apiKeys')
        if m.get('enableHealthCheck') is not None:
            self.enable_health_check = m.get('enableHealthCheck')
        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        return self


class AttachPolicyConfig(TeaModel):
    def __init__(
        self,
        class_name: str = None,
        config: str = None,
        name: str = None,
    ):
        self.class_name = class_name
        self.config = config
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_name is not None:
            result['className'] = self.class_name
        if self.config is not None:
            result['config'] = self.config
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('className') is not None:
            self.class_name = m.get('className')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class BrowserOssLocation(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        prefix: str = None,
    ):
        self.bucket = bucket
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.prefix is not None:
            result['prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        return self


class BrowserRecordingConfiguration(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        oss_location: BrowserOssLocation = None,
    ):
        self.enabled = enabled
        self.oss_location = oss_location

    def validate(self):
        if self.oss_location:
            self.oss_location.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.oss_location is not None:
            result['ossLocation'] = self.oss_location.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('ossLocation') is not None:
            temp_model = BrowserOssLocation()
            self.oss_location = temp_model.from_map(m['ossLocation'])
        return self


class Browser(TeaModel):
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
        network_configuration: NetworkConfiguration = None,
        recording: BrowserRecordingConfiguration = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m['networkConfiguration'])
        if m.get('recording') is not None:
            temp_model = BrowserRecordingConfiguration()
            self.recording = temp_model.from_map(m['recording'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class BrowserAutomationStream(TeaModel):
    def __init__(
        self,
        stream_endpoint: str = None,
        stream_status: str = None,
    ):
        self.stream_endpoint = stream_endpoint
        self.stream_status = stream_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stream_endpoint is not None:
            result['streamEndpoint'] = self.stream_endpoint
        if self.stream_status is not None:
            result['streamStatus'] = self.stream_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('streamEndpoint') is not None:
            self.stream_endpoint = m.get('streamEndpoint')
        if m.get('streamStatus') is not None:
            self.stream_status = m.get('streamStatus')
        return self


class BrowserLiveViewStream(TeaModel):
    def __init__(
        self,
        stream_endpoint: str = None,
    ):
        self.stream_endpoint = stream_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stream_endpoint is not None:
            result['streamEndpoint'] = self.stream_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('streamEndpoint') is not None:
            self.stream_endpoint = m.get('streamEndpoint')
        return self


class BrowserResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Browser = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        # 浏览器的详细信息
        self.data = data
        # 唯一的请求标识符，用于问题追踪
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = Browser()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class BrowserSessionOut(TeaModel):
    def __init__(
        self,
        browser_id: str = None,
        browser_name: str = None,
        created_at: str = None,
        last_updated_at: str = None,
        session_id: str = None,
        session_idle_timeout_seconds: int = None,
        status: str = None,
    ):
        self.browser_id = browser_id
        self.browser_name = browser_name
        self.created_at = created_at
        self.last_updated_at = last_updated_at
        # This parameter is required.
        self.session_id = session_id
        # 会话空闲超时时间，单位为秒
        self.session_idle_timeout_seconds = session_idle_timeout_seconds
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.browser_id is not None:
            result['browserId'] = self.browser_id
        if self.browser_name is not None:
            result['browserName'] = self.browser_name
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.session_idle_timeout_seconds is not None:
            result['sessionIdleTimeoutSeconds'] = self.session_idle_timeout_seconds
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('browserId') is not None:
            self.browser_id = m.get('browserId')
        if m.get('browserName') is not None:
            self.browser_name = m.get('browserName')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('sessionIdleTimeoutSeconds') is not None:
            self.session_idle_timeout_seconds = m.get('sessionIdleTimeoutSeconds')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class BrowserSessionListOut(TeaModel):
    def __init__(
        self,
        items: List[BrowserSessionOut] = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = BrowserSessionOut()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class BrowserStreams(TeaModel):
    def __init__(
        self,
        automation_stream: BrowserAutomationStream = None,
        live_view_stream: BrowserLiveViewStream = None,
    ):
        self.automation_stream = automation_stream
        self.live_view_stream = live_view_stream

    def validate(self):
        if self.automation_stream:
            self.automation_stream.validate()
        if self.live_view_stream:
            self.live_view_stream.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.automation_stream is not None:
            result['automationStream'] = self.automation_stream.to_map()
        if self.live_view_stream is not None:
            result['liveViewStream'] = self.live_view_stream.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('automationStream') is not None:
            temp_model = BrowserAutomationStream()
            self.automation_stream = temp_model.from_map(m['automationStream'])
        if m.get('liveViewStream') is not None:
            temp_model = BrowserLiveViewStream()
            self.live_view_stream = temp_model.from_map(m['liveViewStream'])
        return self


class BrowserViewPort(TeaModel):
    def __init__(
        self,
        height: float = None,
        width: float = None,
    ):
        self.height = height
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['height'] = self.height
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class CAPConfig(TeaModel):
    def __init__(
        self,
        function_name: str = None,
        name: str = None,
        template_id: int = None,
    ):
        self.function_name = function_name
        self.name = name
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.name is not None:
            result['name'] = self.name
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class CodeInfo(TeaModel):
    def __init__(
        self,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
    ):
        self.oss_bucket_name = oss_bucket_name
        self.oss_object_name = oss_object_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_bucket_name is not None:
            result['ossBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['ossObjectName'] = self.oss_object_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ossBucketName') is not None:
            self.oss_bucket_name = m.get('ossBucketName')
        if m.get('ossObjectName') is not None:
            self.oss_object_name = m.get('ossObjectName')
        return self


class CodeInterpreter(TeaModel):
    def __init__(
        self,
        code_interpreter_id: str = None,
        code_interpreter_name: str = None,
        cpu: float = None,
        created_at: str = None,
        description: str = None,
        execution_role_arn: str = None,
        last_updated_at: str = None,
        memory: int = None,
        network_configuration: NetworkConfiguration = None,
        status: str = None,
        status_reason: str = None,
        tenant_id: str = None,
    ):
        # 代码解释器的唯一标识符
        self.code_interpreter_id = code_interpreter_id
        # 代码解释器的名称，用于标识和区分不同的代码解释器实例
        self.code_interpreter_name = code_interpreter_name
        self.cpu = cpu
        # 代码解释器的创建时间，采用ISO 8601格式
        self.created_at = created_at
        # 代码解释器的描述信息，说明该解释器的用途和功能
        self.description = description
        # 此代码解释器的执行角色
        self.execution_role_arn = execution_role_arn
        # 代码解释器的最后更新时间，采用ISO 8601格式
        self.last_updated_at = last_updated_at
        # 内存资源配置（单位：MB）
        self.memory = memory
        # 代码解释器的网络配置信息
        self.network_configuration = network_configuration
        # 代码解释器的当前状态，如READY（就绪）、TERMINATED（已终止）等
        self.status = status
        # 当前状态的原因说明（如适用）
        self.status_reason = status_reason
        self.tenant_id = tenant_id

    def validate(self):
        if self.network_configuration:
            self.network_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_interpreter_id is not None:
            result['codeInterpreterId'] = self.code_interpreter_id
        if self.code_interpreter_name is not None:
            result['codeInterpreterName'] = self.code_interpreter_name
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.created_at is not None:
            result['createdAt'] = self.created_at
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
        if self.status is not None:
            result['status'] = self.status
        if self.status_reason is not None:
            result['statusReason'] = self.status_reason
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeInterpreterId') is not None:
            self.code_interpreter_id = m.get('codeInterpreterId')
        if m.get('codeInterpreterName') is not None:
            self.code_interpreter_name = m.get('codeInterpreterName')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')
        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('networkConfiguration') is not None:
            temp_model = NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m['networkConfiguration'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class CodeInterpreterResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CodeInterpreter = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        # 代码解释器的详细信息
        self.data = data
        # 唯一的请求标识符，用于问题追踪
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CodeInterpreter()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CodeInterpreterSessionConfig(TeaModel):
    def __init__(
        self,
        environment: Dict[str, str] = None,
        timeout: int = None,
        working_directory: str = None,
    ):
        # 代码解释器会话的环境变量配置
        self.environment = environment
        # 代码解释器会话的超时时间，单位为秒
        self.timeout = timeout
        # 代码解释器会话的工作目录路径
        self.working_directory = working_directory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['environment'] = self.environment
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.working_directory is not None:
            result['workingDirectory'] = self.working_directory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environment') is not None:
            self.environment = m.get('environment')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('workingDirectory') is not None:
            self.working_directory = m.get('workingDirectory')
        return self


class CodeInterpreterSessionOut(TeaModel):
    def __init__(
        self,
        code_interpreter_id: str = None,
        code_interpreter_name: str = None,
        created_at: str = None,
        last_updated_at: str = None,
        session_id: str = None,
        session_idle_timeout_seconds: int = None,
        status: str = None,
    ):
        # 关联的代码解释器的唯一标识符
        # 
        # This parameter is required.
        self.code_interpreter_id = code_interpreter_id
        # 代码解释器会话的名称
        self.code_interpreter_name = code_interpreter_name
        # 代码解释器会话的创建时间，采用ISO 8601格式
        self.created_at = created_at
        # 代码解释器会话的最后更新时间，采用ISO 8601格式
        self.last_updated_at = last_updated_at
        # 代码解释器会话的唯一标识符
        # 
        # This parameter is required.
        self.session_id = session_id
        # 代码解释器会话的空闲超时时间，单位为秒。实例没有会话请求后处于空闲状态，空闲态为闲置计费模式，超过此超时时间后会话自动过期，不可继续使用
        self.session_idle_timeout_seconds = session_idle_timeout_seconds
        # 代码解释器会话的当前状态
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_interpreter_id is not None:
            result['codeInterpreterId'] = self.code_interpreter_id
        if self.code_interpreter_name is not None:
            result['codeInterpreterName'] = self.code_interpreter_name
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.session_idle_timeout_seconds is not None:
            result['sessionIdleTimeoutSeconds'] = self.session_idle_timeout_seconds
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeInterpreterId') is not None:
            self.code_interpreter_id = m.get('codeInterpreterId')
        if m.get('codeInterpreterName') is not None:
            self.code_interpreter_name = m.get('codeInterpreterName')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('sessionIdleTimeoutSeconds') is not None:
            self.session_idle_timeout_seconds = m.get('sessionIdleTimeoutSeconds')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class CodeInterpreterSessionListOut(TeaModel):
    def __init__(
        self,
        items: List[CodeInterpreterSessionOut] = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = CodeInterpreterSessionOut()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class CommonResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        # 实际的业务数据内容
        self.data = data
        # 唯一的请求标识符，用于问题追踪
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateAgentRuntimeEndpointInput(TeaModel):
    def __init__(
        self,
        agent_runtime_endpoint_name: str = None,
        description: str = None,
        routing_configuration: RoutingConfiguration = None,
        target_version: str = None,
    ):
        self.agent_runtime_endpoint_name = agent_runtime_endpoint_name
        self.description = description
        # 智能体运行时端点的路由配置，支持多版本权重分配
        self.routing_configuration = routing_configuration
        # 智能体运行时的目标版本
        self.target_version = target_version

    def validate(self):
        if self.routing_configuration:
            self.routing_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_runtime_endpoint_name is not None:
            result['agentRuntimeEndpointName'] = self.agent_runtime_endpoint_name
        if self.description is not None:
            result['description'] = self.description
        if self.routing_configuration is not None:
            result['routingConfiguration'] = self.routing_configuration.to_map()
        if self.target_version is not None:
            result['targetVersion'] = self.target_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeEndpointName') is not None:
            self.agent_runtime_endpoint_name = m.get('agentRuntimeEndpointName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('routingConfiguration') is not None:
            temp_model = RoutingConfiguration()
            self.routing_configuration = temp_model.from_map(m['routingConfiguration'])
        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')
        return self


class CreateAgentRuntimeInput(TeaModel):
    def __init__(
        self,
        agent_runtime_name: str = None,
        artifact_type: str = None,
        code_configuration: CodeConfiguration = None,
        container_configuration: ContainerConfiguration = None,
        cpu: float = None,
        credential_id: str = None,
        description: str = None,
        environment_variables: Dict[str, str] = None,
        execution_role_arn: str = None,
        health_check_configuration: HealthCheckConfiguration = None,
        log_configuration: LogConfiguration = None,
        memory: int = None,
        network_configuration: NetworkConfiguration = None,
        port: int = None,
        protocol_configuration: ProtocolConfiguration = None,
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
        # 智能体运行时的描述信息，用于说明该运行时的用途和功能
        self.description = description
        # 智能体运行时的环境变量配置，用于在运行时传递配置参数
        self.environment_variables = environment_variables
        # 为智能体运行时提供访问云服务权限的执行角色ARN
        self.execution_role_arn = execution_role_arn
        # 智能体运行时的健康检查配置，用于监控运行时实例的健康状态
        self.health_check_configuration = health_check_configuration
        # SLS（简单日志服务）配置
        self.log_configuration = log_configuration
        # 为智能体运行时分配的内存资源，单位为MB
        # 
        # This parameter is required.
        self.memory = memory
        # 智能体运行时的网络配置，包括VPC、安全组等网络访问设置
        # 
        # This parameter is required.
        self.network_configuration = network_configuration
        # 智能体运行时监听的端口号，用于接收外部请求
        # 
        # This parameter is required.
        self.port = port
        # 智能体运行时的通信协议配置，定义运行时如何与外部系统交互
        self.protocol_configuration = protocol_configuration
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
        if self.network_configuration:
            self.network_configuration.validate()
        if self.protocol_configuration:
            self.protocol_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.description is not None:
            result['description'] = self.description
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn
        if self.health_check_configuration is not None:
            result['healthCheckConfiguration'] = self.health_check_configuration.to_map()
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
            temp_model = CodeConfiguration()
            self.code_configuration = temp_model.from_map(m['codeConfiguration'])
        if m.get('containerConfiguration') is not None:
            temp_model = ContainerConfiguration()
            self.container_configuration = temp_model.from_map(m['containerConfiguration'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('credentialId') is not None:
            self.credential_id = m.get('credentialId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')
        if m.get('healthCheckConfiguration') is not None:
            temp_model = HealthCheckConfiguration()
            self.health_check_configuration = temp_model.from_map(m['healthCheckConfiguration'])
        if m.get('logConfiguration') is not None:
            temp_model = LogConfiguration()
            self.log_configuration = temp_model.from_map(m['logConfiguration'])
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('networkConfiguration') is not None:
            temp_model = NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m['networkConfiguration'])
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocolConfiguration') is not None:
            temp_model = ProtocolConfiguration()
            self.protocol_configuration = temp_model.from_map(m['protocolConfiguration'])
        if m.get('sessionConcurrencyLimitPerInstance') is not None:
            self.session_concurrency_limit_per_instance = m.get('sessionConcurrencyLimitPerInstance')
        if m.get('sessionIdleTimeoutSeconds') is not None:
            self.session_idle_timeout_seconds = m.get('sessionIdleTimeoutSeconds')
        return self


class CreateAgentRuntimeVersionInput(TeaModel):
    def __init__(
        self,
        description: str = None,
    ):
        # 版本描述
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class CreateBrowserInput(TeaModel):
    def __init__(
        self,
        browser_name: str = None,
        cpu: float = None,
        credential_id: str = None,
        description: str = None,
        execution_role_arn: str = None,
        memory: int = None,
        network_configuration: NetworkConfiguration = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m['networkConfiguration'])
        if m.get('sessionIdleTimeoutSeconds') is not None:
            self.session_idle_timeout_seconds = m.get('sessionIdleTimeoutSeconds')
        return self


class CreateCodeInterpreterInput(TeaModel):
    def __init__(
        self,
        code_interpreter_name: str = None,
        cpu: float = None,
        credential_id: str = None,
        description: str = None,
        execution_role_arn: str = None,
        memory: int = None,
        network_configuration: NetworkConfiguration = None,
        session_idle_timeout_seconds: int = None,
    ):
        # 代码解释器的名称，用于标识和区分不同的代码解释器实例
        # 
        # This parameter is required.
        self.code_interpreter_name = code_interpreter_name
        # CPU资源配置（单位：核数）
        # 
        # This parameter is required.
        self.cpu = cpu
        self.credential_id = credential_id
        # 代码解释器的描述信息，说明该解释器的用途和功能
        self.description = description
        # 此代码解释器的执行角色
        self.execution_role_arn = execution_role_arn
        # 内存资源配置（单位：MB）
        # 
        # This parameter is required.
        self.memory = memory
        # 代码解释器的网络配置，包括VPC、安全组等网络访问设置
        # 
        # This parameter is required.
        self.network_configuration = network_configuration
        # 会话的空闲超时时间，单位为秒。实例没有会话请求后处于空闲状态，空闲态为闲置计费模式，超过此超时时间后会话自动过期，不可继续使用
        self.session_idle_timeout_seconds = session_idle_timeout_seconds

    def validate(self):
        if self.network_configuration:
            self.network_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m['networkConfiguration'])
        if m.get('sessionIdleTimeoutSeconds') is not None:
            self.session_idle_timeout_seconds = m.get('sessionIdleTimeoutSeconds')
        return self


class CreateCredentialInput(TeaModel):
    def __init__(
        self,
        config: Dict[str, str] = None,
        description: str = None,
        name: str = None,
        secret: str = None,
        type: str = None,
    ):
        self.config = config
        self.description = description
        self.name = name
        self.secret = secret
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.secret is not None:
            result['secret'] = self.secret
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('secret') is not None:
            self.secret = m.get('secret')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateCredentialOutput(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.created_at = created_at
        self.id = id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateDomainInput(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        name: str = None,
        protocol: str = None,
    ):
        self.cert_identifier = cert_identifier
        self.name = name
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['certIdentifier'] = self.cert_identifier
        if self.name is not None:
            result['name'] = self.name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certIdentifier') is not None:
            self.cert_identifier = m.get('certIdentifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class GatewayNetworkConfiguration(TeaModel):
    def __init__(
        self,
        network_mode: str = None,
        vpc_id: str = None,
        vswitch_ids: List[str] = None,
    ):
        self.network_mode = network_mode
        self.vpc_id = vpc_id
        self.vswitch_ids = vswitch_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_mode is not None:
            result['networkMode'] = self.network_mode
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vswitch_ids is not None:
            result['vswitchIds'] = self.vswitch_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('networkMode') is not None:
            self.network_mode = m.get('networkMode')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vswitchIds') is not None:
            self.vswitch_ids = m.get('vswitchIds')
        return self


class CreateGatewayInput(TeaModel):
    def __init__(
        self,
        identity_id: str = None,
        name: str = None,
        network_configuration: GatewayNetworkConfiguration = None,
        type: str = None,
    ):
        self.identity_id = identity_id
        self.name = name
        self.network_configuration = network_configuration
        self.type = type

    def validate(self):
        if self.network_configuration:
            self.network_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity_id is not None:
            result['identityId'] = self.identity_id
        if self.name is not None:
            result['name'] = self.name
        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identityId') is not None:
            self.identity_id = m.get('identityId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('networkConfiguration') is not None:
            temp_model = GatewayNetworkConfiguration()
            self.network_configuration = temp_model.from_map(m['networkConfiguration'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class PolicyConfig(TeaModel):
    def __init__(
        self,
        ai_fallback_config: AiFallbackConfig = None,
        enable: bool = None,
        type: str = None,
    ):
        self.ai_fallback_config = ai_fallback_config
        self.enable = enable
        self.type = type

    def validate(self):
        if self.ai_fallback_config:
            self.ai_fallback_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_fallback_config is not None:
            result['aiFallbackConfig'] = self.ai_fallback_config.to_map()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiFallbackConfig') is not None:
            temp_model = AiFallbackConfig()
            self.ai_fallback_config = temp_model.from_map(m['aiFallbackConfig'])
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class TargetServiceConfig(TeaModel):
    def __init__(
        self,
        model_id: str = None,
        model_name: str = None,
        model_name_pattern: str = None,
        weight: int = None,
    ):
        self.model_id = model_id
        self.model_name = model_name
        self.model_name_pattern = model_name_pattern
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.model_name is not None:
            result['modelName'] = self.model_name
        if self.model_name_pattern is not None:
            result['modelNamePattern'] = self.model_name_pattern
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')
        if m.get('modelNamePattern') is not None:
            self.model_name_pattern = m.get('modelNamePattern')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class LLMDeployConfig(TeaModel):
    def __init__(
        self,
        auto_deploy: bool = None,
        backend_scene: str = None,
        custom_domain_ids: List[str] = None,
        gateway_type: str = None,
        policy_configs: List[PolicyConfig] = None,
        service_configs: List[TargetServiceConfig] = None,
    ):
        self.auto_deploy = auto_deploy
        self.backend_scene = backend_scene
        self.custom_domain_ids = custom_domain_ids
        self.gateway_type = gateway_type
        self.policy_configs = policy_configs
        self.service_configs = service_configs

    def validate(self):
        if self.policy_configs:
            for k in self.policy_configs:
                if k:
                    k.validate()
        if self.service_configs:
            for k in self.service_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_deploy is not None:
            result['autoDeploy'] = self.auto_deploy
        if self.backend_scene is not None:
            result['backendScene'] = self.backend_scene
        if self.custom_domain_ids is not None:
            result['customDomainIds'] = self.custom_domain_ids
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        result['policyConfigs'] = []
        if self.policy_configs is not None:
            for k in self.policy_configs:
                result['policyConfigs'].append(k.to_map() if k else None)
        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k in self.service_configs:
                result['serviceConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoDeploy') is not None:
            self.auto_deploy = m.get('autoDeploy')
        if m.get('backendScene') is not None:
            self.backend_scene = m.get('backendScene')
        if m.get('customDomainIds') is not None:
            self.custom_domain_ids = m.get('customDomainIds')
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        self.policy_configs = []
        if m.get('policyConfigs') is not None:
            for k in m.get('policyConfigs'):
                temp_model = PolicyConfig()
                self.policy_configs.append(temp_model.from_map(k))
        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k in m.get('serviceConfigs'):
                temp_model = TargetServiceConfig()
                self.service_configs.append(temp_model.from_map(k))
        return self


class LLMAPIConfiguration(TeaModel):
    def __init__(
        self,
        ai_protocols: List[str] = None,
        attach_policy_configs: List[AttachPolicyConfig] = None,
        base_path: str = None,
        deploy_configs: List[LLMDeployConfig] = None,
        model_category: str = None,
        remove_base_path_on_forward: bool = None,
        type: str = None,
    ):
        self.ai_protocols = ai_protocols
        self.attach_policy_configs = attach_policy_configs
        self.base_path = base_path
        self.deploy_configs = deploy_configs
        self.model_category = model_category
        self.remove_base_path_on_forward = remove_base_path_on_forward
        self.type = type

    def validate(self):
        if self.attach_policy_configs:
            for k in self.attach_policy_configs:
                if k:
                    k.validate()
        if self.deploy_configs:
            for k in self.deploy_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_protocols is not None:
            result['aiProtocols'] = self.ai_protocols
        result['attachPolicyConfigs'] = []
        if self.attach_policy_configs is not None:
            for k in self.attach_policy_configs:
                result['attachPolicyConfigs'].append(k.to_map() if k else None)
        if self.base_path is not None:
            result['basePath'] = self.base_path
        result['deployConfigs'] = []
        if self.deploy_configs is not None:
            for k in self.deploy_configs:
                result['deployConfigs'].append(k.to_map() if k else None)
        if self.model_category is not None:
            result['modelCategory'] = self.model_category
        if self.remove_base_path_on_forward is not None:
            result['removeBasePathOnForward'] = self.remove_base_path_on_forward
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiProtocols') is not None:
            self.ai_protocols = m.get('aiProtocols')
        self.attach_policy_configs = []
        if m.get('attachPolicyConfigs') is not None:
            for k in m.get('attachPolicyConfigs'):
                temp_model = AttachPolicyConfig()
                self.attach_policy_configs.append(temp_model.from_map(k))
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')
        self.deploy_configs = []
        if m.get('deployConfigs') is not None:
            for k in m.get('deployConfigs'):
                temp_model = LLMDeployConfig()
                self.deploy_configs.append(temp_model.from_map(k))
        if m.get('modelCategory') is not None:
            self.model_category = m.get('modelCategory')
        if m.get('removeBasePathOnForward') is not None:
            self.remove_base_path_on_forward = m.get('removeBasePathOnForward')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class MCPAPIConfiguration(TeaModel):
    def __init__(
        self,
        description: str = None,
        exposed_uri_path: str = None,
        mcp_statistics_enable: bool = None,
        protocol: str = None,
        tool_id: str = None,
    ):
        self.description = description
        self.exposed_uri_path = exposed_uri_path
        self.mcp_statistics_enable = mcp_statistics_enable
        self.protocol = protocol
        self.tool_id = tool_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.exposed_uri_path is not None:
            result['exposedUriPath'] = self.exposed_uri_path
        if self.mcp_statistics_enable is not None:
            result['mcpStatisticsEnable'] = self.mcp_statistics_enable
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.tool_id is not None:
            result['toolId'] = self.tool_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('exposedUriPath') is not None:
            self.exposed_uri_path = m.get('exposedUriPath')
        if m.get('mcpStatisticsEnable') is not None:
            self.mcp_statistics_enable = m.get('mcpStatisticsEnable')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('toolId') is not None:
            self.tool_id = m.get('toolId')
        return self


class TargetConfiguration(TeaModel):
    def __init__(
        self,
        llm_apiconfig: LLMAPIConfiguration = None,
        mcp_apiconfig: MCPAPIConfiguration = None,
        target_type: str = None,
    ):
        self.llm_apiconfig = llm_apiconfig
        self.mcp_apiconfig = mcp_apiconfig
        self.target_type = target_type

    def validate(self):
        if self.llm_apiconfig:
            self.llm_apiconfig.validate()
        if self.mcp_apiconfig:
            self.mcp_apiconfig.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.llm_apiconfig is not None:
            result['llmAPIConfig'] = self.llm_apiconfig.to_map()
        if self.mcp_apiconfig is not None:
            result['mcpAPIConfig'] = self.mcp_apiconfig.to_map()
        if self.target_type is not None:
            result['targetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('llmAPIConfig') is not None:
            temp_model = LLMAPIConfiguration()
            self.llm_apiconfig = temp_model.from_map(m['llmAPIConfig'])
        if m.get('mcpAPIConfig') is not None:
            temp_model = MCPAPIConfiguration()
            self.mcp_apiconfig = temp_model.from_map(m['mcpAPIConfig'])
        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')
        return self


class CreateGatewayTargetInput(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
        target_configuration: TargetConfiguration = None,
    ):
        self.domain_id = domain_id
        self.name = name
        self.target_configuration = target_configuration

    def validate(self):
        if self.target_configuration:
            self.target_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.name is not None:
            result['name'] = self.name
        if self.target_configuration is not None:
            result['targetConfiguration'] = self.target_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('targetConfiguration') is not None:
            temp_model = TargetConfiguration()
            self.target_configuration = temp_model.from_map(m['targetConfiguration'])
        return self


class CreateModelInput(TeaModel):
    def __init__(
        self,
        address: str = None,
        api_key: str = None,
        desc: str = None,
        models: List[str] = None,
        name: str = None,
        provider: str = None,
        type: str = None,
    ):
        self.address = address
        self.api_key = api_key
        self.desc = desc
        self.models = models
        self.name = name
        self.provider = provider
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.api_key is not None:
            result['apiKey'] = self.api_key
        if self.desc is not None:
            result['desc'] = self.desc
        if self.models is not None:
            result['models'] = self.models
        if self.name is not None:
            result['name'] = self.name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('models') is not None:
            self.models = m.get('models')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateToolData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
        name: str = None,
        source_type: str = None,
        tool_type: str = None,
    ):
        self.created_at = created_at
        self.id = id
        self.name = name
        self.source_type = source_type
        self.tool_type = tool_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.tool_type is not None:
            result['toolType'] = self.tool_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('toolType') is not None:
            self.tool_type = m.get('toolType')
        return self


class CreateToolInput(TeaModel):
    def __init__(
        self,
        capconfig: CAPConfig = None,
        description: str = None,
        name: str = None,
        schema: str = None,
        source_type: str = None,
        tool_type: str = None,
    ):
        self.capconfig = capconfig
        self.description = description
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.schema = schema
        # This parameter is required.
        self.source_type = source_type
        # This parameter is required.
        self.tool_type = tool_type

    def validate(self):
        if self.capconfig:
            self.capconfig.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capconfig is not None:
            result['CAPConfig'] = self.capconfig.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.schema is not None:
            result['schema'] = self.schema
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.tool_type is not None:
            result['toolType'] = self.tool_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CAPConfig') is not None:
            temp_model = CAPConfig()
            self.capconfig = temp_model.from_map(m['CAPConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('toolType') is not None:
            self.tool_type = m.get('toolType')
        return self


class CreateToolOutput(TeaModel):
    def __init__(
        self,
        data: CreateToolData = None,
        message: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateToolData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class RelatedWorkload(TeaModel):
    def __init__(
        self,
        workload_id: str = None,
        workload_name: str = None,
        workload_type: str = None,
    ):
        self.workload_id = workload_id
        self.workload_name = workload_name
        self.workload_type = workload_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workload_id is not None:
            result['workloadId'] = self.workload_id
        if self.workload_name is not None:
            result['workloadName'] = self.workload_name
        if self.workload_type is not None:
            result['workloadType'] = self.workload_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workloadId') is not None:
            self.workload_id = m.get('workloadId')
        if m.get('workloadName') is not None:
            self.workload_name = m.get('workloadName')
        if m.get('workloadType') is not None:
            self.workload_type = m.get('workloadType')
        return self


class CredentialListItem(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
        name: str = None,
        related_worloads: List[RelatedWorkload] = None,
        type: str = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.id = id
        self.name = name
        self.related_worloads = related_worloads
        self.type = type
        self.updated_at = updated_at

    def validate(self):
        if self.related_worloads:
            for k in self.related_worloads:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        result['relatedWorloads'] = []
        if self.related_worloads is not None:
            for k in self.related_worloads:
                result['relatedWorloads'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.related_worloads = []
        if m.get('relatedWorloads') is not None:
            for k in m.get('relatedWorloads'):
                temp_model = RelatedWorkload()
                self.related_worloads.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        return self


class CustomRuntimeConfig(TeaModel):
    def __init__(
        self,
        args: List[str] = None,
        command: List[str] = None,
        port: int = None,
    ):
        self.args = args
        self.command = command
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['args'] = self.args
        if self.command is not None:
            result['command'] = self.command
        if self.port is not None:
            result['port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('port') is not None:
            self.port = m.get('port')
        return self


class DeleteBrowserOut(TeaModel):
    def __init__(
        self,
        browser_id: str = None,
        browser_name: str = None,
        status: str = None,
    ):
        self.browser_id = browser_id
        self.browser_name = browser_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.browser_id is not None:
            result['browserId'] = self.browser_id
        if self.browser_name is not None:
            result['browserName'] = self.browser_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('browserId') is not None:
            self.browser_id = m.get('browserId')
        if m.get('browserName') is not None:
            self.browser_name = m.get('browserName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DeleteBrowserResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Browser = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = Browser()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteCodeInterpreterOut(TeaModel):
    def __init__(
        self,
        code_interpreter_id: str = None,
        code_interpreter_name: str = None,
        status: str = None,
    ):
        self.code_interpreter_id = code_interpreter_id
        self.code_interpreter_name = code_interpreter_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_interpreter_id is not None:
            result['codeInterpreterId'] = self.code_interpreter_id
        if self.code_interpreter_name is not None:
            result['codeInterpreterName'] = self.code_interpreter_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeInterpreterId') is not None:
            self.code_interpreter_id = m.get('codeInterpreterId')
        if m.get('codeInterpreterName') is not None:
            self.code_interpreter_name = m.get('codeInterpreterName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DeleteCodeInterpreterResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CodeInterpreter = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CodeInterpreter()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DomainInfo(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        domain_id: str = None,
        name: str = None,
        protocol: str = None,
    ):
        self.cert_identifier = cert_identifier
        self.domain_id = domain_id
        self.name = name
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['certIdentifier'] = self.cert_identifier
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.name is not None:
            result['name'] = self.name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certIdentifier') is not None:
            self.cert_identifier = m.get('certIdentifier')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class ErrorResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        # 错误信息描述
        self.message = message
        # 唯一的请求标识符，用于问题追踪
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class FCLinkConfig(TeaModel):
    def __init__(
        self,
        function_name: str = None,
        version: str = None,
    ):
        self.function_name = function_name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class Gateway(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        gateway_id: str = None,
        internet_url: str = None,
        intranet_url: str = None,
        name: str = None,
        status: str = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.gateway_id = gateway_id
        self.internet_url = internet_url
        self.intranet_url = intranet_url
        self.name = name
        self.status = status
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.internet_url is not None:
            result['internetUrl'] = self.internet_url
        if self.intranet_url is not None:
            result['intranetUrl'] = self.intranet_url
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('internetUrl') is not None:
            self.internet_url = m.get('internetUrl')
        if m.get('intranetUrl') is not None:
            self.intranet_url = m.get('intranetUrl')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        return self


class GetBrowserSessionResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BrowserSessionOut = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = BrowserSessionOut()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetCodeInterpreterSessionResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CodeInterpreterSessionOut = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CodeInterpreterSessionOut()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetCredentialOutput(TeaModel):
    def __init__(
        self,
        config: Dict[str, str] = None,
        created_at: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        secret: str = None,
        type: str = None,
        updated_at: str = None,
    ):
        self.config = config
        self.created_at = created_at
        self.description = description
        self.id = id
        self.name = name
        self.secret = secret
        self.type = type
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.secret is not None:
            result['secret'] = self.secret
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('secret') is not None:
            self.secret = m.get('secret')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        return self


class ToolInfo(TeaModel):
    def __init__(
        self,
        capconfig: CAPConfig = None,
        created_at: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        schema: str = None,
        source_type: str = None,
        tool_type: str = None,
        updated_at: str = None,
    ):
        self.capconfig = capconfig
        self.created_at = created_at
        self.description = description
        self.id = id
        self.name = name
        self.schema = schema
        self.source_type = source_type
        self.tool_type = tool_type
        self.updated_at = updated_at

    def validate(self):
        if self.capconfig:
            self.capconfig.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capconfig is not None:
            result['CAPConfig'] = self.capconfig.to_map()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.schema is not None:
            result['schema'] = self.schema
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.tool_type is not None:
            result['toolType'] = self.tool_type
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CAPConfig') is not None:
            temp_model = CAPConfig()
            self.capconfig = temp_model.from_map(m['CAPConfig'])
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('toolType') is not None:
            self.tool_type = m.get('toolType')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        return self


class GetToolOutput(TeaModel):
    def __init__(
        self,
        data: ToolInfo = None,
        success: bool = None,
    ):
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ToolInfo()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GrayTrafficWeight(TeaModel):
    def __init__(
        self,
        version: str = None,
        weight: float = None,
    ):
        # 灰度版本号
        self.version = version
        # 流量权重比例（0.0-1.0）
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['version'] = self.version
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HealthCheckConfig(TeaModel):
    def __init__(
        self,
        failure_threshold: int = None,
        http_get_url: str = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        timeout_seconds: int = None,
    ):
        # 在将容器视为不健康之前，连续失败的健康检查次数
        self.failure_threshold = failure_threshold
        # 用于健康检查的HTTP GET请求的URL地址
        self.http_get_url = http_get_url
        # 在容器启动后，首次执行健康检查前的延迟时间（秒）
        self.initial_delay_seconds = initial_delay_seconds
        # 执行健康检查的时间间隔（秒）
        self.period_seconds = period_seconds
        # 在将容器视为健康之前，连续成功的健康检查次数
        self.success_threshold = success_threshold
        # 健康检查的超时时间（秒）
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failure_threshold is not None:
            result['failureThreshold'] = self.failure_threshold
        if self.http_get_url is not None:
            result['httpGetUrl'] = self.http_get_url
        if self.initial_delay_seconds is not None:
            result['initialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['periodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['successThreshold'] = self.success_threshold
        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failureThreshold') is not None:
            self.failure_threshold = m.get('failureThreshold')
        if m.get('httpGetUrl') is not None:
            self.http_get_url = m.get('httpGetUrl')
        if m.get('initialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('initialDelaySeconds')
        if m.get('periodSeconds') is not None:
            self.period_seconds = m.get('periodSeconds')
        if m.get('successThreshold') is not None:
            self.success_threshold = m.get('successThreshold')
        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')
        return self


class ListAgentRuntimeEndpointsInput(TeaModel):
    def __init__(
        self,
        endpoint_name: str = None,
        page_number: int = None,
        page_size: int = None,
        statuses: List[str] = None,
    ):
        # 按端点名称过滤
        self.endpoint_name = endpoint_name
        # 页码
        self.page_number = page_number
        # 每页记录数
        self.page_size = page_size
        # 按状态过滤
        self.statuses = statuses

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_name is not None:
            result['endpointName'] = self.endpoint_name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.statuses is not None:
            result['statuses'] = self.statuses
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpointName') is not None:
            self.endpoint_name = m.get('endpointName')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('statuses') is not None:
            self.statuses = m.get('statuses')
        return self


class ListAgentRuntimeEndpointsOutput(TeaModel):
    def __init__(
        self,
        items: List[AgentRuntimeEndpoint] = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = AgentRuntimeEndpoint()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListAgentRuntimeEndpointsResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListAgentRuntimeEndpointsOutput = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        # 智能体运行时端点列表的详细信息
        self.data = data
        # 唯一的请求标识符，用于问题追踪
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListAgentRuntimeEndpointsOutput()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListAgentRuntimeVersionsInput(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # 页码
        self.page_number = page_number
        # 每页记录数
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListAgentRuntimeVersionsOutput(TeaModel):
    def __init__(
        self,
        items: List[AgentRuntimeVersion] = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = AgentRuntimeVersion()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListAgentRuntimeVersionsResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListAgentRuntimeVersionsOutput = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        # 智能体运行时版本列表的详细信息
        self.data = data
        # 唯一的请求标识符，用于问题追踪
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListAgentRuntimeVersionsOutput()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListAgentRuntimesInput(TeaModel):
    def __init__(
        self,
        agent_runtime_name: str = None,
        page_number: int = None,
        page_size: int = None,
        statuses: List[str] = None,
    ):
        # 按名称过滤
        self.agent_runtime_name = agent_runtime_name
        # 页码
        self.page_number = page_number
        # 每页记录数
        self.page_size = page_size
        # 按状态过滤
        self.statuses = statuses

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_runtime_name is not None:
            result['agentRuntimeName'] = self.agent_runtime_name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.statuses is not None:
            result['statuses'] = self.statuses
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeName') is not None:
            self.agent_runtime_name = m.get('agentRuntimeName')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('statuses') is not None:
            self.statuses = m.get('statuses')
        return self


class ListAgentRuntimesOutput(TeaModel):
    def __init__(
        self,
        items: List[AgentRuntime] = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = AgentRuntime()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListAgentRuntimesResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListAgentRuntimesOutput = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        # 智能体运行时列表的详细信息
        self.data = data
        # 唯一的请求标识符，用于问题追踪
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListAgentRuntimesOutput()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListBrowserSessionResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BrowserSessionListOut = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = BrowserSessionListOut()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListBrowsersInput(TeaModel):
    def __init__(
        self,
        browser_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 按浏览器名称过滤
        self.browser_name = browser_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.browser_name is not None:
            result['browserName'] = self.browser_name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('browserName') is not None:
            self.browser_name = m.get('browserName')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListBrowsersOutput(TeaModel):
    def __init__(
        self,
        items: List[Browser] = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = Browser()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListBrowsersResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListBrowsersOutput = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        # 浏览器列表的详细信息
        self.data = data
        # 唯一的请求标识符，用于问题追踪
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListBrowsersOutput()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListCodeInterpreterSessionResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CodeInterpreterSessionListOut = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CodeInterpreterSessionListOut()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListCodeInterpretersInput(TeaModel):
    def __init__(
        self,
        code_interpreter_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 按代码解释器名称过滤
        self.code_interpreter_name = code_interpreter_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_interpreter_name is not None:
            result['codeInterpreterName'] = self.code_interpreter_name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeInterpreterName') is not None:
            self.code_interpreter_name = m.get('codeInterpreterName')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListCodeInterpretersOutput(TeaModel):
    def __init__(
        self,
        items: List[CodeInterpreter] = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = CodeInterpreter()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListCodeInterpretersResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListCodeInterpretersOutput = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        # 代码解释器列表的详细信息
        self.data = data
        # 唯一的请求标识符，用于问题追踪
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListCodeInterpretersOutput()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListCredentialsOutput(TeaModel):
    def __init__(
        self,
        items: CredentialListItem = None,
        page_num: str = None,
        page_size: str = None,
        total: str = None,
    ):
        self.items = items
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['items'] = self.items.to_map()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('items') is not None:
            temp_model = CredentialListItem()
            self.items = temp_model.from_map(m['items'])
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListDomainsOutput(TeaModel):
    def __init__(
        self,
        items: List[DomainInfo] = None,
        page_number: str = None,
        page_size: str = None,
        total_count: str = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = DomainInfo()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListGatewaysOutput(TeaModel):
    def __init__(
        self,
        items: Gateway = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['items'] = self.items.to_map()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('items') is not None:
            temp_model = Gateway()
            self.items = temp_model.from_map(m['items'])
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ToolListItem(TeaModel):
    def __init__(
        self,
        capconfig: CAPConfig = None,
        created_at: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        schema: str = None,
        source_type: str = None,
        tool_type: str = None,
        updated_at: str = None,
    ):
        self.capconfig = capconfig
        self.created_at = created_at
        self.description = description
        self.id = id
        self.name = name
        self.schema = schema
        self.source_type = source_type
        self.tool_type = tool_type
        self.updated_at = updated_at

    def validate(self):
        if self.capconfig:
            self.capconfig.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capconfig is not None:
            result['CAPConfig'] = self.capconfig.to_map()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.schema is not None:
            result['schema'] = self.schema
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.tool_type is not None:
            result['toolType'] = self.tool_type
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CAPConfig') is not None:
            temp_model = CAPConfig()
            self.capconfig = temp_model.from_map(m['CAPConfig'])
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('toolType') is not None:
            self.tool_type = m.get('toolType')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        return self


class ListToolsOutput(TeaModel):
    def __init__(
        self,
        data: List[ToolListItem] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.data = data
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ToolListItem()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class MCPServiceConfig(TeaModel):
    def __init__(
        self,
        service_id: str = None,
    ):
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        return self


class MCPBackendConfig(TeaModel):
    def __init__(
        self,
        scene: str = None,
        services: List[MCPServiceConfig] = None,
    ):
        self.scene = scene
        self.services = services

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene is not None:
            result['scene'] = self.scene
        result['services'] = []
        if self.services is not None:
            for k in self.services:
                result['services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        self.services = []
        if m.get('services') is not None:
            for k in m.get('services'):
                temp_model = MCPServiceConfig()
                self.services.append(temp_model.from_map(k))
        return self


class MCPPathMatch(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class MCPMatch(TeaModel):
    def __init__(
        self,
        path: MCPPathMatch = None,
    ):
        self.path = path

    def validate(self):
        if self.path:
            self.path.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            temp_model = MCPPathMatch()
            self.path = temp_model.from_map(m['path'])
        return self


class MCPAPI(TeaModel):
    def __init__(
        self,
        backend_config: MCPBackendConfig = None,
        description: str = None,
        exposed_uri_path: str = None,
        match: MCPMatch = None,
        mcp_statistics_enable: bool = None,
        protocol: str = None,
        tool_id: str = None,
        tools_config: str = None,
    ):
        self.backend_config = backend_config
        self.description = description
        self.exposed_uri_path = exposed_uri_path
        self.match = match
        self.mcp_statistics_enable = mcp_statistics_enable
        self.protocol = protocol
        self.tool_id = tool_id
        self.tools_config = tools_config

    def validate(self):
        if self.backend_config:
            self.backend_config.validate()
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_config is not None:
            result['backendConfig'] = self.backend_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.exposed_uri_path is not None:
            result['exposedUriPath'] = self.exposed_uri_path
        if self.match is not None:
            result['match'] = self.match.to_map()
        if self.mcp_statistics_enable is not None:
            result['mcpStatisticsEnable'] = self.mcp_statistics_enable
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.tool_id is not None:
            result['toolId'] = self.tool_id
        if self.tools_config is not None:
            result['toolsConfig'] = self.tools_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendConfig') is not None:
            temp_model = MCPBackendConfig()
            self.backend_config = temp_model.from_map(m['backendConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('exposedUriPath') is not None:
            self.exposed_uri_path = m.get('exposedUriPath')
        if m.get('match') is not None:
            temp_model = MCPMatch()
            self.match = temp_model.from_map(m['match'])
        if m.get('mcpStatisticsEnable') is not None:
            self.mcp_statistics_enable = m.get('mcpStatisticsEnable')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('toolId') is not None:
            self.tool_id = m.get('toolId')
        if m.get('toolsConfig') is not None:
            self.tools_config = m.get('toolsConfig')
        return self


class MCPServerConfig(TeaModel):
    def __init__(
        self,
        server_url: str = None,
        sse_path: str = None,
        transport_type: str = None,
    ):
        self.server_url = server_url
        self.sse_path = sse_path
        self.transport_type = transport_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_url is not None:
            result['serverUrl'] = self.server_url
        if self.sse_path is not None:
            result['ssePath'] = self.sse_path
        if self.transport_type is not None:
            result['transportType'] = self.transport_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serverUrl') is not None:
            self.server_url = m.get('serverUrl')
        if m.get('ssePath') is not None:
            self.sse_path = m.get('ssePath')
        if m.get('transportType') is not None:
            self.transport_type = m.get('transportType')
        return self


class Model(TeaModel):
    def __init__(
        self,
        address: str = None,
        api_key: str = None,
        created_time: str = None,
        desc: str = None,
        gateway_id: str = None,
        model_id: str = None,
        models: str = None,
        models_weight: str = None,
        name: str = None,
        provider: str = None,
        target_id: str = None,
        tenant_id: str = None,
        type: str = None,
        update_time: str = None,
    ):
        self.address = address
        self.api_key = api_key
        self.created_time = created_time
        self.desc = desc
        self.gateway_id = gateway_id
        self.model_id = model_id
        self.models = models
        self.models_weight = models_weight
        self.name = name
        self.provider = provider
        self.target_id = target_id
        self.tenant_id = tenant_id
        self.type = type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.api_key is not None:
            result['apiKey'] = self.api_key
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.desc is not None:
            result['desc'] = self.desc
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.models is not None:
            result['models'] = self.models
        if self.models_weight is not None:
            result['modelsWeight'] = self.models_weight
        if self.name is not None:
            result['name'] = self.name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.target_id is not None:
            result['targetId'] = self.target_id
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('models') is not None:
            self.models = m.get('models')
        if m.get('modelsWeight') is not None:
            self.models_weight = m.get('modelsWeight')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('targetId') is not None:
            self.target_id = m.get('targetId')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class PaginationInfo(TeaModel):
    def __init__(
        self,
        limit: int = None,
        page: int = None,
        total: int = None,
        total_pages: int = None,
    ):
        self.limit = limit
        self.page = page
        self.total = total
        self.total_pages = total_pages

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.page is not None:
            result['page'] = self.page
        if self.total is not None:
            result['total'] = self.total
        if self.total_pages is not None:
            result['totalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('totalPages') is not None:
            self.total_pages = m.get('totalPages')
        return self


class PublishRuntimeVersionInput(TeaModel):
    def __init__(
        self,
        description: str = None,
    ):
        # 此版本的描述
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class ServiceConfig(TeaModel):
    def __init__(
        self,
        ai_service_config: AiServiceConfig = None,
        name: str = None,
    ):
        self.ai_service_config = ai_service_config
        self.name = name

    def validate(self):
        if self.ai_service_config:
            self.ai_service_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_service_config is not None:
            result['aiServiceConfig'] = self.ai_service_config.to_map()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiServiceConfig') is not None:
            temp_model = AiServiceConfig()
            self.ai_service_config = temp_model.from_map(m['aiServiceConfig'])
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class StartBrowserSessionInput(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class StartBrowserSessionResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BrowserSessionOut = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = BrowserSessionOut()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class StartCodeInterpreterSessionInput(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # 代码解释器会话的名称，用于标识和区分不同的会话实例
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class StartCodeInterpreterSessionResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CodeInterpreterSessionOut = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CodeInterpreterSessionOut()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class StopCodeInterpreterSessionResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
    ):
        # SUCCESS 为成功，失败情况返回对应错误类型，比如 ERR_BAD_REQUEST ERR_VALIDATION_FAILED ERR_INTERNAL_SERVER_ERROR
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class Target(TeaModel):
    def __init__(
        self,
        llm_config: LLMAPIConfiguration = None,
        mcp_api: MCPAPI = None,
        target_type: str = None,
    ):
        self.llm_config = llm_config
        self.mcp_api = mcp_api
        self.target_type = target_type

    def validate(self):
        if self.llm_config:
            self.llm_config.validate()
        if self.mcp_api:
            self.mcp_api.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.llm_config is not None:
            result['llmConfig'] = self.llm_config.to_map()
        if self.mcp_api is not None:
            result['mcpAPI'] = self.mcp_api.to_map()
        if self.target_type is not None:
            result['targetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('llmConfig') is not None:
            temp_model = LLMAPIConfiguration()
            self.llm_config = temp_model.from_map(m['llmConfig'])
        if m.get('mcpAPI') is not None:
            temp_model = MCPAPI()
            self.mcp_api = temp_model.from_map(m['mcpAPI'])
        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')
        return self


class Template(TeaModel):
    def __init__(
        self,
        template_id: str = None,
        template_version: str = None,
    ):
        self.template_id = template_id
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['templateID'] = self.template_id
        if self.template_version is not None:
            result['templateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')
        if m.get('templateVersion') is not None:
            self.template_version = m.get('templateVersion')
        return self


class TriggerConfig(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        methods: List[str] = None,
    ):
        self.auth_type = auth_type
        self.methods = methods

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.methods is not None:
            result['methods'] = self.methods
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        return self


class UpdateAgentRuntimeEndpointInput(TeaModel):
    def __init__(
        self,
        agent_runtime_endpoint_name: str = None,
        description: str = None,
        routing_configuration: RoutingConfiguration = None,
        target_version: str = None,
    ):
        self.agent_runtime_endpoint_name = agent_runtime_endpoint_name
        self.description = description
        # 智能体运行时端点的路由配置，支持多版本权重分配
        self.routing_configuration = routing_configuration
        # 智能体运行时的目标版本
        self.target_version = target_version

    def validate(self):
        if self.routing_configuration:
            self.routing_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_runtime_endpoint_name is not None:
            result['agentRuntimeEndpointName'] = self.agent_runtime_endpoint_name
        if self.description is not None:
            result['description'] = self.description
        if self.routing_configuration is not None:
            result['routingConfiguration'] = self.routing_configuration.to_map()
        if self.target_version is not None:
            result['targetVersion'] = self.target_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeEndpointName') is not None:
            self.agent_runtime_endpoint_name = m.get('agentRuntimeEndpointName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('routingConfiguration') is not None:
            temp_model = RoutingConfiguration()
            self.routing_configuration = temp_model.from_map(m['routingConfiguration'])
        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')
        return self


class UpdateAgentRuntimeInput(TeaModel):
    def __init__(
        self,
        agent_runtime_name: str = None,
        artifact_type: str = None,
        code_configuration: CodeConfiguration = None,
        container_configuration: ContainerConfiguration = None,
        cpu: float = None,
        description: str = None,
        environment_variables: Dict[str, str] = None,
        execution_role_arn: str = None,
        health_check_configuration: HealthCheckConfiguration = None,
        log_configuration: LogConfiguration = None,
        memory: int = None,
        network_configuration: NetworkConfiguration = None,
        port: int = None,
        protocol_configuration: ProtocolConfiguration = None,
        session_concurrency_limit_per_instance: int = None,
        session_idle_timeout_seconds: int = None,
    ):
        self.agent_runtime_name = agent_runtime_name
        self.artifact_type = artifact_type
        self.code_configuration = code_configuration
        self.container_configuration = container_configuration
        # This parameter is required.
        self.cpu = cpu
        self.description = description
        self.environment_variables = environment_variables
        # 为智能体运行时提供访问云服务权限的执行角色ARN
        self.execution_role_arn = execution_role_arn
        # 智能体运行时的健康检查配置，用于监控运行时实例的健康状态
        self.health_check_configuration = health_check_configuration
        # SLS（简单日志服务）配置
        self.log_configuration = log_configuration
        self.memory = memory
        self.network_configuration = network_configuration
        self.port = port
        self.protocol_configuration = protocol_configuration
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
        if self.network_configuration:
            self.network_configuration.validate()
        if self.protocol_configuration:
            self.protocol_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.description is not None:
            result['description'] = self.description
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn
        if self.health_check_configuration is not None:
            result['healthCheckConfiguration'] = self.health_check_configuration.to_map()
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
            temp_model = CodeConfiguration()
            self.code_configuration = temp_model.from_map(m['codeConfiguration'])
        if m.get('containerConfiguration') is not None:
            temp_model = ContainerConfiguration()
            self.container_configuration = temp_model.from_map(m['containerConfiguration'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')
        if m.get('healthCheckConfiguration') is not None:
            temp_model = HealthCheckConfiguration()
            self.health_check_configuration = temp_model.from_map(m['healthCheckConfiguration'])
        if m.get('logConfiguration') is not None:
            temp_model = LogConfiguration()
            self.log_configuration = temp_model.from_map(m['logConfiguration'])
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('networkConfiguration') is not None:
            temp_model = NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m['networkConfiguration'])
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocolConfiguration') is not None:
            temp_model = ProtocolConfiguration()
            self.protocol_configuration = temp_model.from_map(m['protocolConfiguration'])
        if m.get('sessionConcurrencyLimitPerInstance') is not None:
            self.session_concurrency_limit_per_instance = m.get('sessionConcurrencyLimitPerInstance')
        if m.get('sessionIdleTimeoutSeconds') is not None:
            self.session_idle_timeout_seconds = m.get('sessionIdleTimeoutSeconds')
        return self


class UpdateCredentialInput(TeaModel):
    def __init__(
        self,
        config: Dict[str, str] = None,
        description: str = None,
        name: str = None,
        secret: str = None,
        type: str = None,
    ):
        self.config = config
        self.description = description
        self.name = name
        self.secret = secret
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.secret is not None:
            result['secret'] = self.secret
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('secret') is not None:
            self.secret = m.get('secret')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateCredentialOutput(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: str = None,
        updated_at: str = None,
    ):
        self.id = id
        self.name = name
        self.type = type
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        return self


class UpdateDomainInput(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        protocol: str = None,
    ):
        self.cert_identifier = cert_identifier
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['certIdentifier'] = self.cert_identifier
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certIdentifier') is not None:
            self.cert_identifier = m.get('certIdentifier')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class UpdateModelInput(TeaModel):
    def __init__(
        self,
        address: str = None,
        api_key: str = None,
        desc: str = None,
        models: List[str] = None,
        name: str = None,
        provider: str = None,
        type: str = None,
    ):
        self.address = address
        self.api_key = api_key
        self.desc = desc
        self.models = models
        self.name = name
        self.provider = provider
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.api_key is not None:
            result['apiKey'] = self.api_key
        if self.desc is not None:
            result['desc'] = self.desc
        if self.models is not None:
            result['models'] = self.models
        if self.name is not None:
            result['name'] = self.name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('models') is not None:
            self.models = m.get('models')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateTargetConfigurationInput(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        target_configuration: TargetConfiguration = None,
    ):
        self.domain_id = domain_id
        self.target_configuration = target_configuration

    def validate(self):
        if self.target_configuration:
            self.target_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.target_configuration is not None:
            result['targetConfiguration'] = self.target_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('targetConfiguration') is not None:
            temp_model = TargetConfiguration()
            self.target_configuration = temp_model.from_map(m['targetConfiguration'])
        return self


class UpdateToolData(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        source_type: str = None,
        tool_type: str = None,
        updated_at: str = None,
    ):
        self.id = id
        self.name = name
        self.source_type = source_type
        self.tool_type = tool_type
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.tool_type is not None:
            result['toolType'] = self.tool_type
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('toolType') is not None:
            self.tool_type = m.get('toolType')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        return self


class UpdateToolInput(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        schema: str = None,
    ):
        self.description = description
        self.name = name
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.schema is not None:
            result['schema'] = self.schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        return self


class UpdateToolOutput(TeaModel):
    def __init__(
        self,
        data: UpdateToolData = None,
        message: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = UpdateToolData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateAgentRuntimeRequest(TeaModel):
    def __init__(
        self,
        body: CreateAgentRuntimeInput = None,
    ):
        # 创建智能体运行时所需的完整配置信息，包括运行时名称、资源规格、网络配置、协议配置等
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateAgentRuntimeInput()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAgentRuntimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgentRuntimeResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgentRuntimeResult()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAgentRuntimeEndpointRequest(TeaModel):
    def __init__(
        self,
        body: CreateAgentRuntimeEndpointInput = None,
    ):
        # 包含要创建的智能体运行时端点配置信息的请求体
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateAgentRuntimeEndpointInput()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAgentRuntimeEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgentRuntimeEndpointResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgentRuntimeEndpointResult()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBrowserRequest(TeaModel):
    def __init__(
        self,
        body: CreateBrowserInput = None,
    ):
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateBrowserInput()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBrowserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BrowserResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BrowserResult()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCodeInterpreterRequest(TeaModel):
    def __init__(
        self,
        body: CreateCodeInterpreterInput = None,
    ):
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateCodeInterpreterInput()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCodeInterpreterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CodeInterpreterResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CodeInterpreterResult()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAgentRuntimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgentRuntimeResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgentRuntimeResult()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAgentRuntimeEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgentRuntimeEndpointResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgentRuntimeEndpointResult()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBrowserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBrowserResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBrowserResult()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCodeInterpreterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCodeInterpreterResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCodeInterpreterResult()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentRuntimeRequest(TeaModel):
    def __init__(
        self,
        agent_runtime_version: str = None,
    ):
        # 指定要获取的智能体运行时版本，如果不指定则返回最新版本
        self.agent_runtime_version = agent_runtime_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_runtime_version is not None:
            result['agentRuntimeVersion'] = self.agent_runtime_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeVersion') is not None:
            self.agent_runtime_version = m.get('agentRuntimeVersion')
        return self


class GetAgentRuntimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgentRuntimeResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgentRuntimeResult()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentRuntimeEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgentRuntimeEndpointResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgentRuntimeEndpointResult()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBrowserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BrowserResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BrowserResult()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCodeInterpreterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CodeInterpreterResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CodeInterpreterResult()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAgentRuntimeEndpointsRequest(TeaModel):
    def __init__(
        self,
        endpoint_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 根据端点名称进行模糊匹配过滤
        self.endpoint_name = endpoint_name
        # 当前页码，从1开始计数
        self.page_number = page_number
        # 每页返回的记录数量
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_name is not None:
            result['endpointName'] = self.endpoint_name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpointName') is not None:
            self.endpoint_name = m.get('endpointName')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListAgentRuntimeEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAgentRuntimeEndpointsResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAgentRuntimeEndpointsResult()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAgentRuntimeVersionsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # 当前页码，从1开始计数
        self.page_number = page_number
        # 每页返回的记录数量
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListAgentRuntimeVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAgentRuntimeVersionsResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAgentRuntimeVersionsResult()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAgentRuntimesRequest(TeaModel):
    def __init__(
        self,
        agent_runtime_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 根据智能体运行时名称进行模糊匹配过滤
        self.agent_runtime_name = agent_runtime_name
        # 当前页码，从1开始计数
        self.page_number = page_number
        # 每页返回的记录数量
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_runtime_name is not None:
            result['agentRuntimeName'] = self.agent_runtime_name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeName') is not None:
            self.agent_runtime_name = m.get('agentRuntimeName')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListAgentRuntimesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAgentRuntimesResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAgentRuntimesResult()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBrowsersRequest(TeaModel):
    def __init__(
        self,
        browser_name: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        # 根据浏览器实例名称进行模糊匹配过滤
        self.browser_name = browser_name
        # 当前页码，从1开始计数
        self.page_number = page_number
        # 每页返回的记录数量
        self.page_size = page_size
        # 根据浏览器实例的运行状态进行过滤，可选值：CREATING、READY、DELETING等
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.browser_name is not None:
            result['browserName'] = self.browser_name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('browserName') is not None:
            self.browser_name = m.get('browserName')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListBrowsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBrowsersResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBrowsersResult()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCodeInterpretersRequest(TeaModel):
    def __init__(
        self,
        code_interpreter_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 根据代码解释器实例名称进行模糊匹配过滤
        self.code_interpreter_name = code_interpreter_name
        # 当前页码，从1开始计数
        self.page_number = page_number
        # 每页返回的记录数量
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_interpreter_name is not None:
            result['codeInterpreterName'] = self.code_interpreter_name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeInterpreterName') is not None:
            self.code_interpreter_name = m.get('codeInterpreterName')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListCodeInterpretersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCodeInterpretersResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCodeInterpretersResult()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishRuntimeVersionRequest(TeaModel):
    def __init__(
        self,
        body: PublishRuntimeVersionInput = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PublishRuntimeVersionInput()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishRuntimeVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgentRuntimeVersionResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgentRuntimeVersionResult()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAgentRuntimeRequest(TeaModel):
    def __init__(
        self,
        body: UpdateAgentRuntimeInput = None,
    ):
        # 包含要更新的智能体运行时配置信息的请求体
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = UpdateAgentRuntimeInput()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAgentRuntimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgentRuntimeResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgentRuntimeResult()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAgentRuntimeEndpointRequest(TeaModel):
    def __init__(
        self,
        body: UpdateAgentRuntimeEndpointInput = None,
    ):
        # 包含要更新的智能体运行时端点配置信息的请求体
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = UpdateAgentRuntimeEndpointInput()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAgentRuntimeEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgentRuntimeEndpointResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgentRuntimeEndpointResult()
            self.body = temp_model.from_map(m['body'])
        return self


