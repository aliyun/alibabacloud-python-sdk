# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class InstallMcpMarketItemResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.InstallMcpMarketItemResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The response data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The request ID, which is used to locate and troubleshoot requests.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.InstallMcpMarketItemResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class InstallMcpMarketItemResponseBodyData(DaraModel):
    def __init__(
        self,
        addresses: List[str] = None,
        custom_tags: List[str] = None,
        deployment_config: main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfig = None,
        description: str = None,
        endpoint: str = None,
        function_name: str = None,
        market_source: main_models.InstallMcpMarketItemResponseBodyDataMarketSource = None,
        mcp_server_id: str = None,
        name: str = None,
        official_tag: str = None,
        protocol: str = None,
        status: str = None,
        status_reason: str = None,
        template: main_models.InstallMcpMarketItemResponseBodyDataTemplate = None,
        type: str = None,
        usage_active: bool = None,
    ):
        # The list of remote MCP service addresses.
        self.addresses = addresses
        # The custom tags. Multiple tags are supported.
        self.custom_tags = custom_tags
        # The deployment configuration for code-deployed MCP.
        self.deployment_config = deployment_config
        # The MCP service description.
        self.description = description
        # The MCP server endpoint.
        self.endpoint = endpoint
        # The Function Compute function name that corresponds to the code-deployed MCP server.
        self.function_name = function_name
        # The marketplace template from which the MCP service originates.
        self.market_source = market_source
        # The MCP server ID.
        self.mcp_server_id = mcp_server_id
        # The MCP service name.
        self.name = name
        # The official usage tag, managed by the server.
        self.official_tag = official_tag
        # The MCP protocol.
        self.protocol = protocol
        # The MCP service status.
        self.status = status
        # The reason why the MCP service is in the current status.
        self.status_reason = status_reason
        # The template version and input schema bound to the MCP service.
        self.template = template
        # The MCP type. Valid values:
        # - DIRECT_PROXY: direct proxy.
        # - HTTP_TO_MCP: HTTP-to-MCP conversion.
        # - CODE_PACKAGE: code deployment.
        self.type = type
        # Indicates whether the MCP service is still bound by the usage constraints of the official template.
        self.usage_active = usage_active

    def validate(self):
        if self.deployment_config:
            self.deployment_config.validate()
        if self.market_source:
            self.market_source.validate()
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addresses is not None:
            result['addresses'] = self.addresses

        if self.custom_tags is not None:
            result['customTags'] = self.custom_tags

        if self.deployment_config is not None:
            result['deploymentConfig'] = self.deployment_config.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.function_name is not None:
            result['functionName'] = self.function_name

        if self.market_source is not None:
            result['marketSource'] = self.market_source.to_map()

        if self.mcp_server_id is not None:
            result['mcpServerId'] = self.mcp_server_id

        if self.name is not None:
            result['name'] = self.name

        if self.official_tag is not None:
            result['officialTag'] = self.official_tag

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        if self.template is not None:
            result['template'] = self.template.to_map()

        if self.type is not None:
            result['type'] = self.type

        if self.usage_active is not None:
            result['usageActive'] = self.usage_active

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addresses') is not None:
            self.addresses = m.get('addresses')

        if m.get('customTags') is not None:
            self.custom_tags = m.get('customTags')

        if m.get('deploymentConfig') is not None:
            temp_model = main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfig()
            self.deployment_config = temp_model.from_map(m.get('deploymentConfig'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

        if m.get('marketSource') is not None:
            temp_model = main_models.InstallMcpMarketItemResponseBodyDataMarketSource()
            self.market_source = temp_model.from_map(m.get('marketSource'))

        if m.get('mcpServerId') is not None:
            self.mcp_server_id = m.get('mcpServerId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('officialTag') is not None:
            self.official_tag = m.get('officialTag')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        if m.get('template') is not None:
            temp_model = main_models.InstallMcpMarketItemResponseBodyDataTemplate()
            self.template = temp_model.from_map(m.get('template'))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('usageActive') is not None:
            self.usage_active = m.get('usageActive')

        return self

class InstallMcpMarketItemResponseBodyDataTemplate(DaraModel):
    def __init__(
        self,
        applied_template_version: str = None,
        latest_template_version: str = None,
        schema_version: str = None,
        template_input_schema: str = None,
        update_available: bool = None,
    ):
        # The template version that is currently applied to the MCP service.
        self.applied_template_version = applied_template_version
        # The latest template version.
        self.latest_template_version = latest_template_version
        # The template schema version.
        self.schema_version = schema_version
        # The template input schema, represented as a JSON Schema string.
        self.template_input_schema = template_input_schema
        # Indicates whether a newer template version is available for update.
        self.update_available = update_available

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applied_template_version is not None:
            result['appliedTemplateVersion'] = self.applied_template_version

        if self.latest_template_version is not None:
            result['latestTemplateVersion'] = self.latest_template_version

        if self.schema_version is not None:
            result['schemaVersion'] = self.schema_version

        if self.template_input_schema is not None:
            result['templateInputSchema'] = self.template_input_schema

        if self.update_available is not None:
            result['updateAvailable'] = self.update_available

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appliedTemplateVersion') is not None:
            self.applied_template_version = m.get('appliedTemplateVersion')

        if m.get('latestTemplateVersion') is not None:
            self.latest_template_version = m.get('latestTemplateVersion')

        if m.get('schemaVersion') is not None:
            self.schema_version = m.get('schemaVersion')

        if m.get('templateInputSchema') is not None:
            self.template_input_schema = m.get('templateInputSchema')

        if m.get('updateAvailable') is not None:
            self.update_available = m.get('updateAvailable')

        return self

class InstallMcpMarketItemResponseBodyDataMarketSource(DaraModel):
    def __init__(
        self,
        market_item_id: str = None,
    ):
        # The MCP marketplace template ID.
        self.market_item_id = market_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.market_item_id is not None:
            result['marketItemId'] = self.market_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marketItemId') is not None:
            self.market_item_id = m.get('marketItemId')

        return self

class InstallMcpMarketItemResponseBodyDataDeploymentConfig(DaraModel):
    def __init__(
        self,
        access_control: main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigAccessControl = None,
        agent_identity_configuration: main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigAgentIdentityConfiguration = None,
        artifact_type: str = None,
        code_configuration: main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigCodeConfiguration = None,
        container_configuration: main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigContainerConfiguration = None,
        hook_configuration: main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigHookConfiguration = None,
        log_configuration: main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigLogConfiguration = None,
        mcp_configuration: main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigMcpConfiguration = None,
        nas_configuration: main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigNasConfiguration = None,
        network_configuration: main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigNetworkConfiguration = None,
        oss_mount_configuration: main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigOssMountConfiguration = None,
        parameter_transform_configuration: main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigParameterTransformConfiguration = None,
        proxy_configuration: main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigProxyConfiguration = None,
        runtime_configuration: main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigRuntimeConfiguration = None,
    ):
        # The MCP ingress access control configuration.
        self.access_control = access_control
        # The Agent Identity configuration.
        self.agent_identity_configuration = agent_identity_configuration
        # Code indicates a ZIP code package. Container indicates a custom container.
        self.artifact_type = artifact_type
        # The code package configuration.
        self.code_configuration = code_configuration
        # The custom container configuration.
        self.container_configuration = container_configuration
        # The hook configuration.
        self.hook_configuration = hook_configuration
        # The log configuration.
        self.log_configuration = log_configuration
        # The MCP session configuration.
        self.mcp_configuration = mcp_configuration
        # The NAS storage configuration.
        self.nas_configuration = nas_configuration
        # The network configuration.
        self.network_configuration = network_configuration
        # The OSS mount configuration.
        self.oss_mount_configuration = oss_mount_configuration
        # The parameter transformation and result enhancement configuration.
        self.parameter_transform_configuration = parameter_transform_configuration
        # The MCP proxy configuration.
        self.proxy_configuration = proxy_configuration
        # The runtime and resource configuration.
        self.runtime_configuration = runtime_configuration

    def validate(self):
        if self.access_control:
            self.access_control.validate()
        if self.agent_identity_configuration:
            self.agent_identity_configuration.validate()
        if self.code_configuration:
            self.code_configuration.validate()
        if self.container_configuration:
            self.container_configuration.validate()
        if self.hook_configuration:
            self.hook_configuration.validate()
        if self.log_configuration:
            self.log_configuration.validate()
        if self.mcp_configuration:
            self.mcp_configuration.validate()
        if self.nas_configuration:
            self.nas_configuration.validate()
        if self.network_configuration:
            self.network_configuration.validate()
        if self.oss_mount_configuration:
            self.oss_mount_configuration.validate()
        if self.parameter_transform_configuration:
            self.parameter_transform_configuration.validate()
        if self.proxy_configuration:
            self.proxy_configuration.validate()
        if self.runtime_configuration:
            self.runtime_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_control is not None:
            result['accessControl'] = self.access_control.to_map()

        if self.agent_identity_configuration is not None:
            result['agentIdentityConfiguration'] = self.agent_identity_configuration.to_map()

        if self.artifact_type is not None:
            result['artifactType'] = self.artifact_type

        if self.code_configuration is not None:
            result['codeConfiguration'] = self.code_configuration.to_map()

        if self.container_configuration is not None:
            result['containerConfiguration'] = self.container_configuration.to_map()

        if self.hook_configuration is not None:
            result['hookConfiguration'] = self.hook_configuration.to_map()

        if self.log_configuration is not None:
            result['logConfiguration'] = self.log_configuration.to_map()

        if self.mcp_configuration is not None:
            result['mcpConfiguration'] = self.mcp_configuration.to_map()

        if self.nas_configuration is not None:
            result['nasConfiguration'] = self.nas_configuration.to_map()

        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()

        if self.oss_mount_configuration is not None:
            result['ossMountConfiguration'] = self.oss_mount_configuration.to_map()

        if self.parameter_transform_configuration is not None:
            result['parameterTransformConfiguration'] = self.parameter_transform_configuration.to_map()

        if self.proxy_configuration is not None:
            result['proxyConfiguration'] = self.proxy_configuration.to_map()

        if self.runtime_configuration is not None:
            result['runtimeConfiguration'] = self.runtime_configuration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessControl') is not None:
            temp_model = main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigAccessControl()
            self.access_control = temp_model.from_map(m.get('accessControl'))

        if m.get('agentIdentityConfiguration') is not None:
            temp_model = main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigAgentIdentityConfiguration()
            self.agent_identity_configuration = temp_model.from_map(m.get('agentIdentityConfiguration'))

        if m.get('artifactType') is not None:
            self.artifact_type = m.get('artifactType')

        if m.get('codeConfiguration') is not None:
            temp_model = main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigCodeConfiguration()
            self.code_configuration = temp_model.from_map(m.get('codeConfiguration'))

        if m.get('containerConfiguration') is not None:
            temp_model = main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigContainerConfiguration()
            self.container_configuration = temp_model.from_map(m.get('containerConfiguration'))

        if m.get('hookConfiguration') is not None:
            temp_model = main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigHookConfiguration()
            self.hook_configuration = temp_model.from_map(m.get('hookConfiguration'))

        if m.get('logConfiguration') is not None:
            temp_model = main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigLogConfiguration()
            self.log_configuration = temp_model.from_map(m.get('logConfiguration'))

        if m.get('mcpConfiguration') is not None:
            temp_model = main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigMcpConfiguration()
            self.mcp_configuration = temp_model.from_map(m.get('mcpConfiguration'))

        if m.get('nasConfiguration') is not None:
            temp_model = main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigNasConfiguration()
            self.nas_configuration = temp_model.from_map(m.get('nasConfiguration'))

        if m.get('networkConfiguration') is not None:
            temp_model = main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigNetworkConfiguration()
            self.network_configuration = temp_model.from_map(m.get('networkConfiguration'))

        if m.get('ossMountConfiguration') is not None:
            temp_model = main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigOssMountConfiguration()
            self.oss_mount_configuration = temp_model.from_map(m.get('ossMountConfiguration'))

        if m.get('parameterTransformConfiguration') is not None:
            temp_model = main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigParameterTransformConfiguration()
            self.parameter_transform_configuration = temp_model.from_map(m.get('parameterTransformConfiguration'))

        if m.get('proxyConfiguration') is not None:
            temp_model = main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigProxyConfiguration()
            self.proxy_configuration = temp_model.from_map(m.get('proxyConfiguration'))

        if m.get('runtimeConfiguration') is not None:
            temp_model = main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigRuntimeConfiguration()
            self.runtime_configuration = temp_model.from_map(m.get('runtimeConfiguration'))

        return self

class InstallMcpMarketItemResponseBodyDataDeploymentConfigRuntimeConfiguration(DaraModel):
    def __init__(
        self,
        cpu: float = None,
        disk_size: int = None,
        environment_variables: Dict[str, str] = None,
        execution_role_arn: str = None,
        instance_concurrency: int = None,
        memory: int = None,
        port: int = None,
        timeout: int = None,
    ):
        # The number of vCPUs. Default value: 0.25.
        self.cpu = cpu
        # The ephemeral disk size. Unit: MB. Valid values: 512 and 10240.
        self.disk_size = disk_size
        # The environment variables.
        self.environment_variables = environment_variables
        # The ARN of the RAM role used by user code to access downstream Alibaba Cloud resources.
        self.execution_role_arn = execution_role_arn
        # The maximum number of concurrent requests per instance. Default value: 200.
        self.instance_concurrency = instance_concurrency
        # The memory size. Unit: MB. Default value: 512.
        self.memory = memory
        # The service port. Default value: 9000.
        self.port = port
        # The function timeout period. Unit: seconds. Default value: 300.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.disk_size is not None:
            result['diskSize'] = self.disk_size

        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables

        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn

        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency

        if self.memory is not None:
            result['memory'] = self.memory

        if self.port is not None:
            result['port'] = self.port

        if self.timeout is not None:
            result['timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')

        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')

        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')

        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        return self

class InstallMcpMarketItemResponseBodyDataDeploymentConfigProxyConfiguration(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Specifies whether to enable the MCP proxy.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

class InstallMcpMarketItemResponseBodyDataDeploymentConfigParameterTransformConfiguration(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        rule_set_id: str = None,
        version: str = None,
    ):
        # Specifies whether to enable parameter transformation and result enhancement.
        self.enabled = enabled
        # The reserved reference to a parameter transformation and result enhancement rule set.
        self.rule_set_id = rule_set_id
        # The transformation rule version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.rule_set_id is not None:
            result['ruleSetId'] = self.rule_set_id

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('ruleSetId') is not None:
            self.rule_set_id = m.get('ruleSetId')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class InstallMcpMarketItemResponseBodyDataDeploymentConfigOssMountConfiguration(DaraModel):
    def __init__(
        self,
        mount_points: List[main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigOssMountConfigurationMountPoints] = None,
    ):
        # The list of OSS mount points.
        self.mount_points = mount_points

    def validate(self):
        if self.mount_points:
            for v1 in self.mount_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['mountPoints'] = []
        if self.mount_points is not None:
            for k1 in self.mount_points:
                result['mountPoints'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_points = []
        if m.get('mountPoints') is not None:
            for k1 in m.get('mountPoints'):
                temp_model = main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigOssMountConfigurationMountPoints()
                self.mount_points.append(temp_model.from_map(k1))

        return self

class InstallMcpMarketItemResponseBodyDataDeploymentConfigOssMountConfigurationMountPoints(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_path: str = None,
        endpoint: str = None,
        mount_dir: str = None,
        read_only: bool = None,
    ):
        # The OSS bucket name.
        self.bucket_name = bucket_name
        # The OSS bucket path.
        self.bucket_path = bucket_path
        # The OSS service endpoint.
        self.endpoint = endpoint
        # The local mount directory.
        self.mount_dir = mount_dir
        # Specifies whether the mount point is read-only.
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name

        if self.bucket_path is not None:
            result['bucketPath'] = self.bucket_path

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir

        if self.read_only is not None:
            result['readOnly'] = self.read_only

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')

        if m.get('bucketPath') is not None:
            self.bucket_path = m.get('bucketPath')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')

        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')

        return self

class InstallMcpMarketItemResponseBodyDataDeploymentConfigNetworkConfiguration(DaraModel):
    def __init__(
        self,
        network_mode: str = None,
        security_group_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        # The network mode.
        self.network_mode = network_mode
        # The security group ID.
        self.security_group_id = security_group_id
        # The list of vSwitch IDs.
        self.v_switch_ids = v_switch_ids
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_mode is not None:
            result['networkMode'] = self.network_mode

        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.v_switch_ids is not None:
            result['vSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('networkMode') is not None:
            self.network_mode = m.get('networkMode')

        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('vSwitchIds') is not None:
            self.v_switch_ids = m.get('vSwitchIds')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

class InstallMcpMarketItemResponseBodyDataDeploymentConfigNasConfiguration(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        mount_points: List[main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigNasConfigurationMountPoints] = None,
        user_id: int = None,
    ):
        # The runtime user group ID.
        self.group_id = group_id
        # The list of NAS mount points.
        self.mount_points = mount_points
        # The runtime user ID.
        self.user_id = user_id

    def validate(self):
        if self.mount_points:
            for v1 in self.mount_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['groupId'] = self.group_id

        result['mountPoints'] = []
        if self.mount_points is not None:
            for k1 in self.mount_points:
                result['mountPoints'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        self.mount_points = []
        if m.get('mountPoints') is not None:
            for k1 in m.get('mountPoints'):
                temp_model = main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigNasConfigurationMountPoints()
                self.mount_points.append(temp_model.from_map(k1))

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class InstallMcpMarketItemResponseBodyDataDeploymentConfigNasConfigurationMountPoints(DaraModel):
    def __init__(
        self,
        enable_tls: bool = None,
        mount_dir: str = None,
        server_addr: str = None,
    ):
        # Specifies whether to enable TLS.
        self.enable_tls = enable_tls
        # The local mount directory.
        self.mount_dir = mount_dir
        # The NAS server address.
        self.server_addr = server_addr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_tls is not None:
            result['enableTls'] = self.enable_tls

        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir

        if self.server_addr is not None:
            result['serverAddr'] = self.server_addr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableTls') is not None:
            self.enable_tls = m.get('enableTls')

        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')

        if m.get('serverAddr') is not None:
            self.server_addr = m.get('serverAddr')

        return self

class InstallMcpMarketItemResponseBodyDataDeploymentConfigMcpConfiguration(DaraModel):
    def __init__(
        self,
        endpoint_path: str = None,
        session_concurrency_per_instance: int = None,
        session_idle_timeout_seconds: int = None,
        session_max_lifetime_seconds: int = None,
    ):
        # The MCP endpoint path. For example, /mcp or /sse.
        self.endpoint_path = endpoint_path
        # The number of concurrent sessions per instance. Currently fixed to 1.
        self.session_concurrency_per_instance = session_concurrency_per_instance
        # The session idle timeout period. Unit: seconds. Default value: 1800.
        self.session_idle_timeout_seconds = session_idle_timeout_seconds
        # The maximum session lifetime. Unit: seconds. Default value: 21600.
        self.session_max_lifetime_seconds = session_max_lifetime_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_path is not None:
            result['endpointPath'] = self.endpoint_path

        if self.session_concurrency_per_instance is not None:
            result['sessionConcurrencyPerInstance'] = self.session_concurrency_per_instance

        if self.session_idle_timeout_seconds is not None:
            result['sessionIdleTimeoutSeconds'] = self.session_idle_timeout_seconds

        if self.session_max_lifetime_seconds is not None:
            result['sessionMaxLifetimeSeconds'] = self.session_max_lifetime_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpointPath') is not None:
            self.endpoint_path = m.get('endpointPath')

        if m.get('sessionConcurrencyPerInstance') is not None:
            self.session_concurrency_per_instance = m.get('sessionConcurrencyPerInstance')

        if m.get('sessionIdleTimeoutSeconds') is not None:
            self.session_idle_timeout_seconds = m.get('sessionIdleTimeoutSeconds')

        if m.get('sessionMaxLifetimeSeconds') is not None:
            self.session_max_lifetime_seconds = m.get('sessionMaxLifetimeSeconds')

        return self

class InstallMcpMarketItemResponseBodyDataDeploymentConfigLogConfiguration(DaraModel):
    def __init__(
        self,
        enable_instance_metrics: bool = None,
        enable_request_metrics: bool = None,
        log_begin_rule: str = None,
        logstore: str = None,
        project: str = None,
    ):
        # Specifies whether to collect instance metrics.
        self.enable_instance_metrics = enable_instance_metrics
        # Specifies whether to collect request metrics.
        self.enable_request_metrics = enable_request_metrics
        # The log splitting begin rule for Function Compute (FC).
        self.log_begin_rule = log_begin_rule
        # The Logstore name.
        self.logstore = logstore
        # The Log Service project name.
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_instance_metrics is not None:
            result['enableInstanceMetrics'] = self.enable_instance_metrics

        if self.enable_request_metrics is not None:
            result['enableRequestMetrics'] = self.enable_request_metrics

        if self.log_begin_rule is not None:
            result['logBeginRule'] = self.log_begin_rule

        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.project is not None:
            result['project'] = self.project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableInstanceMetrics') is not None:
            self.enable_instance_metrics = m.get('enableInstanceMetrics')

        if m.get('enableRequestMetrics') is not None:
            self.enable_request_metrics = m.get('enableRequestMetrics')

        if m.get('logBeginRule') is not None:
            self.log_begin_rule = m.get('logBeginRule')

        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('project') is not None:
            self.project = m.get('project')

        return self

class InstallMcpMarketItemResponseBodyDataDeploymentConfigHookConfiguration(DaraModel):
    def __init__(
        self,
        hooks: List[main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigHookConfigurationHooks] = None,
    ):
        # Executes PRE_LIST_TOOLS, PRE_CALL_TOOL, POST_LIST_TOOLS, and POST_CALL_TOOL hooks in array order.
        self.hooks = hooks

    def validate(self):
        if self.hooks:
            for v1 in self.hooks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['hooks'] = []
        if self.hooks is not None:
            for k1 in self.hooks:
                result['hooks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hooks = []
        if m.get('hooks') is not None:
            for k1 in m.get('hooks'):
                temp_model = main_models.InstallMcpMarketItemResponseBodyDataDeploymentConfigHookConfigurationHooks()
                self.hooks.append(temp_model.from_map(k1))

        return self

class InstallMcpMarketItemResponseBodyDataDeploymentConfigHookConfigurationHooks(DaraModel):
    def __init__(
        self,
        api_version: str = None,
        description: str = None,
        enabled: bool = None,
        event: str = None,
        headers: Dict[str, str] = None,
        timeout: int = None,
        url: str = None,
    ):
        # The hook API version.
        self.api_version = api_version
        # The hook description.
        self.description = description
        # Specifies whether to enable the hook.
        self.enabled = enabled
        # The hook event.
        self.event = event
        # The hook request headers.
        self.headers = headers
        # The timeout period, in milliseconds.
        self.timeout = timeout
        # The hook callback URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_version is not None:
            result['apiVersion'] = self.api_version

        if self.description is not None:
            result['description'] = self.description

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.event is not None:
            result['event'] = self.event

        if self.headers is not None:
            result['headers'] = self.headers

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class InstallMcpMarketItemResponseBodyDataDeploymentConfigContainerConfiguration(DaraModel):
    def __init__(
        self,
        acr_instance_id: str = None,
        command: List[str] = None,
        entrypoint: List[str] = None,
        image: str = None,
        image_registry_type: str = None,
        mcp_runtime_mode: str = None,
        source_type: str = None,
    ):
        # The ACR instance ID.
        self.acr_instance_id = acr_instance_id
        # The startup command.
        self.command = command
        # The container entrypoint arguments.
        self.entrypoint = entrypoint
        # The container image URL.
        self.image = image
        # The image registry type.
        self.image_registry_type = image_registry_type
        # Custom containers must expose a standard MCP endpoint. Set this parameter to SELF_HOSTED.
        self.mcp_runtime_mode = mcp_runtime_mode
        # Currently fixed to CONTAINER_IMAGE.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acr_instance_id is not None:
            result['acrInstanceId'] = self.acr_instance_id

        if self.command is not None:
            result['command'] = self.command

        if self.entrypoint is not None:
            result['entrypoint'] = self.entrypoint

        if self.image is not None:
            result['image'] = self.image

        if self.image_registry_type is not None:
            result['imageRegistryType'] = self.image_registry_type

        if self.mcp_runtime_mode is not None:
            result['mcpRuntimeMode'] = self.mcp_runtime_mode

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acrInstanceId') is not None:
            self.acr_instance_id = m.get('acrInstanceId')

        if m.get('command') is not None:
            self.command = m.get('command')

        if m.get('entrypoint') is not None:
            self.entrypoint = m.get('entrypoint')

        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('imageRegistryType') is not None:
            self.image_registry_type = m.get('imageRegistryType')

        if m.get('mcpRuntimeMode') is not None:
            self.mcp_runtime_mode = m.get('mcpRuntimeMode')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        return self

class InstallMcpMarketItemResponseBodyDataDeploymentConfigCodeConfiguration(DaraModel):
    def __init__(
        self,
        code_package_token: str = None,
        command: List[str] = None,
        language: str = None,
    ):
        # The temporary code package token returned by GetMcpCodePackageUploadUrl. After the presigned upload is complete, this token is used to create or update a code deployment.
        self.code_package_token = code_package_token
        # The full startup command, with arguments passed in sequence by parameter boundary. For example, when using supergateway to start a stdio MCP, pass in supergateway, --stdio, the full subcommand, and remaining arguments.
        self.command = command
        # The code package runtime: python3.13, nodejs22, or java17.
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_package_token is not None:
            result['codePackageToken'] = self.code_package_token

        if self.command is not None:
            result['command'] = self.command

        if self.language is not None:
            result['language'] = self.language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codePackageToken') is not None:
            self.code_package_token = m.get('codePackageToken')

        if m.get('command') is not None:
            self.command = m.get('command')

        if m.get('language') is not None:
            self.language = m.get('language')

        return self

class InstallMcpMarketItemResponseBodyDataDeploymentConfigAgentIdentityConfiguration(DaraModel):
    def __init__(
        self,
        authorization_enabled: bool = None,
        credential_provider_arn: str = None,
        credential_provider_type: str = None,
        enabled: bool = None,
    ):
        # Specifies whether authorization is enabled.
        self.authorization_enabled = authorization_enabled
        # The Alibaba Cloud Resource Name (ARN) of the credential provider.
        self.credential_provider_arn = credential_provider_arn
        # The credential provider type.
        self.credential_provider_type = credential_provider_type
        # Specifies whether Agent Identity is enabled.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_enabled is not None:
            result['authorizationEnabled'] = self.authorization_enabled

        if self.credential_provider_arn is not None:
            result['credentialProviderArn'] = self.credential_provider_arn

        if self.credential_provider_type is not None:
            result['credentialProviderType'] = self.credential_provider_type

        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorizationEnabled') is not None:
            self.authorization_enabled = m.get('authorizationEnabled')

        if m.get('credentialProviderArn') is not None:
            self.credential_provider_arn = m.get('credentialProviderArn')

        if m.get('credentialProviderType') is not None:
            self.credential_provider_type = m.get('credentialProviderType')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

class InstallMcpMarketItemResponseBodyDataDeploymentConfigAccessControl(DaraModel):
    def __init__(
        self,
        credential_id: str = None,
        enabled: bool = None,
        mode: str = None,
    ):
        # The AgentCore Credential referenced when mode is set to CREDENTIAL.
        self.credential_id = credential_id
        # Specifies whether to enable ingress access control.
        self.enabled = enabled
        # ANONYMOUS indicates anonymous access. CREDENTIAL indicates access using an AgentCore credential.
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_id is not None:
            result['credentialId'] = self.credential_id

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.mode is not None:
            result['mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialId') is not None:
            self.credential_id = m.get('credentialId')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        return self

