# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class UpdateToolInputV2(DaraModel):
    def __init__(
        self,
        artifact_type: str = None,
        code_configuration: main_models.CodeConfiguration = None,
        container_configuration: main_models.ContainerConfiguration = None,
        cpu: float = None,
        create_method: str = None,
        credential_name: str = None,
        description: str = None,
        environment_variables: Dict[str, str] = None,
        execution_role_arn: str = None,
        log_configuration: main_models.LogConfiguration = None,
        mcp_config: main_models.McpConfig = None,
        memory: int = None,
        nas_config: main_models.NASConfig = None,
        network_configuration: main_models.NetworkConfiguration = None,
        oss_mount_config: main_models.OSSMountConfig = None,
        port: int = None,
        protocol_spec: str = None,
        timeout: int = None,
        workspace_id: str = None,
    ):
        # 更新工具部署的制品类型，支持：Code（代码包）、Container（容器镜像）
        self.artifact_type = artifact_type
        # 更新代码包类型工具的配置信息
        self.code_configuration = code_configuration
        # 更新容器类型工具的配置信息
        self.container_configuration = container_configuration
        # 更新工具实例的 CPU 核心数，单位为核
        self.cpu = cpu
        # 更新工具的创建方式。支持：MCP_REMOTE、MCP_LOCAL_STDIO、MCP_BUNDLE、CODE_PACKAGE、OPENAPI_IMPORT
        self.create_method = create_method
        # 更新工具使用的凭证名称
        self.credential_name = credential_name
        # 更新工具的描述信息
        self.description = description
        # 更新工具运行时的环境变量配置
        self.environment_variables = environment_variables
        # 更新工具执行时使用的 RAM 角色 ARN
        self.execution_role_arn = execution_role_arn
        # 更新工具的日志配置
        self.log_configuration = log_configuration
        # 更新 MCP 工具的配置信息，包括会话亲和性、代理配置等
        self.mcp_config = mcp_config
        # 更新工具实例的内存大小，单位为 MB
        self.memory = memory
        # 更新文件存储 NAS 的配置信息
        self.nas_config = nas_config
        # 更新工具的网络配置
        self.network_configuration = network_configuration
        # 更新对象存储 OSS 的挂载配置
        self.oss_mount_config = oss_mount_config
        # 更新工具服务监听的端口号
        self.port = port
        # 更新工具使用的协议规范定义
        self.protocol_spec = protocol_spec
        # 更新工具执行的超时时间，单位为秒
        self.timeout = timeout
        # 更新工具所属的工作空间标识符
        self.workspace_id = workspace_id

    def validate(self):
        if self.code_configuration:
            self.code_configuration.validate()
        if self.container_configuration:
            self.container_configuration.validate()
        if self.log_configuration:
            self.log_configuration.validate()
        if self.mcp_config:
            self.mcp_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.network_configuration:
            self.network_configuration.validate()
        if self.oss_mount_config:
            self.oss_mount_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_type is not None:
            result['artifactType'] = self.artifact_type

        if self.code_configuration is not None:
            result['codeConfiguration'] = self.code_configuration.to_map()

        if self.container_configuration is not None:
            result['containerConfiguration'] = self.container_configuration.to_map()

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.create_method is not None:
            result['createMethod'] = self.create_method

        if self.credential_name is not None:
            result['credentialName'] = self.credential_name

        if self.description is not None:
            result['description'] = self.description

        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables

        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn

        if self.log_configuration is not None:
            result['logConfiguration'] = self.log_configuration.to_map()

        if self.mcp_config is not None:
            result['mcpConfig'] = self.mcp_config.to_map()

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

        if self.protocol_spec is not None:
            result['protocolSpec'] = self.protocol_spec

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('createMethod') is not None:
            self.create_method = m.get('createMethod')

        if m.get('credentialName') is not None:
            self.credential_name = m.get('credentialName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')

        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')

        if m.get('logConfiguration') is not None:
            temp_model = main_models.LogConfiguration()
            self.log_configuration = temp_model.from_map(m.get('logConfiguration'))

        if m.get('mcpConfig') is not None:
            temp_model = main_models.McpConfig()
            self.mcp_config = temp_model.from_map(m.get('mcpConfig'))

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

        if m.get('protocolSpec') is not None:
            self.protocol_spec = m.get('protocolSpec')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

