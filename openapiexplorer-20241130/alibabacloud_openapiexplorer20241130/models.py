# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Any, List, Dict


class ApiMcpServerValidateHclRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
    ):
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class ApiMcpServerValidateHclResponseBody(TeaModel):
    def __init__(
        self,
        diagnostic_report: Any = None,
        errors: List[str] = None,
        hash: str = None,
        is_valid: bool = None,
        parameters: List[Any] = None,
        request_id: str = None,
        warnings: List[str] = None,
    ):
        self.diagnostic_report = diagnostic_report
        self.errors = errors
        self.hash = hash
        self.is_valid = is_valid
        self.parameters = parameters
        self.request_id = request_id
        self.warnings = warnings

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diagnostic_report is not None:
            result['diagnosticReport'] = self.diagnostic_report
        if self.errors is not None:
            result['errors'] = self.errors
        if self.hash is not None:
            result['hash'] = self.hash
        if self.is_valid is not None:
            result['isValid'] = self.is_valid
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.warnings is not None:
            result['warnings'] = self.warnings
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diagnosticReport') is not None:
            self.diagnostic_report = m.get('diagnosticReport')
        if m.get('errors') is not None:
            self.errors = m.get('errors')
        if m.get('hash') is not None:
            self.hash = m.get('hash')
        if m.get('isValid') is not None:
            self.is_valid = m.get('isValid')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('warnings') is not None:
            self.warnings = m.get('warnings')
        return self


class ApiMcpServerValidateHclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApiMcpServerValidateHclResponseBody = None,
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
            temp_model = ApiMcpServerValidateHclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApiMcpServerRequestAdditionalApiDescriptionsConstParameters(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateApiMcpServerRequestAdditionalApiDescriptions(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        api_override_json: str = None,
        api_version: str = None,
        const_parameters: List[CreateApiMcpServerRequestAdditionalApiDescriptionsConstParameters] = None,
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
            for k in self.const_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.api_override_json is not None:
            result['apiOverrideJson'] = self.api_override_json
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        result['constParameters'] = []
        if self.const_parameters is not None:
            for k in self.const_parameters:
                result['constParameters'].append(k.to_map() if k else None)
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
            for k in m.get('constParameters'):
                temp_model = CreateApiMcpServerRequestAdditionalApiDescriptionsConstParameters()
                self.const_parameters.append(temp_model.from_map(k))
        if m.get('enableOutputSchema') is not None:
            self.enable_output_schema = m.get('enableOutputSchema')
        if m.get('executeCliCommand') is not None:
            self.execute_cli_command = m.get('executeCliCommand')
        if m.get('product') is not None:
            self.product = m.get('product')
        return self


class CreateApiMcpServerRequestApis(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        product: str = None,
        selectors: List[str] = None,
    ):
        # This parameter is required.
        self.api_version = api_version
        # This parameter is required.
        self.product = product
        # This parameter is required.
        self.selectors = selectors

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateApiMcpServerRequestPromptsArguments(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateApiMcpServerRequestPrompts(TeaModel):
    def __init__(
        self,
        arguments: List[CreateApiMcpServerRequestPromptsArguments] = None,
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
            for k in self.arguments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['arguments'] = []
        if self.arguments is not None:
            for k in self.arguments:
                result['arguments'].append(k.to_map() if k else None)
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
            for k in m.get('arguments'):
                temp_model = CreateApiMcpServerRequestPromptsArguments()
                self.arguments.append(temp_model.from_map(k))
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateApiMcpServerRequestTerraformTools(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateApiMcpServerRequest(TeaModel):
    def __init__(
        self,
        additional_api_descriptions: List[CreateApiMcpServerRequestAdditionalApiDescriptions] = None,
        apis: List[CreateApiMcpServerRequestApis] = None,
        assume_role_extra_policy: str = None,
        assume_role_name: str = None,
        client_token: str = None,
        description: str = None,
        enable_assume_role: bool = None,
        enable_custom_vpc_whitelist: bool = None,
        instructions: str = None,
        language: str = None,
        name: str = None,
        oauth_client_id: str = None,
        prompts: List[CreateApiMcpServerRequestPrompts] = None,
        public_access: str = None,
        system_tools: List[str] = None,
        terraform_tools: List[CreateApiMcpServerRequestTerraformTools] = None,
        vpc_whitelists: List[str] = None,
    ):
        self.additional_api_descriptions = additional_api_descriptions
        # This parameter is required.
        self.apis = apis
        self.assume_role_extra_policy = assume_role_extra_policy
        self.assume_role_name = assume_role_name
        self.client_token = client_token
        self.description = description
        self.enable_assume_role = enable_assume_role
        self.enable_custom_vpc_whitelist = enable_custom_vpc_whitelist
        self.instructions = instructions
        self.language = language
        # This parameter is required.
        self.name = name
        self.oauth_client_id = oauth_client_id
        self.prompts = prompts
        self.public_access = public_access
        self.system_tools = system_tools
        self.terraform_tools = terraform_tools
        self.vpc_whitelists = vpc_whitelists

    def validate(self):
        if self.additional_api_descriptions:
            for k in self.additional_api_descriptions:
                if k:
                    k.validate()
        if self.apis:
            for k in self.apis:
                if k:
                    k.validate()
        if self.prompts:
            for k in self.prompts:
                if k:
                    k.validate()
        if self.terraform_tools:
            for k in self.terraform_tools:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['additionalApiDescriptions'] = []
        if self.additional_api_descriptions is not None:
            for k in self.additional_api_descriptions:
                result['additionalApiDescriptions'].append(k.to_map() if k else None)
        result['apis'] = []
        if self.apis is not None:
            for k in self.apis:
                result['apis'].append(k.to_map() if k else None)
        if self.assume_role_extra_policy is not None:
            result['assumeRoleExtraPolicy'] = self.assume_role_extra_policy
        if self.assume_role_name is not None:
            result['assumeRoleName'] = self.assume_role_name
        if self.client_token is not None:
            result['clientToken'] = self.client_token
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
        if self.name is not None:
            result['name'] = self.name
        if self.oauth_client_id is not None:
            result['oauthClientId'] = self.oauth_client_id
        result['prompts'] = []
        if self.prompts is not None:
            for k in self.prompts:
                result['prompts'].append(k.to_map() if k else None)
        if self.public_access is not None:
            result['publicAccess'] = self.public_access
        if self.system_tools is not None:
            result['systemTools'] = self.system_tools
        result['terraformTools'] = []
        if self.terraform_tools is not None:
            for k in self.terraform_tools:
                result['terraformTools'].append(k.to_map() if k else None)
        if self.vpc_whitelists is not None:
            result['vpcWhitelists'] = self.vpc_whitelists
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_api_descriptions = []
        if m.get('additionalApiDescriptions') is not None:
            for k in m.get('additionalApiDescriptions'):
                temp_model = CreateApiMcpServerRequestAdditionalApiDescriptions()
                self.additional_api_descriptions.append(temp_model.from_map(k))
        self.apis = []
        if m.get('apis') is not None:
            for k in m.get('apis'):
                temp_model = CreateApiMcpServerRequestApis()
                self.apis.append(temp_model.from_map(k))
        if m.get('assumeRoleExtraPolicy') is not None:
            self.assume_role_extra_policy = m.get('assumeRoleExtraPolicy')
        if m.get('assumeRoleName') is not None:
            self.assume_role_name = m.get('assumeRoleName')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
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
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('oauthClientId') is not None:
            self.oauth_client_id = m.get('oauthClientId')
        self.prompts = []
        if m.get('prompts') is not None:
            for k in m.get('prompts'):
                temp_model = CreateApiMcpServerRequestPrompts()
                self.prompts.append(temp_model.from_map(k))
        if m.get('publicAccess') is not None:
            self.public_access = m.get('publicAccess')
        if m.get('systemTools') is not None:
            self.system_tools = m.get('systemTools')
        self.terraform_tools = []
        if m.get('terraformTools') is not None:
            for k in m.get('terraformTools'):
                temp_model = CreateApiMcpServerRequestTerraformTools()
                self.terraform_tools.append(temp_model.from_map(k))
        if m.get('vpcWhitelists') is not None:
            self.vpc_whitelists = m.get('vpcWhitelists')
        return self


class CreateApiMcpServerResponseBodyUrls(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateApiMcpServerResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
        urls: CreateApiMcpServerResponseBodyUrls = None,
    ):
        self.id = id
        self.request_id = request_id
        self.urls = urls

    def validate(self):
        if self.urls:
            self.urls.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.urls is not None:
            result['urls'] = self.urls.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('urls') is not None:
            temp_model = CreateApiMcpServerResponseBodyUrls()
            self.urls = temp_model.from_map(m['urls'])
        return self


class CreateApiMcpServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateApiMcpServerResponseBody = None,
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
            temp_model = CreateApiMcpServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApiMcpServerRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        id: str = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class DeleteApiMcpServerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteApiMcpServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApiMcpServerResponseBody = None,
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
            temp_model = DeleteApiMcpServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateCLICommandRequest(TeaModel):
    def __init__(
        self,
        api: str = None,
        api_params: Dict[str, Any] = None,
        api_version: str = None,
        json_api_params: str = None,
        product: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.api = api
        self.api_params = api_params
        # This parameter is required.
        self.api_version = api_version
        self.json_api_params = json_api_params
        # This parameter is required.
        self.product = product
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api is not None:
            result['api'] = self.api
        if self.api_params is not None:
            result['apiParams'] = self.api_params
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.json_api_params is not None:
            result['jsonApiParams'] = self.json_api_params
        if self.product is not None:
            result['product'] = self.product
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('api') is not None:
            self.api = m.get('api')
        if m.get('apiParams') is not None:
            self.api_params = m.get('apiParams')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('jsonApiParams') is not None:
            self.json_api_params = m.get('jsonApiParams')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class GenerateCLICommandShrinkRequest(TeaModel):
    def __init__(
        self,
        api: str = None,
        api_params_shrink: str = None,
        api_version: str = None,
        json_api_params: str = None,
        product: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.api = api
        self.api_params_shrink = api_params_shrink
        # This parameter is required.
        self.api_version = api_version
        self.json_api_params = json_api_params
        # This parameter is required.
        self.product = product
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api is not None:
            result['api'] = self.api
        if self.api_params_shrink is not None:
            result['apiParams'] = self.api_params_shrink
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.json_api_params is not None:
            result['jsonApiParams'] = self.json_api_params
        if self.product is not None:
            result['product'] = self.product
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('api') is not None:
            self.api = m.get('api')
        if m.get('apiParams') is not None:
            self.api_params_shrink = m.get('apiParams')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('jsonApiParams') is not None:
            self.json_api_params = m.get('jsonApiParams')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class GenerateCLICommandResponseBody(TeaModel):
    def __init__(
        self,
        cli: str = None,
    ):
        self.cli = cli

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cli is not None:
            result['cli'] = self.cli
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cli') is not None:
            self.cli = m.get('cli')
        return self


class GenerateCLICommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateCLICommandResponseBody = None,
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
            temp_model = GenerateCLICommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApiDefinitionRequest(TeaModel):
    def __init__(
        self,
        api: str = None,
        api_version: str = None,
        product: str = None,
    ):
        # This parameter is required.
        self.api = api
        # This parameter is required.
        self.api_version = api_version
        # This parameter is required.
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api is not None:
            result['api'] = self.api
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.product is not None:
            result['product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('api') is not None:
            self.api = m.get('api')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('product') is not None:
            self.product = m.get('product')
        return self


class GetApiDefinitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: dict = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        pass

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
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GetApiMcpServerRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class GetApiMcpServerResponseBodyAdditionalApiDescriptionsConstParameters(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetApiMcpServerResponseBodyAdditionalApiDescriptions(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        api_override_json: str = None,
        api_version: str = None,
        const_parameters: List[GetApiMcpServerResponseBodyAdditionalApiDescriptionsConstParameters] = None,
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
            for k in self.const_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.api_override_json is not None:
            result['apiOverrideJson'] = self.api_override_json
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        result['constParameters'] = []
        if self.const_parameters is not None:
            for k in self.const_parameters:
                result['constParameters'].append(k.to_map() if k else None)
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
            for k in m.get('constParameters'):
                temp_model = GetApiMcpServerResponseBodyAdditionalApiDescriptionsConstParameters()
                self.const_parameters.append(temp_model.from_map(k))
        if m.get('enableOutputSchema') is not None:
            self.enable_output_schema = m.get('enableOutputSchema')
        if m.get('executeCliCommand') is not None:
            self.execute_cli_command = m.get('executeCliCommand')
        if m.get('product') is not None:
            self.product = m.get('product')
        return self


class GetApiMcpServerResponseBodyApiInfos(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        api_version: str = None,
        product: str = None,
    ):
        self.api_name = api_name
        self.api_version = api_version
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetApiMcpServerResponseBodyApis(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetApiMcpServerResponseBodyPromptsArguments(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetApiMcpServerResponseBodyPrompts(TeaModel):
    def __init__(
        self,
        arguments: List[GetApiMcpServerResponseBodyPromptsArguments] = None,
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
            for k in self.arguments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['arguments'] = []
        if self.arguments is not None:
            for k in self.arguments:
                result['arguments'].append(k.to_map() if k else None)
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
            for k in m.get('arguments'):
                temp_model = GetApiMcpServerResponseBodyPromptsArguments()
                self.arguments.append(temp_model.from_map(k))
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetApiMcpServerResponseBodySystemMcpServerInfo(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetApiMcpServerResponseBodyTerraformTools(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetApiMcpServerResponseBodyUrls(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetApiMcpServerResponseBody(TeaModel):
    def __init__(
        self,
        additional_api_descriptions: List[GetApiMcpServerResponseBodyAdditionalApiDescriptions] = None,
        api_infos: List[GetApiMcpServerResponseBodyApiInfos] = None,
        apis: List[GetApiMcpServerResponseBodyApis] = None,
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
        prompts: List[GetApiMcpServerResponseBodyPrompts] = None,
        public_access: str = None,
        request_id: str = None,
        required_rampolicy: str = None,
        source_type: str = None,
        system_mcp_server_info: GetApiMcpServerResponseBodySystemMcpServerInfo = None,
        system_tools: List[str] = None,
        terraform_tools: List[GetApiMcpServerResponseBodyTerraformTools] = None,
        update_time: str = None,
        urls: GetApiMcpServerResponseBodyUrls = None,
        vpc_whitelists: List[str] = None,
    ):
        self.additional_api_descriptions = additional_api_descriptions
        self.api_infos = api_infos
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
        self.request_id = request_id
        self.required_rampolicy = required_rampolicy
        self.source_type = source_type
        self.system_mcp_server_info = system_mcp_server_info
        self.system_tools = system_tools
        self.terraform_tools = terraform_tools
        self.update_time = update_time
        self.urls = urls
        self.vpc_whitelists = vpc_whitelists

    def validate(self):
        if self.additional_api_descriptions:
            for k in self.additional_api_descriptions:
                if k:
                    k.validate()
        if self.api_infos:
            for k in self.api_infos:
                if k:
                    k.validate()
        if self.apis:
            for k in self.apis:
                if k:
                    k.validate()
        if self.prompts:
            for k in self.prompts:
                if k:
                    k.validate()
        if self.system_mcp_server_info:
            self.system_mcp_server_info.validate()
        if self.terraform_tools:
            for k in self.terraform_tools:
                if k:
                    k.validate()
        if self.urls:
            self.urls.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['additionalApiDescriptions'] = []
        if self.additional_api_descriptions is not None:
            for k in self.additional_api_descriptions:
                result['additionalApiDescriptions'].append(k.to_map() if k else None)
        result['apiInfos'] = []
        if self.api_infos is not None:
            for k in self.api_infos:
                result['apiInfos'].append(k.to_map() if k else None)
        result['apis'] = []
        if self.apis is not None:
            for k in self.apis:
                result['apis'].append(k.to_map() if k else None)
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
            for k in self.prompts:
                result['prompts'].append(k.to_map() if k else None)
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
            for k in self.terraform_tools:
                result['terraformTools'].append(k.to_map() if k else None)
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
            for k in m.get('additionalApiDescriptions'):
                temp_model = GetApiMcpServerResponseBodyAdditionalApiDescriptions()
                self.additional_api_descriptions.append(temp_model.from_map(k))
        self.api_infos = []
        if m.get('apiInfos') is not None:
            for k in m.get('apiInfos'):
                temp_model = GetApiMcpServerResponseBodyApiInfos()
                self.api_infos.append(temp_model.from_map(k))
        self.apis = []
        if m.get('apis') is not None:
            for k in m.get('apis'):
                temp_model = GetApiMcpServerResponseBodyApis()
                self.apis.append(temp_model.from_map(k))
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
            for k in m.get('prompts'):
                temp_model = GetApiMcpServerResponseBodyPrompts()
                self.prompts.append(temp_model.from_map(k))
        if m.get('publicAccess') is not None:
            self.public_access = m.get('publicAccess')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('requiredRAMPolicy') is not None:
            self.required_rampolicy = m.get('requiredRAMPolicy')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('systemMcpServerInfo') is not None:
            temp_model = GetApiMcpServerResponseBodySystemMcpServerInfo()
            self.system_mcp_server_info = temp_model.from_map(m['systemMcpServerInfo'])
        if m.get('systemTools') is not None:
            self.system_tools = m.get('systemTools')
        self.terraform_tools = []
        if m.get('terraformTools') is not None:
            for k in m.get('terraformTools'):
                temp_model = GetApiMcpServerResponseBodyTerraformTools()
                self.terraform_tools.append(temp_model.from_map(k))
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('urls') is not None:
            temp_model = GetApiMcpServerResponseBodyUrls()
            self.urls = temp_model.from_map(m['urls'])
        if m.get('vpcWhitelists') is not None:
            self.vpc_whitelists = m.get('vpcWhitelists')
        return self


class GetApiMcpServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApiMcpServerResponseBody = None,
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
            temp_model = GetApiMcpServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApiMcpServerUserConfigResponseBody(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        enable_public_access: bool = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        request_id: str = None,
        vpc_whitelists: List[str] = None,
    ):
        self.account_id = account_id
        self.enable_public_access = enable_public_access
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.request_id = request_id
        self.vpc_whitelists = vpc_whitelists

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.enable_public_access is not None:
            result['enablePublicAccess'] = self.enable_public_access
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.vpc_whitelists is not None:
            result['vpcWhitelists'] = self.vpc_whitelists
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('enablePublicAccess') is not None:
            self.enable_public_access = m.get('enablePublicAccess')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('vpcWhitelists') is not None:
            self.vpc_whitelists = m.get('vpcWhitelists')
        return self


class GetApiMcpServerUserConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApiMcpServerUserConfigResponseBody = None,
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
            temp_model = GetApiMcpServerUserConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetErrorCodeSolutionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        error_code: str = None,
        error_message: str = None,
        product: str = None,
    ):
        # The language of the solution. Valid values: zh-CN and en-US. Not all of the solutions are available in English. If you set this parameter to en-US, but the corresponding solution is actually not available in English, no response is returned.
        self.accept_language = accept_language
        # The error code based on which you want to query a solution.
        # 
        # This parameter is required.
        self.error_code = error_code
        # The error message for which you want to query a solution. This parameter must be configured together with the errorCode parameter.
        self.error_message = error_message
        # The product code. You can use one of the following methods to query a product code:
        # 
        # *   Call the GetRequestLog operation to query a product code from the response.
        # *   Query the code of a product in the OpenAPI Explorer URL of the product. For example, the OpenAPI Explorer URL of Short Message Service (SMS) is https://api.alibabacloud.com/product/Dysmsapi. Therefore, the product code of SMS is Dysmsapi.
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['acceptLanguage'] = self.accept_language
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.product is not None:
            result['product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptLanguage') is not None:
            self.accept_language = m.get('acceptLanguage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('product') is not None:
            self.product = m.get('product')
        return self


class GetErrorCodeSolutionsResponseBodySolutions(TeaModel):
    def __init__(
        self,
        content: str = None,
        error_code: str = None,
        error_message: str = None,
        product: str = None,
        product_name: str = None,
        solution_id: str = None,
    ):
        # The content of the solution, which is in the markdown format.
        self.content = content
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The code of the product to which the solution belongs.
        self.product = product
        # The name of the product to which the solution belongs.
        self.product_name = product_name
        # The solution ID.
        self.solution_id = solution_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.product is not None:
            result['product'] = self.product
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.solution_id is not None:
            result['solutionId'] = self.solution_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('solutionId') is not None:
            self.solution_id = m.get('solutionId')
        return self


class GetErrorCodeSolutionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        solutions: List[GetErrorCodeSolutionsResponseBodySolutions] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The solutions. Not all error codes have corresponding solutions. You can submit a ticket or use OpenAPI Explorer to contact technical support if necessary.
        self.solutions = solutions

    def validate(self):
        if self.solutions:
            for k in self.solutions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['solutions'] = []
        if self.solutions is not None:
            for k in self.solutions:
                result['solutions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.solutions = []
        if m.get('solutions') is not None:
            for k in m.get('solutions'):
                temp_model = GetErrorCodeSolutionsResponseBodySolutions()
                self.solutions.append(temp_model.from_map(k))
        return self


class GetErrorCodeSolutionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetErrorCodeSolutionsResponseBody = None,
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
            temp_model = GetErrorCodeSolutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOwnRequestLogRequest(TeaModel):
    def __init__(
        self,
        log_request_id: str = None,
    ):
        # The request ID returned by the API for which you want to query the log. The value is the universally unique identifiers (UUID) of the API request and must be uppercase.
        # 
        # This parameter is required.
        self.log_request_id = log_request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_request_id is not None:
            result['logRequestId'] = self.log_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logRequestId') is not None:
            self.log_request_id = m.get('logRequestId')
        return self


class GetOwnRequestLogResponseBodyLogInfoAuthenticationInfo(TeaModel):
    def __init__(
        self,
        authentication_type: str = None,
        signature_method: str = None,
        signature_version: str = None,
    ):
        # The authentication type. Valid values:
        # 
        # *   AK: includes a permanent AccessKey pair, a temporary AccessKey pair, and a STS token.
        # *   PRIVATEKEY: an AccessKey pair for an asymmetric cryptography algorithm.
        # *   BEARETOKEN: an authentication mechanism that is widely used in the OAuth 2.0 framework and cloud services.
        # *   CUSTOM_SPI: an efficient and secure authentication method that is suitable for the delivery and management of Software as a Service (SaaS) services in Alibaba Cloud Marketplace.
        # *   Anonymous: anonymous access.
        # *   DPS: an authentication method that is similar to AK. Its signature algorithm is different from that of Alibaba Cloud services and is exclusive to specific products.
        self.authentication_type = authentication_type
        # The signature algorithm. Valid values:
        # 
        # *   HMAC-SHA1
        # *   HMAC-SHA256
        self.signature_method = signature_method
        # The signature version.
        self.signature_version = signature_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_type is not None:
            result['authenticationType'] = self.authentication_type
        if self.signature_method is not None:
            result['signatureMethod'] = self.signature_method
        if self.signature_version is not None:
            result['signatureVersion'] = self.signature_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authenticationType') is not None:
            self.authentication_type = m.get('authenticationType')
        if m.get('signatureMethod') is not None:
            self.signature_method = m.get('signatureMethod')
        if m.get('signatureVersion') is not None:
            self.signature_version = m.get('signatureVersion')
        return self


class GetOwnRequestLogResponseBodyLogInfoBasicInfoAccessDeniedDetail(TeaModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # The operation that the operator does not have permissions to perform.
        self.auth_action = auth_action
        # The identity.
        self.auth_principal_display_name = auth_principal_display_name
        # The ID of the Alibaba Cloud account to which the current identity belongs.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The identity type of the operator.
        self.auth_principal_type = auth_principal_type
        # The information after encoding, which can be used for troubleshooting. You can call the DecodeDiagnosticMessage operation of Resource Access Management (RAM) for further diagnostics.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The cause of the permission-related error.
        self.no_permission_type = no_permission_type
        # The type of the policy that causes the permission-related error.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_action is not None:
            result['authAction'] = self.auth_action
        if self.auth_principal_display_name is not None:
            result['authPrincipalDisplayName'] = self.auth_principal_display_name
        if self.auth_principal_owner_id is not None:
            result['authPrincipalOwnerId'] = self.auth_principal_owner_id
        if self.auth_principal_type is not None:
            result['authPrincipalType'] = self.auth_principal_type
        if self.encoded_diagnostic_message is not None:
            result['encodedDiagnosticMessage'] = self.encoded_diagnostic_message
        if self.no_permission_type is not None:
            result['noPermissionType'] = self.no_permission_type
        if self.policy_type is not None:
            result['policyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authAction') is not None:
            self.auth_action = m.get('authAction')
        if m.get('authPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('authPrincipalDisplayName')
        if m.get('authPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('authPrincipalOwnerId')
        if m.get('authPrincipalType') is not None:
            self.auth_principal_type = m.get('authPrincipalType')
        if m.get('encodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('encodedDiagnosticMessage')
        if m.get('noPermissionType') is not None:
            self.no_permission_type = m.get('noPermissionType')
        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')
        return self


class GetOwnRequestLogResponseBodyLogInfoBasicInfoApiDoc(TeaModel):
    def __init__(
        self,
        alibabacloud_site: str = None,
        aliyun_site: str = None,
    ):
        # The documentation URL on the international site (alibabacloud.com).
        self.alibabacloud_site = alibabacloud_site
        # The documentation URL on the China site (aliyun.com).
        self.aliyun_site = aliyun_site

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alibabacloud_site is not None:
            result['alibabacloudSite'] = self.alibabacloud_site
        if self.aliyun_site is not None:
            result['aliyunSite'] = self.aliyun_site
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alibabacloudSite') is not None:
            self.alibabacloud_site = m.get('alibabacloudSite')
        if m.get('aliyunSite') is not None:
            self.aliyun_site = m.get('aliyunSite')
        return self


class GetOwnRequestLogResponseBodyLogInfoBasicInfoProductName(TeaModel):
    def __init__(
        self,
        cn_name: str = None,
        en_name: str = None,
    ):
        # The product name in Chinese.
        self.cn_name = cn_name
        # The product name in English.
        self.en_name = en_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cn_name is not None:
            result['cnName'] = self.cn_name
        if self.en_name is not None:
            result['enName'] = self.en_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cnName') is not None:
            self.cn_name = m.get('cnName')
        if m.get('enName') is not None:
            self.en_name = m.get('enName')
        return self


class GetOwnRequestLogResponseBodyLogInfoBasicInfo(TeaModel):
    def __init__(
        self,
        access_denied_detail: GetOwnRequestLogResponseBodyLogInfoBasicInfoAccessDeniedDetail = None,
        api: str = None,
        api_doc: GetOwnRequestLogResponseBodyLogInfoBasicInfoApiDoc = None,
        api_style: str = None,
        api_version: str = None,
        endpoint: str = None,
        error_code: str = None,
        error_message: str = None,
        gateway_process_time: str = None,
        http_method: str = None,
        http_status_code: str = None,
        log_request_id: str = None,
        product: str = None,
        product_name: GetOwnRequestLogResponseBodyLogInfoBasicInfoProductName = None,
        region_id: str = None,
        request_duration: str = None,
        sdk_request_time: str = None,
        throttling_result: str = None,
    ):
        # The error message returned if the operator does not have the required permissions.
        self.access_denied_detail = access_denied_detail
        # The name of the API.
        self.api = api
        # The information about the API documentation.
        self.api_doc = api_doc
        # The API style. Valid values: roa and rpc.
        self.api_style = api_style
        # The version of the API.
        self.api_version = api_version
        # The endpoint of the service region.
        self.endpoint = endpoint
        # The error code in the log. This parameter is left empty if no error is reported in the API call.
        self.error_code = error_code
        # The error message in the log. This parameter is left empty if no error is reported in the API call.
        self.error_message = error_message
        # The time when the gateway receives the request. Indicate the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.gateway_process_time = gateway_process_time
        # The HTTP request method.
        self.http_method = http_method
        # The HTTP status code in the log.
        self.http_status_code = http_status_code
        # The request ID.
        self.log_request_id = log_request_id
        # The product code.
        self.product = product
        # The product name, which includes the Chinese name and English name.
        self.product_name = product_name
        # The service region ID.
        self.region_id = region_id
        # The duration from when the gateway receives the request to when the client receives a response. Unit: milliseconds.
        self.request_duration = request_duration
        # The time when the request is initiated. Indicate the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.sdk_request_time = sdk_request_time
        # The throttling result. Valid values: FC.PASS: The task is not blocked by throttling. FC.DENY: The task is blocked by throttling.
        self.throttling_result = throttling_result

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.api_doc:
            self.api_doc.validate()
        if self.product_name:
            self.product_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail.to_map()
        if self.api is not None:
            result['api'] = self.api
        if self.api_doc is not None:
            result['apiDoc'] = self.api_doc.to_map()
        if self.api_style is not None:
            result['apiStyle'] = self.api_style
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.gateway_process_time is not None:
            result['gatewayProcessTime'] = self.gateway_process_time
        if self.http_method is not None:
            result['httpMethod'] = self.http_method
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.log_request_id is not None:
            result['logRequestId'] = self.log_request_id
        if self.product is not None:
            result['product'] = self.product
        if self.product_name is not None:
            result['productName'] = self.product_name.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.request_duration is not None:
            result['requestDuration'] = self.request_duration
        if self.sdk_request_time is not None:
            result['sdkRequestTime'] = self.sdk_request_time
        if self.throttling_result is not None:
            result['throttlingResult'] = self.throttling_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            temp_model = GetOwnRequestLogResponseBodyLogInfoBasicInfoAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['accessDeniedDetail'])
        if m.get('api') is not None:
            self.api = m.get('api')
        if m.get('apiDoc') is not None:
            temp_model = GetOwnRequestLogResponseBodyLogInfoBasicInfoApiDoc()
            self.api_doc = temp_model.from_map(m['apiDoc'])
        if m.get('apiStyle') is not None:
            self.api_style = m.get('apiStyle')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('gatewayProcessTime') is not None:
            self.gateway_process_time = m.get('gatewayProcessTime')
        if m.get('httpMethod') is not None:
            self.http_method = m.get('httpMethod')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('logRequestId') is not None:
            self.log_request_id = m.get('logRequestId')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('productName') is not None:
            temp_model = GetOwnRequestLogResponseBodyLogInfoBasicInfoProductName()
            self.product_name = temp_model.from_map(m['productName'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('requestDuration') is not None:
            self.request_duration = m.get('requestDuration')
        if m.get('sdkRequestTime') is not None:
            self.sdk_request_time = m.get('sdkRequestTime')
        if m.get('throttlingResult') is not None:
            self.throttling_result = m.get('throttlingResult')
        return self


class GetOwnRequestLogResponseBodyLogInfoCallerInfo(TeaModel):
    def __init__(
        self,
        caller_account_id: str = None,
        caller_ip: str = None,
        caller_type: str = None,
        master_account_id: str = None,
        user_agent: str = None,
    ):
        # The account ID of the caller.
        self.caller_account_id = caller_account_id
        # The IP address of the caller.
        self.caller_ip = caller_ip
        # The type of the caller. Valid values:
        # 
        # 1.  customer: an Alibaba Cloud account
        # 2.  sub: a RAM user
        # 3.  AssumedRoleUser: a user that uses a temporary Security Token Service (STS) token
        self.caller_type = caller_type
        # The ID of the Alibaba Cloud account.
        self.master_account_id = master_account_id
        # The information about the user agent.
        self.user_agent = user_agent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller_account_id is not None:
            result['callerAccountId'] = self.caller_account_id
        if self.caller_ip is not None:
            result['callerIp'] = self.caller_ip
        if self.caller_type is not None:
            result['callerType'] = self.caller_type
        if self.master_account_id is not None:
            result['masterAccountId'] = self.master_account_id
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callerAccountId') is not None:
            self.caller_account_id = m.get('callerAccountId')
        if m.get('callerIp') is not None:
            self.caller_ip = m.get('callerIp')
        if m.get('callerType') is not None:
            self.caller_type = m.get('callerType')
        if m.get('masterAccountId') is not None:
            self.master_account_id = m.get('masterAccountId')
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        return self


class GetOwnRequestLogResponseBodyLogInfoParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        required: bool = None,
        type: str = None,
        value: Any = None,
    ):
        # The name of the request parameter.
        self.name = name
        # Indicates whether the request parameter is required.
        self.required = required
        # The type of the request parameter.
        self.type = type
        # The value of the request parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.required is not None:
            result['required'] = self.required
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetOwnRequestLogResponseBodyLogInfoResponses(TeaModel):
    def __init__(
        self,
        response_body: str = None,
        response_body_format: str = None,
    ):
        # The response body.
        self.response_body = response_body
        # The type of the response body. Valid values: JSON, XML, and HTML.
        self.response_body_format = response_body_format

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.response_body is not None:
            result['responseBody'] = self.response_body
        if self.response_body_format is not None:
            result['responseBodyFormat'] = self.response_body_format
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('responseBody') is not None:
            self.response_body = m.get('responseBody')
        if m.get('responseBodyFormat') is not None:
            self.response_body_format = m.get('responseBodyFormat')
        return self


class GetOwnRequestLogResponseBodyLogInfo(TeaModel):
    def __init__(
        self,
        authentication_info: GetOwnRequestLogResponseBodyLogInfoAuthenticationInfo = None,
        basic_info: GetOwnRequestLogResponseBodyLogInfoBasicInfo = None,
        caller_info: GetOwnRequestLogResponseBodyLogInfoCallerInfo = None,
        parameters: List[GetOwnRequestLogResponseBodyLogInfoParameters] = None,
        responses: GetOwnRequestLogResponseBodyLogInfoResponses = None,
    ):
        # The authentication information.
        self.authentication_info = authentication_info
        # The basic information about the log of the API call.
        self.basic_info = basic_info
        # The information about the caller.
        self.caller_info = caller_info
        # The information about the request parameters.
        self.parameters = parameters
        # The information that is returned for the request.
        self.responses = responses

    def validate(self):
        if self.authentication_info:
            self.authentication_info.validate()
        if self.basic_info:
            self.basic_info.validate()
        if self.caller_info:
            self.caller_info.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.responses:
            self.responses.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_info is not None:
            result['authenticationInfo'] = self.authentication_info.to_map()
        if self.basic_info is not None:
            result['basicInfo'] = self.basic_info.to_map()
        if self.caller_info is not None:
            result['callerInfo'] = self.caller_info.to_map()
        result['parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['parameters'].append(k.to_map() if k else None)
        if self.responses is not None:
            result['responses'] = self.responses.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authenticationInfo') is not None:
            temp_model = GetOwnRequestLogResponseBodyLogInfoAuthenticationInfo()
            self.authentication_info = temp_model.from_map(m['authenticationInfo'])
        if m.get('basicInfo') is not None:
            temp_model = GetOwnRequestLogResponseBodyLogInfoBasicInfo()
            self.basic_info = temp_model.from_map(m['basicInfo'])
        if m.get('callerInfo') is not None:
            temp_model = GetOwnRequestLogResponseBodyLogInfoCallerInfo()
            self.caller_info = temp_model.from_map(m['callerInfo'])
        self.parameters = []
        if m.get('parameters') is not None:
            for k in m.get('parameters'):
                temp_model = GetOwnRequestLogResponseBodyLogInfoParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('responses') is not None:
            temp_model = GetOwnRequestLogResponseBodyLogInfoResponses()
            self.responses = temp_model.from_map(m['responses'])
        return self


class GetOwnRequestLogResponseBody(TeaModel):
    def __init__(
        self,
        log_info: GetOwnRequestLogResponseBodyLogInfo = None,
        request_id: str = None,
    ):
        # The detailed information about the log of the API call.
        self.log_info = log_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.log_info:
            self.log_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_info is not None:
            result['logInfo'] = self.log_info.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logInfo') is not None:
            temp_model = GetOwnRequestLogResponseBodyLogInfo()
            self.log_info = temp_model.from_map(m['logInfo'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetOwnRequestLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOwnRequestLogResponseBody = None,
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
            temp_model = GetOwnRequestLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductEndpointsRequest(TeaModel):
    def __init__(
        self,
        product: str = None,
    ):
        # This parameter is required.
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('product') is not None:
            self.product = m.get('product')
        return self


class GetProductEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: dict = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        pass

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
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GetRequestLogRequest(TeaModel):
    def __init__(
        self,
        log_request_id: str = None,
    ):
        # The request ID returned by the API for which you want to query the log. The value is the universally unique identifiers (UUID) of the API request and must be uppercase.
        # 
        # This parameter is required.
        self.log_request_id = log_request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_request_id is not None:
            result['logRequestId'] = self.log_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logRequestId') is not None:
            self.log_request_id = m.get('logRequestId')
        return self


class GetRequestLogResponseBodyLogInfoAuthenticationInfo(TeaModel):
    def __init__(
        self,
        authentication_type: str = None,
        signature_method: str = None,
        signature_version: str = None,
    ):
        # The authentication type. Valid values:
        # 
        # *   AK: includes a permanent AccessKey pair, a temporary AccessKey pair, and a STS token.
        # *   PRIVATEKEY: an AccessKey pair for an asymmetric cryptography algorithm.
        # *   BEARETOKEN: an authentication mechanism that is widely used in the OAuth 2.0 framework and cloud services.
        # *   CUSTOM_SPI: an efficient and secure authentication method that is suitable for the delivery and management of Software as a Service (SaaS) services in Alibaba Cloud Marketplace.
        # *   Anonymous: anonymous access.
        # *   DPS: an authentication method that is similar to AK. Its signature algorithm is different from that of Alibaba Cloud services and is exclusive to specific products.
        self.authentication_type = authentication_type
        # The signature algorithm. Valid values:
        # 
        # *   HMAC-SHA1
        # *   HMAC-SHA256
        self.signature_method = signature_method
        # The signature version.
        self.signature_version = signature_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_type is not None:
            result['authenticationType'] = self.authentication_type
        if self.signature_method is not None:
            result['signatureMethod'] = self.signature_method
        if self.signature_version is not None:
            result['signatureVersion'] = self.signature_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authenticationType') is not None:
            self.authentication_type = m.get('authenticationType')
        if m.get('signatureMethod') is not None:
            self.signature_method = m.get('signatureMethod')
        if m.get('signatureVersion') is not None:
            self.signature_version = m.get('signatureVersion')
        return self


class GetRequestLogResponseBodyLogInfoBasicInfoAccessDeniedDetail(TeaModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # The operation that the operator does not have permissions to perform.
        self.auth_action = auth_action
        # The identity.
        self.auth_principal_display_name = auth_principal_display_name
        # The ID of the Alibaba Cloud account to which the current identity belongs.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The identity type of the operator.
        self.auth_principal_type = auth_principal_type
        # The information after encoding, which can be used for troubleshooting. You can call the DecodeDiagnosticMessage operation of Resource Access Management (RAM) for further diagnostics.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The cause of the permission-related error.
        self.no_permission_type = no_permission_type
        # The type of the policy that causes the permission-related error.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_action is not None:
            result['authAction'] = self.auth_action
        if self.auth_principal_display_name is not None:
            result['authPrincipalDisplayName'] = self.auth_principal_display_name
        if self.auth_principal_owner_id is not None:
            result['authPrincipalOwnerId'] = self.auth_principal_owner_id
        if self.auth_principal_type is not None:
            result['authPrincipalType'] = self.auth_principal_type
        if self.encoded_diagnostic_message is not None:
            result['encodedDiagnosticMessage'] = self.encoded_diagnostic_message
        if self.no_permission_type is not None:
            result['noPermissionType'] = self.no_permission_type
        if self.policy_type is not None:
            result['policyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authAction') is not None:
            self.auth_action = m.get('authAction')
        if m.get('authPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('authPrincipalDisplayName')
        if m.get('authPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('authPrincipalOwnerId')
        if m.get('authPrincipalType') is not None:
            self.auth_principal_type = m.get('authPrincipalType')
        if m.get('encodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('encodedDiagnosticMessage')
        if m.get('noPermissionType') is not None:
            self.no_permission_type = m.get('noPermissionType')
        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')
        return self


class GetRequestLogResponseBodyLogInfoBasicInfoApiDoc(TeaModel):
    def __init__(
        self,
        alibabacloud_site: str = None,
        aliyun_site: str = None,
    ):
        # The documentation URL on the international site (alibabacloud.com).
        self.alibabacloud_site = alibabacloud_site
        # The documentation URL on the China site (aliyun.com).
        self.aliyun_site = aliyun_site

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alibabacloud_site is not None:
            result['alibabacloudSite'] = self.alibabacloud_site
        if self.aliyun_site is not None:
            result['aliyunSite'] = self.aliyun_site
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alibabacloudSite') is not None:
            self.alibabacloud_site = m.get('alibabacloudSite')
        if m.get('aliyunSite') is not None:
            self.aliyun_site = m.get('aliyunSite')
        return self


class GetRequestLogResponseBodyLogInfoBasicInfoProductName(TeaModel):
    def __init__(
        self,
        cn_name: str = None,
        en_name: str = None,
    ):
        # The product name in Chinese.
        self.cn_name = cn_name
        # The product name in English.
        self.en_name = en_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cn_name is not None:
            result['cnName'] = self.cn_name
        if self.en_name is not None:
            result['enName'] = self.en_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cnName') is not None:
            self.cn_name = m.get('cnName')
        if m.get('enName') is not None:
            self.en_name = m.get('enName')
        return self


class GetRequestLogResponseBodyLogInfoBasicInfo(TeaModel):
    def __init__(
        self,
        access_denied_detail: GetRequestLogResponseBodyLogInfoBasicInfoAccessDeniedDetail = None,
        api: str = None,
        api_doc: GetRequestLogResponseBodyLogInfoBasicInfoApiDoc = None,
        api_style: str = None,
        api_version: str = None,
        endpoint: str = None,
        error_code: str = None,
        error_message: str = None,
        gateway_process_time: str = None,
        http_method: str = None,
        http_status_code: str = None,
        log_request_id: str = None,
        product: str = None,
        product_name: GetRequestLogResponseBodyLogInfoBasicInfoProductName = None,
        region_id: str = None,
        request_duration: str = None,
        sdk_request_time: str = None,
        throttling_result: str = None,
    ):
        # The error message returned if the operator does not have the required permissions. This parameter is available only if an authentication error is reported for the request ID.
        self.access_denied_detail = access_denied_detail
        # The name of the API.
        self.api = api
        # The information about the API documentation.
        self.api_doc = api_doc
        # The API style. Valid values: roa and rpc.
        self.api_style = api_style
        # The version of the API.
        self.api_version = api_version
        # The endpoint of the service region.
        self.endpoint = endpoint
        # The error code in the log. This parameter is left empty if no error is reported in the API call.
        self.error_code = error_code
        # The error message in the log. This parameter is left empty if no error is reported in the API call.
        self.error_message = error_message
        # The time when the gateway receives the request. Indicate the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.gateway_process_time = gateway_process_time
        # The HTTP request method. Valid values: GET, PUT, and POST.
        self.http_method = http_method
        # The HTTP status code in the log.
        self.http_status_code = http_status_code
        # The request ID.
        self.log_request_id = log_request_id
        # The product code.
        self.product = product
        # The product name, which includes the Chinese name and English name.
        self.product_name = product_name
        # The service region ID.
        self.region_id = region_id
        # The duration from when the gateway receives the request to when the client receives a response. Unit: milliseconds.
        self.request_duration = request_duration
        # The time when the request is initiated. Indicate the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.sdk_request_time = sdk_request_time
        # The throttling result. Valid values: FC.PASS: The task is not blocked by throttling. FC.DENY: The task is blocked by throttling.
        self.throttling_result = throttling_result

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.api_doc:
            self.api_doc.validate()
        if self.product_name:
            self.product_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail.to_map()
        if self.api is not None:
            result['api'] = self.api
        if self.api_doc is not None:
            result['apiDoc'] = self.api_doc.to_map()
        if self.api_style is not None:
            result['apiStyle'] = self.api_style
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.gateway_process_time is not None:
            result['gatewayProcessTime'] = self.gateway_process_time
        if self.http_method is not None:
            result['httpMethod'] = self.http_method
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.log_request_id is not None:
            result['logRequestId'] = self.log_request_id
        if self.product is not None:
            result['product'] = self.product
        if self.product_name is not None:
            result['productName'] = self.product_name.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.request_duration is not None:
            result['requestDuration'] = self.request_duration
        if self.sdk_request_time is not None:
            result['sdkRequestTime'] = self.sdk_request_time
        if self.throttling_result is not None:
            result['throttlingResult'] = self.throttling_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            temp_model = GetRequestLogResponseBodyLogInfoBasicInfoAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['accessDeniedDetail'])
        if m.get('api') is not None:
            self.api = m.get('api')
        if m.get('apiDoc') is not None:
            temp_model = GetRequestLogResponseBodyLogInfoBasicInfoApiDoc()
            self.api_doc = temp_model.from_map(m['apiDoc'])
        if m.get('apiStyle') is not None:
            self.api_style = m.get('apiStyle')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('gatewayProcessTime') is not None:
            self.gateway_process_time = m.get('gatewayProcessTime')
        if m.get('httpMethod') is not None:
            self.http_method = m.get('httpMethod')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('logRequestId') is not None:
            self.log_request_id = m.get('logRequestId')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('productName') is not None:
            temp_model = GetRequestLogResponseBodyLogInfoBasicInfoProductName()
            self.product_name = temp_model.from_map(m['productName'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('requestDuration') is not None:
            self.request_duration = m.get('requestDuration')
        if m.get('sdkRequestTime') is not None:
            self.sdk_request_time = m.get('sdkRequestTime')
        if m.get('throttlingResult') is not None:
            self.throttling_result = m.get('throttlingResult')
        return self


class GetRequestLogResponseBodyLogInfoCallerInfo(TeaModel):
    def __init__(
        self,
        caller_account_id: str = None,
        caller_ip: str = None,
        caller_type: str = None,
        master_account_id: str = None,
        user_agent: str = None,
    ):
        # The account ID of the caller.
        self.caller_account_id = caller_account_id
        # The IP address of the caller.
        self.caller_ip = caller_ip
        # The type of the caller. Valid values:
        # 
        # 1.  customer: an Alibaba Cloud account
        # 2.  sub: a RAM user
        # 3.  AssumedRoleUser: a user that uses a temporary Security Token Service (STS) token
        self.caller_type = caller_type
        # The ID of the Alibaba Cloud account.
        self.master_account_id = master_account_id
        # The information about the user agent.
        self.user_agent = user_agent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller_account_id is not None:
            result['callerAccountId'] = self.caller_account_id
        if self.caller_ip is not None:
            result['callerIp'] = self.caller_ip
        if self.caller_type is not None:
            result['callerType'] = self.caller_type
        if self.master_account_id is not None:
            result['masterAccountId'] = self.master_account_id
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callerAccountId') is not None:
            self.caller_account_id = m.get('callerAccountId')
        if m.get('callerIp') is not None:
            self.caller_ip = m.get('callerIp')
        if m.get('callerType') is not None:
            self.caller_type = m.get('callerType')
        if m.get('masterAccountId') is not None:
            self.master_account_id = m.get('masterAccountId')
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        return self


class GetRequestLogResponseBodyLogInfoParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        required: bool = None,
        type: str = None,
        value: Any = None,
    ):
        # The name of the request parameter.
        self.name = name
        # Indicates whether the request parameter is required.
        self.required = required
        # The type of the request parameter.
        self.type = type
        # The value of the request parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.required is not None:
            result['required'] = self.required
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetRequestLogResponseBodyLogInfoResponses(TeaModel):
    def __init__(
        self,
        response_body: str = None,
        response_body_format: str = None,
    ):
        # The response body.
        self.response_body = response_body
        # The type of the response body. Valid values: JSON, XML, and HTML.
        self.response_body_format = response_body_format

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.response_body is not None:
            result['responseBody'] = self.response_body
        if self.response_body_format is not None:
            result['responseBodyFormat'] = self.response_body_format
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('responseBody') is not None:
            self.response_body = m.get('responseBody')
        if m.get('responseBodyFormat') is not None:
            self.response_body_format = m.get('responseBodyFormat')
        return self


class GetRequestLogResponseBodyLogInfo(TeaModel):
    def __init__(
        self,
        authentication_info: GetRequestLogResponseBodyLogInfoAuthenticationInfo = None,
        basic_info: GetRequestLogResponseBodyLogInfoBasicInfo = None,
        caller_info: GetRequestLogResponseBodyLogInfoCallerInfo = None,
        parameters: List[GetRequestLogResponseBodyLogInfoParameters] = None,
        responses: GetRequestLogResponseBodyLogInfoResponses = None,
    ):
        # The authentication information.
        self.authentication_info = authentication_info
        # The basic information about the log of the API call.
        self.basic_info = basic_info
        # The information about the caller.
        self.caller_info = caller_info
        # The information about the request parameters.
        self.parameters = parameters
        # The information that is returned for the request.
        self.responses = responses

    def validate(self):
        if self.authentication_info:
            self.authentication_info.validate()
        if self.basic_info:
            self.basic_info.validate()
        if self.caller_info:
            self.caller_info.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.responses:
            self.responses.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_info is not None:
            result['authenticationInfo'] = self.authentication_info.to_map()
        if self.basic_info is not None:
            result['basicInfo'] = self.basic_info.to_map()
        if self.caller_info is not None:
            result['callerInfo'] = self.caller_info.to_map()
        result['parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['parameters'].append(k.to_map() if k else None)
        if self.responses is not None:
            result['responses'] = self.responses.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authenticationInfo') is not None:
            temp_model = GetRequestLogResponseBodyLogInfoAuthenticationInfo()
            self.authentication_info = temp_model.from_map(m['authenticationInfo'])
        if m.get('basicInfo') is not None:
            temp_model = GetRequestLogResponseBodyLogInfoBasicInfo()
            self.basic_info = temp_model.from_map(m['basicInfo'])
        if m.get('callerInfo') is not None:
            temp_model = GetRequestLogResponseBodyLogInfoCallerInfo()
            self.caller_info = temp_model.from_map(m['callerInfo'])
        self.parameters = []
        if m.get('parameters') is not None:
            for k in m.get('parameters'):
                temp_model = GetRequestLogResponseBodyLogInfoParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('responses') is not None:
            temp_model = GetRequestLogResponseBodyLogInfoResponses()
            self.responses = temp_model.from_map(m['responses'])
        return self


class GetRequestLogResponseBody(TeaModel):
    def __init__(
        self,
        log_info: GetRequestLogResponseBodyLogInfo = None,
        request_id: str = None,
    ):
        # The detailed information about the log of the API call.
        self.log_info = log_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.log_info:
            self.log_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_info is not None:
            result['logInfo'] = self.log_info.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logInfo') is not None:
            temp_model = GetRequestLogResponseBodyLogInfo()
            self.log_info = temp_model.from_map(m['logInfo'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRequestLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRequestLogResponseBody = None,
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
            temp_model = GetRequestLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApiDefinitionsRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        product: str = None,
    ):
        # This parameter is required.
        self.api_version = api_version
        # This parameter is required.
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.product is not None:
            result['product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('product') is not None:
            self.product = m.get('product')
        return self


class ListApiDefinitionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: dict = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        pass

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
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ListApiMcpServerSystemToolsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        skip: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.skip = skip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.skip is not None:
            result['skip'] = self.skip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('skip') is not None:
            self.skip = m.get('skip')
        return self


class ListApiMcpServerSystemToolsResponseBodySystemTools(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        self.name = name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListApiMcpServerSystemToolsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        system_tools: List[ListApiMcpServerSystemToolsResponseBodySystemTools] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.system_tools = system_tools
        self.total_count = total_count

    def validate(self):
        if self.system_tools:
            for k in self.system_tools:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['systemTools'] = []
        if self.system_tools is not None:
            for k in self.system_tools:
                result['systemTools'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.system_tools = []
        if m.get('systemTools') is not None:
            for k in m.get('systemTools'):
                temp_model = ListApiMcpServerSystemToolsResponseBodySystemTools()
                self.system_tools.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListApiMcpServerSystemToolsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListApiMcpServerSystemToolsResponseBody = None,
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
            temp_model = ListApiMcpServerSystemToolsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApiMcpServersRequest(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        id: str = None,
        keyword: str = None,
        language: str = None,
        max_results: int = None,
        next_token: str = None,
        skip: int = None,
        source_type: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.id = id
        self.keyword = keyword
        self.language = language
        self.max_results = max_results
        self.next_token = next_token
        self.skip = skip
        self.source_type = source_type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.language is not None:
            result['language'] = self.language
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.skip is not None:
            result['skip'] = self.skip
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('skip') is not None:
            self.skip = m.get('skip')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListApiMcpServersResponseBodyApiMcpServersAdditionalApiDescriptionsConstParameters(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListApiMcpServersResponseBodyApiMcpServersAdditionalApiDescriptions(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        api_override_json: str = None,
        api_version: str = None,
        const_parameters: List[ListApiMcpServersResponseBodyApiMcpServersAdditionalApiDescriptionsConstParameters] = None,
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
            for k in self.const_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.api_override_json is not None:
            result['apiOverrideJson'] = self.api_override_json
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        result['constParameters'] = []
        if self.const_parameters is not None:
            for k in self.const_parameters:
                result['constParameters'].append(k.to_map() if k else None)
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
            for k in m.get('constParameters'):
                temp_model = ListApiMcpServersResponseBodyApiMcpServersAdditionalApiDescriptionsConstParameters()
                self.const_parameters.append(temp_model.from_map(k))
        if m.get('enableOutputSchema') is not None:
            self.enable_output_schema = m.get('enableOutputSchema')
        if m.get('executeCliCommand') is not None:
            self.execute_cli_command = m.get('executeCliCommand')
        if m.get('product') is not None:
            self.product = m.get('product')
        return self


class ListApiMcpServersResponseBodyApiMcpServersApis(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListApiMcpServersResponseBodyApiMcpServersPromptsArguments(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListApiMcpServersResponseBodyApiMcpServersPrompts(TeaModel):
    def __init__(
        self,
        arguments: List[ListApiMcpServersResponseBodyApiMcpServersPromptsArguments] = None,
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
            for k in self.arguments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['arguments'] = []
        if self.arguments is not None:
            for k in self.arguments:
                result['arguments'].append(k.to_map() if k else None)
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
            for k in m.get('arguments'):
                temp_model = ListApiMcpServersResponseBodyApiMcpServersPromptsArguments()
                self.arguments.append(temp_model.from_map(k))
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListApiMcpServersResponseBodyApiMcpServersSystemMcpServerInfo(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListApiMcpServersResponseBodyApiMcpServersTerraformTools(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListApiMcpServersResponseBodyApiMcpServersUrls(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListApiMcpServersResponseBodyApiMcpServers(TeaModel):
    def __init__(
        self,
        additional_api_descriptions: List[ListApiMcpServersResponseBodyApiMcpServersAdditionalApiDescriptions] = None,
        apis: List[ListApiMcpServersResponseBodyApiMcpServersApis] = None,
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
        prompts: List[ListApiMcpServersResponseBodyApiMcpServersPrompts] = None,
        public_access: str = None,
        source_type: str = None,
        system_mcp_server_info: ListApiMcpServersResponseBodyApiMcpServersSystemMcpServerInfo = None,
        system_tools: List[str] = None,
        terraform_tools: List[ListApiMcpServersResponseBodyApiMcpServersTerraformTools] = None,
        update_time: str = None,
        urls: ListApiMcpServersResponseBodyApiMcpServersUrls = None,
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
            for k in self.additional_api_descriptions:
                if k:
                    k.validate()
        if self.apis:
            for k in self.apis:
                if k:
                    k.validate()
        if self.prompts:
            for k in self.prompts:
                if k:
                    k.validate()
        if self.system_mcp_server_info:
            self.system_mcp_server_info.validate()
        if self.terraform_tools:
            for k in self.terraform_tools:
                if k:
                    k.validate()
        if self.urls:
            self.urls.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['additionalApiDescriptions'] = []
        if self.additional_api_descriptions is not None:
            for k in self.additional_api_descriptions:
                result['additionalApiDescriptions'].append(k.to_map() if k else None)
        result['apis'] = []
        if self.apis is not None:
            for k in self.apis:
                result['apis'].append(k.to_map() if k else None)
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
            for k in self.prompts:
                result['prompts'].append(k.to_map() if k else None)
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
            for k in self.terraform_tools:
                result['terraformTools'].append(k.to_map() if k else None)
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
            for k in m.get('additionalApiDescriptions'):
                temp_model = ListApiMcpServersResponseBodyApiMcpServersAdditionalApiDescriptions()
                self.additional_api_descriptions.append(temp_model.from_map(k))
        self.apis = []
        if m.get('apis') is not None:
            for k in m.get('apis'):
                temp_model = ListApiMcpServersResponseBodyApiMcpServersApis()
                self.apis.append(temp_model.from_map(k))
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
            for k in m.get('prompts'):
                temp_model = ListApiMcpServersResponseBodyApiMcpServersPrompts()
                self.prompts.append(temp_model.from_map(k))
        if m.get('publicAccess') is not None:
            self.public_access = m.get('publicAccess')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('systemMcpServerInfo') is not None:
            temp_model = ListApiMcpServersResponseBodyApiMcpServersSystemMcpServerInfo()
            self.system_mcp_server_info = temp_model.from_map(m['systemMcpServerInfo'])
        if m.get('systemTools') is not None:
            self.system_tools = m.get('systemTools')
        self.terraform_tools = []
        if m.get('terraformTools') is not None:
            for k in m.get('terraformTools'):
                temp_model = ListApiMcpServersResponseBodyApiMcpServersTerraformTools()
                self.terraform_tools.append(temp_model.from_map(k))
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('urls') is not None:
            temp_model = ListApiMcpServersResponseBodyApiMcpServersUrls()
            self.urls = temp_model.from_map(m['urls'])
        if m.get('vpcWhitelists') is not None:
            self.vpc_whitelists = m.get('vpcWhitelists')
        return self


class ListApiMcpServersResponseBody(TeaModel):
    def __init__(
        self,
        api_mcp_servers: List[ListApiMcpServersResponseBodyApiMcpServers] = None,
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
            for k in self.api_mcp_servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['apiMcpServers'] = []
        if self.api_mcp_servers is not None:
            for k in self.api_mcp_servers:
                result['apiMcpServers'].append(k.to_map() if k else None)
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
            for k in m.get('apiMcpServers'):
                temp_model = ListApiMcpServersResponseBodyApiMcpServers()
                self.api_mcp_servers.append(temp_model.from_map(k))
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListApiMcpServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListApiMcpServersResponseBody = None,
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
            temp_model = ListApiMcpServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApiMcpServerRequestAdditionalApiDescriptionsConstParameters(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateApiMcpServerRequestAdditionalApiDescriptions(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        api_override_json: str = None,
        api_version: str = None,
        const_parameters: List[UpdateApiMcpServerRequestAdditionalApiDescriptionsConstParameters] = None,
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
            for k in self.const_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.api_override_json is not None:
            result['apiOverrideJson'] = self.api_override_json
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        result['constParameters'] = []
        if self.const_parameters is not None:
            for k in self.const_parameters:
                result['constParameters'].append(k.to_map() if k else None)
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
            for k in m.get('constParameters'):
                temp_model = UpdateApiMcpServerRequestAdditionalApiDescriptionsConstParameters()
                self.const_parameters.append(temp_model.from_map(k))
        if m.get('enableOutputSchema') is not None:
            self.enable_output_schema = m.get('enableOutputSchema')
        if m.get('executeCliCommand') is not None:
            self.execute_cli_command = m.get('executeCliCommand')
        if m.get('product') is not None:
            self.product = m.get('product')
        return self


class UpdateApiMcpServerRequestApis(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateApiMcpServerRequestPromptsArguments(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateApiMcpServerRequestPrompts(TeaModel):
    def __init__(
        self,
        arguments: List[UpdateApiMcpServerRequestPromptsArguments] = None,
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
            for k in self.arguments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['arguments'] = []
        if self.arguments is not None:
            for k in self.arguments:
                result['arguments'].append(k.to_map() if k else None)
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
            for k in m.get('arguments'):
                temp_model = UpdateApiMcpServerRequestPromptsArguments()
                self.arguments.append(temp_model.from_map(k))
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateApiMcpServerRequestTerraformTools(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateApiMcpServerRequest(TeaModel):
    def __init__(
        self,
        additional_api_descriptions: List[UpdateApiMcpServerRequestAdditionalApiDescriptions] = None,
        apis: List[UpdateApiMcpServerRequestApis] = None,
        assume_role_extra_policy: str = None,
        assume_role_name: str = None,
        description: str = None,
        enable_assume_role: bool = None,
        enable_custom_vpc_whitelist: bool = None,
        instructions: str = None,
        language: str = None,
        oauth_client_id: str = None,
        prompts: List[UpdateApiMcpServerRequestPrompts] = None,
        public_access: str = None,
        system_tools: List[str] = None,
        terraform_tools: List[UpdateApiMcpServerRequestTerraformTools] = None,
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
            for k in self.additional_api_descriptions:
                if k:
                    k.validate()
        if self.apis:
            for k in self.apis:
                if k:
                    k.validate()
        if self.prompts:
            for k in self.prompts:
                if k:
                    k.validate()
        if self.terraform_tools:
            for k in self.terraform_tools:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['additionalApiDescriptions'] = []
        if self.additional_api_descriptions is not None:
            for k in self.additional_api_descriptions:
                result['additionalApiDescriptions'].append(k.to_map() if k else None)
        result['apis'] = []
        if self.apis is not None:
            for k in self.apis:
                result['apis'].append(k.to_map() if k else None)
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
            for k in self.prompts:
                result['prompts'].append(k.to_map() if k else None)
        if self.public_access is not None:
            result['publicAccess'] = self.public_access
        if self.system_tools is not None:
            result['systemTools'] = self.system_tools
        result['terraformTools'] = []
        if self.terraform_tools is not None:
            for k in self.terraform_tools:
                result['terraformTools'].append(k.to_map() if k else None)
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
            for k in m.get('additionalApiDescriptions'):
                temp_model = UpdateApiMcpServerRequestAdditionalApiDescriptions()
                self.additional_api_descriptions.append(temp_model.from_map(k))
        self.apis = []
        if m.get('apis') is not None:
            for k in m.get('apis'):
                temp_model = UpdateApiMcpServerRequestApis()
                self.apis.append(temp_model.from_map(k))
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
            for k in m.get('prompts'):
                temp_model = UpdateApiMcpServerRequestPrompts()
                self.prompts.append(temp_model.from_map(k))
        if m.get('publicAccess') is not None:
            self.public_access = m.get('publicAccess')
        if m.get('systemTools') is not None:
            self.system_tools = m.get('systemTools')
        self.terraform_tools = []
        if m.get('terraformTools') is not None:
            for k in m.get('terraformTools'):
                temp_model = UpdateApiMcpServerRequestTerraformTools()
                self.terraform_tools.append(temp_model.from_map(k))
        if m.get('vpcWhitelists') is not None:
            self.vpc_whitelists = m.get('vpcWhitelists')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class UpdateApiMcpServerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateApiMcpServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateApiMcpServerResponseBody = None,
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
            temp_model = UpdateApiMcpServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApiMcpServerUserConfigRequest(TeaModel):
    def __init__(
        self,
        enable_public_access: bool = None,
        vpc_whitelists: List[str] = None,
    ):
        self.enable_public_access = enable_public_access
        self.vpc_whitelists = vpc_whitelists

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_public_access is not None:
            result['enablePublicAccess'] = self.enable_public_access
        if self.vpc_whitelists is not None:
            result['vpcWhitelists'] = self.vpc_whitelists
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enablePublicAccess') is not None:
            self.enable_public_access = m.get('enablePublicAccess')
        if m.get('vpcWhitelists') is not None:
            self.vpc_whitelists = m.get('vpcWhitelists')
        return self


class UpdateApiMcpServerUserConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateApiMcpServerUserConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateApiMcpServerUserConfigResponseBody = None,
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
            temp_model = UpdateApiMcpServerUserConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


