# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sfmmultimodalapp20250909 import models as sfm_multi_modal_app_20250909_models
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
        self._endpoint = self.get_endpoint('sfmmultimodalapp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_command_with_options(
        self,
        tmp_req: sfm_multi_modal_app_20250909_models.CreateCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.CreateCommandResponse:
        """
        @summary 指令创建
        
        @param tmp_req: CreateCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCommandResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sfm_multi_modal_app_20250909_models.CreateCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tool_examples):
            request.tool_examples_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tool_examples, 'ToolExamples', 'json')
        if not UtilClient.is_unset(tmp_req.tool_params):
            request.tool_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tool_params, 'ToolParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.tool_description):
            query['ToolDescription'] = request.tool_description
        if not UtilClient.is_unset(request.tool_examples_shrink):
            query['ToolExamples'] = request.tool_examples_shrink
        if not UtilClient.is_unset(request.tool_name):
            query['ToolName'] = request.tool_name
        if not UtilClient.is_unset(request.tool_params_shrink):
            query['ToolParams'] = request.tool_params_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCommand',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.CreateCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_command_with_options_async(
        self,
        tmp_req: sfm_multi_modal_app_20250909_models.CreateCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.CreateCommandResponse:
        """
        @summary 指令创建
        
        @param tmp_req: CreateCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCommandResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sfm_multi_modal_app_20250909_models.CreateCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tool_examples):
            request.tool_examples_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tool_examples, 'ToolExamples', 'json')
        if not UtilClient.is_unset(tmp_req.tool_params):
            request.tool_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tool_params, 'ToolParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.tool_description):
            query['ToolDescription'] = request.tool_description
        if not UtilClient.is_unset(request.tool_examples_shrink):
            query['ToolExamples'] = request.tool_examples_shrink
        if not UtilClient.is_unset(request.tool_name):
            query['ToolName'] = request.tool_name
        if not UtilClient.is_unset(request.tool_params_shrink):
            query['ToolParams'] = request.tool_params_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCommand',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.CreateCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_command(
        self,
        request: sfm_multi_modal_app_20250909_models.CreateCommandRequest,
    ) -> sfm_multi_modal_app_20250909_models.CreateCommandResponse:
        """
        @summary 指令创建
        
        @param request: CreateCommandRequest
        @return: CreateCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_command_with_options(request, runtime)

    async def create_command_async(
        self,
        request: sfm_multi_modal_app_20250909_models.CreateCommandRequest,
    ) -> sfm_multi_modal_app_20250909_models.CreateCommandResponse:
        """
        @summary 指令创建
        
        @param request: CreateCommandRequest
        @return: CreateCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_command_with_options_async(request, runtime)

    def create_mm_app_with_options(
        self,
        tmp_req: sfm_multi_modal_app_20250909_models.CreateMmAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.CreateMmAppResponse:
        """
        @summary 创建多模态应用
        
        @param tmp_req: CreateMmAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMmAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sfm_multi_modal_app_20250909_models.CreateMmAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.binding_config):
            request.binding_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.binding_config, 'BindingConfig', 'json')
        if not UtilClient.is_unset(tmp_req.conversation_config):
            request.conversation_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.conversation_config, 'ConversationConfig', 'json')
        if not UtilClient.is_unset(tmp_req.model_config):
            request.model_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model_config, 'ModelConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.binding_config_shrink):
            query['BindingConfig'] = request.binding_config_shrink
        if not UtilClient.is_unset(request.conversation_config_shrink):
            query['ConversationConfig'] = request.conversation_config_shrink
        if not UtilClient.is_unset(request.model_config_shrink):
            query['ModelConfig'] = request.model_config_shrink
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMmApp',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.CreateMmAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mm_app_with_options_async(
        self,
        tmp_req: sfm_multi_modal_app_20250909_models.CreateMmAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.CreateMmAppResponse:
        """
        @summary 创建多模态应用
        
        @param tmp_req: CreateMmAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMmAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sfm_multi_modal_app_20250909_models.CreateMmAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.binding_config):
            request.binding_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.binding_config, 'BindingConfig', 'json')
        if not UtilClient.is_unset(tmp_req.conversation_config):
            request.conversation_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.conversation_config, 'ConversationConfig', 'json')
        if not UtilClient.is_unset(tmp_req.model_config):
            request.model_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model_config, 'ModelConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.binding_config_shrink):
            query['BindingConfig'] = request.binding_config_shrink
        if not UtilClient.is_unset(request.conversation_config_shrink):
            query['ConversationConfig'] = request.conversation_config_shrink
        if not UtilClient.is_unset(request.model_config_shrink):
            query['ModelConfig'] = request.model_config_shrink
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMmApp',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.CreateMmAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mm_app(
        self,
        request: sfm_multi_modal_app_20250909_models.CreateMmAppRequest,
    ) -> sfm_multi_modal_app_20250909_models.CreateMmAppResponse:
        """
        @summary 创建多模态应用
        
        @param request: CreateMmAppRequest
        @return: CreateMmAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mm_app_with_options(request, runtime)

    async def create_mm_app_async(
        self,
        request: sfm_multi_modal_app_20250909_models.CreateMmAppRequest,
    ) -> sfm_multi_modal_app_20250909_models.CreateMmAppResponse:
        """
        @summary 创建多模态应用
        
        @param request: CreateMmAppRequest
        @return: CreateMmAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mm_app_with_options_async(request, runtime)

    def delete_command_with_options(
        self,
        request: sfm_multi_modal_app_20250909_models.DeleteCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.DeleteCommandResponse:
        """
        @summary 删除指令
        
        @param request: DeleteCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCommandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.tool_id):
            query['ToolId'] = request.tool_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCommand',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.DeleteCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_command_with_options_async(
        self,
        request: sfm_multi_modal_app_20250909_models.DeleteCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.DeleteCommandResponse:
        """
        @summary 删除指令
        
        @param request: DeleteCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCommandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.tool_id):
            query['ToolId'] = request.tool_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCommand',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.DeleteCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_command(
        self,
        request: sfm_multi_modal_app_20250909_models.DeleteCommandRequest,
    ) -> sfm_multi_modal_app_20250909_models.DeleteCommandResponse:
        """
        @summary 删除指令
        
        @param request: DeleteCommandRequest
        @return: DeleteCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_command_with_options(request, runtime)

    async def delete_command_async(
        self,
        request: sfm_multi_modal_app_20250909_models.DeleteCommandRequest,
    ) -> sfm_multi_modal_app_20250909_models.DeleteCommandResponse:
        """
        @summary 删除指令
        
        @param request: DeleteCommandRequest
        @return: DeleteCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_command_with_options_async(request, runtime)

    def delete_mm_app_with_options(
        self,
        request: sfm_multi_modal_app_20250909_models.DeleteMmAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.DeleteMmAppResponse:
        """
        @summary 删除多模态应用
        
        @param request: DeleteMmAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMmAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMmApp',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.DeleteMmAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mm_app_with_options_async(
        self,
        request: sfm_multi_modal_app_20250909_models.DeleteMmAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.DeleteMmAppResponse:
        """
        @summary 删除多模态应用
        
        @param request: DeleteMmAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMmAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMmApp',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.DeleteMmAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mm_app(
        self,
        request: sfm_multi_modal_app_20250909_models.DeleteMmAppRequest,
    ) -> sfm_multi_modal_app_20250909_models.DeleteMmAppResponse:
        """
        @summary 删除多模态应用
        
        @param request: DeleteMmAppRequest
        @return: DeleteMmAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mm_app_with_options(request, runtime)

    async def delete_mm_app_async(
        self,
        request: sfm_multi_modal_app_20250909_models.DeleteMmAppRequest,
    ) -> sfm_multi_modal_app_20250909_models.DeleteMmAppResponse:
        """
        @summary 删除多模态应用
        
        @param request: DeleteMmAppRequest
        @return: DeleteMmAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_mm_app_with_options_async(request, runtime)

    def describe_command_with_options(
        self,
        request: sfm_multi_modal_app_20250909_models.DescribeCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.DescribeCommandResponse:
        """
        @summary 指令详情
        
        @param request: DescribeCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCommandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.tool_id):
            query['ToolId'] = request.tool_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCommand',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.DescribeCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_command_with_options_async(
        self,
        request: sfm_multi_modal_app_20250909_models.DescribeCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.DescribeCommandResponse:
        """
        @summary 指令详情
        
        @param request: DescribeCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCommandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.tool_id):
            query['ToolId'] = request.tool_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCommand',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.DescribeCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_command(
        self,
        request: sfm_multi_modal_app_20250909_models.DescribeCommandRequest,
    ) -> sfm_multi_modal_app_20250909_models.DescribeCommandResponse:
        """
        @summary 指令详情
        
        @param request: DescribeCommandRequest
        @return: DescribeCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_command_with_options(request, runtime)

    async def describe_command_async(
        self,
        request: sfm_multi_modal_app_20250909_models.DescribeCommandRequest,
    ) -> sfm_multi_modal_app_20250909_models.DescribeCommandResponse:
        """
        @summary 指令详情
        
        @param request: DescribeCommandRequest
        @return: DescribeCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_command_with_options_async(request, runtime)

    def describe_mm_app_with_options(
        self,
        request: sfm_multi_modal_app_20250909_models.DescribeMmAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.DescribeMmAppResponse:
        """
        @summary 多模态应用详情
        
        @param request: DescribeMmAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMmAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMmApp',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.DescribeMmAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mm_app_with_options_async(
        self,
        request: sfm_multi_modal_app_20250909_models.DescribeMmAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.DescribeMmAppResponse:
        """
        @summary 多模态应用详情
        
        @param request: DescribeMmAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMmAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMmApp',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.DescribeMmAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mm_app(
        self,
        request: sfm_multi_modal_app_20250909_models.DescribeMmAppRequest,
    ) -> sfm_multi_modal_app_20250909_models.DescribeMmAppResponse:
        """
        @summary 多模态应用详情
        
        @param request: DescribeMmAppRequest
        @return: DescribeMmAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_mm_app_with_options(request, runtime)

    async def describe_mm_app_async(
        self,
        request: sfm_multi_modal_app_20250909_models.DescribeMmAppRequest,
    ) -> sfm_multi_modal_app_20250909_models.DescribeMmAppResponse:
        """
        @summary 多模态应用详情
        
        @param request: DescribeMmAppRequest
        @return: DescribeMmAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_mm_app_with_options_async(request, runtime)

    def list_command_with_options(
        self,
        request: sfm_multi_modal_app_20250909_models.ListCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.ListCommandResponse:
        """
        @summary 指令列表
        
        @param request: ListCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCommandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tool_name):
            query['ToolName'] = request.tool_name
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommand',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.ListCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_command_with_options_async(
        self,
        request: sfm_multi_modal_app_20250909_models.ListCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.ListCommandResponse:
        """
        @summary 指令列表
        
        @param request: ListCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCommandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tool_name):
            query['ToolName'] = request.tool_name
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommand',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.ListCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_command(
        self,
        request: sfm_multi_modal_app_20250909_models.ListCommandRequest,
    ) -> sfm_multi_modal_app_20250909_models.ListCommandResponse:
        """
        @summary 指令列表
        
        @param request: ListCommandRequest
        @return: ListCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_command_with_options(request, runtime)

    async def list_command_async(
        self,
        request: sfm_multi_modal_app_20250909_models.ListCommandRequest,
    ) -> sfm_multi_modal_app_20250909_models.ListCommandResponse:
        """
        @summary 指令列表
        
        @param request: ListCommandRequest
        @return: ListCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_command_with_options_async(request, runtime)

    def list_mm_app_with_options(
        self,
        request: sfm_multi_modal_app_20250909_models.ListMmAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.ListMmAppResponse:
        """
        @summary 获取多模态应用列表
        
        @param request: ListMmAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMmAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMmApp',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.ListMmAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mm_app_with_options_async(
        self,
        request: sfm_multi_modal_app_20250909_models.ListMmAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.ListMmAppResponse:
        """
        @summary 获取多模态应用列表
        
        @param request: ListMmAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMmAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMmApp',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.ListMmAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mm_app(
        self,
        request: sfm_multi_modal_app_20250909_models.ListMmAppRequest,
    ) -> sfm_multi_modal_app_20250909_models.ListMmAppResponse:
        """
        @summary 获取多模态应用列表
        
        @param request: ListMmAppRequest
        @return: ListMmAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mm_app_with_options(request, runtime)

    async def list_mm_app_async(
        self,
        request: sfm_multi_modal_app_20250909_models.ListMmAppRequest,
    ) -> sfm_multi_modal_app_20250909_models.ListMmAppResponse:
        """
        @summary 获取多模态应用列表
        
        @param request: ListMmAppRequest
        @return: ListMmAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mm_app_with_options_async(request, runtime)

    def list_published_mm_app_with_options(
        self,
        request: sfm_multi_modal_app_20250909_models.ListPublishedMmAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.ListPublishedMmAppResponse:
        """
        @summary 应用发布列表
        
        @param request: ListPublishedMmAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublishedMmAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishedMmApp',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.ListPublishedMmAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_published_mm_app_with_options_async(
        self,
        request: sfm_multi_modal_app_20250909_models.ListPublishedMmAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.ListPublishedMmAppResponse:
        """
        @summary 应用发布列表
        
        @param request: ListPublishedMmAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublishedMmAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishedMmApp',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.ListPublishedMmAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_published_mm_app(
        self,
        request: sfm_multi_modal_app_20250909_models.ListPublishedMmAppRequest,
    ) -> sfm_multi_modal_app_20250909_models.ListPublishedMmAppResponse:
        """
        @summary 应用发布列表
        
        @param request: ListPublishedMmAppRequest
        @return: ListPublishedMmAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_published_mm_app_with_options(request, runtime)

    async def list_published_mm_app_async(
        self,
        request: sfm_multi_modal_app_20250909_models.ListPublishedMmAppRequest,
    ) -> sfm_multi_modal_app_20250909_models.ListPublishedMmAppResponse:
        """
        @summary 应用发布列表
        
        @param request: ListPublishedMmAppRequest
        @return: ListPublishedMmAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_published_mm_app_with_options_async(request, runtime)

    def publish_mm_app_with_options(
        self,
        request: sfm_multi_modal_app_20250909_models.PublishMmAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.PublishMmAppResponse:
        """
        @summary 多模态应用发布
        
        @param request: PublishMmAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishMmAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishMmApp',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.PublishMmAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_mm_app_with_options_async(
        self,
        request: sfm_multi_modal_app_20250909_models.PublishMmAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.PublishMmAppResponse:
        """
        @summary 多模态应用发布
        
        @param request: PublishMmAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishMmAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishMmApp',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.PublishMmAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_mm_app(
        self,
        request: sfm_multi_modal_app_20250909_models.PublishMmAppRequest,
    ) -> sfm_multi_modal_app_20250909_models.PublishMmAppResponse:
        """
        @summary 多模态应用发布
        
        @param request: PublishMmAppRequest
        @return: PublishMmAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.publish_mm_app_with_options(request, runtime)

    async def publish_mm_app_async(
        self,
        request: sfm_multi_modal_app_20250909_models.PublishMmAppRequest,
    ) -> sfm_multi_modal_app_20250909_models.PublishMmAppResponse:
        """
        @summary 多模态应用发布
        
        @param request: PublishMmAppRequest
        @return: PublishMmAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.publish_mm_app_with_options_async(request, runtime)

    def update_command_with_options(
        self,
        tmp_req: sfm_multi_modal_app_20250909_models.UpdateCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.UpdateCommandResponse:
        """
        @summary 指令更新
        
        @param tmp_req: UpdateCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCommandResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sfm_multi_modal_app_20250909_models.UpdateCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tool_examples):
            request.tool_examples_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tool_examples, 'ToolExamples', 'json')
        if not UtilClient.is_unset(tmp_req.tool_params):
            request.tool_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tool_params, 'ToolParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.tool_description):
            query['ToolDescription'] = request.tool_description
        if not UtilClient.is_unset(request.tool_examples_shrink):
            query['ToolExamples'] = request.tool_examples_shrink
        if not UtilClient.is_unset(request.tool_id):
            query['ToolId'] = request.tool_id
        if not UtilClient.is_unset(request.tool_name):
            query['ToolName'] = request.tool_name
        if not UtilClient.is_unset(request.tool_params_shrink):
            query['ToolParams'] = request.tool_params_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCommand',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.UpdateCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_command_with_options_async(
        self,
        tmp_req: sfm_multi_modal_app_20250909_models.UpdateCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.UpdateCommandResponse:
        """
        @summary 指令更新
        
        @param tmp_req: UpdateCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCommandResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sfm_multi_modal_app_20250909_models.UpdateCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tool_examples):
            request.tool_examples_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tool_examples, 'ToolExamples', 'json')
        if not UtilClient.is_unset(tmp_req.tool_params):
            request.tool_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tool_params, 'ToolParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.tool_description):
            query['ToolDescription'] = request.tool_description
        if not UtilClient.is_unset(request.tool_examples_shrink):
            query['ToolExamples'] = request.tool_examples_shrink
        if not UtilClient.is_unset(request.tool_id):
            query['ToolId'] = request.tool_id
        if not UtilClient.is_unset(request.tool_name):
            query['ToolName'] = request.tool_name
        if not UtilClient.is_unset(request.tool_params_shrink):
            query['ToolParams'] = request.tool_params_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCommand',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.UpdateCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_command(
        self,
        request: sfm_multi_modal_app_20250909_models.UpdateCommandRequest,
    ) -> sfm_multi_modal_app_20250909_models.UpdateCommandResponse:
        """
        @summary 指令更新
        
        @param request: UpdateCommandRequest
        @return: UpdateCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_command_with_options(request, runtime)

    async def update_command_async(
        self,
        request: sfm_multi_modal_app_20250909_models.UpdateCommandRequest,
    ) -> sfm_multi_modal_app_20250909_models.UpdateCommandResponse:
        """
        @summary 指令更新
        
        @param request: UpdateCommandRequest
        @return: UpdateCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_command_with_options_async(request, runtime)

    def update_mm_app_with_options(
        self,
        tmp_req: sfm_multi_modal_app_20250909_models.UpdateMmAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.UpdateMmAppResponse:
        """
        @summary 多模态应用更新
        
        @param tmp_req: UpdateMmAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMmAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sfm_multi_modal_app_20250909_models.UpdateMmAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.binding_config):
            request.binding_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.binding_config, 'BindingConfig', 'json')
        if not UtilClient.is_unset(tmp_req.conversation_config):
            request.conversation_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.conversation_config, 'ConversationConfig', 'json')
        if not UtilClient.is_unset(tmp_req.model_config):
            request.model_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model_config, 'ModelConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.binding_config_shrink):
            query['BindingConfig'] = request.binding_config_shrink
        if not UtilClient.is_unset(request.conversation_config_shrink):
            query['ConversationConfig'] = request.conversation_config_shrink
        if not UtilClient.is_unset(request.model_config_shrink):
            query['ModelConfig'] = request.model_config_shrink
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMmApp',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.UpdateMmAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mm_app_with_options_async(
        self,
        tmp_req: sfm_multi_modal_app_20250909_models.UpdateMmAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sfm_multi_modal_app_20250909_models.UpdateMmAppResponse:
        """
        @summary 多模态应用更新
        
        @param tmp_req: UpdateMmAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMmAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sfm_multi_modal_app_20250909_models.UpdateMmAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.binding_config):
            request.binding_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.binding_config, 'BindingConfig', 'json')
        if not UtilClient.is_unset(tmp_req.conversation_config):
            request.conversation_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.conversation_config, 'ConversationConfig', 'json')
        if not UtilClient.is_unset(tmp_req.model_config):
            request.model_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model_config, 'ModelConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.binding_config_shrink):
            query['BindingConfig'] = request.binding_config_shrink
        if not UtilClient.is_unset(request.conversation_config_shrink):
            query['ConversationConfig'] = request.conversation_config_shrink
        if not UtilClient.is_unset(request.model_config_shrink):
            query['ModelConfig'] = request.model_config_shrink
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMmApp',
            version='2025-09-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sfm_multi_modal_app_20250909_models.UpdateMmAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mm_app(
        self,
        request: sfm_multi_modal_app_20250909_models.UpdateMmAppRequest,
    ) -> sfm_multi_modal_app_20250909_models.UpdateMmAppResponse:
        """
        @summary 多模态应用更新
        
        @param request: UpdateMmAppRequest
        @return: UpdateMmAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_mm_app_with_options(request, runtime)

    async def update_mm_app_async(
        self,
        request: sfm_multi_modal_app_20250909_models.UpdateMmAppRequest,
    ) -> sfm_multi_modal_app_20250909_models.UpdateMmAppResponse:
        """
        @summary 多模态应用更新
        
        @param request: UpdateMmAppRequest
        @return: UpdateMmAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_mm_app_with_options_async(request, runtime)
