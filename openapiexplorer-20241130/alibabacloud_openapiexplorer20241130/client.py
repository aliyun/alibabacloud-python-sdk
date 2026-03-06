# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_openapiexplorer20241130 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'ap-southeast-1': 'openapi-mcp.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou': 'openapi-mcp.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('openapiexplorer', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def api_mcp_server_validate_hcl_with_options(
        self,
        request: main_models.ApiMcpServerValidateHclRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ApiMcpServerValidateHclResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ApiMcpServerValidateHcl',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/terraform/validate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApiMcpServerValidateHclResponse(),
            self.call_api(params, req, runtime)
        )

    async def api_mcp_server_validate_hcl_with_options_async(
        self,
        request: main_models.ApiMcpServerValidateHclRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ApiMcpServerValidateHclResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ApiMcpServerValidateHcl',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/terraform/validate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApiMcpServerValidateHclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def api_mcp_server_validate_hcl(
        self,
        request: main_models.ApiMcpServerValidateHclRequest,
    ) -> main_models.ApiMcpServerValidateHclResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.api_mcp_server_validate_hcl_with_options(request, headers, runtime)

    async def api_mcp_server_validate_hcl_async(
        self,
        request: main_models.ApiMcpServerValidateHclRequest,
    ) -> main_models.ApiMcpServerValidateHclResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.api_mcp_server_validate_hcl_with_options_async(request, headers, runtime)

    def create_api_mcp_server_with_options(
        self,
        request: main_models.CreateApiMcpServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiMcpServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.additional_api_descriptions):
            body['additionalApiDescriptions'] = request.additional_api_descriptions
        if not DaraCore.is_null(request.apis):
            body['apis'] = request.apis
        if not DaraCore.is_null(request.assume_role_extra_policy):
            body['assumeRoleExtraPolicy'] = request.assume_role_extra_policy
        if not DaraCore.is_null(request.assume_role_name):
            body['assumeRoleName'] = request.assume_role_name
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable_assume_role):
            body['enableAssumeRole'] = request.enable_assume_role
        if not DaraCore.is_null(request.enable_custom_vpc_whitelist):
            body['enableCustomVpcWhitelist'] = request.enable_custom_vpc_whitelist
        if not DaraCore.is_null(request.instructions):
            body['instructions'] = request.instructions
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.oauth_client_id):
            body['oauthClientId'] = request.oauth_client_id
        if not DaraCore.is_null(request.prompts):
            body['prompts'] = request.prompts
        if not DaraCore.is_null(request.public_access):
            body['publicAccess'] = request.public_access
        if not DaraCore.is_null(request.system_tools):
            body['systemTools'] = request.system_tools
        if not DaraCore.is_null(request.terraform_tools):
            body['terraformTools'] = request.terraform_tools
        if not DaraCore.is_null(request.vpc_whitelists):
            body['vpcWhitelists'] = request.vpc_whitelists
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiMcpServer',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/apimcpserver',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_mcp_server_with_options_async(
        self,
        request: main_models.CreateApiMcpServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiMcpServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.additional_api_descriptions):
            body['additionalApiDescriptions'] = request.additional_api_descriptions
        if not DaraCore.is_null(request.apis):
            body['apis'] = request.apis
        if not DaraCore.is_null(request.assume_role_extra_policy):
            body['assumeRoleExtraPolicy'] = request.assume_role_extra_policy
        if not DaraCore.is_null(request.assume_role_name):
            body['assumeRoleName'] = request.assume_role_name
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable_assume_role):
            body['enableAssumeRole'] = request.enable_assume_role
        if not DaraCore.is_null(request.enable_custom_vpc_whitelist):
            body['enableCustomVpcWhitelist'] = request.enable_custom_vpc_whitelist
        if not DaraCore.is_null(request.instructions):
            body['instructions'] = request.instructions
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.oauth_client_id):
            body['oauthClientId'] = request.oauth_client_id
        if not DaraCore.is_null(request.prompts):
            body['prompts'] = request.prompts
        if not DaraCore.is_null(request.public_access):
            body['publicAccess'] = request.public_access
        if not DaraCore.is_null(request.system_tools):
            body['systemTools'] = request.system_tools
        if not DaraCore.is_null(request.terraform_tools):
            body['terraformTools'] = request.terraform_tools
        if not DaraCore.is_null(request.vpc_whitelists):
            body['vpcWhitelists'] = request.vpc_whitelists
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiMcpServer',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/apimcpserver',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_mcp_server(
        self,
        request: main_models.CreateApiMcpServerRequest,
    ) -> main_models.CreateApiMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_api_mcp_server_with_options(request, headers, runtime)

    async def create_api_mcp_server_async(
        self,
        request: main_models.CreateApiMcpServerRequest,
    ) -> main_models.CreateApiMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_api_mcp_server_with_options_async(request, headers, runtime)

    def delete_api_mcp_server_with_options(
        self,
        request: main_models.DeleteApiMcpServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiMcpServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiMcpServer',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/apimcpserver',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_mcp_server_with_options_async(
        self,
        request: main_models.DeleteApiMcpServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiMcpServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiMcpServer',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/apimcpserver',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_mcp_server(
        self,
        request: main_models.DeleteApiMcpServerRequest,
    ) -> main_models.DeleteApiMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_api_mcp_server_with_options(request, headers, runtime)

    async def delete_api_mcp_server_async(
        self,
        request: main_models.DeleteApiMcpServerRequest,
    ) -> main_models.DeleteApiMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_api_mcp_server_with_options_async(request, headers, runtime)

    def generate_clicommand_with_options(
        self,
        tmp_req: main_models.GenerateCLICommandRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateCLICommandResponse:
        tmp_req.validate()
        request = main_models.GenerateCLICommandShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.api_params):
            request.api_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.api_params, 'apiParams', 'json')
        body = {}
        if not DaraCore.is_null(request.aggregate_pagination):
            body['aggregatePagination'] = request.aggregate_pagination
        if not DaraCore.is_null(request.api):
            body['api'] = request.api
        if not DaraCore.is_null(request.api_params_shrink):
            body['apiParams'] = request.api_params_shrink
        if not DaraCore.is_null(request.api_version):
            body['apiVersion'] = request.api_version
        if not DaraCore.is_null(request.json_api_params):
            body['jsonApiParams'] = request.json_api_params
        if not DaraCore.is_null(request.product):
            body['product'] = request.product
        if not DaraCore.is_null(request.region_id):
            body['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateCLICommand',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/api/cli/makeCode',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateCLICommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_clicommand_with_options_async(
        self,
        tmp_req: main_models.GenerateCLICommandRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateCLICommandResponse:
        tmp_req.validate()
        request = main_models.GenerateCLICommandShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.api_params):
            request.api_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.api_params, 'apiParams', 'json')
        body = {}
        if not DaraCore.is_null(request.aggregate_pagination):
            body['aggregatePagination'] = request.aggregate_pagination
        if not DaraCore.is_null(request.api):
            body['api'] = request.api
        if not DaraCore.is_null(request.api_params_shrink):
            body['apiParams'] = request.api_params_shrink
        if not DaraCore.is_null(request.api_version):
            body['apiVersion'] = request.api_version
        if not DaraCore.is_null(request.json_api_params):
            body['jsonApiParams'] = request.json_api_params
        if not DaraCore.is_null(request.product):
            body['product'] = request.product
        if not DaraCore.is_null(request.region_id):
            body['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateCLICommand',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/api/cli/makeCode',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateCLICommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_clicommand(
        self,
        request: main_models.GenerateCLICommandRequest,
    ) -> main_models.GenerateCLICommandResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.generate_clicommand_with_options(request, headers, runtime)

    async def generate_clicommand_async(
        self,
        request: main_models.GenerateCLICommandRequest,
    ) -> main_models.GenerateCLICommandResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.generate_clicommand_with_options_async(request, headers, runtime)

    def get_api_definition_with_options(
        self,
        request: main_models.GetApiDefinitionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetApiDefinitionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api):
            query['api'] = request.api
        if not DaraCore.is_null(request.api_version):
            query['apiVersion'] = request.api_version
        if not DaraCore.is_null(request.product):
            query['product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApiDefinition',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/api/definition',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApiDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_api_definition_with_options_async(
        self,
        request: main_models.GetApiDefinitionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetApiDefinitionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api):
            query['api'] = request.api
        if not DaraCore.is_null(request.api_version):
            query['apiVersion'] = request.api_version
        if not DaraCore.is_null(request.product):
            query['product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApiDefinition',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/api/definition',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApiDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_api_definition(
        self,
        request: main_models.GetApiDefinitionRequest,
    ) -> main_models.GetApiDefinitionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_api_definition_with_options(request, headers, runtime)

    async def get_api_definition_async(
        self,
        request: main_models.GetApiDefinitionRequest,
    ) -> main_models.GetApiDefinitionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_api_definition_with_options_async(request, headers, runtime)

    def get_api_mcp_server_with_options(
        self,
        request: main_models.GetApiMcpServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetApiMcpServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApiMcpServer',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/apimcpserver',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApiMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_api_mcp_server_with_options_async(
        self,
        request: main_models.GetApiMcpServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetApiMcpServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApiMcpServer',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/apimcpserver',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApiMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_api_mcp_server(
        self,
        request: main_models.GetApiMcpServerRequest,
    ) -> main_models.GetApiMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_api_mcp_server_with_options(request, headers, runtime)

    async def get_api_mcp_server_async(
        self,
        request: main_models.GetApiMcpServerRequest,
    ) -> main_models.GetApiMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_api_mcp_server_with_options_async(request, headers, runtime)

    def get_api_mcp_server_user_config_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetApiMcpServerUserConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetApiMcpServerUserConfig',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/userconfig/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApiMcpServerUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_api_mcp_server_user_config_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetApiMcpServerUserConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetApiMcpServerUserConfig',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/userconfig/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApiMcpServerUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_api_mcp_server_user_config(self) -> main_models.GetApiMcpServerUserConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_api_mcp_server_user_config_with_options(headers, runtime)

    async def get_api_mcp_server_user_config_async(self) -> main_models.GetApiMcpServerUserConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_api_mcp_server_user_config_with_options_async(headers, runtime)

    def get_error_code_solutions_with_options(
        self,
        request: main_models.GetErrorCodeSolutionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetErrorCodeSolutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.error_code):
            query['errorCode'] = request.error_code
        if not DaraCore.is_null(request.error_message):
            query['errorMessage'] = request.error_message
        if not DaraCore.is_null(request.product):
            query['product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetErrorCodeSolutions',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/getErrorCodeSolutions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetErrorCodeSolutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_error_code_solutions_with_options_async(
        self,
        request: main_models.GetErrorCodeSolutionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetErrorCodeSolutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.error_code):
            query['errorCode'] = request.error_code
        if not DaraCore.is_null(request.error_message):
            query['errorMessage'] = request.error_message
        if not DaraCore.is_null(request.product):
            query['product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetErrorCodeSolutions',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/getErrorCodeSolutions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetErrorCodeSolutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_error_code_solutions(
        self,
        request: main_models.GetErrorCodeSolutionsRequest,
    ) -> main_models.GetErrorCodeSolutionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_error_code_solutions_with_options(request, headers, runtime)

    async def get_error_code_solutions_async(
        self,
        request: main_models.GetErrorCodeSolutionsRequest,
    ) -> main_models.GetErrorCodeSolutionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_error_code_solutions_with_options_async(request, headers, runtime)

    def get_own_request_log_with_options(
        self,
        request: main_models.GetOwnRequestLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOwnRequestLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_request_id):
            query['logRequestId'] = request.log_request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOwnRequestLog',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/getOwnRequestLog',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOwnRequestLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_own_request_log_with_options_async(
        self,
        request: main_models.GetOwnRequestLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOwnRequestLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_request_id):
            query['logRequestId'] = request.log_request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOwnRequestLog',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/getOwnRequestLog',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOwnRequestLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_own_request_log(
        self,
        request: main_models.GetOwnRequestLogRequest,
    ) -> main_models.GetOwnRequestLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_own_request_log_with_options(request, headers, runtime)

    async def get_own_request_log_async(
        self,
        request: main_models.GetOwnRequestLogRequest,
    ) -> main_models.GetOwnRequestLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_own_request_log_with_options_async(request, headers, runtime)

    def get_product_endpoints_with_options(
        self,
        request: main_models.GetProductEndpointsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProductEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product):
            query['product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProductEndpoints',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/product/endpoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProductEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_endpoints_with_options_async(
        self,
        request: main_models.GetProductEndpointsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProductEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product):
            query['product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProductEndpoints',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/product/endpoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProductEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_endpoints(
        self,
        request: main_models.GetProductEndpointsRequest,
    ) -> main_models.GetProductEndpointsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_product_endpoints_with_options(request, headers, runtime)

    async def get_product_endpoints_async(
        self,
        request: main_models.GetProductEndpointsRequest,
    ) -> main_models.GetProductEndpointsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_product_endpoints_with_options_async(request, headers, runtime)

    def get_request_log_with_options(
        self,
        request: main_models.GetRequestLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRequestLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_request_id):
            query['logRequestId'] = request.log_request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRequestLog',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/getRequestLog',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRequestLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_request_log_with_options_async(
        self,
        request: main_models.GetRequestLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRequestLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_request_id):
            query['logRequestId'] = request.log_request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRequestLog',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/getRequestLog',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRequestLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_request_log(
        self,
        request: main_models.GetRequestLogRequest,
    ) -> main_models.GetRequestLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_request_log_with_options(request, headers, runtime)

    async def get_request_log_async(
        self,
        request: main_models.GetRequestLogRequest,
    ) -> main_models.GetRequestLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_request_log_with_options_async(request, headers, runtime)

    def list_api_definitions_with_options(
        self,
        request: main_models.ListApiDefinitionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApiDefinitionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_version):
            query['apiVersion'] = request.api_version
        if not DaraCore.is_null(request.product):
            query['product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiDefinitions',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/api/definitions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiDefinitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_definitions_with_options_async(
        self,
        request: main_models.ListApiDefinitionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApiDefinitionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_version):
            query['apiVersion'] = request.api_version
        if not DaraCore.is_null(request.product):
            query['product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiDefinitions',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/api/definitions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiDefinitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_definitions(
        self,
        request: main_models.ListApiDefinitionsRequest,
    ) -> main_models.ListApiDefinitionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_api_definitions_with_options(request, headers, runtime)

    async def list_api_definitions_async(
        self,
        request: main_models.ListApiDefinitionsRequest,
    ) -> main_models.ListApiDefinitionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_api_definitions_with_options_async(request, headers, runtime)

    def list_api_mcp_server_system_tools_with_options(
        self,
        request: main_models.ListApiMcpServerSystemToolsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApiMcpServerSystemToolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            query['skip'] = request.skip
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiMcpServerSystemTools',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/mcpSystemTools',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiMcpServerSystemToolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_mcp_server_system_tools_with_options_async(
        self,
        request: main_models.ListApiMcpServerSystemToolsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApiMcpServerSystemToolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            query['skip'] = request.skip
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiMcpServerSystemTools',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/mcpSystemTools',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiMcpServerSystemToolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_mcp_server_system_tools(
        self,
        request: main_models.ListApiMcpServerSystemToolsRequest,
    ) -> main_models.ListApiMcpServerSystemToolsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_api_mcp_server_system_tools_with_options(request, headers, runtime)

    async def list_api_mcp_server_system_tools_async(
        self,
        request: main_models.ListApiMcpServerSystemToolsRequest,
    ) -> main_models.ListApiMcpServerSystemToolsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_api_mcp_server_system_tools_with_options_async(request, headers, runtime)

    def list_api_mcp_servers_with_options(
        self,
        request: main_models.ListApiMcpServersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApiMcpServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time):
            query['createTime'] = request.create_time
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            query['skip'] = request.skip
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        if not DaraCore.is_null(request.update_time):
            query['updateTime'] = request.update_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiMcpServers',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/apimcpservers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiMcpServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_mcp_servers_with_options_async(
        self,
        request: main_models.ListApiMcpServersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApiMcpServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time):
            query['createTime'] = request.create_time
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            query['skip'] = request.skip
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        if not DaraCore.is_null(request.update_time):
            query['updateTime'] = request.update_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiMcpServers',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/apimcpservers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiMcpServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_mcp_servers(
        self,
        request: main_models.ListApiMcpServersRequest,
    ) -> main_models.ListApiMcpServersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_api_mcp_servers_with_options(request, headers, runtime)

    async def list_api_mcp_servers_async(
        self,
        request: main_models.ListApiMcpServersRequest,
    ) -> main_models.ListApiMcpServersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_api_mcp_servers_with_options_async(request, headers, runtime)

    def update_api_mcp_server_with_options(
        self,
        request: main_models.UpdateApiMcpServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApiMcpServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        body = {}
        if not DaraCore.is_null(request.additional_api_descriptions):
            body['additionalApiDescriptions'] = request.additional_api_descriptions
        if not DaraCore.is_null(request.apis):
            body['apis'] = request.apis
        if not DaraCore.is_null(request.assume_role_extra_policy):
            body['assumeRoleExtraPolicy'] = request.assume_role_extra_policy
        if not DaraCore.is_null(request.assume_role_name):
            body['assumeRoleName'] = request.assume_role_name
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable_assume_role):
            body['enableAssumeRole'] = request.enable_assume_role
        if not DaraCore.is_null(request.enable_custom_vpc_whitelist):
            body['enableCustomVpcWhitelist'] = request.enable_custom_vpc_whitelist
        if not DaraCore.is_null(request.instructions):
            body['instructions'] = request.instructions
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.oauth_client_id):
            body['oauthClientId'] = request.oauth_client_id
        if not DaraCore.is_null(request.prompts):
            body['prompts'] = request.prompts
        if not DaraCore.is_null(request.public_access):
            body['publicAccess'] = request.public_access
        if not DaraCore.is_null(request.system_tools):
            body['systemTools'] = request.system_tools
        if not DaraCore.is_null(request.terraform_tools):
            body['terraformTools'] = request.terraform_tools
        if not DaraCore.is_null(request.vpc_whitelists):
            body['vpcWhitelists'] = request.vpc_whitelists
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApiMcpServer',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/apimcpserver',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApiMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_api_mcp_server_with_options_async(
        self,
        request: main_models.UpdateApiMcpServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApiMcpServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        body = {}
        if not DaraCore.is_null(request.additional_api_descriptions):
            body['additionalApiDescriptions'] = request.additional_api_descriptions
        if not DaraCore.is_null(request.apis):
            body['apis'] = request.apis
        if not DaraCore.is_null(request.assume_role_extra_policy):
            body['assumeRoleExtraPolicy'] = request.assume_role_extra_policy
        if not DaraCore.is_null(request.assume_role_name):
            body['assumeRoleName'] = request.assume_role_name
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable_assume_role):
            body['enableAssumeRole'] = request.enable_assume_role
        if not DaraCore.is_null(request.enable_custom_vpc_whitelist):
            body['enableCustomVpcWhitelist'] = request.enable_custom_vpc_whitelist
        if not DaraCore.is_null(request.instructions):
            body['instructions'] = request.instructions
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.oauth_client_id):
            body['oauthClientId'] = request.oauth_client_id
        if not DaraCore.is_null(request.prompts):
            body['prompts'] = request.prompts
        if not DaraCore.is_null(request.public_access):
            body['publicAccess'] = request.public_access
        if not DaraCore.is_null(request.system_tools):
            body['systemTools'] = request.system_tools
        if not DaraCore.is_null(request.terraform_tools):
            body['terraformTools'] = request.terraform_tools
        if not DaraCore.is_null(request.vpc_whitelists):
            body['vpcWhitelists'] = request.vpc_whitelists
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApiMcpServer',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/apimcpserver',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApiMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_api_mcp_server(
        self,
        request: main_models.UpdateApiMcpServerRequest,
    ) -> main_models.UpdateApiMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_api_mcp_server_with_options(request, headers, runtime)

    async def update_api_mcp_server_async(
        self,
        request: main_models.UpdateApiMcpServerRequest,
    ) -> main_models.UpdateApiMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_api_mcp_server_with_options_async(request, headers, runtime)

    def update_api_mcp_server_user_config_with_options(
        self,
        request: main_models.UpdateApiMcpServerUserConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApiMcpServerUserConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_public_access):
            body['enablePublicAccess'] = request.enable_public_access
        if not DaraCore.is_null(request.vpc_whitelists):
            body['vpcWhitelists'] = request.vpc_whitelists
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApiMcpServerUserConfig',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/userconfig/update',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApiMcpServerUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_api_mcp_server_user_config_with_options_async(
        self,
        request: main_models.UpdateApiMcpServerUserConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApiMcpServerUserConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_public_access):
            body['enablePublicAccess'] = request.enable_public_access
        if not DaraCore.is_null(request.vpc_whitelists):
            body['vpcWhitelists'] = request.vpc_whitelists
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApiMcpServerUserConfig',
            version = '2024-11-30',
            protocol = 'HTTPS',
            pathname = f'/userconfig/update',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApiMcpServerUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_api_mcp_server_user_config(
        self,
        request: main_models.UpdateApiMcpServerUserConfigRequest,
    ) -> main_models.UpdateApiMcpServerUserConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_api_mcp_server_user_config_with_options(request, headers, runtime)

    async def update_api_mcp_server_user_config_async(
        self,
        request: main_models.UpdateApiMcpServerUserConfigRequest,
    ) -> main_models.UpdateApiMcpServerUserConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_api_mcp_server_user_config_with_options_async(request, headers, runtime)
