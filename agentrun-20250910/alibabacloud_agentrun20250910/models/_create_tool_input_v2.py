# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateToolInputV2(DaraModel):
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
        tool_name: str = None,
        tool_type: str = None,
        workspace_id: str = None,
    ):
        # 工具部署的制品类型，支持：Code（代码包）、Container（容器镜像）
        self.artifact_type = artifact_type
        # 代码包类型工具的配置信息，包括代码位置、入口函数、运行时等，仅在制品类型为 Code 时需要提供
        self.code_configuration = code_configuration
        # 容器类型工具的配置信息，包括镜像地址、启动命令、端口映射等，仅在制品类型为 Container 时需要提供
        self.container_configuration = container_configuration
        # 工具实例的 CPU 核心数，单位为核，支持小数，如 0.5 表示半核
        self.cpu = cpu
        # 工具的创建方式，必填项。支持：MCP_REMOTE（远程 MCP 服务器）、MCP_LOCAL_STDIO（本地 MCP 标准输入输出）、MCP_BUNDLE（MCP 打包部署）、CODE_PACKAGE（代码包部署）、OPENAPI_IMPORT（OpenAPI 导入）
        # 
        # This parameter is required.
        self.create_method = create_method
        # 工具使用的凭证名称，用于访问需要认证的外部服务，需要提前在系统中创建凭证
        self.credential_name = credential_name
        # 工具的详细描述信息，说明工具的功能和用途
        self.description = description
        # 工具运行时的环境变量配置，键值对形式，用于传递配置信息到工具运行环境
        self.environment_variables = environment_variables
        # 工具执行时使用的 RAM 角色 ARN，用于权限控制，格式如：acs:ram::123456789:role/AliyunFCDefaultRole
        self.execution_role_arn = execution_role_arn
        # 工具的日志配置，包括日志存储位置（SLS）、日志级别等
        self.log_configuration = log_configuration
        # MCP 工具的配置信息，包括会话亲和性、代理配置、绑定配置等，仅在工具类型为 MCP 时需要提供
        self.mcp_config = mcp_config
        # 工具实例的内存大小，单位为 MB，建议根据工具的实际需求配置
        self.memory = memory
        # 文件存储 NAS 的配置信息，用于工具访问 NAS 文件系统，实现持久化存储
        self.nas_config = nas_config
        # 工具的网络配置，包括 VPC、安全组、交换机等信息，用于配置工具的网络访问能力
        self.network_configuration = network_configuration
        # 对象存储 OSS 的挂载配置，用于工具访问 OSS 存储桶中的文件
        self.oss_mount_config = oss_mount_config
        # 工具服务监听的端口号，用于接收请求
        self.port = port
        # 工具使用的协议规范定义，JSON 格式的字符串，定义工具的接口和交互方式
        self.protocol_spec = protocol_spec
        # 工具执行的超时时间，单位为秒，超过此时间工具调用将被终止
        self.timeout = timeout
        # 工具的名称，必填项，用于标识和引用工具，需要在工作空间内唯一
        # 
        # This parameter is required.
        self.tool_name = tool_name
        # 工具的类型，必填项。支持：MCP（Model Context Protocol 工具）、FUNCTIONCALL（函数调用工具）、SKILL（技能工具）
        # 
        # This parameter is required.
        self.tool_type = tool_type
        # 工具所属的工作空间标识符，可选项，不填则使用默认工作空间
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

        if self.tool_name is not None:
            result['toolName'] = self.tool_name

        if self.tool_type is not None:
            result['toolType'] = self.tool_type

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

        if m.get('toolName') is not None:
            self.tool_name = m.get('toolName')

        if m.get('toolType') is not None:
            self.tool_type = m.get('toolType')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

