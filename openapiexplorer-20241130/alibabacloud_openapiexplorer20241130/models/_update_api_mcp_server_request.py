# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_openapiexplorer20241130 import models as main_models
from darabonba.model import DaraModel

class UpdateApiMcpServerRequest(DaraModel):
    def __init__(
        self,
        additional_api_descriptions: List[main_models.UpdateApiMcpServerRequestAdditionalApiDescriptions] = None,
        apis: List[main_models.UpdateApiMcpServerRequestApis] = None,
        assume_role_extra_policy: str = None,
        assume_role_name: str = None,
        description: str = None,
        enable_assume_role: bool = None,
        enable_custom_vpc_whitelist: bool = None,
        instructions: str = None,
        language: str = None,
        oauth_client_id: str = None,
        prompts: List[main_models.UpdateApiMcpServerRequestPrompts] = None,
        public_access: str = None,
        system_tools: List[str] = None,
        terraform_tools: List[main_models.UpdateApiMcpServerRequestTerraformTools] = None,
        vpc_whitelists: List[str] = None,
        client_token: str = None,
        id: str = None,
    ):
        self.additional_api_descriptions = additional_api_descriptions
        self.apis = apis
        self.assume_role_extra_policy = assume_role_extra_policy
        self.assume_role_name = assume_role_name
        self.description = description
        self.enable_assume_role = enable_assume_role
        self.enable_custom_vpc_whitelist = enable_custom_vpc_whitelist
        self.instructions = instructions
        self.language = language
        self.oauth_client_id = oauth_client_id
        self.prompts = prompts
        self.public_access = public_access
        self.system_tools = system_tools
        self.terraform_tools = terraform_tools
        self.vpc_whitelists = vpc_whitelists
        self.client_token = client_token
        # This parameter is required.
        self.id = id

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
        if self.terraform_tools:
            for v1 in self.terraform_tools:
                 if v1:
                    v1.validate()

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

        if self.description is not None:
            result['description'] = self.description

        if self.enable_assume_role is not None:
            result['enableAssumeRole'] = self.enable_assume_role

        if self.enable_custom_vpc_whitelist is not None:
            result['enableCustomVpcWhitelist'] = self.enable_custom_vpc_whitelist

        if self.instructions is not None:
            result['instructions'] = self.instructions

        if self.language is not None:
            result['language'] = self.language

        if self.oauth_client_id is not None:
            result['oauthClientId'] = self.oauth_client_id

        result['prompts'] = []
        if self.prompts is not None:
            for k1 in self.prompts:
                result['prompts'].append(k1.to_map() if k1 else None)

        if self.public_access is not None:
            result['publicAccess'] = self.public_access

        if self.system_tools is not None:
            result['systemTools'] = self.system_tools

        result['terraformTools'] = []
        if self.terraform_tools is not None:
            for k1 in self.terraform_tools:
                result['terraformTools'].append(k1.to_map() if k1 else None)

        if self.vpc_whitelists is not None:
            result['vpcWhitelists'] = self.vpc_whitelists

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.id is not None:
            result['id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_api_descriptions = []
        if m.get('additionalApiDescriptions') is not None:
            for k1 in m.get('additionalApiDescriptions'):
                temp_model = main_models.UpdateApiMcpServerRequestAdditionalApiDescriptions()
                self.additional_api_descriptions.append(temp_model.from_map(k1))

        self.apis = []
        if m.get('apis') is not None:
            for k1 in m.get('apis'):
                temp_model = main_models.UpdateApiMcpServerRequestApis()
                self.apis.append(temp_model.from_map(k1))

        if m.get('assumeRoleExtraPolicy') is not None:
            self.assume_role_extra_policy = m.get('assumeRoleExtraPolicy')

        if m.get('assumeRoleName') is not None:
            self.assume_role_name = m.get('assumeRoleName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enableAssumeRole') is not None:
            self.enable_assume_role = m.get('enableAssumeRole')

        if m.get('enableCustomVpcWhitelist') is not None:
            self.enable_custom_vpc_whitelist = m.get('enableCustomVpcWhitelist')

        if m.get('instructions') is not None:
            self.instructions = m.get('instructions')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('oauthClientId') is not None:
            self.oauth_client_id = m.get('oauthClientId')

        self.prompts = []
        if m.get('prompts') is not None:
            for k1 in m.get('prompts'):
                temp_model = main_models.UpdateApiMcpServerRequestPrompts()
                self.prompts.append(temp_model.from_map(k1))

        if m.get('publicAccess') is not None:
            self.public_access = m.get('publicAccess')

        if m.get('systemTools') is not None:
            self.system_tools = m.get('systemTools')

        self.terraform_tools = []
        if m.get('terraformTools') is not None:
            for k1 in m.get('terraformTools'):
                temp_model = main_models.UpdateApiMcpServerRequestTerraformTools()
                self.terraform_tools.append(temp_model.from_map(k1))

        if m.get('vpcWhitelists') is not None:
            self.vpc_whitelists = m.get('vpcWhitelists')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('id') is not None:
            self.id = m.get('id')

        return self

class UpdateApiMcpServerRequestTerraformTools(DaraModel):
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

class UpdateApiMcpServerRequestPrompts(DaraModel):
    def __init__(
        self,
        arguments: List[main_models.UpdateApiMcpServerRequestPromptsArguments] = None,
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
                temp_model = main_models.UpdateApiMcpServerRequestPromptsArguments()
                self.arguments.append(temp_model.from_map(k1))

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class UpdateApiMcpServerRequestPromptsArguments(DaraModel):
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

class UpdateApiMcpServerRequestApis(DaraModel):
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

class UpdateApiMcpServerRequestAdditionalApiDescriptions(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        api_override_json: str = None,
        api_version: str = None,
        const_parameters: List[main_models.UpdateApiMcpServerRequestAdditionalApiDescriptionsConstParameters] = None,
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
                temp_model = main_models.UpdateApiMcpServerRequestAdditionalApiDescriptionsConstParameters()
                self.const_parameters.append(temp_model.from_map(k1))

        if m.get('enableOutputSchema') is not None:
            self.enable_output_schema = m.get('enableOutputSchema')

        if m.get('executeCliCommand') is not None:
            self.execute_cli_command = m.get('executeCliCommand')

        if m.get('product') is not None:
            self.product = m.get('product')

        return self

class UpdateApiMcpServerRequestAdditionalApiDescriptionsConstParameters(DaraModel):
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

