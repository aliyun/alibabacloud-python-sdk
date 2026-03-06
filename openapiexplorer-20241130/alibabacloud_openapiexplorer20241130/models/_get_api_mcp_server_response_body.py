# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_openapiexplorer20241130 import models as main_models
from darabonba.model import DaraModel

class GetApiMcpServerResponseBody(DaraModel):
    def __init__(
        self,
        additional_api_descriptions: List[main_models.GetApiMcpServerResponseBodyAdditionalApiDescriptions] = None,
        api_infos: List[main_models.GetApiMcpServerResponseBodyApiInfos] = None,
        apis: List[main_models.GetApiMcpServerResponseBodyApis] = None,
        assume_role_extra_policy: str = None,
        assume_role_name: str = None,
        create_time: str = None,
        description: str = None,
        enable_assume_role: bool = None,
        enable_custom_vpc_whitelist: bool = None,
        id: str = None,
        instructions: str = None,
        language: str = None,
        name: str = None,
        oauth_client_id: str = None,
        prompts: List[main_models.GetApiMcpServerResponseBodyPrompts] = None,
        public_access: str = None,
        request_id: str = None,
        required_rampolicy: str = None,
        source_type: str = None,
        system_mcp_server_info: main_models.GetApiMcpServerResponseBodySystemMcpServerInfo = None,
        system_tools: List[str] = None,
        terraform_tools: List[main_models.GetApiMcpServerResponseBodyTerraformTools] = None,
        update_time: str = None,
        urls: main_models.GetApiMcpServerResponseBodyUrls = None,
        vpc_whitelists: List[str] = None,
    ):
        # A list of supplementary API descriptions.
        self.additional_api_descriptions = additional_api_descriptions
        # A list of API information for the API MCP service.
        self.api_infos = api_infos
        # A list of API information.
        self.apis = apis
        # The extra policy for role assumption when multi-account access is enabled. If this policy is specified, the permissions for the role assumption are based on this policy and overwrite the permissions that are defined for the role.
        self.assume_role_extra_policy = assume_role_extra_policy
        # The name of the RAM role of the destination account that is assumed when you perform cross-account operations with multi-account access enabled.
        self.assume_role_name = assume_role_name
        # The time when the API MCP server was created.
        self.create_time = create_time
        # The description of the API MCP server.
        self.description = description
        # Indicates whether to enable multi-account access.
        self.enable_assume_role = enable_assume_role
        # Indicates whether to enable a custom VPC whitelist. If this parameter is not enabled, the account-level configuration is used.
        self.enable_custom_vpc_whitelist = enable_custom_vpc_whitelist
        # The ID of the API MCP service.
        self.id = id
        # The MCP instruction. It prompts the large model on how to use the MCP. The client must support the Instructions field of the standard MCP protocol.
        self.instructions = instructions
        # The language of the API documentation for the API MCP service. You can select Chinese or English API documentation. The language of the prompt may affect the AI\\"s response.
        self.language = language
        # The name of the MCP server. The name must be 3 to 64 characters in length and can contain lowercase letters and digits. It must not start with a digit. The name must be unique within the same Alibaba Cloud account.
        self.name = name
        # The custom OAuth client ID when you select a custom OAuth configuration.
        # 
        # `Only web and native applications are supported. The OAuth scope must include /acs/mcp-server.`
        self.oauth_client_id = oauth_client_id
        # A list of prompt configurations.
        self.prompts = prompts
        # Indicates whether to enable public access.
        self.public_access = public_access
        # The request ID.
        self.request_id = request_id
        # The RAM access policy that is required by the API MCP service.
        self.required_rampolicy = required_rampolicy
        # The type of the API MCP service.
        # 
        # - custom: a custom service
        # 
        # - system: a system service
        self.source_type = source_type
        # A list of system MCP services.
        self.system_mcp_server_info = system_mcp_server_info
        # A list of system tools.
        self.system_tools = system_tools
        # A list of Terraform tools.
        self.terraform_tools = terraform_tools
        # The time when the API MCP server was last modified.
        self.update_time = update_time
        # The connection information for the MCP server.
        self.urls = urls
        # The VPC whitelist that specifies the allowed source VPCs after public access is disabled. If you do not set this parameter or leave it empty, access from all sources is allowed.
        self.vpc_whitelists = vpc_whitelists

    def validate(self):
        if self.additional_api_descriptions:
            for v1 in self.additional_api_descriptions:
                 if v1:
                    v1.validate()
        if self.api_infos:
            for v1 in self.api_infos:
                 if v1:
                    v1.validate()
        if self.apis:
            for v1 in self.apis:
                 if v1:
                    v1.validate()
        if self.prompts:
            for v1 in self.prompts:
                 if v1:
                    v1.validate()
        if self.system_mcp_server_info:
            self.system_mcp_server_info.validate()
        if self.terraform_tools:
            for v1 in self.terraform_tools:
                 if v1:
                    v1.validate()
        if self.urls:
            self.urls.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['additionalApiDescriptions'] = []
        if self.additional_api_descriptions is not None:
            for k1 in self.additional_api_descriptions:
                result['additionalApiDescriptions'].append(k1.to_map() if k1 else None)

        result['apiInfos'] = []
        if self.api_infos is not None:
            for k1 in self.api_infos:
                result['apiInfos'].append(k1.to_map() if k1 else None)

        result['apis'] = []
        if self.apis is not None:
            for k1 in self.apis:
                result['apis'].append(k1.to_map() if k1 else None)

        if self.assume_role_extra_policy is not None:
            result['assumeRoleExtraPolicy'] = self.assume_role_extra_policy

        if self.assume_role_name is not None:
            result['assumeRoleName'] = self.assume_role_name

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.enable_assume_role is not None:
            result['enableAssumeRole'] = self.enable_assume_role

        if self.enable_custom_vpc_whitelist is not None:
            result['enableCustomVpcWhitelist'] = self.enable_custom_vpc_whitelist

        if self.id is not None:
            result['id'] = self.id

        if self.instructions is not None:
            result['instructions'] = self.instructions

        if self.language is not None:
            result['language'] = self.language

        if self.name is not None:
            result['name'] = self.name

        if self.oauth_client_id is not None:
            result['oauthClientId'] = self.oauth_client_id

        result['prompts'] = []
        if self.prompts is not None:
            for k1 in self.prompts:
                result['prompts'].append(k1.to_map() if k1 else None)

        if self.public_access is not None:
            result['publicAccess'] = self.public_access

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.required_rampolicy is not None:
            result['requiredRAMPolicy'] = self.required_rampolicy

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.system_mcp_server_info is not None:
            result['systemMcpServerInfo'] = self.system_mcp_server_info.to_map()

        if self.system_tools is not None:
            result['systemTools'] = self.system_tools

        result['terraformTools'] = []
        if self.terraform_tools is not None:
            for k1 in self.terraform_tools:
                result['terraformTools'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.urls is not None:
            result['urls'] = self.urls.to_map()

        if self.vpc_whitelists is not None:
            result['vpcWhitelists'] = self.vpc_whitelists

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_api_descriptions = []
        if m.get('additionalApiDescriptions') is not None:
            for k1 in m.get('additionalApiDescriptions'):
                temp_model = main_models.GetApiMcpServerResponseBodyAdditionalApiDescriptions()
                self.additional_api_descriptions.append(temp_model.from_map(k1))

        self.api_infos = []
        if m.get('apiInfos') is not None:
            for k1 in m.get('apiInfos'):
                temp_model = main_models.GetApiMcpServerResponseBodyApiInfos()
                self.api_infos.append(temp_model.from_map(k1))

        self.apis = []
        if m.get('apis') is not None:
            for k1 in m.get('apis'):
                temp_model = main_models.GetApiMcpServerResponseBodyApis()
                self.apis.append(temp_model.from_map(k1))

        if m.get('assumeRoleExtraPolicy') is not None:
            self.assume_role_extra_policy = m.get('assumeRoleExtraPolicy')

        if m.get('assumeRoleName') is not None:
            self.assume_role_name = m.get('assumeRoleName')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enableAssumeRole') is not None:
            self.enable_assume_role = m.get('enableAssumeRole')

        if m.get('enableCustomVpcWhitelist') is not None:
            self.enable_custom_vpc_whitelist = m.get('enableCustomVpcWhitelist')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('instructions') is not None:
            self.instructions = m.get('instructions')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('oauthClientId') is not None:
            self.oauth_client_id = m.get('oauthClientId')

        self.prompts = []
        if m.get('prompts') is not None:
            for k1 in m.get('prompts'):
                temp_model = main_models.GetApiMcpServerResponseBodyPrompts()
                self.prompts.append(temp_model.from_map(k1))

        if m.get('publicAccess') is not None:
            self.public_access = m.get('publicAccess')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('requiredRAMPolicy') is not None:
            self.required_rampolicy = m.get('requiredRAMPolicy')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('systemMcpServerInfo') is not None:
            temp_model = main_models.GetApiMcpServerResponseBodySystemMcpServerInfo()
            self.system_mcp_server_info = temp_model.from_map(m.get('systemMcpServerInfo'))

        if m.get('systemTools') is not None:
            self.system_tools = m.get('systemTools')

        self.terraform_tools = []
        if m.get('terraformTools') is not None:
            for k1 in m.get('terraformTools'):
                temp_model = main_models.GetApiMcpServerResponseBodyTerraformTools()
                self.terraform_tools.append(temp_model.from_map(k1))

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('urls') is not None:
            temp_model = main_models.GetApiMcpServerResponseBodyUrls()
            self.urls = temp_model.from_map(m.get('urls'))

        if m.get('vpcWhitelists') is not None:
            self.vpc_whitelists = m.get('vpcWhitelists')

        return self

class GetApiMcpServerResponseBodyUrls(DaraModel):
    def __init__(
        self,
        mcp: str = None,
        sse: str = None,
        vpc_mcp: str = None,
        vpc_sse: str = None,
    ):
        # The connection information for the streamable HTTP protocol. This protocol is recommended.
        self.mcp = mcp
        # The connection information for the Server-Sent Events (SSE) protocol.
        self.sse = sse
        # The endpoint of the streamable HTTP protocol in a VPC.
        self.vpc_mcp = vpc_mcp
        # The endpoint of the SSE protocol in a VPC.
        self.vpc_sse = vpc_sse

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mcp is not None:
            result['mcp'] = self.mcp

        if self.sse is not None:
            result['sse'] = self.sse

        if self.vpc_mcp is not None:
            result['vpcMcp'] = self.vpc_mcp

        if self.vpc_sse is not None:
            result['vpcSse'] = self.vpc_sse

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mcp') is not None:
            self.mcp = m.get('mcp')

        if m.get('sse') is not None:
            self.sse = m.get('sse')

        if m.get('vpcMcp') is not None:
            self.vpc_mcp = m.get('vpcMcp')

        if m.get('vpcSse') is not None:
            self.vpc_sse = m.get('vpcSse')

        return self

class GetApiMcpServerResponseBodyTerraformTools(DaraModel):
    def __init__(
        self,
        async_: bool = None,
        code: str = None,
        description: str = None,
        destroy_policy: str = None,
        name: str = None,
    ):
        # Indicates whether to execute tasks asynchronously. If set to true, the system immediately starts the next task after the current task is initiated, without waiting for each resource operation to complete.
        self.async_ = async_
        # The code for the Terraform tool. For more information, see [HCL language overview](https://help.aliyun.com/zh/terraform/terraform-configuration-and-hcl-language-overview).
        self.code = code
        # The description of the Terraform tool.
        self.description = description
        # The destroy policy. After a task is complete, the system applies the following cleanup policy to temporary resources based on the task execution status.
        # 
        # - NEVER: All created resources are retained, regardless of whether the task succeeds or fails.
        # 
        # - ALWAYS: All related resources are immediately destroyed after the task is complete, regardless of whether the task succeeds or fails.
        # 
        # - ON_FAILURE: Related resources are deleted only if the task fails. If the task succeeds, the resources are retained.
        self.destroy_policy = destroy_policy
        # The name of the Terraform tool.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_ is not None:
            result['async'] = self.async_

        if self.code is not None:
            result['code'] = self.code

        if self.description is not None:
            result['description'] = self.description

        if self.destroy_policy is not None:
            result['destroyPolicy'] = self.destroy_policy

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async') is not None:
            self.async_ = m.get('async')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('destroyPolicy') is not None:
            self.destroy_policy = m.get('destroyPolicy')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class GetApiMcpServerResponseBodySystemMcpServerInfo(DaraModel):
    def __init__(
        self,
        name: str = None,
        product: str = None,
    ):
        # The name of the system MCP service.
        self.name = name
        # The product code.
        # 
        # - Call the GetRequestLog operation to obtain the product code from the response.
        # 
        # <props="intl">
        # 
        # - Find the corresponding product code from the URL of the OpenAPI Portal. For example, the URL of the OpenAPI Portal for Short Message Service is https\\://api.alibabacloud.com/product/Dysmsapi. The product code for Short Message Service is Dysmsapi.
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.product is not None:
            result['product'] = self.product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('product') is not None:
            self.product = m.get('product')

        return self

class GetApiMcpServerResponseBodyPrompts(DaraModel):
    def __init__(
        self,
        arguments: List[main_models.GetApiMcpServerResponseBodyPromptsArguments] = None,
        content: str = None,
        description: str = None,
        name: str = None,
    ):
        # A list of parameters that the prompt supports.
        self.arguments = arguments
        # The content of the prompt. Variables are specified in the {{xxx}} format. The xxx variable must be defined in the arguments parameter.
        self.content = content
        # The description.
        self.description = description
        # The prompt name.
        self.name = name

    def validate(self):
        if self.arguments:
            for v1 in self.arguments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['arguments'] = []
        if self.arguments is not None:
            for k1 in self.arguments:
                result['arguments'].append(k1.to_map() if k1 else None)

        if self.content is not None:
            result['content'] = self.content

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.arguments = []
        if m.get('arguments') is not None:
            for k1 in m.get('arguments'):
                temp_model = main_models.GetApiMcpServerResponseBodyPromptsArguments()
                self.arguments.append(temp_model.from_map(k1))

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class GetApiMcpServerResponseBodyPromptsArguments(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        required: bool = None,
    ):
        # The description of the parameter.
        self.description = description
        # The parameter name.
        self.name = name
        # Indicates whether this parameter is required.
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.required is not None:
            result['required'] = self.required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('required') is not None:
            self.required = m.get('required')

        return self

class GetApiMcpServerResponseBodyApis(DaraModel):
    def __init__(
        self,
        api_version: str = None,
        product: str = None,
        selectors: List[str] = None,
    ):
        # The POP version of the API that is exposed to the MCP server.
        self.api_version = api_version
        # The product code.
        # 
        # - Call the GetRequestLog operation to obtain the product code from the response.
        # 
        # <props="intl">
        # 
        # - Find the corresponding product code from the URL of the OpenAPI Portal. For example, the URL of the OpenAPI Portal for Short Message Service is https\\://api.alibabacloud.com/product/Dysmsapi. The product code for Short Message Service is Dysmsapi.
        self.product = product
        # A list of API name matching rules.
        self.selectors = selectors

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_version is not None:
            result['apiVersion'] = self.api_version

        if self.product is not None:
            result['product'] = self.product

        if self.selectors is not None:
            result['selectors'] = self.selectors

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')

        if m.get('product') is not None:
            self.product = m.get('product')

        if m.get('selectors') is not None:
            self.selectors = m.get('selectors')

        return self

class GetApiMcpServerResponseBodyApiInfos(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        api_version: str = None,
        product: str = None,
    ):
        # The API name.
        self.api_name = api_name
        # The POP version of the API that is exposed to the MCP server.
        self.api_version = api_version
        # The product code.
        # 
        # - Call the GetRequestLog operation to obtain the product code from the response.
        # 
        # <props="intl">
        # 
        # - Find the corresponding product code from the URL of the OpenAPI Portal. For example, the URL of the OpenAPI Portal for Short Message Service is https\\://api.alibabacloud.com/product/Dysmsapi. The product code for Short Message Service is Dysmsapi.
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['apiName'] = self.api_name

        if self.api_version is not None:
            result['apiVersion'] = self.api_version

        if self.product is not None:
            result['product'] = self.product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')

        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')

        if m.get('product') is not None:
            self.product = m.get('product')

        return self

class GetApiMcpServerResponseBodyAdditionalApiDescriptions(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        api_override_json: str = None,
        api_version: str = None,
        const_parameters: List[main_models.GetApiMcpServerResponseBodyAdditionalApiDescriptionsConstParameters] = None,
        enable_output_schema: bool = None,
        execute_cli_command: bool = None,
        product: str = None,
    ):
        # The API name.
        self.api_name = api_name
        # The API metadata in JSON format. For an example of the format, see https\\://api.aliyun.com/meta/v1/products/Ecs/versions/2014-05-26/apis/DescribeInstances/api.json. You can overwrite the summary and parameters fields.
        self.api_override_json = api_override_json
        # The POP version of the API that is exposed to the MCP server.
        self.api_version = api_version
        # A list of constant input parameters. These parameters are not included in the output during API parameter parsing.
        self.const_parameters = const_parameters
        # Indicates whether to return the schema of the response parameters. Returning the schema increases the size of the entire API MCP server. The default value is null, which means the schema is not returned.
        self.enable_output_schema = enable_output_schema
        # Indicates whether to return the command-line interface (CLI) command. In this mode, the API is not called. Instead, the corresponding CLI command is returned. This is suitable for long-running tasks that need to be executed using Alibaba Cloud CLI.
        self.execute_cli_command = execute_cli_command
        # The product code.
        # 
        # - Call the GetRequestLog operation to obtain the product code from the response.
        # 
        # <props="intl">
        # 
        # - Find the corresponding product code from the URL of the OpenAPI Portal. For example, the URL of the OpenAPI Portal for Short Message Service is https\\://api.alibabacloud.com/product/Dysmsapi. The product code for Short Message Service is Dysmsapi.
        self.product = product

    def validate(self):
        if self.const_parameters:
            for v1 in self.const_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['apiName'] = self.api_name

        if self.api_override_json is not None:
            result['apiOverrideJson'] = self.api_override_json

        if self.api_version is not None:
            result['apiVersion'] = self.api_version

        result['constParameters'] = []
        if self.const_parameters is not None:
            for k1 in self.const_parameters:
                result['constParameters'].append(k1.to_map() if k1 else None)

        if self.enable_output_schema is not None:
            result['enableOutputSchema'] = self.enable_output_schema

        if self.execute_cli_command is not None:
            result['executeCliCommand'] = self.execute_cli_command

        if self.product is not None:
            result['product'] = self.product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')

        if m.get('apiOverrideJson') is not None:
            self.api_override_json = m.get('apiOverrideJson')

        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')

        self.const_parameters = []
        if m.get('constParameters') is not None:
            for k1 in m.get('constParameters'):
                temp_model = main_models.GetApiMcpServerResponseBodyAdditionalApiDescriptionsConstParameters()
                self.const_parameters.append(temp_model.from_map(k1))

        if m.get('enableOutputSchema') is not None:
            self.enable_output_schema = m.get('enableOutputSchema')

        if m.get('executeCliCommand') is not None:
            self.execute_cli_command = m.get('executeCliCommand')

        if m.get('product') is not None:
            self.product = m.get('product')

        return self

class GetApiMcpServerResponseBodyAdditionalApiDescriptionsConstParameters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: Any = None,
    ):
        # The parameter name. Only first-level parameter names are supported. For ROA-style APIs, you can set parameters such as body.xx. You cannot set values that exceed the top-level parameters.
        self.key = key
        # The value of the parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

