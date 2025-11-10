# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_openapiexplorer20241130 import models as open_apiexplorer_20241130_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def api_mcp_server_validate_hcl_with_options(
        self,
        request: open_apiexplorer_20241130_models.ApiMcpServerValidateHclRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.ApiMcpServerValidateHclResponse:
        """
        @summary 验证 Terraform HCL 语法
        
        @param request: ApiMcpServerValidateHclRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApiMcpServerValidateHclResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApiMcpServerValidateHcl',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/terraform/validate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.ApiMcpServerValidateHclResponse(),
            self.call_api(params, req, runtime)
        )

    async def api_mcp_server_validate_hcl_with_options_async(
        self,
        request: open_apiexplorer_20241130_models.ApiMcpServerValidateHclRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.ApiMcpServerValidateHclResponse:
        """
        @summary 验证 Terraform HCL 语法
        
        @param request: ApiMcpServerValidateHclRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApiMcpServerValidateHclResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApiMcpServerValidateHcl',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/terraform/validate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.ApiMcpServerValidateHclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def api_mcp_server_validate_hcl(
        self,
        request: open_apiexplorer_20241130_models.ApiMcpServerValidateHclRequest,
    ) -> open_apiexplorer_20241130_models.ApiMcpServerValidateHclResponse:
        """
        @summary 验证 Terraform HCL 语法
        
        @param request: ApiMcpServerValidateHclRequest
        @return: ApiMcpServerValidateHclResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.api_mcp_server_validate_hcl_with_options(request, headers, runtime)

    async def api_mcp_server_validate_hcl_async(
        self,
        request: open_apiexplorer_20241130_models.ApiMcpServerValidateHclRequest,
    ) -> open_apiexplorer_20241130_models.ApiMcpServerValidateHclResponse:
        """
        @summary 验证 Terraform HCL 语法
        
        @param request: ApiMcpServerValidateHclRequest
        @return: ApiMcpServerValidateHclResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.api_mcp_server_validate_hcl_with_options_async(request, headers, runtime)

    def create_api_mcp_server_with_options(
        self,
        request: open_apiexplorer_20241130_models.CreateApiMcpServerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.CreateApiMcpServerResponse:
        """
        @summary 创建ApiMcpServer
        
        @param request: CreateApiMcpServerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApiMcpServerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.additional_api_descriptions):
            body['additionalApiDescriptions'] = request.additional_api_descriptions
        if not UtilClient.is_unset(request.apis):
            body['apis'] = request.apis
        if not UtilClient.is_unset(request.assume_role_extra_policy):
            body['assumeRoleExtraPolicy'] = request.assume_role_extra_policy
        if not UtilClient.is_unset(request.assume_role_name):
            body['assumeRoleName'] = request.assume_role_name
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enable_assume_role):
            body['enableAssumeRole'] = request.enable_assume_role
        if not UtilClient.is_unset(request.instructions):
            body['instructions'] = request.instructions
        if not UtilClient.is_unset(request.language):
            body['language'] = request.language
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.oauth_client_id):
            body['oauthClientId'] = request.oauth_client_id
        if not UtilClient.is_unset(request.prompts):
            body['prompts'] = request.prompts
        if not UtilClient.is_unset(request.system_tools):
            body['systemTools'] = request.system_tools
        if not UtilClient.is_unset(request.terraform_tools):
            body['terraformTools'] = request.terraform_tools
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApiMcpServer',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/apimcpserver',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.CreateApiMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_mcp_server_with_options_async(
        self,
        request: open_apiexplorer_20241130_models.CreateApiMcpServerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.CreateApiMcpServerResponse:
        """
        @summary 创建ApiMcpServer
        
        @param request: CreateApiMcpServerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApiMcpServerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.additional_api_descriptions):
            body['additionalApiDescriptions'] = request.additional_api_descriptions
        if not UtilClient.is_unset(request.apis):
            body['apis'] = request.apis
        if not UtilClient.is_unset(request.assume_role_extra_policy):
            body['assumeRoleExtraPolicy'] = request.assume_role_extra_policy
        if not UtilClient.is_unset(request.assume_role_name):
            body['assumeRoleName'] = request.assume_role_name
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enable_assume_role):
            body['enableAssumeRole'] = request.enable_assume_role
        if not UtilClient.is_unset(request.instructions):
            body['instructions'] = request.instructions
        if not UtilClient.is_unset(request.language):
            body['language'] = request.language
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.oauth_client_id):
            body['oauthClientId'] = request.oauth_client_id
        if not UtilClient.is_unset(request.prompts):
            body['prompts'] = request.prompts
        if not UtilClient.is_unset(request.system_tools):
            body['systemTools'] = request.system_tools
        if not UtilClient.is_unset(request.terraform_tools):
            body['terraformTools'] = request.terraform_tools
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApiMcpServer',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/apimcpserver',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.CreateApiMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_mcp_server(
        self,
        request: open_apiexplorer_20241130_models.CreateApiMcpServerRequest,
    ) -> open_apiexplorer_20241130_models.CreateApiMcpServerResponse:
        """
        @summary 创建ApiMcpServer
        
        @param request: CreateApiMcpServerRequest
        @return: CreateApiMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_api_mcp_server_with_options(request, headers, runtime)

    async def create_api_mcp_server_async(
        self,
        request: open_apiexplorer_20241130_models.CreateApiMcpServerRequest,
    ) -> open_apiexplorer_20241130_models.CreateApiMcpServerResponse:
        """
        @summary 创建ApiMcpServer
        
        @param request: CreateApiMcpServerRequest
        @return: CreateApiMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_api_mcp_server_with_options_async(request, headers, runtime)

    def delete_api_mcp_server_with_options(
        self,
        request: open_apiexplorer_20241130_models.DeleteApiMcpServerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.DeleteApiMcpServerResponse:
        """
        @summary 删除ApiMcpServer
        
        @param request: DeleteApiMcpServerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApiMcpServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApiMcpServer',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/apimcpserver',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.DeleteApiMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_mcp_server_with_options_async(
        self,
        request: open_apiexplorer_20241130_models.DeleteApiMcpServerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.DeleteApiMcpServerResponse:
        """
        @summary 删除ApiMcpServer
        
        @param request: DeleteApiMcpServerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApiMcpServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApiMcpServer',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/apimcpserver',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.DeleteApiMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_mcp_server(
        self,
        request: open_apiexplorer_20241130_models.DeleteApiMcpServerRequest,
    ) -> open_apiexplorer_20241130_models.DeleteApiMcpServerResponse:
        """
        @summary 删除ApiMcpServer
        
        @param request: DeleteApiMcpServerRequest
        @return: DeleteApiMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_api_mcp_server_with_options(request, headers, runtime)

    async def delete_api_mcp_server_async(
        self,
        request: open_apiexplorer_20241130_models.DeleteApiMcpServerRequest,
    ) -> open_apiexplorer_20241130_models.DeleteApiMcpServerResponse:
        """
        @summary 删除ApiMcpServer
        
        @param request: DeleteApiMcpServerRequest
        @return: DeleteApiMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_api_mcp_server_with_options_async(request, headers, runtime)

    def generate_clicommand_with_options(
        self,
        tmp_req: open_apiexplorer_20241130_models.GenerateCLICommandRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GenerateCLICommandResponse:
        """
        @summary 动态生成Aliyun CLI命令
        
        @param tmp_req: GenerateCLICommandRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCLICommandResponse
        """
        UtilClient.validate_model(tmp_req)
        request = open_apiexplorer_20241130_models.GenerateCLICommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.api_params):
            request.api_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.api_params, 'apiParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.api):
            body['api'] = request.api
        if not UtilClient.is_unset(request.api_params_shrink):
            body['apiParams'] = request.api_params_shrink
        if not UtilClient.is_unset(request.api_version):
            body['apiVersion'] = request.api_version
        if not UtilClient.is_unset(request.product):
            body['product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            body['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateCLICommand',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/api/cli/makeCode',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.GenerateCLICommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_clicommand_with_options_async(
        self,
        tmp_req: open_apiexplorer_20241130_models.GenerateCLICommandRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GenerateCLICommandResponse:
        """
        @summary 动态生成Aliyun CLI命令
        
        @param tmp_req: GenerateCLICommandRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCLICommandResponse
        """
        UtilClient.validate_model(tmp_req)
        request = open_apiexplorer_20241130_models.GenerateCLICommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.api_params):
            request.api_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.api_params, 'apiParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.api):
            body['api'] = request.api
        if not UtilClient.is_unset(request.api_params_shrink):
            body['apiParams'] = request.api_params_shrink
        if not UtilClient.is_unset(request.api_version):
            body['apiVersion'] = request.api_version
        if not UtilClient.is_unset(request.product):
            body['product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            body['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateCLICommand',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/api/cli/makeCode',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.GenerateCLICommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_clicommand(
        self,
        request: open_apiexplorer_20241130_models.GenerateCLICommandRequest,
    ) -> open_apiexplorer_20241130_models.GenerateCLICommandResponse:
        """
        @summary 动态生成Aliyun CLI命令
        
        @param request: GenerateCLICommandRequest
        @return: GenerateCLICommandResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_clicommand_with_options(request, headers, runtime)

    async def generate_clicommand_async(
        self,
        request: open_apiexplorer_20241130_models.GenerateCLICommandRequest,
    ) -> open_apiexplorer_20241130_models.GenerateCLICommandResponse:
        """
        @summary 动态生成Aliyun CLI命令
        
        @param request: GenerateCLICommandRequest
        @return: GenerateCLICommandResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_clicommand_with_options_async(request, headers, runtime)

    def get_api_definition_with_options(
        self,
        request: open_apiexplorer_20241130_models.GetApiDefinitionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetApiDefinitionResponse:
        """
        @summary 获取产品相关接口的开放元数据
        
        @param request: GetApiDefinitionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApiDefinitionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api):
            query['api'] = request.api
        if not UtilClient.is_unset(request.api_version):
            query['apiVersion'] = request.api_version
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApiDefinition',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/api/definition',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.GetApiDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_api_definition_with_options_async(
        self,
        request: open_apiexplorer_20241130_models.GetApiDefinitionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetApiDefinitionResponse:
        """
        @summary 获取产品相关接口的开放元数据
        
        @param request: GetApiDefinitionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApiDefinitionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api):
            query['api'] = request.api
        if not UtilClient.is_unset(request.api_version):
            query['apiVersion'] = request.api_version
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApiDefinition',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/api/definition',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.GetApiDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_api_definition(
        self,
        request: open_apiexplorer_20241130_models.GetApiDefinitionRequest,
    ) -> open_apiexplorer_20241130_models.GetApiDefinitionResponse:
        """
        @summary 获取产品相关接口的开放元数据
        
        @param request: GetApiDefinitionRequest
        @return: GetApiDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_api_definition_with_options(request, headers, runtime)

    async def get_api_definition_async(
        self,
        request: open_apiexplorer_20241130_models.GetApiDefinitionRequest,
    ) -> open_apiexplorer_20241130_models.GetApiDefinitionResponse:
        """
        @summary 获取产品相关接口的开放元数据
        
        @param request: GetApiDefinitionRequest
        @return: GetApiDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_api_definition_with_options_async(request, headers, runtime)

    def get_api_mcp_server_with_options(
        self,
        request: open_apiexplorer_20241130_models.GetApiMcpServerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetApiMcpServerResponse:
        """
        @summary 查询 ApiMcpServer
        
        @param request: GetApiMcpServerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApiMcpServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApiMcpServer',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/apimcpserver',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.GetApiMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_api_mcp_server_with_options_async(
        self,
        request: open_apiexplorer_20241130_models.GetApiMcpServerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetApiMcpServerResponse:
        """
        @summary 查询 ApiMcpServer
        
        @param request: GetApiMcpServerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApiMcpServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApiMcpServer',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/apimcpserver',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.GetApiMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_api_mcp_server(
        self,
        request: open_apiexplorer_20241130_models.GetApiMcpServerRequest,
    ) -> open_apiexplorer_20241130_models.GetApiMcpServerResponse:
        """
        @summary 查询 ApiMcpServer
        
        @param request: GetApiMcpServerRequest
        @return: GetApiMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_api_mcp_server_with_options(request, headers, runtime)

    async def get_api_mcp_server_async(
        self,
        request: open_apiexplorer_20241130_models.GetApiMcpServerRequest,
    ) -> open_apiexplorer_20241130_models.GetApiMcpServerResponse:
        """
        @summary 查询 ApiMcpServer
        
        @param request: GetApiMcpServerRequest
        @return: GetApiMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_api_mcp_server_with_options_async(request, headers, runtime)

    def get_error_code_solutions_with_options(
        self,
        request: open_apiexplorer_20241130_models.GetErrorCodeSolutionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetErrorCodeSolutionsResponse:
        """
        @summary Queries an error solution by error code.
        
        @description You can call this API operation to query public information instead of special information, such as the account ownership. Permissions on this API operation cannot be granted to other members.
        
        @param request: GetErrorCodeSolutionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErrorCodeSolutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.error_code):
            query['errorCode'] = request.error_code
        if not UtilClient.is_unset(request.error_message):
            query['errorMessage'] = request.error_message
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetErrorCodeSolutions',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/getErrorCodeSolutions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.GetErrorCodeSolutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_error_code_solutions_with_options_async(
        self,
        request: open_apiexplorer_20241130_models.GetErrorCodeSolutionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetErrorCodeSolutionsResponse:
        """
        @summary Queries an error solution by error code.
        
        @description You can call this API operation to query public information instead of special information, such as the account ownership. Permissions on this API operation cannot be granted to other members.
        
        @param request: GetErrorCodeSolutionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErrorCodeSolutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.error_code):
            query['errorCode'] = request.error_code
        if not UtilClient.is_unset(request.error_message):
            query['errorMessage'] = request.error_message
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetErrorCodeSolutions',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/getErrorCodeSolutions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.GetErrorCodeSolutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_error_code_solutions(
        self,
        request: open_apiexplorer_20241130_models.GetErrorCodeSolutionsRequest,
    ) -> open_apiexplorer_20241130_models.GetErrorCodeSolutionsResponse:
        """
        @summary Queries an error solution by error code.
        
        @description You can call this API operation to query public information instead of special information, such as the account ownership. Permissions on this API operation cannot be granted to other members.
        
        @param request: GetErrorCodeSolutionsRequest
        @return: GetErrorCodeSolutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_error_code_solutions_with_options(request, headers, runtime)

    async def get_error_code_solutions_async(
        self,
        request: open_apiexplorer_20241130_models.GetErrorCodeSolutionsRequest,
    ) -> open_apiexplorer_20241130_models.GetErrorCodeSolutionsResponse:
        """
        @summary Queries an error solution by error code.
        
        @description You can call this API operation to query public information instead of special information, such as the account ownership. Permissions on this API operation cannot be granted to other members.
        
        @param request: GetErrorCodeSolutionsRequest
        @return: GetErrorCodeSolutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_error_code_solutions_with_options_async(request, headers, runtime)

    def get_own_request_log_with_options(
        self,
        request: open_apiexplorer_20241130_models.GetOwnRequestLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetOwnRequestLogResponse:
        """
        @summary Queries the log of an API call performed by using the current account based on the returned request ID of the API to troubleshoot issues.
        
        @description Permissions on this API cannot be granted to other members.
        
        @param request: GetOwnRequestLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOwnRequestLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_request_id):
            query['logRequestId'] = request.log_request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOwnRequestLog',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/getOwnRequestLog',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.GetOwnRequestLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_own_request_log_with_options_async(
        self,
        request: open_apiexplorer_20241130_models.GetOwnRequestLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetOwnRequestLogResponse:
        """
        @summary Queries the log of an API call performed by using the current account based on the returned request ID of the API to troubleshoot issues.
        
        @description Permissions on this API cannot be granted to other members.
        
        @param request: GetOwnRequestLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOwnRequestLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_request_id):
            query['logRequestId'] = request.log_request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOwnRequestLog',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/getOwnRequestLog',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.GetOwnRequestLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_own_request_log(
        self,
        request: open_apiexplorer_20241130_models.GetOwnRequestLogRequest,
    ) -> open_apiexplorer_20241130_models.GetOwnRequestLogResponse:
        """
        @summary Queries the log of an API call performed by using the current account based on the returned request ID of the API to troubleshoot issues.
        
        @description Permissions on this API cannot be granted to other members.
        
        @param request: GetOwnRequestLogRequest
        @return: GetOwnRequestLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_own_request_log_with_options(request, headers, runtime)

    async def get_own_request_log_async(
        self,
        request: open_apiexplorer_20241130_models.GetOwnRequestLogRequest,
    ) -> open_apiexplorer_20241130_models.GetOwnRequestLogResponse:
        """
        @summary Queries the log of an API call performed by using the current account based on the returned request ID of the API to troubleshoot issues.
        
        @description Permissions on this API cannot be granted to other members.
        
        @param request: GetOwnRequestLogRequest
        @return: GetOwnRequestLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_own_request_log_with_options_async(request, headers, runtime)

    def get_product_endpoints_with_options(
        self,
        request: open_apiexplorer_20241130_models.GetProductEndpointsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetProductEndpointsResponse:
        """
        @summary 获取产品的接入点信息
        
        @param request: GetProductEndpointsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProductEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductEndpoints',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/product/endpoints',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.GetProductEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_endpoints_with_options_async(
        self,
        request: open_apiexplorer_20241130_models.GetProductEndpointsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetProductEndpointsResponse:
        """
        @summary 获取产品的接入点信息
        
        @param request: GetProductEndpointsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProductEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductEndpoints',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/product/endpoints',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.GetProductEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_endpoints(
        self,
        request: open_apiexplorer_20241130_models.GetProductEndpointsRequest,
    ) -> open_apiexplorer_20241130_models.GetProductEndpointsResponse:
        """
        @summary 获取产品的接入点信息
        
        @param request: GetProductEndpointsRequest
        @return: GetProductEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_endpoints_with_options(request, headers, runtime)

    async def get_product_endpoints_async(
        self,
        request: open_apiexplorer_20241130_models.GetProductEndpointsRequest,
    ) -> open_apiexplorer_20241130_models.GetProductEndpointsResponse:
        """
        @summary 获取产品的接入点信息
        
        @param request: GetProductEndpointsRequest
        @return: GetProductEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_product_endpoints_with_options_async(request, headers, runtime)

    def get_request_log_with_options(
        self,
        request: open_apiexplorer_20241130_models.GetRequestLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetRequestLogResponse:
        """
        @summary Queries the log of an API call based on the returned request ID of the API to troubleshoot issues.
        
        @description You can grant permissions to a Resource Access Management (RAM) user or assume a role to query the log of an API call across RAM users or Alibaba Cloud accounts. For more information, see [Grant permissions to troubleshoot API errors across accounts](https://help.aliyun.com/document_detail/2868101.html).
        
        @param request: GetRequestLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRequestLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_request_id):
            query['logRequestId'] = request.log_request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRequestLog',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/getRequestLog',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.GetRequestLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_request_log_with_options_async(
        self,
        request: open_apiexplorer_20241130_models.GetRequestLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.GetRequestLogResponse:
        """
        @summary Queries the log of an API call based on the returned request ID of the API to troubleshoot issues.
        
        @description You can grant permissions to a Resource Access Management (RAM) user or assume a role to query the log of an API call across RAM users or Alibaba Cloud accounts. For more information, see [Grant permissions to troubleshoot API errors across accounts](https://help.aliyun.com/document_detail/2868101.html).
        
        @param request: GetRequestLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRequestLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_request_id):
            query['logRequestId'] = request.log_request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRequestLog',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/getRequestLog',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.GetRequestLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_request_log(
        self,
        request: open_apiexplorer_20241130_models.GetRequestLogRequest,
    ) -> open_apiexplorer_20241130_models.GetRequestLogResponse:
        """
        @summary Queries the log of an API call based on the returned request ID of the API to troubleshoot issues.
        
        @description You can grant permissions to a Resource Access Management (RAM) user or assume a role to query the log of an API call across RAM users or Alibaba Cloud accounts. For more information, see [Grant permissions to troubleshoot API errors across accounts](https://help.aliyun.com/document_detail/2868101.html).
        
        @param request: GetRequestLogRequest
        @return: GetRequestLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_request_log_with_options(request, headers, runtime)

    async def get_request_log_async(
        self,
        request: open_apiexplorer_20241130_models.GetRequestLogRequest,
    ) -> open_apiexplorer_20241130_models.GetRequestLogResponse:
        """
        @summary Queries the log of an API call based on the returned request ID of the API to troubleshoot issues.
        
        @description You can grant permissions to a Resource Access Management (RAM) user or assume a role to query the log of an API call across RAM users or Alibaba Cloud accounts. For more information, see [Grant permissions to troubleshoot API errors across accounts](https://help.aliyun.com/document_detail/2868101.html).
        
        @param request: GetRequestLogRequest
        @return: GetRequestLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_request_log_with_options_async(request, headers, runtime)

    def list_api_definitions_with_options(
        self,
        request: open_apiexplorer_20241130_models.ListApiDefinitionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.ListApiDefinitionsResponse:
        """
        @summary 获取产品的开放元数据
        
        @param request: ListApiDefinitionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApiDefinitionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['apiVersion'] = request.api_version
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApiDefinitions',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/api/definitions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.ListApiDefinitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_definitions_with_options_async(
        self,
        request: open_apiexplorer_20241130_models.ListApiDefinitionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.ListApiDefinitionsResponse:
        """
        @summary 获取产品的开放元数据
        
        @param request: ListApiDefinitionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApiDefinitionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['apiVersion'] = request.api_version
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApiDefinitions',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/api/definitions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.ListApiDefinitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_definitions(
        self,
        request: open_apiexplorer_20241130_models.ListApiDefinitionsRequest,
    ) -> open_apiexplorer_20241130_models.ListApiDefinitionsResponse:
        """
        @summary 获取产品的开放元数据
        
        @param request: ListApiDefinitionsRequest
        @return: ListApiDefinitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_api_definitions_with_options(request, headers, runtime)

    async def list_api_definitions_async(
        self,
        request: open_apiexplorer_20241130_models.ListApiDefinitionsRequest,
    ) -> open_apiexplorer_20241130_models.ListApiDefinitionsResponse:
        """
        @summary 获取产品的开放元数据
        
        @param request: ListApiDefinitionsRequest
        @return: ListApiDefinitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_api_definitions_with_options_async(request, headers, runtime)

    def list_api_mcp_server_system_tools_with_options(
        self,
        request: open_apiexplorer_20241130_models.ListApiMcpServerSystemToolsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.ListApiMcpServerSystemToolsResponse:
        """
        @summary 查询系统工具列表
        
        @param request: ListApiMcpServerSystemToolsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApiMcpServerSystemToolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.skip):
            query['skip'] = request.skip
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApiMcpServerSystemTools',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/mcpSystemTools',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.ListApiMcpServerSystemToolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_mcp_server_system_tools_with_options_async(
        self,
        request: open_apiexplorer_20241130_models.ListApiMcpServerSystemToolsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.ListApiMcpServerSystemToolsResponse:
        """
        @summary 查询系统工具列表
        
        @param request: ListApiMcpServerSystemToolsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApiMcpServerSystemToolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.skip):
            query['skip'] = request.skip
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApiMcpServerSystemTools',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/mcpSystemTools',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.ListApiMcpServerSystemToolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_mcp_server_system_tools(
        self,
        request: open_apiexplorer_20241130_models.ListApiMcpServerSystemToolsRequest,
    ) -> open_apiexplorer_20241130_models.ListApiMcpServerSystemToolsResponse:
        """
        @summary 查询系统工具列表
        
        @param request: ListApiMcpServerSystemToolsRequest
        @return: ListApiMcpServerSystemToolsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_api_mcp_server_system_tools_with_options(request, headers, runtime)

    async def list_api_mcp_server_system_tools_async(
        self,
        request: open_apiexplorer_20241130_models.ListApiMcpServerSystemToolsRequest,
    ) -> open_apiexplorer_20241130_models.ListApiMcpServerSystemToolsResponse:
        """
        @summary 查询系统工具列表
        
        @param request: ListApiMcpServerSystemToolsRequest
        @return: ListApiMcpServerSystemToolsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_api_mcp_server_system_tools_with_options_async(request, headers, runtime)

    def list_api_mcp_servers_with_options(
        self,
        request: open_apiexplorer_20241130_models.ListApiMcpServersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.ListApiMcpServersResponse:
        """
        @summary 列出资源ApiMcpServer
        
        @param request: ListApiMcpServersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApiMcpServersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time):
            query['createTime'] = request.create_time
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.language):
            query['language'] = request.language
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.skip):
            query['skip'] = request.skip
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        if not UtilClient.is_unset(request.update_time):
            query['updateTime'] = request.update_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApiMcpServers',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/apimcpservers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.ListApiMcpServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_mcp_servers_with_options_async(
        self,
        request: open_apiexplorer_20241130_models.ListApiMcpServersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.ListApiMcpServersResponse:
        """
        @summary 列出资源ApiMcpServer
        
        @param request: ListApiMcpServersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApiMcpServersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time):
            query['createTime'] = request.create_time
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.language):
            query['language'] = request.language
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.skip):
            query['skip'] = request.skip
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        if not UtilClient.is_unset(request.update_time):
            query['updateTime'] = request.update_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApiMcpServers',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/apimcpservers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.ListApiMcpServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_mcp_servers(
        self,
        request: open_apiexplorer_20241130_models.ListApiMcpServersRequest,
    ) -> open_apiexplorer_20241130_models.ListApiMcpServersResponse:
        """
        @summary 列出资源ApiMcpServer
        
        @param request: ListApiMcpServersRequest
        @return: ListApiMcpServersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_api_mcp_servers_with_options(request, headers, runtime)

    async def list_api_mcp_servers_async(
        self,
        request: open_apiexplorer_20241130_models.ListApiMcpServersRequest,
    ) -> open_apiexplorer_20241130_models.ListApiMcpServersResponse:
        """
        @summary 列出资源ApiMcpServer
        
        @param request: ListApiMcpServersRequest
        @return: ListApiMcpServersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_api_mcp_servers_with_options_async(request, headers, runtime)

    def update_api_mcp_server_with_options(
        self,
        request: open_apiexplorer_20241130_models.UpdateApiMcpServerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.UpdateApiMcpServerResponse:
        """
        @summary 更新UpdateApiMcpServer
        
        @param request: UpdateApiMcpServerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApiMcpServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        body = {}
        if not UtilClient.is_unset(request.additional_api_descriptions):
            body['additionalApiDescriptions'] = request.additional_api_descriptions
        if not UtilClient.is_unset(request.apis):
            body['apis'] = request.apis
        if not UtilClient.is_unset(request.assume_role_extra_policy):
            body['assumeRoleExtraPolicy'] = request.assume_role_extra_policy
        if not UtilClient.is_unset(request.assume_role_name):
            body['assumeRoleName'] = request.assume_role_name
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enable_assume_role):
            body['enableAssumeRole'] = request.enable_assume_role
        if not UtilClient.is_unset(request.instructions):
            body['instructions'] = request.instructions
        if not UtilClient.is_unset(request.language):
            body['language'] = request.language
        if not UtilClient.is_unset(request.oauth_client_id):
            body['oauthClientId'] = request.oauth_client_id
        if not UtilClient.is_unset(request.prompts):
            body['prompts'] = request.prompts
        if not UtilClient.is_unset(request.system_tools):
            body['systemTools'] = request.system_tools
        if not UtilClient.is_unset(request.terraform_tools):
            body['terraformTools'] = request.terraform_tools
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateApiMcpServer',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/apimcpserver',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.UpdateApiMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_api_mcp_server_with_options_async(
        self,
        request: open_apiexplorer_20241130_models.UpdateApiMcpServerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_apiexplorer_20241130_models.UpdateApiMcpServerResponse:
        """
        @summary 更新UpdateApiMcpServer
        
        @param request: UpdateApiMcpServerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApiMcpServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        body = {}
        if not UtilClient.is_unset(request.additional_api_descriptions):
            body['additionalApiDescriptions'] = request.additional_api_descriptions
        if not UtilClient.is_unset(request.apis):
            body['apis'] = request.apis
        if not UtilClient.is_unset(request.assume_role_extra_policy):
            body['assumeRoleExtraPolicy'] = request.assume_role_extra_policy
        if not UtilClient.is_unset(request.assume_role_name):
            body['assumeRoleName'] = request.assume_role_name
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enable_assume_role):
            body['enableAssumeRole'] = request.enable_assume_role
        if not UtilClient.is_unset(request.instructions):
            body['instructions'] = request.instructions
        if not UtilClient.is_unset(request.language):
            body['language'] = request.language
        if not UtilClient.is_unset(request.oauth_client_id):
            body['oauthClientId'] = request.oauth_client_id
        if not UtilClient.is_unset(request.prompts):
            body['prompts'] = request.prompts
        if not UtilClient.is_unset(request.system_tools):
            body['systemTools'] = request.system_tools
        if not UtilClient.is_unset(request.terraform_tools):
            body['terraformTools'] = request.terraform_tools
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateApiMcpServer',
            version='2024-11-30',
            protocol='HTTPS',
            pathname=f'/apimcpserver',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_apiexplorer_20241130_models.UpdateApiMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_api_mcp_server(
        self,
        request: open_apiexplorer_20241130_models.UpdateApiMcpServerRequest,
    ) -> open_apiexplorer_20241130_models.UpdateApiMcpServerResponse:
        """
        @summary 更新UpdateApiMcpServer
        
        @param request: UpdateApiMcpServerRequest
        @return: UpdateApiMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_api_mcp_server_with_options(request, headers, runtime)

    async def update_api_mcp_server_async(
        self,
        request: open_apiexplorer_20241130_models.UpdateApiMcpServerRequest,
    ) -> open_apiexplorer_20241130_models.UpdateApiMcpServerResponse:
        """
        @summary 更新UpdateApiMcpServer
        
        @param request: UpdateApiMcpServerRequest
        @return: UpdateApiMcpServerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_api_mcp_server_with_options_async(request, headers, runtime)
