# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_openapiexplorer20241130 import models as main_models
from darabonba.model import DaraModel

class ListApiMcpServersResponseBody(DaraModel):
    def __init__(
        self,
        api_mcp_servers: List[main_models.ListApiMcpServersResponseBodyApiMcpServers] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_mcp_servers = api_mcp_servers
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_mcp_servers:
            for v1 in self.api_mcp_servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['apiMcpServers'] = []
        if self.api_mcp_servers is not None:
            for k1 in self.api_mcp_servers:
                result['apiMcpServers'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_mcp_servers = []
        if m.get('apiMcpServers') is not None:
            for k1 in m.get('apiMcpServers'):
                temp_model = main_models.ListApiMcpServersResponseBodyApiMcpServers()
                self.api_mcp_servers.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListApiMcpServersResponseBodyApiMcpServers(DaraModel):
    def __init__(
        self,
        additional_api_descriptions: List[main_models.ListApiMcpServersResponseBodyApiMcpServersAdditionalApiDescriptions] = None,
        apis: List[main_models.ListApiMcpServersResponseBodyApiMcpServersApis] = None,
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
        prompts: List[main_models.ListApiMcpServersResponseBodyApiMcpServersPrompts] = None,
        public_access: str = None,
        source_type: str = None,
        system_mcp_server_info: main_models.ListApiMcpServersResponseBodyApiMcpServersSystemMcpServerInfo = None,
        system_tools: List[str] = None,
        terraform_tools: List[main_models.ListApiMcpServersResponseBodyApiMcpServersTerraformTools] = None,
        update_time: str = None,
        urls: main_models.ListApiMcpServersResponseBodyApiMcpServersUrls = None,
        vpc_whitelists: List[str] = None,
    ):
        self.additional_api_descriptions = additional_api_descriptions
        self.apis = apis
        self.assume_role_extra_policy = assume_role_extra_policy
        self.assume_role_name = assume_role_name
        self.create_time = create_time
        self.description = description
        self.enable_assume_role = enable_assume_role
        self.enable_custom_vpc_whitelist = enable_custom_vpc_whitelist
        self.id = id
        self.instructions = instructions
        self.language = language
        self.name = name
        self.oauth_client_id = oauth_client_id
        self.prompts = prompts
        self.public_access = public_access
        self.source_type = source_type
        self.system_mcp_server_info = system_mcp_server_info
        self.system_tools = system_tools
        self.terraform_tools = terraform_tools
        self.update_time = update_time
        self.urls = urls
        self.vpc_whitelists = vpc_whitelists

    def validate(self):
        if self.additional_api_descriptions:
            for v1 in self.additional_api_descriptions:
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
                temp_model = main_models.ListApiMcpServersResponseBodyApiMcpServersAdditionalApiDescriptions()
                self.additional_api_descriptions.append(temp_model.from_map(k1))

        self.apis = []
        if m.get('apis') is not None:
            for k1 in m.get('apis'):
                temp_model = main_models.ListApiMcpServersResponseBodyApiMcpServersApis()
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
                temp_model = main_models.ListApiMcpServersResponseBodyApiMcpServersPrompts()
                self.prompts.append(temp_model.from_map(k1))

        if m.get('publicAccess') is not None:
            self.public_access = m.get('publicAccess')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('systemMcpServerInfo') is not None:
            temp_model = main_models.ListApiMcpServersResponseBodyApiMcpServersSystemMcpServerInfo()
            self.system_mcp_server_info = temp_model.from_map(m.get('systemMcpServerInfo'))

        if m.get('systemTools') is not None:
            self.system_tools = m.get('systemTools')

        self.terraform_tools = []
        if m.get('terraformTools') is not None:
            for k1 in m.get('terraformTools'):
                temp_model = main_models.ListApiMcpServersResponseBodyApiMcpServersTerraformTools()
                self.terraform_tools.append(temp_model.from_map(k1))

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('urls') is not None:
            temp_model = main_models.ListApiMcpServersResponseBodyApiMcpServersUrls()
            self.urls = temp_model.from_map(m.get('urls'))

        if m.get('vpcWhitelists') is not None:
            self.vpc_whitelists = m.get('vpcWhitelists')

        return self

class ListApiMcpServersResponseBodyApiMcpServersUrls(DaraModel):
    def __init__(
        self,
        mcp: str = None,
        sse: str = None,
        vpc_mcp: str = None,
        vpc_sse: str = None,
    ):
        self.mcp = mcp
        self.sse = sse
        self.vpc_mcp = vpc_mcp
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

class ListApiMcpServersResponseBodyApiMcpServersTerraformTools(DaraModel):
    def __init__(
        self,
        async_: bool = None,
        code: str = None,
        description: str = None,
        destroy_policy: str = None,
        name: str = None,
    ):
        self.async_ = async_
        self.code = code
        self.description = description
        self.destroy_policy = destroy_policy
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

class ListApiMcpServersResponseBodyApiMcpServersSystemMcpServerInfo(DaraModel):
    def __init__(
        self,
        name: str = None,
        product: str = None,
    ):
        self.name = name
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

class ListApiMcpServersResponseBodyApiMcpServersPrompts(DaraModel):
    def __init__(
        self,
        arguments: List[main_models.ListApiMcpServersResponseBodyApiMcpServersPromptsArguments] = None,
        content: str = None,
        description: str = None,
        name: str = None,
    ):
        self.arguments = arguments
        self.content = content
        self.description = description
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
                temp_model = main_models.ListApiMcpServersResponseBodyApiMcpServersPromptsArguments()
                self.arguments.append(temp_model.from_map(k1))

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ListApiMcpServersResponseBodyApiMcpServersPromptsArguments(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        required: bool = None,
    ):
        self.description = description
        self.name = name
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

class ListApiMcpServersResponseBodyApiMcpServersApis(DaraModel):
    def __init__(
        self,
        api_version: str = None,
        product: str = None,
        selectors: List[str] = None,
    ):
        self.api_version = api_version
        self.product = product
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

class ListApiMcpServersResponseBodyApiMcpServersAdditionalApiDescriptions(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        api_override_json: str = None,
        api_version: str = None,
        const_parameters: List[main_models.ListApiMcpServersResponseBodyApiMcpServersAdditionalApiDescriptionsConstParameters] = None,
        enable_output_schema: bool = None,
        execute_cli_command: bool = None,
        product: str = None,
    ):
        self.api_name = api_name
        self.api_override_json = api_override_json
        self.api_version = api_version
        self.const_parameters = const_parameters
        self.enable_output_schema = enable_output_schema
        self.execute_cli_command = execute_cli_command
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
                temp_model = main_models.ListApiMcpServersResponseBodyApiMcpServersAdditionalApiDescriptionsConstParameters()
                self.const_parameters.append(temp_model.from_map(k1))

        if m.get('enableOutputSchema') is not None:
            self.enable_output_schema = m.get('enableOutputSchema')

        if m.get('executeCliCommand') is not None:
            self.execute_cli_command = m.get('executeCliCommand')

        if m.get('product') is not None:
            self.product = m.get('product')

        return self

class ListApiMcpServersResponseBodyApiMcpServersAdditionalApiDescriptionsConstParameters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: Any = None,
    ):
        self.key = key
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

