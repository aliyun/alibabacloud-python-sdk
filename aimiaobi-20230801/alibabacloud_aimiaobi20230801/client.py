# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aimiaobi20230801 import models as ai_miao_bi_20230801_models
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
        self._endpoint = self.get_endpoint('aimiaobi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_dataset_document_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.AddDatasetDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.AddDatasetDocumentResponse:
        """
        @summary 添加文档到数据集
        
        @param tmp_req: AddDatasetDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDatasetDocumentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.AddDatasetDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.document):
            request.document_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document, 'Document', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.document_shrink):
            body['Document'] = request.document_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDatasetDocument',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.AddDatasetDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dataset_document_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.AddDatasetDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.AddDatasetDocumentResponse:
        """
        @summary 添加文档到数据集
        
        @param tmp_req: AddDatasetDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDatasetDocumentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.AddDatasetDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.document):
            request.document_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document, 'Document', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.document_shrink):
            body['Document'] = request.document_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDatasetDocument',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.AddDatasetDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dataset_document(
        self,
        request: ai_miao_bi_20230801_models.AddDatasetDocumentRequest,
    ) -> ai_miao_bi_20230801_models.AddDatasetDocumentResponse:
        """
        @summary 添加文档到数据集
        
        @param request: AddDatasetDocumentRequest
        @return: AddDatasetDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_dataset_document_with_options(request, runtime)

    async def add_dataset_document_async(
        self,
        request: ai_miao_bi_20230801_models.AddDatasetDocumentRequest,
    ) -> ai_miao_bi_20230801_models.AddDatasetDocumentResponse:
        """
        @summary 添加文档到数据集
        
        @param request: AddDatasetDocumentRequest
        @return: AddDatasetDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_dataset_document_with_options_async(request, runtime)

    def cancel_async_task_with_options(
        self,
        request: ai_miao_bi_20230801_models.CancelAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.CancelAsyncTaskResponse:
        """
        @summary 取消异步任务
        
        @param request: CancelAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelAsyncTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.CancelAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_async_task_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.CancelAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.CancelAsyncTaskResponse:
        """
        @summary 取消异步任务
        
        @param request: CancelAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelAsyncTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.CancelAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_async_task(
        self,
        request: ai_miao_bi_20230801_models.CancelAsyncTaskRequest,
    ) -> ai_miao_bi_20230801_models.CancelAsyncTaskResponse:
        """
        @summary 取消异步任务
        
        @param request: CancelAsyncTaskRequest
        @return: CancelAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_async_task_with_options(request, runtime)

    async def cancel_async_task_async(
        self,
        request: ai_miao_bi_20230801_models.CancelAsyncTaskRequest,
    ) -> ai_miao_bi_20230801_models.CancelAsyncTaskResponse:
        """
        @summary 取消异步任务
        
        @param request: CancelAsyncTaskRequest
        @return: CancelAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_async_task_with_options_async(request, runtime)

    def clear_intervenes_with_options(
        self,
        request: ai_miao_bi_20230801_models.ClearIntervenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ClearIntervenesResponse:
        """
        @summary 清除所有干预内容
        
        @param request: ClearIntervenesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ClearIntervenesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearIntervenes',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ClearIntervenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_intervenes_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ClearIntervenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ClearIntervenesResponse:
        """
        @summary 清除所有干预内容
        
        @param request: ClearIntervenesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ClearIntervenesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearIntervenes',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ClearIntervenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_intervenes(
        self,
        request: ai_miao_bi_20230801_models.ClearIntervenesRequest,
    ) -> ai_miao_bi_20230801_models.ClearIntervenesResponse:
        """
        @summary 清除所有干预内容
        
        @param request: ClearIntervenesRequest
        @return: ClearIntervenesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.clear_intervenes_with_options(request, runtime)

    async def clear_intervenes_async(
        self,
        request: ai_miao_bi_20230801_models.ClearIntervenesRequest,
    ) -> ai_miao_bi_20230801_models.ClearIntervenesResponse:
        """
        @summary 清除所有干预内容
        
        @param request: ClearIntervenesRequest
        @return: ClearIntervenesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.clear_intervenes_with_options_async(request, runtime)

    def create_dataset_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.CreateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.CreateDatasetResponse:
        """
        @summary 数据集管理-创建
        
        @param tmp_req: CreateDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.CreateDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dataset_config):
            request.dataset_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dataset_config, 'DatasetConfig', 'json')
        if not UtilClient.is_unset(tmp_req.document_handle_config):
            request.document_handle_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document_handle_config, 'DocumentHandleConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_config_shrink):
            body['DatasetConfig'] = request.dataset_config_shrink
        if not UtilClient.is_unset(request.dataset_description):
            body['DatasetDescription'] = request.dataset_description
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.dataset_type):
            body['DatasetType'] = request.dataset_type
        if not UtilClient.is_unset(request.document_handle_config_shrink):
            body['DocumentHandleConfig'] = request.document_handle_config_shrink
        if not UtilClient.is_unset(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.search_dataset_enable):
            body['SearchDatasetEnable'] = request.search_dataset_enable
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataset',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.CreateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.CreateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.CreateDatasetResponse:
        """
        @summary 数据集管理-创建
        
        @param tmp_req: CreateDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.CreateDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dataset_config):
            request.dataset_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dataset_config, 'DatasetConfig', 'json')
        if not UtilClient.is_unset(tmp_req.document_handle_config):
            request.document_handle_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document_handle_config, 'DocumentHandleConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_config_shrink):
            body['DatasetConfig'] = request.dataset_config_shrink
        if not UtilClient.is_unset(request.dataset_description):
            body['DatasetDescription'] = request.dataset_description
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.dataset_type):
            body['DatasetType'] = request.dataset_type
        if not UtilClient.is_unset(request.document_handle_config_shrink):
            body['DocumentHandleConfig'] = request.document_handle_config_shrink
        if not UtilClient.is_unset(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.search_dataset_enable):
            body['SearchDatasetEnable'] = request.search_dataset_enable
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataset',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.CreateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset(
        self,
        request: ai_miao_bi_20230801_models.CreateDatasetRequest,
    ) -> ai_miao_bi_20230801_models.CreateDatasetResponse:
        """
        @summary 数据集管理-创建
        
        @param request: CreateDatasetRequest
        @return: CreateDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dataset_with_options(request, runtime)

    async def create_dataset_async(
        self,
        request: ai_miao_bi_20230801_models.CreateDatasetRequest,
    ) -> ai_miao_bi_20230801_models.CreateDatasetResponse:
        """
        @summary 数据集管理-创建
        
        @param request: CreateDatasetRequest
        @return: CreateDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dataset_with_options_async(request, runtime)

    def create_generated_content_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.CreateGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.CreateGeneratedContentResponse:
        """
        @summary 文档管理-创建
        
        @param tmp_req: CreateGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGeneratedContentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.CreateGeneratedContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.keywords):
            request.keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_domain):
            body['ContentDomain'] = request.content_domain
        if not UtilClient.is_unset(request.content_text):
            body['ContentText'] = request.content_text
        if not UtilClient.is_unset(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.CreateGeneratedContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_generated_content_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.CreateGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.CreateGeneratedContentResponse:
        """
        @summary 文档管理-创建
        
        @param tmp_req: CreateGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGeneratedContentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.CreateGeneratedContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.keywords):
            request.keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_domain):
            body['ContentDomain'] = request.content_domain
        if not UtilClient.is_unset(request.content_text):
            body['ContentText'] = request.content_text
        if not UtilClient.is_unset(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.CreateGeneratedContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_generated_content(
        self,
        request: ai_miao_bi_20230801_models.CreateGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.CreateGeneratedContentResponse:
        """
        @summary 文档管理-创建
        
        @param request: CreateGeneratedContentRequest
        @return: CreateGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_generated_content_with_options(request, runtime)

    async def create_generated_content_async(
        self,
        request: ai_miao_bi_20230801_models.CreateGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.CreateGeneratedContentResponse:
        """
        @summary 文档管理-创建
        
        @param request: CreateGeneratedContentRequest
        @return: CreateGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_generated_content_with_options_async(request, runtime)

    def create_token_with_options(
        self,
        request: ai_miao_bi_20230801_models.CreateTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.CreateTokenResponse:
        """
        @summary 获取授权token
        
        @param request: CreateTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateToken',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.CreateTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_token_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.CreateTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.CreateTokenResponse:
        """
        @summary 获取授权token
        
        @param request: CreateTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateToken',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.CreateTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_token(
        self,
        request: ai_miao_bi_20230801_models.CreateTokenRequest,
    ) -> ai_miao_bi_20230801_models.CreateTokenResponse:
        """
        @summary 获取授权token
        
        @param request: CreateTokenRequest
        @return: CreateTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_token_with_options(request, runtime)

    async def create_token_async(
        self,
        request: ai_miao_bi_20230801_models.CreateTokenRequest,
    ) -> ai_miao_bi_20230801_models.CreateTokenResponse:
        """
        @summary 获取授权token
        
        @param request: CreateTokenRequest
        @return: CreateTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_token_with_options_async(request, runtime)

    def delete_custom_text_with_options(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTextResponse:
        """
        @summary 删除自定义文本
        
        @param request: DeleteCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomText',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteCustomTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_text_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTextResponse:
        """
        @summary 删除自定义文本
        
        @param request: DeleteCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomText',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteCustomTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_text(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTextResponse:
        """
        @summary 删除自定义文本
        
        @param request: DeleteCustomTextRequest
        @return: DeleteCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_text_with_options(request, runtime)

    async def delete_custom_text_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTextResponse:
        """
        @summary 删除自定义文本
        
        @param request: DeleteCustomTextRequest
        @return: DeleteCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_text_with_options_async(request, runtime)

    def delete_custom_topic_by_topic_with_options(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTopicByTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTopicByTopicResponse:
        """
        @summary 根据主题删除自定义主题事件
        
        @param request: DeleteCustomTopicByTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomTopicByTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomTopicByTopic',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteCustomTopicByTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_topic_by_topic_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTopicByTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTopicByTopicResponse:
        """
        @summary 根据主题删除自定义主题事件
        
        @param request: DeleteCustomTopicByTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomTopicByTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomTopicByTopic',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteCustomTopicByTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_topic_by_topic(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTopicByTopicRequest,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTopicByTopicResponse:
        """
        @summary 根据主题删除自定义主题事件
        
        @param request: DeleteCustomTopicByTopicRequest
        @return: DeleteCustomTopicByTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_topic_by_topic_with_options(request, runtime)

    async def delete_custom_topic_by_topic_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTopicByTopicRequest,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTopicByTopicResponse:
        """
        @summary 根据主题删除自定义主题事件
        
        @param request: DeleteCustomTopicByTopicRequest
        @return: DeleteCustomTopicByTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_topic_by_topic_with_options_async(request, runtime)

    def delete_custom_topic_view_point_by_id_with_options(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdResponse:
        """
        @summary 根据自定义观点ID删除自定义观点
        
        @param request: DeleteCustomTopicViewPointByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomTopicViewPointByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomTopicViewPointById',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_topic_view_point_by_id_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdResponse:
        """
        @summary 根据自定义观点ID删除自定义观点
        
        @param request: DeleteCustomTopicViewPointByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomTopicViewPointByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomTopicViewPointById',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_topic_view_point_by_id(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdRequest,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdResponse:
        """
        @summary 根据自定义观点ID删除自定义观点
        
        @param request: DeleteCustomTopicViewPointByIdRequest
        @return: DeleteCustomTopicViewPointByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_topic_view_point_by_id_with_options(request, runtime)

    async def delete_custom_topic_view_point_by_id_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdRequest,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdResponse:
        """
        @summary 根据自定义观点ID删除自定义观点
        
        @param request: DeleteCustomTopicViewPointByIdRequest
        @return: DeleteCustomTopicViewPointByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_topic_view_point_by_id_with_options_async(request, runtime)

    def delete_dataset_with_options(
        self,
        request: ai_miao_bi_20230801_models.DeleteDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteDatasetResponse:
        """
        @summary 数据集管理-删除
        
        @param request: DeleteDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataset',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteDatasetResponse:
        """
        @summary 数据集管理-删除
        
        @param request: DeleteDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataset',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset(
        self,
        request: ai_miao_bi_20230801_models.DeleteDatasetRequest,
    ) -> ai_miao_bi_20230801_models.DeleteDatasetResponse:
        """
        @summary 数据集管理-删除
        
        @param request: DeleteDatasetRequest
        @return: DeleteDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dataset_with_options(request, runtime)

    async def delete_dataset_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteDatasetRequest,
    ) -> ai_miao_bi_20230801_models.DeleteDatasetResponse:
        """
        @summary 数据集管理-删除
        
        @param request: DeleteDatasetRequest
        @return: DeleteDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dataset_with_options_async(request, runtime)

    def delete_dataset_document_with_options(
        self,
        request: ai_miao_bi_20230801_models.DeleteDatasetDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteDatasetDocumentResponse:
        """
        @summary 删除数据集文档
        
        @param request: DeleteDatasetDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.doc_uuid):
            body['DocUuid'] = request.doc_uuid
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDatasetDocument',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteDatasetDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_document_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteDatasetDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteDatasetDocumentResponse:
        """
        @summary 删除数据集文档
        
        @param request: DeleteDatasetDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.doc_uuid):
            body['DocUuid'] = request.doc_uuid
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDatasetDocument',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteDatasetDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset_document(
        self,
        request: ai_miao_bi_20230801_models.DeleteDatasetDocumentRequest,
    ) -> ai_miao_bi_20230801_models.DeleteDatasetDocumentResponse:
        """
        @summary 删除数据集文档
        
        @param request: DeleteDatasetDocumentRequest
        @return: DeleteDatasetDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dataset_document_with_options(request, runtime)

    async def delete_dataset_document_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteDatasetDocumentRequest,
    ) -> ai_miao_bi_20230801_models.DeleteDatasetDocumentResponse:
        """
        @summary 删除数据集文档
        
        @param request: DeleteDatasetDocumentRequest
        @return: DeleteDatasetDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dataset_document_with_options_async(request, runtime)

    def delete_docs_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.DeleteDocsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteDocsResponse:
        """
        @summary 妙读删除多个文档
        
        @param tmp_req: DeleteDocsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDocsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.DeleteDocsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_ids):
            request.doc_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_ids, 'DocIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.doc_ids_shrink):
            body['DocIds'] = request.doc_ids_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDocs',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteDocsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_docs_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.DeleteDocsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteDocsResponse:
        """
        @summary 妙读删除多个文档
        
        @param tmp_req: DeleteDocsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDocsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.DeleteDocsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_ids):
            request.doc_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_ids, 'DocIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.doc_ids_shrink):
            body['DocIds'] = request.doc_ids_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDocs',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteDocsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_docs(
        self,
        request: ai_miao_bi_20230801_models.DeleteDocsRequest,
    ) -> ai_miao_bi_20230801_models.DeleteDocsResponse:
        """
        @summary 妙读删除多个文档
        
        @param request: DeleteDocsRequest
        @return: DeleteDocsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_docs_with_options(request, runtime)

    async def delete_docs_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteDocsRequest,
    ) -> ai_miao_bi_20230801_models.DeleteDocsResponse:
        """
        @summary 妙读删除多个文档
        
        @param request: DeleteDocsRequest
        @return: DeleteDocsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_docs_with_options_async(request, runtime)

    def delete_generated_content_with_options(
        self,
        request: ai_miao_bi_20230801_models.DeleteGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteGeneratedContentResponse:
        """
        @summary 文档管理-删除。
        
        @param request: DeleteGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGeneratedContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteGeneratedContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_generated_content_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteGeneratedContentResponse:
        """
        @summary 文档管理-删除。
        
        @param request: DeleteGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGeneratedContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteGeneratedContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_generated_content(
        self,
        request: ai_miao_bi_20230801_models.DeleteGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.DeleteGeneratedContentResponse:
        """
        @summary 文档管理-删除。
        
        @param request: DeleteGeneratedContentRequest
        @return: DeleteGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_generated_content_with_options(request, runtime)

    async def delete_generated_content_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.DeleteGeneratedContentResponse:
        """
        @summary 文档管理-删除。
        
        @param request: DeleteGeneratedContentRequest
        @return: DeleteGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_generated_content_with_options_async(request, runtime)

    def delete_intervene_rule_with_options(
        self,
        request: ai_miao_bi_20230801_models.DeleteInterveneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteInterveneRuleResponse:
        """
        @summary 删除干预规则
        
        @param request: DeleteInterveneRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInterveneRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteInterveneRule',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteInterveneRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_intervene_rule_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteInterveneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteInterveneRuleResponse:
        """
        @summary 删除干预规则
        
        @param request: DeleteInterveneRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInterveneRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteInterveneRule',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteInterveneRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_intervene_rule(
        self,
        request: ai_miao_bi_20230801_models.DeleteInterveneRuleRequest,
    ) -> ai_miao_bi_20230801_models.DeleteInterveneRuleResponse:
        """
        @summary 删除干预规则
        
        @param request: DeleteInterveneRuleRequest
        @return: DeleteInterveneRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_intervene_rule_with_options(request, runtime)

    async def delete_intervene_rule_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteInterveneRuleRequest,
    ) -> ai_miao_bi_20230801_models.DeleteInterveneRuleResponse:
        """
        @summary 删除干预规则
        
        @param request: DeleteInterveneRuleRequest
        @return: DeleteInterveneRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_intervene_rule_with_options_async(request, runtime)

    def delete_material_by_id_with_options(
        self,
        request: ai_miao_bi_20230801_models.DeleteMaterialByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteMaterialByIdResponse:
        """
        @summary 根据ID删除素材
        
        @param request: DeleteMaterialByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMaterialByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMaterialById',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteMaterialByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_material_by_id_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteMaterialByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteMaterialByIdResponse:
        """
        @summary 根据ID删除素材
        
        @param request: DeleteMaterialByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMaterialByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMaterialById',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteMaterialByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_material_by_id(
        self,
        request: ai_miao_bi_20230801_models.DeleteMaterialByIdRequest,
    ) -> ai_miao_bi_20230801_models.DeleteMaterialByIdResponse:
        """
        @summary 根据ID删除素材
        
        @param request: DeleteMaterialByIdRequest
        @return: DeleteMaterialByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_material_by_id_with_options(request, runtime)

    async def delete_material_by_id_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteMaterialByIdRequest,
    ) -> ai_miao_bi_20230801_models.DeleteMaterialByIdResponse:
        """
        @summary 根据ID删除素材
        
        @param request: DeleteMaterialByIdRequest
        @return: DeleteMaterialByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_material_by_id_with_options_async(request, runtime)

    def document_extraction_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.DocumentExtractionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DocumentExtractionResponse:
        """
        @summary 从链接中提取文档内容
        
        @param tmp_req: DocumentExtractionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DocumentExtractionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.DocumentExtractionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.urls):
            request.urls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.urls, 'Urls', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.urls_shrink):
            body['Urls'] = request.urls_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DocumentExtraction',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DocumentExtractionResponse(),
            self.call_api(params, req, runtime)
        )

    async def document_extraction_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.DocumentExtractionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DocumentExtractionResponse:
        """
        @summary 从链接中提取文档内容
        
        @param tmp_req: DocumentExtractionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DocumentExtractionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.DocumentExtractionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.urls):
            request.urls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.urls, 'Urls', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.urls_shrink):
            body['Urls'] = request.urls_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DocumentExtraction',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DocumentExtractionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def document_extraction(
        self,
        request: ai_miao_bi_20230801_models.DocumentExtractionRequest,
    ) -> ai_miao_bi_20230801_models.DocumentExtractionResponse:
        """
        @summary 从链接中提取文档内容
        
        @param request: DocumentExtractionRequest
        @return: DocumentExtractionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.document_extraction_with_options(request, runtime)

    async def document_extraction_async(
        self,
        request: ai_miao_bi_20230801_models.DocumentExtractionRequest,
    ) -> ai_miao_bi_20230801_models.DocumentExtractionResponse:
        """
        @summary 从链接中提取文档内容
        
        @param request: DocumentExtractionRequest
        @return: DocumentExtractionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.document_extraction_with_options_async(request, runtime)

    def export_analysis_tag_detail_by_task_id_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ExportAnalysisTagDetailByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ExportAnalysisTagDetailByTaskIdResponse:
        """
        @summary 导出企业VOC分析任务明细列表
        
        @param tmp_req: ExportAnalysisTagDetailByTaskIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportAnalysisTagDetailByTaskIdResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ExportAnalysisTagDetailByTaskIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.categories):
            request.categories_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        body = {}
        if not UtilClient.is_unset(request.categories_shrink):
            body['Categories'] = request.categories_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportAnalysisTagDetailByTaskId',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ExportAnalysisTagDetailByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_analysis_tag_detail_by_task_id_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ExportAnalysisTagDetailByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ExportAnalysisTagDetailByTaskIdResponse:
        """
        @summary 导出企业VOC分析任务明细列表
        
        @param tmp_req: ExportAnalysisTagDetailByTaskIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportAnalysisTagDetailByTaskIdResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ExportAnalysisTagDetailByTaskIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.categories):
            request.categories_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        body = {}
        if not UtilClient.is_unset(request.categories_shrink):
            body['Categories'] = request.categories_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportAnalysisTagDetailByTaskId',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ExportAnalysisTagDetailByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_analysis_tag_detail_by_task_id(
        self,
        request: ai_miao_bi_20230801_models.ExportAnalysisTagDetailByTaskIdRequest,
    ) -> ai_miao_bi_20230801_models.ExportAnalysisTagDetailByTaskIdResponse:
        """
        @summary 导出企业VOC分析任务明细列表
        
        @param request: ExportAnalysisTagDetailByTaskIdRequest
        @return: ExportAnalysisTagDetailByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_analysis_tag_detail_by_task_id_with_options(request, runtime)

    async def export_analysis_tag_detail_by_task_id_async(
        self,
        request: ai_miao_bi_20230801_models.ExportAnalysisTagDetailByTaskIdRequest,
    ) -> ai_miao_bi_20230801_models.ExportAnalysisTagDetailByTaskIdResponse:
        """
        @summary 导出企业VOC分析任务明细列表
        
        @param request: ExportAnalysisTagDetailByTaskIdRequest
        @return: ExportAnalysisTagDetailByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_analysis_tag_detail_by_task_id_with_options_async(request, runtime)

    def export_generated_content_with_options(
        self,
        request: ai_miao_bi_20230801_models.ExportGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ExportGeneratedContentResponse:
        """
        @summary 文档管理-导出。
        
        @param request: ExportGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportGeneratedContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ExportGeneratedContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_generated_content_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ExportGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ExportGeneratedContentResponse:
        """
        @summary 文档管理-导出。
        
        @param request: ExportGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportGeneratedContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ExportGeneratedContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_generated_content(
        self,
        request: ai_miao_bi_20230801_models.ExportGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.ExportGeneratedContentResponse:
        """
        @summary 文档管理-导出。
        
        @param request: ExportGeneratedContentRequest
        @return: ExportGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_generated_content_with_options(request, runtime)

    async def export_generated_content_async(
        self,
        request: ai_miao_bi_20230801_models.ExportGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.ExportGeneratedContentResponse:
        """
        @summary 文档管理-导出。
        
        @param request: ExportGeneratedContentRequest
        @return: ExportGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_generated_content_with_options_async(request, runtime)

    def export_hot_topic_planning_proposals_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsResponse:
        """
        @summary 导出选题策划文档，响应为一个可公开访问的URL。一小时后失效
        
        @param tmp_req: ExportHotTopicPlanningProposalsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportHotTopicPlanningProposalsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        if not UtilClient.is_unset(tmp_req.titles):
            request.titles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.titles, 'Titles', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not UtilClient.is_unset(request.export_type):
            body['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.titles_shrink):
            body['Titles'] = request.titles_shrink
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not UtilClient.is_unset(request.view_point_type):
            body['ViewPointType'] = request.view_point_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportHotTopicPlanningProposals',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_hot_topic_planning_proposals_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsResponse:
        """
        @summary 导出选题策划文档，响应为一个可公开访问的URL。一小时后失效
        
        @param tmp_req: ExportHotTopicPlanningProposalsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportHotTopicPlanningProposalsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        if not UtilClient.is_unset(tmp_req.titles):
            request.titles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.titles, 'Titles', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not UtilClient.is_unset(request.export_type):
            body['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.titles_shrink):
            body['Titles'] = request.titles_shrink
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not UtilClient.is_unset(request.view_point_type):
            body['ViewPointType'] = request.view_point_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportHotTopicPlanningProposals',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_hot_topic_planning_proposals(
        self,
        request: ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsRequest,
    ) -> ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsResponse:
        """
        @summary 导出选题策划文档，响应为一个可公开访问的URL。一小时后失效
        
        @param request: ExportHotTopicPlanningProposalsRequest
        @return: ExportHotTopicPlanningProposalsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_hot_topic_planning_proposals_with_options(request, runtime)

    async def export_hot_topic_planning_proposals_async(
        self,
        request: ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsRequest,
    ) -> ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsResponse:
        """
        @summary 导出选题策划文档，响应为一个可公开访问的URL。一小时后失效
        
        @param request: ExportHotTopicPlanningProposalsRequest
        @return: ExportHotTopicPlanningProposalsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_hot_topic_planning_proposals_with_options_async(request, runtime)

    def export_intervenes_with_options(
        self,
        request: ai_miao_bi_20230801_models.ExportIntervenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ExportIntervenesResponse:
        """
        @summary 导出所有干预内容
        
        @param request: ExportIntervenesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportIntervenesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportIntervenes',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ExportIntervenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_intervenes_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ExportIntervenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ExportIntervenesResponse:
        """
        @summary 导出所有干预内容
        
        @param request: ExportIntervenesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportIntervenesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportIntervenes',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ExportIntervenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_intervenes(
        self,
        request: ai_miao_bi_20230801_models.ExportIntervenesRequest,
    ) -> ai_miao_bi_20230801_models.ExportIntervenesResponse:
        """
        @summary 导出所有干预内容
        
        @param request: ExportIntervenesRequest
        @return: ExportIntervenesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_intervenes_with_options(request, runtime)

    async def export_intervenes_async(
        self,
        request: ai_miao_bi_20230801_models.ExportIntervenesRequest,
    ) -> ai_miao_bi_20230801_models.ExportIntervenesResponse:
        """
        @summary 导出所有干预内容
        
        @param request: ExportIntervenesRequest
        @return: ExportIntervenesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_intervenes_with_options_async(request, runtime)

    def feedback_dialogue_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.FeedbackDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.FeedbackDialogueResponse:
        """
        @summary 反馈某次生成的结果
        
        @param tmp_req: FeedbackDialogueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FeedbackDialogueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.FeedbackDialogueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rating_tags):
            request.rating_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rating_tags, 'RatingTags', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.customer_response):
            body['CustomerResponse'] = request.customer_response
        if not UtilClient.is_unset(request.good_text):
            body['GoodText'] = request.good_text
        if not UtilClient.is_unset(request.modified_response):
            body['ModifiedResponse'] = request.modified_response
        if not UtilClient.is_unset(request.rating):
            body['Rating'] = request.rating
        if not UtilClient.is_unset(request.rating_tags_shrink):
            body['RatingTags'] = request.rating_tags_shrink
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FeedbackDialogue',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.FeedbackDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def feedback_dialogue_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.FeedbackDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.FeedbackDialogueResponse:
        """
        @summary 反馈某次生成的结果
        
        @param tmp_req: FeedbackDialogueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FeedbackDialogueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.FeedbackDialogueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rating_tags):
            request.rating_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rating_tags, 'RatingTags', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.customer_response):
            body['CustomerResponse'] = request.customer_response
        if not UtilClient.is_unset(request.good_text):
            body['GoodText'] = request.good_text
        if not UtilClient.is_unset(request.modified_response):
            body['ModifiedResponse'] = request.modified_response
        if not UtilClient.is_unset(request.rating):
            body['Rating'] = request.rating
        if not UtilClient.is_unset(request.rating_tags_shrink):
            body['RatingTags'] = request.rating_tags_shrink
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FeedbackDialogue',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.FeedbackDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def feedback_dialogue(
        self,
        request: ai_miao_bi_20230801_models.FeedbackDialogueRequest,
    ) -> ai_miao_bi_20230801_models.FeedbackDialogueResponse:
        """
        @summary 反馈某次生成的结果
        
        @param request: FeedbackDialogueRequest
        @return: FeedbackDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.feedback_dialogue_with_options(request, runtime)

    async def feedback_dialogue_async(
        self,
        request: ai_miao_bi_20230801_models.FeedbackDialogueRequest,
    ) -> ai_miao_bi_20230801_models.FeedbackDialogueResponse:
        """
        @summary 反馈某次生成的结果
        
        @param request: FeedbackDialogueRequest
        @return: FeedbackDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.feedback_dialogue_with_options_async(request, runtime)

    def fetch_image_task_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.FetchImageTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.FetchImageTaskResponse:
        """
        @summary 获取图片任务执行结果
        
        @param tmp_req: FetchImageTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchImageTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.FetchImageTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_id_list):
            request.task_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_id_list, 'TaskIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.article_task_id):
            body['ArticleTaskId'] = request.article_task_id
        if not UtilClient.is_unset(request.task_id_list_shrink):
            body['TaskIdList'] = request.task_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FetchImageTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.FetchImageTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_image_task_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.FetchImageTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.FetchImageTaskResponse:
        """
        @summary 获取图片任务执行结果
        
        @param tmp_req: FetchImageTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchImageTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.FetchImageTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_id_list):
            request.task_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_id_list, 'TaskIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.article_task_id):
            body['ArticleTaskId'] = request.article_task_id
        if not UtilClient.is_unset(request.task_id_list_shrink):
            body['TaskIdList'] = request.task_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FetchImageTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.FetchImageTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_image_task(
        self,
        request: ai_miao_bi_20230801_models.FetchImageTaskRequest,
    ) -> ai_miao_bi_20230801_models.FetchImageTaskResponse:
        """
        @summary 获取图片任务执行结果
        
        @param request: FetchImageTaskRequest
        @return: FetchImageTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.fetch_image_task_with_options(request, runtime)

    async def fetch_image_task_async(
        self,
        request: ai_miao_bi_20230801_models.FetchImageTaskRequest,
    ) -> ai_miao_bi_20230801_models.FetchImageTaskResponse:
        """
        @summary 获取图片任务执行结果
        
        @param request: FetchImageTaskRequest
        @return: FetchImageTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.fetch_image_task_with_options_async(request, runtime)

    def generate_file_url_by_key_with_options(
        self,
        request: ai_miao_bi_20230801_models.GenerateFileUrlByKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateFileUrlByKeyResponse:
        """
        @summary 生成临时可访问的公开url
        
        @param request: GenerateFileUrlByKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateFileUrlByKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.file_key):
            body['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateFileUrlByKey',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GenerateFileUrlByKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_file_url_by_key_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GenerateFileUrlByKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateFileUrlByKeyResponse:
        """
        @summary 生成临时可访问的公开url
        
        @param request: GenerateFileUrlByKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateFileUrlByKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.file_key):
            body['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateFileUrlByKey',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GenerateFileUrlByKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_file_url_by_key(
        self,
        request: ai_miao_bi_20230801_models.GenerateFileUrlByKeyRequest,
    ) -> ai_miao_bi_20230801_models.GenerateFileUrlByKeyResponse:
        """
        @summary 生成临时可访问的公开url
        
        @param request: GenerateFileUrlByKeyRequest
        @return: GenerateFileUrlByKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_file_url_by_key_with_options(request, runtime)

    async def generate_file_url_by_key_async(
        self,
        request: ai_miao_bi_20230801_models.GenerateFileUrlByKeyRequest,
    ) -> ai_miao_bi_20230801_models.GenerateFileUrlByKeyResponse:
        """
        @summary 生成临时可访问的公开url
        
        @param request: GenerateFileUrlByKeyRequest
        @return: GenerateFileUrlByKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_file_url_by_key_with_options_async(request, runtime)

    def generate_image_task_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.GenerateImageTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateImageTaskResponse:
        """
        @summary 智能配图，图片生成任务
        
        @param tmp_req: GenerateImageTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateImageTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.GenerateImageTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.paragraph_list):
            request.paragraph_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.paragraph_list, 'ParagraphList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.article_task_id):
            body['ArticleTaskId'] = request.article_task_id
        if not UtilClient.is_unset(request.paragraph_list_shrink):
            body['ParagraphList'] = request.paragraph_list_shrink
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.style):
            body['Style'] = request.style
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateImageTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GenerateImageTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_image_task_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.GenerateImageTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateImageTaskResponse:
        """
        @summary 智能配图，图片生成任务
        
        @param tmp_req: GenerateImageTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateImageTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.GenerateImageTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.paragraph_list):
            request.paragraph_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.paragraph_list, 'ParagraphList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.article_task_id):
            body['ArticleTaskId'] = request.article_task_id
        if not UtilClient.is_unset(request.paragraph_list_shrink):
            body['ParagraphList'] = request.paragraph_list_shrink
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.style):
            body['Style'] = request.style
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateImageTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GenerateImageTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_image_task(
        self,
        request: ai_miao_bi_20230801_models.GenerateImageTaskRequest,
    ) -> ai_miao_bi_20230801_models.GenerateImageTaskResponse:
        """
        @summary 智能配图，图片生成任务
        
        @param request: GenerateImageTaskRequest
        @return: GenerateImageTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_image_task_with_options(request, runtime)

    async def generate_image_task_async(
        self,
        request: ai_miao_bi_20230801_models.GenerateImageTaskRequest,
    ) -> ai_miao_bi_20230801_models.GenerateImageTaskResponse:
        """
        @summary 智能配图，图片生成任务
        
        @param request: GenerateImageTaskRequest
        @return: GenerateImageTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_image_task_with_options_async(request, runtime)

    def generate_upload_config_with_options(
        self,
        request: ai_miao_bi_20230801_models.GenerateUploadConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateUploadConfigResponse:
        """
        @summary 生成上传配置
        
        @param request: GenerateUploadConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateUploadConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.parent_dir):
            body['ParentDir'] = request.parent_dir
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateUploadConfig',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GenerateUploadConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_upload_config_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GenerateUploadConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateUploadConfigResponse:
        """
        @summary 生成上传配置
        
        @param request: GenerateUploadConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateUploadConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.parent_dir):
            body['ParentDir'] = request.parent_dir
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateUploadConfig',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GenerateUploadConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_upload_config(
        self,
        request: ai_miao_bi_20230801_models.GenerateUploadConfigRequest,
    ) -> ai_miao_bi_20230801_models.GenerateUploadConfigResponse:
        """
        @summary 生成上传配置
        
        @param request: GenerateUploadConfigRequest
        @return: GenerateUploadConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_upload_config_with_options(request, runtime)

    async def generate_upload_config_async(
        self,
        request: ai_miao_bi_20230801_models.GenerateUploadConfigRequest,
    ) -> ai_miao_bi_20230801_models.GenerateUploadConfigResponse:
        """
        @summary 生成上传配置
        
        @param request: GenerateUploadConfigRequest
        @return: GenerateUploadConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_upload_config_with_options_async(request, runtime)

    def generate_view_point_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.GenerateViewPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateViewPointResponse:
        """
        @summary 视角生成
        
        @param tmp_req: GenerateViewPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateViewPointResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.GenerateViewPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateViewPoint',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GenerateViewPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_view_point_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.GenerateViewPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateViewPointResponse:
        """
        @summary 视角生成
        
        @param tmp_req: GenerateViewPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateViewPointResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.GenerateViewPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateViewPoint',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GenerateViewPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_view_point(
        self,
        request: ai_miao_bi_20230801_models.GenerateViewPointRequest,
    ) -> ai_miao_bi_20230801_models.GenerateViewPointResponse:
        """
        @summary 视角生成
        
        @param request: GenerateViewPointRequest
        @return: GenerateViewPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_view_point_with_options(request, runtime)

    async def generate_view_point_async(
        self,
        request: ai_miao_bi_20230801_models.GenerateViewPointRequest,
    ) -> ai_miao_bi_20230801_models.GenerateViewPointResponse:
        """
        @summary 视角生成
        
        @param request: GenerateViewPointRequest
        @return: GenerateViewPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_view_point_with_options_async(request, runtime)

    def get_categories_by_task_id_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetCategoriesByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetCategoriesByTaskIdResponse:
        """
        @summary 获取某次标签挖掘结果分类
        
        @param request: GetCategoriesByTaskIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCategoriesByTaskIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCategoriesByTaskId',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetCategoriesByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_categories_by_task_id_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetCategoriesByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetCategoriesByTaskIdResponse:
        """
        @summary 获取某次标签挖掘结果分类
        
        @param request: GetCategoriesByTaskIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCategoriesByTaskIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCategoriesByTaskId',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetCategoriesByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_categories_by_task_id(
        self,
        request: ai_miao_bi_20230801_models.GetCategoriesByTaskIdRequest,
    ) -> ai_miao_bi_20230801_models.GetCategoriesByTaskIdResponse:
        """
        @summary 获取某次标签挖掘结果分类
        
        @param request: GetCategoriesByTaskIdRequest
        @return: GetCategoriesByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_categories_by_task_id_with_options(request, runtime)

    async def get_categories_by_task_id_async(
        self,
        request: ai_miao_bi_20230801_models.GetCategoriesByTaskIdRequest,
    ) -> ai_miao_bi_20230801_models.GetCategoriesByTaskIdResponse:
        """
        @summary 获取某次标签挖掘结果分类
        
        @param request: GetCategoriesByTaskIdRequest
        @return: GetCategoriesByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_categories_by_task_id_with_options_async(request, runtime)

    def get_custom_hot_topic_broadcast_job_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetCustomHotTopicBroadcastJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetCustomHotTopicBroadcastJobResponse:
        """
        @summary 获取自定义播报单任务结果
        
        @param request: GetCustomHotTopicBroadcastJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomHotTopicBroadcastJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCustomHotTopicBroadcastJob',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetCustomHotTopicBroadcastJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_hot_topic_broadcast_job_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetCustomHotTopicBroadcastJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetCustomHotTopicBroadcastJobResponse:
        """
        @summary 获取自定义播报单任务结果
        
        @param request: GetCustomHotTopicBroadcastJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomHotTopicBroadcastJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCustomHotTopicBroadcastJob',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetCustomHotTopicBroadcastJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_hot_topic_broadcast_job(
        self,
        request: ai_miao_bi_20230801_models.GetCustomHotTopicBroadcastJobRequest,
    ) -> ai_miao_bi_20230801_models.GetCustomHotTopicBroadcastJobResponse:
        """
        @summary 获取自定义播报单任务结果
        
        @param request: GetCustomHotTopicBroadcastJobRequest
        @return: GetCustomHotTopicBroadcastJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_custom_hot_topic_broadcast_job_with_options(request, runtime)

    async def get_custom_hot_topic_broadcast_job_async(
        self,
        request: ai_miao_bi_20230801_models.GetCustomHotTopicBroadcastJobRequest,
    ) -> ai_miao_bi_20230801_models.GetCustomHotTopicBroadcastJobResponse:
        """
        @summary 获取自定义播报单任务结果
        
        @param request: GetCustomHotTopicBroadcastJobRequest
        @return: GetCustomHotTopicBroadcastJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_custom_hot_topic_broadcast_job_with_options_async(request, runtime)

    def get_custom_text_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetCustomTextResponse:
        """
        @summary 获取自定义文本
        
        @param request: GetCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCustomText',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetCustomTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_text_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetCustomTextResponse:
        """
        @summary 获取自定义文本
        
        @param request: GetCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCustomText',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetCustomTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_text(
        self,
        request: ai_miao_bi_20230801_models.GetCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.GetCustomTextResponse:
        """
        @summary 获取自定义文本
        
        @param request: GetCustomTextRequest
        @return: GetCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_custom_text_with_options(request, runtime)

    async def get_custom_text_async(
        self,
        request: ai_miao_bi_20230801_models.GetCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.GetCustomTextResponse:
        """
        @summary 获取自定义文本
        
        @param request: GetCustomTextRequest
        @return: GetCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_custom_text_with_options_async(request, runtime)

    def get_custom_topic_selection_perspective_analysis_task_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 获取自定义选题视角分析任务结果
        
        @param request: GetCustomTopicSelectionPerspectiveAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomTopicSelectionPerspectiveAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCustomTopicSelectionPerspectiveAnalysisTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_topic_selection_perspective_analysis_task_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 获取自定义选题视角分析任务结果
        
        @param request: GetCustomTopicSelectionPerspectiveAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomTopicSelectionPerspectiveAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCustomTopicSelectionPerspectiveAnalysisTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_topic_selection_perspective_analysis_task(
        self,
        request: ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 获取自定义选题视角分析任务结果
        
        @param request: GetCustomTopicSelectionPerspectiveAnalysisTaskRequest
        @return: GetCustomTopicSelectionPerspectiveAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_custom_topic_selection_perspective_analysis_task_with_options(request, runtime)

    async def get_custom_topic_selection_perspective_analysis_task_async(
        self,
        request: ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 获取自定义选题视角分析任务结果
        
        @param request: GetCustomTopicSelectionPerspectiveAnalysisTaskRequest
        @return: GetCustomTopicSelectionPerspectiveAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_custom_topic_selection_perspective_analysis_task_with_options_async(request, runtime)

    def get_data_source_order_config_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetDataSourceOrderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetDataSourceOrderConfigResponse:
        """
        @summary 获取系统数据源配置和个人配置
        
        @param request: GetDataSourceOrderConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataSourceOrderConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataSourceOrderConfig',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetDataSourceOrderConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_source_order_config_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetDataSourceOrderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetDataSourceOrderConfigResponse:
        """
        @summary 获取系统数据源配置和个人配置
        
        @param request: GetDataSourceOrderConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataSourceOrderConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataSourceOrderConfig',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetDataSourceOrderConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_source_order_config(
        self,
        request: ai_miao_bi_20230801_models.GetDataSourceOrderConfigRequest,
    ) -> ai_miao_bi_20230801_models.GetDataSourceOrderConfigResponse:
        """
        @summary 获取系统数据源配置和个人配置
        
        @param request: GetDataSourceOrderConfigRequest
        @return: GetDataSourceOrderConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_source_order_config_with_options(request, runtime)

    async def get_data_source_order_config_async(
        self,
        request: ai_miao_bi_20230801_models.GetDataSourceOrderConfigRequest,
    ) -> ai_miao_bi_20230801_models.GetDataSourceOrderConfigResponse:
        """
        @summary 获取系统数据源配置和个人配置
        
        @param request: GetDataSourceOrderConfigRequest
        @return: GetDataSourceOrderConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_data_source_order_config_with_options_async(request, runtime)

    def get_dataset_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetDatasetResponse:
        """
        @summary 数据集管理-详情
        
        @param request: GetDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataset',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetDatasetResponse:
        """
        @summary 数据集管理-详情
        
        @param request: GetDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataset',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset(
        self,
        request: ai_miao_bi_20230801_models.GetDatasetRequest,
    ) -> ai_miao_bi_20230801_models.GetDatasetResponse:
        """
        @summary 数据集管理-详情
        
        @param request: GetDatasetRequest
        @return: GetDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dataset_with_options(request, runtime)

    async def get_dataset_async(
        self,
        request: ai_miao_bi_20230801_models.GetDatasetRequest,
    ) -> ai_miao_bi_20230801_models.GetDatasetResponse:
        """
        @summary 数据集管理-详情
        
        @param request: GetDatasetRequest
        @return: GetDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dataset_with_options_async(request, runtime)

    def get_dataset_document_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetDatasetDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetDatasetDocumentResponse:
        """
        @summary 获取数据集文档
        
        @param request: GetDatasetDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.doc_uuid):
            body['DocUuid'] = request.doc_uuid
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDatasetDocument',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetDatasetDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_document_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetDatasetDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetDatasetDocumentResponse:
        """
        @summary 获取数据集文档
        
        @param request: GetDatasetDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.doc_uuid):
            body['DocUuid'] = request.doc_uuid
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDatasetDocument',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetDatasetDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset_document(
        self,
        request: ai_miao_bi_20230801_models.GetDatasetDocumentRequest,
    ) -> ai_miao_bi_20230801_models.GetDatasetDocumentResponse:
        """
        @summary 获取数据集文档
        
        @param request: GetDatasetDocumentRequest
        @return: GetDatasetDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dataset_document_with_options(request, runtime)

    async def get_dataset_document_async(
        self,
        request: ai_miao_bi_20230801_models.GetDatasetDocumentRequest,
    ) -> ai_miao_bi_20230801_models.GetDatasetDocumentResponse:
        """
        @summary 获取数据集文档
        
        @param request: GetDatasetDocumentRequest
        @return: GetDatasetDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dataset_document_with_options_async(request, runtime)

    def get_doc_cluster_task_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetDocClusterTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetDocClusterTaskResponse:
        """
        @summary 获取文档聚合任务结果
        
        @param request: GetDocClusterTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocClusterTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocClusterTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetDocClusterTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doc_cluster_task_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetDocClusterTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetDocClusterTaskResponse:
        """
        @summary 获取文档聚合任务结果
        
        @param request: GetDocClusterTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocClusterTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocClusterTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetDocClusterTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doc_cluster_task(
        self,
        request: ai_miao_bi_20230801_models.GetDocClusterTaskRequest,
    ) -> ai_miao_bi_20230801_models.GetDocClusterTaskResponse:
        """
        @summary 获取文档聚合任务结果
        
        @param request: GetDocClusterTaskRequest
        @return: GetDocClusterTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doc_cluster_task_with_options(request, runtime)

    async def get_doc_cluster_task_async(
        self,
        request: ai_miao_bi_20230801_models.GetDocClusterTaskRequest,
    ) -> ai_miao_bi_20230801_models.GetDocClusterTaskResponse:
        """
        @summary 获取文档聚合任务结果
        
        @param request: GetDocClusterTaskRequest
        @return: GetDocClusterTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doc_cluster_task_with_options_async(request, runtime)

    def get_doc_info_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetDocInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetDocInfoResponse:
        """
        @summary 妙读获取文档信息
        
        @param request: GetDocInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocInfo',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetDocInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doc_info_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetDocInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetDocInfoResponse:
        """
        @summary 妙读获取文档信息
        
        @param request: GetDocInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocInfo',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetDocInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doc_info(
        self,
        request: ai_miao_bi_20230801_models.GetDocInfoRequest,
    ) -> ai_miao_bi_20230801_models.GetDocInfoResponse:
        """
        @summary 妙读获取文档信息
        
        @param request: GetDocInfoRequest
        @return: GetDocInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doc_info_with_options(request, runtime)

    async def get_doc_info_async(
        self,
        request: ai_miao_bi_20230801_models.GetDocInfoRequest,
    ) -> ai_miao_bi_20230801_models.GetDocInfoResponse:
        """
        @summary 妙读获取文档信息
        
        @param request: GetDocInfoRequest
        @return: GetDocInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doc_info_with_options_async(request, runtime)

    def get_enterprise_voc_analysis_task_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetEnterpriseVocAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetEnterpriseVocAnalysisTaskResponse:
        """
        @summary 获取企业VOC分析任务结果
        
        @param request: GetEnterpriseVocAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnterpriseVocAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEnterpriseVocAnalysisTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetEnterpriseVocAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_enterprise_voc_analysis_task_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetEnterpriseVocAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetEnterpriseVocAnalysisTaskResponse:
        """
        @summary 获取企业VOC分析任务结果
        
        @param request: GetEnterpriseVocAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnterpriseVocAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEnterpriseVocAnalysisTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetEnterpriseVocAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_enterprise_voc_analysis_task(
        self,
        request: ai_miao_bi_20230801_models.GetEnterpriseVocAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.GetEnterpriseVocAnalysisTaskResponse:
        """
        @summary 获取企业VOC分析任务结果
        
        @param request: GetEnterpriseVocAnalysisTaskRequest
        @return: GetEnterpriseVocAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_enterprise_voc_analysis_task_with_options(request, runtime)

    async def get_enterprise_voc_analysis_task_async(
        self,
        request: ai_miao_bi_20230801_models.GetEnterpriseVocAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.GetEnterpriseVocAnalysisTaskResponse:
        """
        @summary 获取企业VOC分析任务结果
        
        @param request: GetEnterpriseVocAnalysisTaskRequest
        @return: GetEnterpriseVocAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_enterprise_voc_analysis_task_with_options_async(request, runtime)

    def get_generated_content_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetGeneratedContentResponse:
        """
        @summary 文档管理-查询详情。
        
        @param request: GetGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGeneratedContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetGeneratedContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_generated_content_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetGeneratedContentResponse:
        """
        @summary 文档管理-查询详情。
        
        @param request: GetGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGeneratedContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetGeneratedContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_generated_content(
        self,
        request: ai_miao_bi_20230801_models.GetGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.GetGeneratedContentResponse:
        """
        @summary 文档管理-查询详情。
        
        @param request: GetGeneratedContentRequest
        @return: GetGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_generated_content_with_options(request, runtime)

    async def get_generated_content_async(
        self,
        request: ai_miao_bi_20230801_models.GetGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.GetGeneratedContentResponse:
        """
        @summary 文档管理-查询详情。
        
        @param request: GetGeneratedContentRequest
        @return: GetGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_generated_content_with_options_async(request, runtime)

    def get_hot_topic_broadcast_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.GetHotTopicBroadcastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetHotTopicBroadcastResponse:
        """
        @summary 查询新闻播报单
        
        @param tmp_req: GetHotTopicBroadcastRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotTopicBroadcastResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.GetHotTopicBroadcastShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.locations):
            request.locations_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.locations, 'Locations', 'json')
        if not UtilClient.is_unset(tmp_req.step_for_custom_summary_style_config):
            request.step_for_custom_summary_style_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.step_for_custom_summary_style_config, 'StepForCustomSummaryStyleConfig', 'json')
        if not UtilClient.is_unset(tmp_req.step_for_news_broadcast_content_config):
            request.step_for_news_broadcast_content_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.step_for_news_broadcast_content_config, 'StepForNewsBroadcastContentConfig', 'json')
        if not UtilClient.is_unset(tmp_req.topics):
            request.topics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        body = {}
        if not UtilClient.is_unset(request.calc_total_token):
            body['CalcTotalToken'] = request.calc_total_token
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.hot_topic_version):
            body['HotTopicVersion'] = request.hot_topic_version
        if not UtilClient.is_unset(request.location_query):
            body['LocationQuery'] = request.location_query
        if not UtilClient.is_unset(request.locations_shrink):
            body['Locations'] = request.locations_shrink
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.step_for_custom_summary_style_config_shrink):
            body['StepForCustomSummaryStyleConfig'] = request.step_for_custom_summary_style_config_shrink
        if not UtilClient.is_unset(request.step_for_news_broadcast_content_config_shrink):
            body['StepForNewsBroadcastContentConfig'] = request.step_for_news_broadcast_content_config_shrink
        if not UtilClient.is_unset(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotTopicBroadcast',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetHotTopicBroadcastResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hot_topic_broadcast_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.GetHotTopicBroadcastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetHotTopicBroadcastResponse:
        """
        @summary 查询新闻播报单
        
        @param tmp_req: GetHotTopicBroadcastRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotTopicBroadcastResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.GetHotTopicBroadcastShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.locations):
            request.locations_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.locations, 'Locations', 'json')
        if not UtilClient.is_unset(tmp_req.step_for_custom_summary_style_config):
            request.step_for_custom_summary_style_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.step_for_custom_summary_style_config, 'StepForCustomSummaryStyleConfig', 'json')
        if not UtilClient.is_unset(tmp_req.step_for_news_broadcast_content_config):
            request.step_for_news_broadcast_content_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.step_for_news_broadcast_content_config, 'StepForNewsBroadcastContentConfig', 'json')
        if not UtilClient.is_unset(tmp_req.topics):
            request.topics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        body = {}
        if not UtilClient.is_unset(request.calc_total_token):
            body['CalcTotalToken'] = request.calc_total_token
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.hot_topic_version):
            body['HotTopicVersion'] = request.hot_topic_version
        if not UtilClient.is_unset(request.location_query):
            body['LocationQuery'] = request.location_query
        if not UtilClient.is_unset(request.locations_shrink):
            body['Locations'] = request.locations_shrink
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.step_for_custom_summary_style_config_shrink):
            body['StepForCustomSummaryStyleConfig'] = request.step_for_custom_summary_style_config_shrink
        if not UtilClient.is_unset(request.step_for_news_broadcast_content_config_shrink):
            body['StepForNewsBroadcastContentConfig'] = request.step_for_news_broadcast_content_config_shrink
        if not UtilClient.is_unset(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotTopicBroadcast',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetHotTopicBroadcastResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hot_topic_broadcast(
        self,
        request: ai_miao_bi_20230801_models.GetHotTopicBroadcastRequest,
    ) -> ai_miao_bi_20230801_models.GetHotTopicBroadcastResponse:
        """
        @summary 查询新闻播报单
        
        @param request: GetHotTopicBroadcastRequest
        @return: GetHotTopicBroadcastResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_hot_topic_broadcast_with_options(request, runtime)

    async def get_hot_topic_broadcast_async(
        self,
        request: ai_miao_bi_20230801_models.GetHotTopicBroadcastRequest,
    ) -> ai_miao_bi_20230801_models.GetHotTopicBroadcastResponse:
        """
        @summary 查询新闻播报单
        
        @param request: GetHotTopicBroadcastRequest
        @return: GetHotTopicBroadcastResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_hot_topic_broadcast_with_options_async(request, runtime)

    def get_intervene_global_reply_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneGlobalReplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneGlobalReplyResponse:
        """
        @summary 获得干预全局回复
        
        @param request: GetInterveneGlobalReplyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInterveneGlobalReplyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInterveneGlobalReply',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetInterveneGlobalReplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_intervene_global_reply_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneGlobalReplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneGlobalReplyResponse:
        """
        @summary 获得干预全局回复
        
        @param request: GetInterveneGlobalReplyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInterveneGlobalReplyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInterveneGlobalReply',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetInterveneGlobalReplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_intervene_global_reply(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneGlobalReplyRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneGlobalReplyResponse:
        """
        @summary 获得干预全局回复
        
        @param request: GetInterveneGlobalReplyRequest
        @return: GetInterveneGlobalReplyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_intervene_global_reply_with_options(request, runtime)

    async def get_intervene_global_reply_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneGlobalReplyRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneGlobalReplyResponse:
        """
        @summary 获得干预全局回复
        
        @param request: GetInterveneGlobalReplyRequest
        @return: GetInterveneGlobalReplyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_intervene_global_reply_with_options_async(request, runtime)

    def get_intervene_import_task_info_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneImportTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneImportTaskInfoResponse:
        """
        @summary 获得导入任务信息
        
        @param request: GetInterveneImportTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInterveneImportTaskInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInterveneImportTaskInfo',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetInterveneImportTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_intervene_import_task_info_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneImportTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneImportTaskInfoResponse:
        """
        @summary 获得导入任务信息
        
        @param request: GetInterveneImportTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInterveneImportTaskInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInterveneImportTaskInfo',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetInterveneImportTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_intervene_import_task_info(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneImportTaskInfoRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneImportTaskInfoResponse:
        """
        @summary 获得导入任务信息
        
        @param request: GetInterveneImportTaskInfoRequest
        @return: GetInterveneImportTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_intervene_import_task_info_with_options(request, runtime)

    async def get_intervene_import_task_info_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneImportTaskInfoRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneImportTaskInfoResponse:
        """
        @summary 获得导入任务信息
        
        @param request: GetInterveneImportTaskInfoRequest
        @return: GetInterveneImportTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_intervene_import_task_info_with_options_async(request, runtime)

    def get_intervene_rule_detail_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneRuleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneRuleDetailResponse:
        """
        @summary 获得干预项规则详情
        
        @param request: GetInterveneRuleDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInterveneRuleDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInterveneRuleDetail',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetInterveneRuleDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_intervene_rule_detail_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneRuleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneRuleDetailResponse:
        """
        @summary 获得干预项规则详情
        
        @param request: GetInterveneRuleDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInterveneRuleDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInterveneRuleDetail',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetInterveneRuleDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_intervene_rule_detail(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneRuleDetailRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneRuleDetailResponse:
        """
        @summary 获得干预项规则详情
        
        @param request: GetInterveneRuleDetailRequest
        @return: GetInterveneRuleDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_intervene_rule_detail_with_options(request, runtime)

    async def get_intervene_rule_detail_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneRuleDetailRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneRuleDetailResponse:
        """
        @summary 获得干预项规则详情
        
        @param request: GetInterveneRuleDetailRequest
        @return: GetInterveneRuleDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_intervene_rule_detail_with_options_async(request, runtime)

    def get_intervene_template_file_url_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlResponse:
        """
        @summary 获得干预导入模版文件下载地址
        
        @param request: GetInterveneTemplateFileUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInterveneTemplateFileUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInterveneTemplateFileUrl',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_intervene_template_file_url_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlResponse:
        """
        @summary 获得干预导入模版文件下载地址
        
        @param request: GetInterveneTemplateFileUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInterveneTemplateFileUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInterveneTemplateFileUrl',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_intervene_template_file_url(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlResponse:
        """
        @summary 获得干预导入模版文件下载地址
        
        @param request: GetInterveneTemplateFileUrlRequest
        @return: GetInterveneTemplateFileUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_intervene_template_file_url_with_options(request, runtime)

    async def get_intervene_template_file_url_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlResponse:
        """
        @summary 获得干预导入模版文件下载地址
        
        @param request: GetInterveneTemplateFileUrlRequest
        @return: GetInterveneTemplateFileUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_intervene_template_file_url_with_options_async(request, runtime)

    def get_material_by_id_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetMaterialByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetMaterialByIdResponse:
        """
        @summary 根据ID获取素材内容
        
        @param request: GetMaterialByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMaterialByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMaterialById',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetMaterialByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_material_by_id_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetMaterialByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetMaterialByIdResponse:
        """
        @summary 根据ID获取素材内容
        
        @param request: GetMaterialByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMaterialByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMaterialById',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetMaterialByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_material_by_id(
        self,
        request: ai_miao_bi_20230801_models.GetMaterialByIdRequest,
    ) -> ai_miao_bi_20230801_models.GetMaterialByIdResponse:
        """
        @summary 根据ID获取素材内容
        
        @param request: GetMaterialByIdRequest
        @return: GetMaterialByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_material_by_id_with_options(request, runtime)

    async def get_material_by_id_async(
        self,
        request: ai_miao_bi_20230801_models.GetMaterialByIdRequest,
    ) -> ai_miao_bi_20230801_models.GetMaterialByIdResponse:
        """
        @summary 根据ID获取素材内容
        
        @param request: GetMaterialByIdRequest
        @return: GetMaterialByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_material_by_id_with_options_async(request, runtime)

    def get_properties_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetPropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetPropertiesResponse:
        """
        @summary 获取当前用户的配置
        
        @param request: GetPropertiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPropertiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProperties',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetPropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_properties_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetPropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetPropertiesResponse:
        """
        @summary 获取当前用户的配置
        
        @param request: GetPropertiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPropertiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProperties',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetPropertiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_properties(
        self,
        request: ai_miao_bi_20230801_models.GetPropertiesRequest,
    ) -> ai_miao_bi_20230801_models.GetPropertiesResponse:
        """
        @summary 获取当前用户的配置
        
        @param request: GetPropertiesRequest
        @return: GetPropertiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_properties_with_options(request, runtime)

    async def get_properties_async(
        self,
        request: ai_miao_bi_20230801_models.GetPropertiesRequest,
    ) -> ai_miao_bi_20230801_models.GetPropertiesResponse:
        """
        @summary 获取当前用户的配置
        
        @param request: GetPropertiesRequest
        @return: GetPropertiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_properties_with_options_async(request, runtime)

    def get_smart_clip_task_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetSmartClipTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetSmartClipTaskResponse:
        """
        @summary 查询一键成片剪辑任务
        
        @param request: GetSmartClipTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSmartClipTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSmartClipTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetSmartClipTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_smart_clip_task_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetSmartClipTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetSmartClipTaskResponse:
        """
        @summary 查询一键成片剪辑任务
        
        @param request: GetSmartClipTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSmartClipTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSmartClipTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetSmartClipTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_smart_clip_task(
        self,
        request: ai_miao_bi_20230801_models.GetSmartClipTaskRequest,
    ) -> ai_miao_bi_20230801_models.GetSmartClipTaskResponse:
        """
        @summary 查询一键成片剪辑任务
        
        @param request: GetSmartClipTaskRequest
        @return: GetSmartClipTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_smart_clip_task_with_options(request, runtime)

    async def get_smart_clip_task_async(
        self,
        request: ai_miao_bi_20230801_models.GetSmartClipTaskRequest,
    ) -> ai_miao_bi_20230801_models.GetSmartClipTaskResponse:
        """
        @summary 查询一键成片剪辑任务
        
        @param request: GetSmartClipTaskRequest
        @return: GetSmartClipTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_smart_clip_task_with_options_async(request, runtime)

    def get_topic_by_id_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetTopicByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetTopicByIdResponse:
        """
        @summary 根据ID获取热点事件信息
        
        @param request: GetTopicByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTopicById',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetTopicByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_by_id_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetTopicByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetTopicByIdResponse:
        """
        @summary 根据ID获取热点事件信息
        
        @param request: GetTopicByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTopicById',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetTopicByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic_by_id(
        self,
        request: ai_miao_bi_20230801_models.GetTopicByIdRequest,
    ) -> ai_miao_bi_20230801_models.GetTopicByIdResponse:
        """
        @summary 根据ID获取热点事件信息
        
        @param request: GetTopicByIdRequest
        @return: GetTopicByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_topic_by_id_with_options(request, runtime)

    async def get_topic_by_id_async(
        self,
        request: ai_miao_bi_20230801_models.GetTopicByIdRequest,
    ) -> ai_miao_bi_20230801_models.GetTopicByIdResponse:
        """
        @summary 根据ID获取热点事件信息
        
        @param request: GetTopicByIdRequest
        @return: GetTopicByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_by_id_with_options_async(request, runtime)

    def get_topic_selection_perspective_analysis_task_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 获取选题视角分析任务结果
        
        @param request: GetTopicSelectionPerspectiveAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicSelectionPerspectiveAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTopicSelectionPerspectiveAnalysisTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_selection_perspective_analysis_task_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 获取选题视角分析任务结果
        
        @param request: GetTopicSelectionPerspectiveAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicSelectionPerspectiveAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTopicSelectionPerspectiveAnalysisTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic_selection_perspective_analysis_task(
        self,
        request: ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 获取选题视角分析任务结果
        
        @param request: GetTopicSelectionPerspectiveAnalysisTaskRequest
        @return: GetTopicSelectionPerspectiveAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_topic_selection_perspective_analysis_task_with_options(request, runtime)

    async def get_topic_selection_perspective_analysis_task_async(
        self,
        request: ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 获取选题视角分析任务结果
        
        @param request: GetTopicSelectionPerspectiveAnalysisTaskRequest
        @return: GetTopicSelectionPerspectiveAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_selection_perspective_analysis_task_with_options_async(request, runtime)

    def import_intervene_file_with_options(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileResponse:
        """
        @summary 导入干预文件
        
        @param request: ImportInterveneFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportInterveneFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.doc_name):
            body['DocName'] = request.doc_name
        if not UtilClient.is_unset(request.file_key):
            body['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportInterveneFile',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ImportInterveneFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_intervene_file_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileResponse:
        """
        @summary 导入干预文件
        
        @param request: ImportInterveneFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportInterveneFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.doc_name):
            body['DocName'] = request.doc_name
        if not UtilClient.is_unset(request.file_key):
            body['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportInterveneFile',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ImportInterveneFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_intervene_file(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileRequest,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileResponse:
        """
        @summary 导入干预文件
        
        @param request: ImportInterveneFileRequest
        @return: ImportInterveneFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_intervene_file_with_options(request, runtime)

    async def import_intervene_file_async(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileRequest,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileResponse:
        """
        @summary 导入干预文件
        
        @param request: ImportInterveneFileRequest
        @return: ImportInterveneFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_intervene_file_with_options_async(request, runtime)

    def import_intervene_file_async_with_options(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileAsyncResponse:
        """
        @summary 异步导入干预文件
        
        @param request: ImportInterveneFileAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportInterveneFileAsyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.doc_name):
            body['DocName'] = request.doc_name
        if not UtilClient.is_unset(request.file_key):
            body['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportInterveneFileAsync',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ImportInterveneFileAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_intervene_file_async_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileAsyncResponse:
        """
        @summary 异步导入干预文件
        
        @param request: ImportInterveneFileAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportInterveneFileAsyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.doc_name):
            body['DocName'] = request.doc_name
        if not UtilClient.is_unset(request.file_key):
            body['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportInterveneFileAsync',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ImportInterveneFileAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_intervene_file_async(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileAsyncRequest,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileAsyncResponse:
        """
        @summary 异步导入干预文件
        
        @param request: ImportInterveneFileAsyncRequest
        @return: ImportInterveneFileAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_intervene_file_async_with_options(request, runtime)

    async def import_intervene_file_async_async(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileAsyncRequest,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileAsyncResponse:
        """
        @summary 异步导入干预文件
        
        @param request: ImportInterveneFileAsyncRequest
        @return: ImportInterveneFileAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_intervene_file_async_with_options_async(request, runtime)

    def insert_intervene_global_reply_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.InsertInterveneGlobalReplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.InsertInterveneGlobalReplyResponse:
        """
        @summary 设置干预全局回复
        
        @param tmp_req: InsertInterveneGlobalReplyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertInterveneGlobalReplyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.InsertInterveneGlobalReplyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reply_messag_list):
            request.reply_messag_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reply_messag_list, 'ReplyMessagList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.reply_messag_list_shrink):
            body['ReplyMessagList'] = request.reply_messag_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertInterveneGlobalReply',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.InsertInterveneGlobalReplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_intervene_global_reply_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.InsertInterveneGlobalReplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.InsertInterveneGlobalReplyResponse:
        """
        @summary 设置干预全局回复
        
        @param tmp_req: InsertInterveneGlobalReplyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertInterveneGlobalReplyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.InsertInterveneGlobalReplyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reply_messag_list):
            request.reply_messag_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reply_messag_list, 'ReplyMessagList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.reply_messag_list_shrink):
            body['ReplyMessagList'] = request.reply_messag_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertInterveneGlobalReply',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.InsertInterveneGlobalReplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_intervene_global_reply(
        self,
        request: ai_miao_bi_20230801_models.InsertInterveneGlobalReplyRequest,
    ) -> ai_miao_bi_20230801_models.InsertInterveneGlobalReplyResponse:
        """
        @summary 设置干预全局回复
        
        @param request: InsertInterveneGlobalReplyRequest
        @return: InsertInterveneGlobalReplyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.insert_intervene_global_reply_with_options(request, runtime)

    async def insert_intervene_global_reply_async(
        self,
        request: ai_miao_bi_20230801_models.InsertInterveneGlobalReplyRequest,
    ) -> ai_miao_bi_20230801_models.InsertInterveneGlobalReplyResponse:
        """
        @summary 设置干预全局回复
        
        @param request: InsertInterveneGlobalReplyRequest
        @return: InsertInterveneGlobalReplyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.insert_intervene_global_reply_with_options_async(request, runtime)

    def insert_intervene_rule_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.InsertInterveneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.InsertInterveneRuleResponse:
        """
        @summary 插入干预规则
        
        @param tmp_req: InsertInterveneRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertInterveneRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.InsertInterveneRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intervene_rule_config):
            request.intervene_rule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.intervene_rule_config, 'InterveneRuleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.intervene_rule_config_shrink):
            body['InterveneRuleConfig'] = request.intervene_rule_config_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertInterveneRule',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.InsertInterveneRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_intervene_rule_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.InsertInterveneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.InsertInterveneRuleResponse:
        """
        @summary 插入干预规则
        
        @param tmp_req: InsertInterveneRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertInterveneRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.InsertInterveneRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intervene_rule_config):
            request.intervene_rule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.intervene_rule_config, 'InterveneRuleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.intervene_rule_config_shrink):
            body['InterveneRuleConfig'] = request.intervene_rule_config_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertInterveneRule',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.InsertInterveneRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_intervene_rule(
        self,
        request: ai_miao_bi_20230801_models.InsertInterveneRuleRequest,
    ) -> ai_miao_bi_20230801_models.InsertInterveneRuleResponse:
        """
        @summary 插入干预规则
        
        @param request: InsertInterveneRuleRequest
        @return: InsertInterveneRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.insert_intervene_rule_with_options(request, runtime)

    async def insert_intervene_rule_async(
        self,
        request: ai_miao_bi_20230801_models.InsertInterveneRuleRequest,
    ) -> ai_miao_bi_20230801_models.InsertInterveneRuleResponse:
        """
        @summary 插入干预规则
        
        @param request: InsertInterveneRuleRequest
        @return: InsertInterveneRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.insert_intervene_rule_with_options_async(request, runtime)

    def list_analysis_tag_detail_by_task_id_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListAnalysisTagDetailByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListAnalysisTagDetailByTaskIdResponse:
        """
        @summary 分页获取企业VOC分析任务明细列表
        
        @param tmp_req: ListAnalysisTagDetailByTaskIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAnalysisTagDetailByTaskIdResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListAnalysisTagDetailByTaskIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.categories):
            request.categories_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        body = {}
        if not UtilClient.is_unset(request.categories_shrink):
            body['Categories'] = request.categories_shrink
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAnalysisTagDetailByTaskId',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListAnalysisTagDetailByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_analysis_tag_detail_by_task_id_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListAnalysisTagDetailByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListAnalysisTagDetailByTaskIdResponse:
        """
        @summary 分页获取企业VOC分析任务明细列表
        
        @param tmp_req: ListAnalysisTagDetailByTaskIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAnalysisTagDetailByTaskIdResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListAnalysisTagDetailByTaskIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.categories):
            request.categories_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        body = {}
        if not UtilClient.is_unset(request.categories_shrink):
            body['Categories'] = request.categories_shrink
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAnalysisTagDetailByTaskId',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListAnalysisTagDetailByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_analysis_tag_detail_by_task_id(
        self,
        request: ai_miao_bi_20230801_models.ListAnalysisTagDetailByTaskIdRequest,
    ) -> ai_miao_bi_20230801_models.ListAnalysisTagDetailByTaskIdResponse:
        """
        @summary 分页获取企业VOC分析任务明细列表
        
        @param request: ListAnalysisTagDetailByTaskIdRequest
        @return: ListAnalysisTagDetailByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_analysis_tag_detail_by_task_id_with_options(request, runtime)

    async def list_analysis_tag_detail_by_task_id_async(
        self,
        request: ai_miao_bi_20230801_models.ListAnalysisTagDetailByTaskIdRequest,
    ) -> ai_miao_bi_20230801_models.ListAnalysisTagDetailByTaskIdResponse:
        """
        @summary 分页获取企业VOC分析任务明细列表
        
        @param request: ListAnalysisTagDetailByTaskIdRequest
        @return: ListAnalysisTagDetailByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_analysis_tag_detail_by_task_id_with_options_async(request, runtime)

    def list_async_tasks_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListAsyncTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListAsyncTasksResponse:
        """
        @summary 查询任务列表
        
        @param tmp_req: ListAsyncTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAsyncTasksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListAsyncTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_status_list):
            request.task_status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_status_list, 'TaskStatusList', 'json')
        if not UtilClient.is_unset(tmp_req.task_type_list):
            request.task_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_type_list, 'TaskTypeList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.task_code):
            body['TaskCode'] = request.task_code
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.task_status_list_shrink):
            body['TaskStatusList'] = request.task_status_list_shrink
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.task_type_list_shrink):
            body['TaskTypeList'] = request.task_type_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAsyncTasks',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListAsyncTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_async_tasks_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListAsyncTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListAsyncTasksResponse:
        """
        @summary 查询任务列表
        
        @param tmp_req: ListAsyncTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAsyncTasksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListAsyncTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_status_list):
            request.task_status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_status_list, 'TaskStatusList', 'json')
        if not UtilClient.is_unset(tmp_req.task_type_list):
            request.task_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_type_list, 'TaskTypeList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.task_code):
            body['TaskCode'] = request.task_code
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.task_status_list_shrink):
            body['TaskStatusList'] = request.task_status_list_shrink
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.task_type_list_shrink):
            body['TaskTypeList'] = request.task_type_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAsyncTasks',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListAsyncTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_async_tasks(
        self,
        request: ai_miao_bi_20230801_models.ListAsyncTasksRequest,
    ) -> ai_miao_bi_20230801_models.ListAsyncTasksResponse:
        """
        @summary 查询任务列表
        
        @param request: ListAsyncTasksRequest
        @return: ListAsyncTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_async_tasks_with_options(request, runtime)

    async def list_async_tasks_async(
        self,
        request: ai_miao_bi_20230801_models.ListAsyncTasksRequest,
    ) -> ai_miao_bi_20230801_models.ListAsyncTasksResponse:
        """
        @summary 查询任务列表
        
        @param request: ListAsyncTasksRequest
        @return: ListAsyncTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_async_tasks_with_options_async(request, runtime)

    def list_build_configs_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListBuildConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListBuildConfigsResponse:
        """
        @summary 获取系统自定义预设
        
        @param request: ListBuildConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBuildConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBuildConfigs',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListBuildConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_build_configs_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListBuildConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListBuildConfigsResponse:
        """
        @summary 获取系统自定义预设
        
        @param request: ListBuildConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBuildConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBuildConfigs',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListBuildConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_build_configs(
        self,
        request: ai_miao_bi_20230801_models.ListBuildConfigsRequest,
    ) -> ai_miao_bi_20230801_models.ListBuildConfigsResponse:
        """
        @summary 获取系统自定义预设
        
        @param request: ListBuildConfigsRequest
        @return: ListBuildConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_build_configs_with_options(request, runtime)

    async def list_build_configs_async(
        self,
        request: ai_miao_bi_20230801_models.ListBuildConfigsRequest,
    ) -> ai_miao_bi_20230801_models.ListBuildConfigsResponse:
        """
        @summary 获取系统自定义预设
        
        @param request: ListBuildConfigsRequest
        @return: ListBuildConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_build_configs_with_options_async(request, runtime)

    def list_custom_text_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListCustomTextResponse:
        """
        @summary 自定义文本列表
        
        @param request: ListCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCustomText',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListCustomTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_text_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListCustomTextResponse:
        """
        @summary 自定义文本列表
        
        @param request: ListCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCustomText',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListCustomTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_text(
        self,
        request: ai_miao_bi_20230801_models.ListCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.ListCustomTextResponse:
        """
        @summary 自定义文本列表
        
        @param request: ListCustomTextRequest
        @return: ListCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_text_with_options(request, runtime)

    async def list_custom_text_async(
        self,
        request: ai_miao_bi_20230801_models.ListCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.ListCustomTextResponse:
        """
        @summary 自定义文本列表
        
        @param request: ListCustomTextRequest
        @return: ListCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_text_with_options_async(request, runtime)

    def list_custom_view_points_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListCustomViewPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListCustomViewPointsResponse:
        """
        @summary 自定义视角列表
        
        @param tmp_req: ListCustomViewPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomViewPointsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListCustomViewPointsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attitudes):
            request.attitudes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attitudes, 'Attitudes', 'json')
        if not UtilClient.is_unset(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.attitude):
            body['Attitude'] = request.attitude
        if not UtilClient.is_unset(request.attitudes_shrink):
            body['Attitudes'] = request.attitudes_shrink
        if not UtilClient.is_unset(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        if not UtilClient.is_unset(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_id):
            body['TopicId'] = request.topic_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCustomViewPoints',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListCustomViewPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_view_points_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListCustomViewPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListCustomViewPointsResponse:
        """
        @summary 自定义视角列表
        
        @param tmp_req: ListCustomViewPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomViewPointsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListCustomViewPointsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attitudes):
            request.attitudes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attitudes, 'Attitudes', 'json')
        if not UtilClient.is_unset(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.attitude):
            body['Attitude'] = request.attitude
        if not UtilClient.is_unset(request.attitudes_shrink):
            body['Attitudes'] = request.attitudes_shrink
        if not UtilClient.is_unset(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        if not UtilClient.is_unset(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_id):
            body['TopicId'] = request.topic_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCustomViewPoints',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListCustomViewPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_view_points(
        self,
        request: ai_miao_bi_20230801_models.ListCustomViewPointsRequest,
    ) -> ai_miao_bi_20230801_models.ListCustomViewPointsResponse:
        """
        @summary 自定义视角列表
        
        @param request: ListCustomViewPointsRequest
        @return: ListCustomViewPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_view_points_with_options(request, runtime)

    async def list_custom_view_points_async(
        self,
        request: ai_miao_bi_20230801_models.ListCustomViewPointsRequest,
    ) -> ai_miao_bi_20230801_models.ListCustomViewPointsResponse:
        """
        @summary 自定义视角列表
        
        @param request: ListCustomViewPointsRequest
        @return: ListCustomViewPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_view_points_with_options_async(request, runtime)

    def list_dataset_documents_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListDatasetDocumentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListDatasetDocumentsResponse:
        """
        @summary 查询数据集文档列表
        
        @param tmp_req: ListDatasetDocumentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetDocumentsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListDatasetDocumentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.exclude_fields):
            request.exclude_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exclude_fields, 'ExcludeFields', 'json')
        if not UtilClient.is_unset(tmp_req.include_fields):
            request.include_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.include_fields, 'IncludeFields', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_description):
            body['DatasetDescription'] = request.dataset_description
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.exclude_fields_shrink):
            body['ExcludeFields'] = request.exclude_fields_shrink
        if not UtilClient.is_unset(request.include_fields_shrink):
            body['IncludeFields'] = request.include_fields_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDatasetDocuments',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListDatasetDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dataset_documents_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListDatasetDocumentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListDatasetDocumentsResponse:
        """
        @summary 查询数据集文档列表
        
        @param tmp_req: ListDatasetDocumentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetDocumentsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListDatasetDocumentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.exclude_fields):
            request.exclude_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exclude_fields, 'ExcludeFields', 'json')
        if not UtilClient.is_unset(tmp_req.include_fields):
            request.include_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.include_fields, 'IncludeFields', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_description):
            body['DatasetDescription'] = request.dataset_description
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.exclude_fields_shrink):
            body['ExcludeFields'] = request.exclude_fields_shrink
        if not UtilClient.is_unset(request.include_fields_shrink):
            body['IncludeFields'] = request.include_fields_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDatasetDocuments',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListDatasetDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dataset_documents(
        self,
        request: ai_miao_bi_20230801_models.ListDatasetDocumentsRequest,
    ) -> ai_miao_bi_20230801_models.ListDatasetDocumentsResponse:
        """
        @summary 查询数据集文档列表
        
        @param request: ListDatasetDocumentsRequest
        @return: ListDatasetDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dataset_documents_with_options(request, runtime)

    async def list_dataset_documents_async(
        self,
        request: ai_miao_bi_20230801_models.ListDatasetDocumentsRequest,
    ) -> ai_miao_bi_20230801_models.ListDatasetDocumentsResponse:
        """
        @summary 查询数据集文档列表
        
        @param request: ListDatasetDocumentsRequest
        @return: ListDatasetDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dataset_documents_with_options_async(request, runtime)

    def list_datasets_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListDatasetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListDatasetsResponse:
        """
        @summary 数据集管理-查询
        
        @param request: ListDatasetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.dataset_type):
            body['DatasetType'] = request.dataset_type
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_dataset_enable):
            body['SearchDatasetEnable'] = request.search_dataset_enable
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDatasets',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListDatasetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasets_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListDatasetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListDatasetsResponse:
        """
        @summary 数据集管理-查询
        
        @param request: ListDatasetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.dataset_type):
            body['DatasetType'] = request.dataset_type
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_dataset_enable):
            body['SearchDatasetEnable'] = request.search_dataset_enable
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDatasets',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListDatasetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasets(
        self,
        request: ai_miao_bi_20230801_models.ListDatasetsRequest,
    ) -> ai_miao_bi_20230801_models.ListDatasetsResponse:
        """
        @summary 数据集管理-查询
        
        @param request: ListDatasetsRequest
        @return: ListDatasetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_datasets_with_options(request, runtime)

    async def list_datasets_async(
        self,
        request: ai_miao_bi_20230801_models.ListDatasetsRequest,
    ) -> ai_miao_bi_20230801_models.ListDatasetsResponse:
        """
        @summary 数据集管理-查询
        
        @param request: ListDatasetsRequest
        @return: ListDatasetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_datasets_with_options_async(request, runtime)

    def list_dialogues_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListDialoguesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListDialoguesResponse:
        """
        @summary 生成历史列表
        
        @param request: ListDialoguesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDialoguesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.dialogue_type):
            body['DialogueType'] = request.dialogue_type
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDialogues',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListDialoguesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dialogues_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListDialoguesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListDialoguesResponse:
        """
        @summary 生成历史列表
        
        @param request: ListDialoguesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDialoguesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.dialogue_type):
            body['DialogueType'] = request.dialogue_type
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDialogues',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListDialoguesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dialogues(
        self,
        request: ai_miao_bi_20230801_models.ListDialoguesRequest,
    ) -> ai_miao_bi_20230801_models.ListDialoguesResponse:
        """
        @summary 生成历史列表
        
        @param request: ListDialoguesRequest
        @return: ListDialoguesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dialogues_with_options(request, runtime)

    async def list_dialogues_async(
        self,
        request: ai_miao_bi_20230801_models.ListDialoguesRequest,
    ) -> ai_miao_bi_20230801_models.ListDialoguesResponse:
        """
        @summary 生成历史列表
        
        @param request: ListDialoguesRequest
        @return: ListDialoguesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dialogues_with_options_async(request, runtime)

    def list_docs_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListDocsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListDocsResponse:
        """
        @summary 妙读获取文档列表
        
        @param tmp_req: ListDocsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDocsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListDocsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.statuses):
            request.statuses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.statuses, 'Statuses', 'json')
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.doc_name):
            body['DocName'] = request.doc_name
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.skip):
            body['Skip'] = request.skip
        if not UtilClient.is_unset(request.statuses_shrink):
            body['Statuses'] = request.statuses_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDocs',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListDocsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_docs_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListDocsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListDocsResponse:
        """
        @summary 妙读获取文档列表
        
        @param tmp_req: ListDocsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDocsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListDocsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.statuses):
            request.statuses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.statuses, 'Statuses', 'json')
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.doc_name):
            body['DocName'] = request.doc_name
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.skip):
            body['Skip'] = request.skip
        if not UtilClient.is_unset(request.statuses_shrink):
            body['Statuses'] = request.statuses_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDocs',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListDocsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_docs(
        self,
        request: ai_miao_bi_20230801_models.ListDocsRequest,
    ) -> ai_miao_bi_20230801_models.ListDocsResponse:
        """
        @summary 妙读获取文档列表
        
        @param request: ListDocsRequest
        @return: ListDocsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_docs_with_options(request, runtime)

    async def list_docs_async(
        self,
        request: ai_miao_bi_20230801_models.ListDocsRequest,
    ) -> ai_miao_bi_20230801_models.ListDocsResponse:
        """
        @summary 妙读获取文档列表
        
        @param request: ListDocsRequest
        @return: ListDocsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_docs_with_options_async(request, runtime)

    def list_fresh_view_points_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListFreshViewPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListFreshViewPointsResponse:
        """
        @summary 新颖视角列表
        
        @param request: ListFreshViewPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFreshViewPointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFreshViewPoints',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListFreshViewPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fresh_view_points_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListFreshViewPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListFreshViewPointsResponse:
        """
        @summary 新颖视角列表
        
        @param request: ListFreshViewPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFreshViewPointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFreshViewPoints',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListFreshViewPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fresh_view_points(
        self,
        request: ai_miao_bi_20230801_models.ListFreshViewPointsRequest,
    ) -> ai_miao_bi_20230801_models.ListFreshViewPointsResponse:
        """
        @summary 新颖视角列表
        
        @param request: ListFreshViewPointsRequest
        @return: ListFreshViewPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_fresh_view_points_with_options(request, runtime)

    async def list_fresh_view_points_async(
        self,
        request: ai_miao_bi_20230801_models.ListFreshViewPointsRequest,
    ) -> ai_miao_bi_20230801_models.ListFreshViewPointsResponse:
        """
        @summary 新颖视角列表
        
        @param request: ListFreshViewPointsRequest
        @return: ListFreshViewPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_fresh_view_points_with_options_async(request, runtime)

    def list_generated_contents_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListGeneratedContentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListGeneratedContentsResponse:
        """
        @summary 文档管理-列表。
        
        @param request: ListGeneratedContentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGeneratedContentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content_domain):
            body['ContentDomain'] = request.content_domain
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGeneratedContents',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListGeneratedContentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_generated_contents_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListGeneratedContentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListGeneratedContentsResponse:
        """
        @summary 文档管理-列表。
        
        @param request: ListGeneratedContentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGeneratedContentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content_domain):
            body['ContentDomain'] = request.content_domain
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGeneratedContents',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListGeneratedContentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_generated_contents(
        self,
        request: ai_miao_bi_20230801_models.ListGeneratedContentsRequest,
    ) -> ai_miao_bi_20230801_models.ListGeneratedContentsResponse:
        """
        @summary 文档管理-列表。
        
        @param request: ListGeneratedContentsRequest
        @return: ListGeneratedContentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_generated_contents_with_options(request, runtime)

    async def list_generated_contents_async(
        self,
        request: ai_miao_bi_20230801_models.ListGeneratedContentsRequest,
    ) -> ai_miao_bi_20230801_models.ListGeneratedContentsResponse:
        """
        @summary 文档管理-列表。
        
        @param request: ListGeneratedContentsRequest
        @return: ListGeneratedContentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_generated_contents_with_options_async(request, runtime)

    def list_hot_news_with_type_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListHotNewsWithTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListHotNewsWithTypeResponse:
        """
        @summary 获取分类的热点新闻
        
        @param tmp_req: ListHotNewsWithTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotNewsWithTypeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListHotNewsWithTypeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.news_types):
            request.news_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.news_types, 'NewsTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.news_type):
            body['NewsType'] = request.news_type
        if not UtilClient.is_unset(request.news_types_shrink):
            body['NewsTypes'] = request.news_types_shrink
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotNewsWithType',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListHotNewsWithTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hot_news_with_type_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListHotNewsWithTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListHotNewsWithTypeResponse:
        """
        @summary 获取分类的热点新闻
        
        @param tmp_req: ListHotNewsWithTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotNewsWithTypeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListHotNewsWithTypeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.news_types):
            request.news_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.news_types, 'NewsTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.news_type):
            body['NewsType'] = request.news_type
        if not UtilClient.is_unset(request.news_types_shrink):
            body['NewsTypes'] = request.news_types_shrink
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotNewsWithType',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListHotNewsWithTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hot_news_with_type(
        self,
        request: ai_miao_bi_20230801_models.ListHotNewsWithTypeRequest,
    ) -> ai_miao_bi_20230801_models.ListHotNewsWithTypeResponse:
        """
        @summary 获取分类的热点新闻
        
        @param request: ListHotNewsWithTypeRequest
        @return: ListHotNewsWithTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hot_news_with_type_with_options(request, runtime)

    async def list_hot_news_with_type_async(
        self,
        request: ai_miao_bi_20230801_models.ListHotNewsWithTypeRequest,
    ) -> ai_miao_bi_20230801_models.ListHotNewsWithTypeResponse:
        """
        @summary 获取分类的热点新闻
        
        @param request: ListHotNewsWithTypeRequest
        @return: ListHotNewsWithTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_hot_news_with_type_with_options_async(request, runtime)

    def list_hot_sources_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListHotSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListHotSourcesResponse:
        """
        @summary 获取所有平台热榜源列表
        
        @param request: ListHotSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotSources',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListHotSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hot_sources_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListHotSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListHotSourcesResponse:
        """
        @summary 获取所有平台热榜源列表
        
        @param request: ListHotSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotSources',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListHotSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hot_sources(
        self,
        request: ai_miao_bi_20230801_models.ListHotSourcesRequest,
    ) -> ai_miao_bi_20230801_models.ListHotSourcesResponse:
        """
        @summary 获取所有平台热榜源列表
        
        @param request: ListHotSourcesRequest
        @return: ListHotSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hot_sources_with_options(request, runtime)

    async def list_hot_sources_async(
        self,
        request: ai_miao_bi_20230801_models.ListHotSourcesRequest,
    ) -> ai_miao_bi_20230801_models.ListHotSourcesResponse:
        """
        @summary 获取所有平台热榜源列表
        
        @param request: ListHotSourcesRequest
        @return: ListHotSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_hot_sources_with_options_async(request, runtime)

    def list_hot_topics_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListHotTopicsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListHotTopicsResponse:
        """
        @summary 获取热点事件列表
        
        @param tmp_req: ListHotTopicsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotTopicsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListHotTopicsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.topic_ids):
            request.topic_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topic_ids, 'TopicIds', 'json')
        if not UtilClient.is_unset(tmp_req.topics):
            request.topics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic_ids_shrink):
            body['TopicIds'] = request.topic_ids_shrink
        if not UtilClient.is_unset(request.topic_query):
            body['TopicQuery'] = request.topic_query
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not UtilClient.is_unset(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not UtilClient.is_unset(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not UtilClient.is_unset(request.with_news):
            body['WithNews'] = request.with_news
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotTopics',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListHotTopicsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hot_topics_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListHotTopicsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListHotTopicsResponse:
        """
        @summary 获取热点事件列表
        
        @param tmp_req: ListHotTopicsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotTopicsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListHotTopicsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.topic_ids):
            request.topic_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topic_ids, 'TopicIds', 'json')
        if not UtilClient.is_unset(tmp_req.topics):
            request.topics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic_ids_shrink):
            body['TopicIds'] = request.topic_ids_shrink
        if not UtilClient.is_unset(request.topic_query):
            body['TopicQuery'] = request.topic_query
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not UtilClient.is_unset(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not UtilClient.is_unset(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not UtilClient.is_unset(request.with_news):
            body['WithNews'] = request.with_news
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotTopics',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListHotTopicsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hot_topics(
        self,
        request: ai_miao_bi_20230801_models.ListHotTopicsRequest,
    ) -> ai_miao_bi_20230801_models.ListHotTopicsResponse:
        """
        @summary 获取热点事件列表
        
        @param request: ListHotTopicsRequest
        @return: ListHotTopicsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hot_topics_with_options(request, runtime)

    async def list_hot_topics_async(
        self,
        request: ai_miao_bi_20230801_models.ListHotTopicsRequest,
    ) -> ai_miao_bi_20230801_models.ListHotTopicsResponse:
        """
        @summary 获取热点事件列表
        
        @param request: ListHotTopicsRequest
        @return: ListHotTopicsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_hot_topics_with_options_async(request, runtime)

    def list_hot_view_points_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListHotViewPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListHotViewPointsResponse:
        """
        @summary 热门视角列表
        
        @param request: ListHotViewPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotViewPointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotViewPoints',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListHotViewPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hot_view_points_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListHotViewPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListHotViewPointsResponse:
        """
        @summary 热门视角列表
        
        @param request: ListHotViewPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotViewPointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotViewPoints',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListHotViewPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hot_view_points(
        self,
        request: ai_miao_bi_20230801_models.ListHotViewPointsRequest,
    ) -> ai_miao_bi_20230801_models.ListHotViewPointsResponse:
        """
        @summary 热门视角列表
        
        @param request: ListHotViewPointsRequest
        @return: ListHotViewPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hot_view_points_with_options(request, runtime)

    async def list_hot_view_points_async(
        self,
        request: ai_miao_bi_20230801_models.ListHotViewPointsRequest,
    ) -> ai_miao_bi_20230801_models.ListHotViewPointsResponse:
        """
        @summary 热门视角列表
        
        @param request: ListHotViewPointsRequest
        @return: ListHotViewPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_hot_view_points_with_options_async(request, runtime)

    def list_intervene_cnt_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneCntRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListInterveneCntResponse:
        """
        @summary 获得干预项目数量列表
        
        @param request: ListInterveneCntRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterveneCntResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInterveneCnt',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListInterveneCntResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervene_cnt_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneCntRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListInterveneCntResponse:
        """
        @summary 获得干预项目数量列表
        
        @param request: ListInterveneCntRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterveneCntResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInterveneCnt',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListInterveneCntResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervene_cnt(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneCntRequest,
    ) -> ai_miao_bi_20230801_models.ListInterveneCntResponse:
        """
        @summary 获得干预项目数量列表
        
        @param request: ListInterveneCntRequest
        @return: ListInterveneCntResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_intervene_cnt_with_options(request, runtime)

    async def list_intervene_cnt_async(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneCntRequest,
    ) -> ai_miao_bi_20230801_models.ListInterveneCntResponse:
        """
        @summary 获得干预项目数量列表
        
        @param request: ListInterveneCntRequest
        @return: ListInterveneCntResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_intervene_cnt_with_options_async(request, runtime)

    def list_intervene_import_tasks_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneImportTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListInterveneImportTasksResponse:
        """
        @summary 获得导入任务列表
        
        @param request: ListInterveneImportTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterveneImportTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInterveneImportTasks',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListInterveneImportTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervene_import_tasks_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneImportTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListInterveneImportTasksResponse:
        """
        @summary 获得导入任务列表
        
        @param request: ListInterveneImportTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterveneImportTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInterveneImportTasks',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListInterveneImportTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervene_import_tasks(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneImportTasksRequest,
    ) -> ai_miao_bi_20230801_models.ListInterveneImportTasksResponse:
        """
        @summary 获得导入任务列表
        
        @param request: ListInterveneImportTasksRequest
        @return: ListInterveneImportTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_intervene_import_tasks_with_options(request, runtime)

    async def list_intervene_import_tasks_async(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneImportTasksRequest,
    ) -> ai_miao_bi_20230801_models.ListInterveneImportTasksResponse:
        """
        @summary 获得导入任务列表
        
        @param request: ListInterveneImportTasksRequest
        @return: ListInterveneImportTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_intervene_import_tasks_with_options_async(request, runtime)

    def list_intervene_rules_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListInterveneRulesResponse:
        """
        @summary 获得干预规则列表
        
        @param request: ListInterveneRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterveneRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInterveneRules',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListInterveneRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervene_rules_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListInterveneRulesResponse:
        """
        @summary 获得干预规则列表
        
        @param request: ListInterveneRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterveneRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInterveneRules',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListInterveneRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervene_rules(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneRulesRequest,
    ) -> ai_miao_bi_20230801_models.ListInterveneRulesResponse:
        """
        @summary 获得干预规则列表
        
        @param request: ListInterveneRulesRequest
        @return: ListInterveneRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_intervene_rules_with_options(request, runtime)

    async def list_intervene_rules_async(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneRulesRequest,
    ) -> ai_miao_bi_20230801_models.ListInterveneRulesResponse:
        """
        @summary 获得干预规则列表
        
        @param request: ListInterveneRulesRequest
        @return: ListInterveneRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_intervene_rules_with_options_async(request, runtime)

    def list_intervenes_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListIntervenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListIntervenesResponse:
        """
        @summary 获得干预项列表
        
        @param request: ListIntervenesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntervenesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.intervene_type):
            body['InterveneType'] = request.intervene_type
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIntervenes',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListIntervenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervenes_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListIntervenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListIntervenesResponse:
        """
        @summary 获得干预项列表
        
        @param request: ListIntervenesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntervenesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.intervene_type):
            body['InterveneType'] = request.intervene_type
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIntervenes',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListIntervenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervenes(
        self,
        request: ai_miao_bi_20230801_models.ListIntervenesRequest,
    ) -> ai_miao_bi_20230801_models.ListIntervenesResponse:
        """
        @summary 获得干预项列表
        
        @param request: ListIntervenesRequest
        @return: ListIntervenesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_intervenes_with_options(request, runtime)

    async def list_intervenes_async(
        self,
        request: ai_miao_bi_20230801_models.ListIntervenesRequest,
    ) -> ai_miao_bi_20230801_models.ListIntervenesResponse:
        """
        @summary 获得干预项列表
        
        @param request: ListIntervenesRequest
        @return: ListIntervenesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_intervenes_with_options_async(request, runtime)

    def list_material_documents_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListMaterialDocumentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListMaterialDocumentsResponse:
        """
        @summary 查询素材列表
        
        @param tmp_req: ListMaterialDocumentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMaterialDocumentsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListMaterialDocumentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_type_list):
            request.doc_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_type_list, 'DocTypeList', 'json')
        if not UtilClient.is_unset(tmp_req.keywords):
            request.keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.doc_type_list_shrink):
            body['DocTypeList'] = request.doc_type_list_shrink
        if not UtilClient.is_unset(request.generate_public_url):
            body['GeneratePublicUrl'] = request.generate_public_url
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.update_time_end):
            body['UpdateTimeEnd'] = request.update_time_end
        if not UtilClient.is_unset(request.update_time_start):
            body['UpdateTimeStart'] = request.update_time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMaterialDocuments',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListMaterialDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_material_documents_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListMaterialDocumentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListMaterialDocumentsResponse:
        """
        @summary 查询素材列表
        
        @param tmp_req: ListMaterialDocumentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMaterialDocumentsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListMaterialDocumentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_type_list):
            request.doc_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_type_list, 'DocTypeList', 'json')
        if not UtilClient.is_unset(tmp_req.keywords):
            request.keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.doc_type_list_shrink):
            body['DocTypeList'] = request.doc_type_list_shrink
        if not UtilClient.is_unset(request.generate_public_url):
            body['GeneratePublicUrl'] = request.generate_public_url
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.update_time_end):
            body['UpdateTimeEnd'] = request.update_time_end
        if not UtilClient.is_unset(request.update_time_start):
            body['UpdateTimeStart'] = request.update_time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMaterialDocuments',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListMaterialDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_material_documents(
        self,
        request: ai_miao_bi_20230801_models.ListMaterialDocumentsRequest,
    ) -> ai_miao_bi_20230801_models.ListMaterialDocumentsResponse:
        """
        @summary 查询素材列表
        
        @param request: ListMaterialDocumentsRequest
        @return: ListMaterialDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_material_documents_with_options(request, runtime)

    async def list_material_documents_async(
        self,
        request: ai_miao_bi_20230801_models.ListMaterialDocumentsRequest,
    ) -> ai_miao_bi_20230801_models.ListMaterialDocumentsResponse:
        """
        @summary 查询素材列表
        
        @param request: ListMaterialDocumentsRequest
        @return: ListMaterialDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_material_documents_with_options_async(request, runtime)

    def list_planning_proposal_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListPlanningProposalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListPlanningProposalResponse:
        """
        @summary 获取选题策划列表
        
        @param tmp_req: ListPlanningProposalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPlanningProposalResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListPlanningProposalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        if not UtilClient.is_unset(tmp_req.titles):
            request.titles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.titles, 'Titles', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        if not UtilClient.is_unset(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.titles_shrink):
            body['Titles'] = request.titles_shrink
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not UtilClient.is_unset(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not UtilClient.is_unset(request.view_point_type):
            body['ViewPointType'] = request.view_point_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPlanningProposal',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListPlanningProposalResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_planning_proposal_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListPlanningProposalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListPlanningProposalResponse:
        """
        @summary 获取选题策划列表
        
        @param tmp_req: ListPlanningProposalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPlanningProposalResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListPlanningProposalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        if not UtilClient.is_unset(tmp_req.titles):
            request.titles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.titles, 'Titles', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        if not UtilClient.is_unset(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.titles_shrink):
            body['Titles'] = request.titles_shrink
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not UtilClient.is_unset(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not UtilClient.is_unset(request.view_point_type):
            body['ViewPointType'] = request.view_point_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPlanningProposal',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListPlanningProposalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_planning_proposal(
        self,
        request: ai_miao_bi_20230801_models.ListPlanningProposalRequest,
    ) -> ai_miao_bi_20230801_models.ListPlanningProposalResponse:
        """
        @summary 获取选题策划列表
        
        @param request: ListPlanningProposalRequest
        @return: ListPlanningProposalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_planning_proposal_with_options(request, runtime)

    async def list_planning_proposal_async(
        self,
        request: ai_miao_bi_20230801_models.ListPlanningProposalRequest,
    ) -> ai_miao_bi_20230801_models.ListPlanningProposalResponse:
        """
        @summary 获取选题策划列表
        
        @param request: ListPlanningProposalRequest
        @return: ListPlanningProposalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_planning_proposal_with_options_async(request, runtime)

    def list_search_task_dialogue_datas_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListSearchTaskDialogueDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListSearchTaskDialogueDatasResponse:
        """
        @summary 查询搜索生成任务对话详情中数据列表
        
        @param request: ListSearchTaskDialogueDatasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSearchTaskDialogueDatasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.include_content):
            body['IncludeContent'] = request.include_content
        if not UtilClient.is_unset(request.multimodal_search_type):
            body['MultimodalSearchType'] = request.multimodal_search_type
        if not UtilClient.is_unset(request.original_session_id):
            body['OriginalSessionId'] = request.original_session_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.search_model):
            body['SearchModel'] = request.search_model
        if not UtilClient.is_unset(request.search_model_data_value):
            body['SearchModelDataValue'] = request.search_model_data_value
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSearchTaskDialogueDatas',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListSearchTaskDialogueDatasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_search_task_dialogue_datas_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListSearchTaskDialogueDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListSearchTaskDialogueDatasResponse:
        """
        @summary 查询搜索生成任务对话详情中数据列表
        
        @param request: ListSearchTaskDialogueDatasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSearchTaskDialogueDatasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.include_content):
            body['IncludeContent'] = request.include_content
        if not UtilClient.is_unset(request.multimodal_search_type):
            body['MultimodalSearchType'] = request.multimodal_search_type
        if not UtilClient.is_unset(request.original_session_id):
            body['OriginalSessionId'] = request.original_session_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.search_model):
            body['SearchModel'] = request.search_model
        if not UtilClient.is_unset(request.search_model_data_value):
            body['SearchModelDataValue'] = request.search_model_data_value
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSearchTaskDialogueDatas',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListSearchTaskDialogueDatasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_search_task_dialogue_datas(
        self,
        request: ai_miao_bi_20230801_models.ListSearchTaskDialogueDatasRequest,
    ) -> ai_miao_bi_20230801_models.ListSearchTaskDialogueDatasResponse:
        """
        @summary 查询搜索生成任务对话详情中数据列表
        
        @param request: ListSearchTaskDialogueDatasRequest
        @return: ListSearchTaskDialogueDatasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_search_task_dialogue_datas_with_options(request, runtime)

    async def list_search_task_dialogue_datas_async(
        self,
        request: ai_miao_bi_20230801_models.ListSearchTaskDialogueDatasRequest,
    ) -> ai_miao_bi_20230801_models.ListSearchTaskDialogueDatasResponse:
        """
        @summary 查询搜索生成任务对话详情中数据列表
        
        @param request: ListSearchTaskDialogueDatasRequest
        @return: ListSearchTaskDialogueDatasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_search_task_dialogue_datas_with_options_async(request, runtime)

    def list_search_task_dialogues_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListSearchTaskDialoguesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListSearchTaskDialoguesResponse:
        """
        @summary 查询妙搜搜索生成任务详情列表
        
        @param request: ListSearchTaskDialoguesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSearchTaskDialoguesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSearchTaskDialogues',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListSearchTaskDialoguesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_search_task_dialogues_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListSearchTaskDialoguesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListSearchTaskDialoguesResponse:
        """
        @summary 查询妙搜搜索生成任务详情列表
        
        @param request: ListSearchTaskDialoguesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSearchTaskDialoguesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSearchTaskDialogues',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListSearchTaskDialoguesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_search_task_dialogues(
        self,
        request: ai_miao_bi_20230801_models.ListSearchTaskDialoguesRequest,
    ) -> ai_miao_bi_20230801_models.ListSearchTaskDialoguesResponse:
        """
        @summary 查询妙搜搜索生成任务详情列表
        
        @param request: ListSearchTaskDialoguesRequest
        @return: ListSearchTaskDialoguesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_search_task_dialogues_with_options(request, runtime)

    async def list_search_task_dialogues_async(
        self,
        request: ai_miao_bi_20230801_models.ListSearchTaskDialoguesRequest,
    ) -> ai_miao_bi_20230801_models.ListSearchTaskDialoguesResponse:
        """
        @summary 查询妙搜搜索生成任务详情列表
        
        @param request: ListSearchTaskDialoguesRequest
        @return: ListSearchTaskDialoguesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_search_task_dialogues_with_options_async(request, runtime)

    def list_search_tasks_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListSearchTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListSearchTasksResponse:
        """
        @summary 查询妙搜搜索生成历史任务列表
        
        @param tmp_req: ListSearchTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSearchTasksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListSearchTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dialogue_types):
            request.dialogue_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dialogue_types, 'DialogueTypes', 'json')
        body = {}
        if not UtilClient.is_unset(request.dialogue_types_shrink):
            body['DialogueTypes'] = request.dialogue_types_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSearchTasks',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListSearchTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_search_tasks_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListSearchTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListSearchTasksResponse:
        """
        @summary 查询妙搜搜索生成历史任务列表
        
        @param tmp_req: ListSearchTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSearchTasksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListSearchTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dialogue_types):
            request.dialogue_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dialogue_types, 'DialogueTypes', 'json')
        body = {}
        if not UtilClient.is_unset(request.dialogue_types_shrink):
            body['DialogueTypes'] = request.dialogue_types_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSearchTasks',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListSearchTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_search_tasks(
        self,
        request: ai_miao_bi_20230801_models.ListSearchTasksRequest,
    ) -> ai_miao_bi_20230801_models.ListSearchTasksResponse:
        """
        @summary 查询妙搜搜索生成历史任务列表
        
        @param request: ListSearchTasksRequest
        @return: ListSearchTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_search_tasks_with_options(request, runtime)

    async def list_search_tasks_async(
        self,
        request: ai_miao_bi_20230801_models.ListSearchTasksRequest,
    ) -> ai_miao_bi_20230801_models.ListSearchTasksResponse:
        """
        @summary 查询妙搜搜索生成历史任务列表
        
        @param request: ListSearchTasksRequest
        @return: ListSearchTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_search_tasks_with_options_async(request, runtime)

    def list_style_learning_result_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListStyleLearningResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListStyleLearningResultResponse:
        """
        @summary 获取文体学习分析结果列表
        
        @param request: ListStyleLearningResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStyleLearningResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListStyleLearningResult',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListStyleLearningResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_style_learning_result_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListStyleLearningResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListStyleLearningResultResponse:
        """
        @summary 获取文体学习分析结果列表
        
        @param request: ListStyleLearningResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStyleLearningResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListStyleLearningResult',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListStyleLearningResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_style_learning_result(
        self,
        request: ai_miao_bi_20230801_models.ListStyleLearningResultRequest,
    ) -> ai_miao_bi_20230801_models.ListStyleLearningResultResponse:
        """
        @summary 获取文体学习分析结果列表
        
        @param request: ListStyleLearningResultRequest
        @return: ListStyleLearningResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_style_learning_result_with_options(request, runtime)

    async def list_style_learning_result_async(
        self,
        request: ai_miao_bi_20230801_models.ListStyleLearningResultRequest,
    ) -> ai_miao_bi_20230801_models.ListStyleLearningResultResponse:
        """
        @summary 获取文体学习分析结果列表
        
        @param request: ListStyleLearningResultRequest
        @return: ListStyleLearningResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_style_learning_result_with_options_async(request, runtime)

    def list_timed_view_attitude_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListTimedViewAttitudeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListTimedViewAttitudeResponse:
        """
        @summary 时效性视角列表
        
        @param request: ListTimedViewAttitudeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTimedViewAttitudeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTimedViewAttitude',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListTimedViewAttitudeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_timed_view_attitude_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListTimedViewAttitudeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListTimedViewAttitudeResponse:
        """
        @summary 时效性视角列表
        
        @param request: ListTimedViewAttitudeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTimedViewAttitudeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTimedViewAttitude',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListTimedViewAttitudeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_timed_view_attitude(
        self,
        request: ai_miao_bi_20230801_models.ListTimedViewAttitudeRequest,
    ) -> ai_miao_bi_20230801_models.ListTimedViewAttitudeResponse:
        """
        @summary 时效性视角列表
        
        @param request: ListTimedViewAttitudeRequest
        @return: ListTimedViewAttitudeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_timed_view_attitude_with_options(request, runtime)

    async def list_timed_view_attitude_async(
        self,
        request: ai_miao_bi_20230801_models.ListTimedViewAttitudeRequest,
    ) -> ai_miao_bi_20230801_models.ListTimedViewAttitudeResponse:
        """
        @summary 时效性视角列表
        
        @param request: ListTimedViewAttitudeRequest
        @return: ListTimedViewAttitudeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_timed_view_attitude_with_options_async(request, runtime)

    def list_topic_recommend_event_list_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListTopicRecommendEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListTopicRecommendEventListResponse:
        """
        @summary 获取热点推荐事件
        
        @param request: ListTopicRecommendEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTopicRecommendEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTopicRecommendEventList',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListTopicRecommendEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_topic_recommend_event_list_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListTopicRecommendEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListTopicRecommendEventListResponse:
        """
        @summary 获取热点推荐事件
        
        @param request: ListTopicRecommendEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTopicRecommendEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTopicRecommendEventList',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListTopicRecommendEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_topic_recommend_event_list(
        self,
        request: ai_miao_bi_20230801_models.ListTopicRecommendEventListRequest,
    ) -> ai_miao_bi_20230801_models.ListTopicRecommendEventListResponse:
        """
        @summary 获取热点推荐事件
        
        @param request: ListTopicRecommendEventListRequest
        @return: ListTopicRecommendEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_topic_recommend_event_list_with_options(request, runtime)

    async def list_topic_recommend_event_list_async(
        self,
        request: ai_miao_bi_20230801_models.ListTopicRecommendEventListRequest,
    ) -> ai_miao_bi_20230801_models.ListTopicRecommendEventListResponse:
        """
        @summary 获取热点推荐事件
        
        @param request: ListTopicRecommendEventListRequest
        @return: ListTopicRecommendEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_topic_recommend_event_list_with_options_async(request, runtime)

    def list_topic_view_point_recommend_event_list_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListResponse:
        """
        @summary 获取主题事件推荐观点列表
        
        @param request: ListTopicViewPointRecommendEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTopicViewPointRecommendEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTopicViewPointRecommendEventList',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_topic_view_point_recommend_event_list_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListResponse:
        """
        @summary 获取主题事件推荐观点列表
        
        @param request: ListTopicViewPointRecommendEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTopicViewPointRecommendEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTopicViewPointRecommendEventList',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_topic_view_point_recommend_event_list(
        self,
        request: ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListRequest,
    ) -> ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListResponse:
        """
        @summary 获取主题事件推荐观点列表
        
        @param request: ListTopicViewPointRecommendEventListRequest
        @return: ListTopicViewPointRecommendEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_topic_view_point_recommend_event_list_with_options(request, runtime)

    async def list_topic_view_point_recommend_event_list_async(
        self,
        request: ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListRequest,
    ) -> ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListResponse:
        """
        @summary 获取主题事件推荐观点列表
        
        @param request: ListTopicViewPointRecommendEventListRequest
        @return: ListTopicViewPointRecommendEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_topic_view_point_recommend_event_list_with_options_async(request, runtime)

    def list_versions_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListVersionsResponse:
        """
        @summary 获取系统所有实例信息
        
        @param request: ListVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVersions',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_versions_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListVersionsResponse:
        """
        @summary 获取系统所有实例信息
        
        @param request: ListVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVersions',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_versions(
        self,
        request: ai_miao_bi_20230801_models.ListVersionsRequest,
    ) -> ai_miao_bi_20230801_models.ListVersionsResponse:
        """
        @summary 获取系统所有实例信息
        
        @param request: ListVersionsRequest
        @return: ListVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_versions_with_options(request, runtime)

    async def list_versions_async(
        self,
        request: ai_miao_bi_20230801_models.ListVersionsRequest,
    ) -> ai_miao_bi_20230801_models.ListVersionsResponse:
        """
        @summary 获取系统所有实例信息
        
        @param request: ListVersionsRequest
        @return: ListVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_versions_with_options_async(request, runtime)

    def list_web_review_points_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListWebReviewPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListWebReviewPointsResponse:
        """
        @summary 网友视角列表
        
        @param request: ListWebReviewPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWebReviewPointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListWebReviewPoints',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListWebReviewPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_web_review_points_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListWebReviewPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListWebReviewPointsResponse:
        """
        @summary 网友视角列表
        
        @param request: ListWebReviewPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWebReviewPointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListWebReviewPoints',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListWebReviewPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_web_review_points(
        self,
        request: ai_miao_bi_20230801_models.ListWebReviewPointsRequest,
    ) -> ai_miao_bi_20230801_models.ListWebReviewPointsResponse:
        """
        @summary 网友视角列表
        
        @param request: ListWebReviewPointsRequest
        @return: ListWebReviewPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_web_review_points_with_options(request, runtime)

    async def list_web_review_points_async(
        self,
        request: ai_miao_bi_20230801_models.ListWebReviewPointsRequest,
    ) -> ai_miao_bi_20230801_models.ListWebReviewPointsResponse:
        """
        @summary 网友视角列表
        
        @param request: ListWebReviewPointsRequest
        @return: ListWebReviewPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_web_review_points_with_options_async(request, runtime)

    def query_async_task_with_options(
        self,
        request: ai_miao_bi_20230801_models.QueryAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.QueryAsyncTaskResponse:
        """
        @summary 根据taskId查询异步任务状态
        
        @param request: QueryAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAsyncTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.QueryAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_async_task_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.QueryAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.QueryAsyncTaskResponse:
        """
        @summary 根据taskId查询异步任务状态
        
        @param request: QueryAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAsyncTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.QueryAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_async_task(
        self,
        request: ai_miao_bi_20230801_models.QueryAsyncTaskRequest,
    ) -> ai_miao_bi_20230801_models.QueryAsyncTaskResponse:
        """
        @summary 根据taskId查询异步任务状态
        
        @param request: QueryAsyncTaskRequest
        @return: QueryAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_async_task_with_options(request, runtime)

    async def query_async_task_async(
        self,
        request: ai_miao_bi_20230801_models.QueryAsyncTaskRequest,
    ) -> ai_miao_bi_20230801_models.QueryAsyncTaskResponse:
        """
        @summary 根据taskId查询异步任务状态
        
        @param request: QueryAsyncTaskRequest
        @return: QueryAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_async_task_with_options_async(request, runtime)

    def run_abbreviation_content_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunAbbreviationContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunAbbreviationContentResponse:
        """
        @summary 内容缩写
        
        @param request: RunAbbreviationContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunAbbreviationContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunAbbreviationContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunAbbreviationContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_abbreviation_content_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunAbbreviationContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunAbbreviationContentResponse:
        """
        @summary 内容缩写
        
        @param request: RunAbbreviationContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunAbbreviationContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunAbbreviationContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunAbbreviationContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_abbreviation_content(
        self,
        request: ai_miao_bi_20230801_models.RunAbbreviationContentRequest,
    ) -> ai_miao_bi_20230801_models.RunAbbreviationContentResponse:
        """
        @summary 内容缩写
        
        @param request: RunAbbreviationContentRequest
        @return: RunAbbreviationContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_abbreviation_content_with_options(request, runtime)

    async def run_abbreviation_content_async(
        self,
        request: ai_miao_bi_20230801_models.RunAbbreviationContentRequest,
    ) -> ai_miao_bi_20230801_models.RunAbbreviationContentResponse:
        """
        @summary 内容缩写
        
        @param request: RunAbbreviationContentRequest
        @return: RunAbbreviationContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_abbreviation_content_with_options_async(request, runtime)

    def run_book_introduction_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunBookIntroductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunBookIntroductionResponse:
        """
        @summary 书籍导读接口
        
        @param request: RunBookIntroductionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunBookIntroductionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunBookIntroduction',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunBookIntroductionResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_book_introduction_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunBookIntroductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunBookIntroductionResponse:
        """
        @summary 书籍导读接口
        
        @param request: RunBookIntroductionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunBookIntroductionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunBookIntroduction',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunBookIntroductionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_book_introduction(
        self,
        request: ai_miao_bi_20230801_models.RunBookIntroductionRequest,
    ) -> ai_miao_bi_20230801_models.RunBookIntroductionResponse:
        """
        @summary 书籍导读接口
        
        @param request: RunBookIntroductionRequest
        @return: RunBookIntroductionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_book_introduction_with_options(request, runtime)

    async def run_book_introduction_async(
        self,
        request: ai_miao_bi_20230801_models.RunBookIntroductionRequest,
    ) -> ai_miao_bi_20230801_models.RunBookIntroductionResponse:
        """
        @summary 书籍导读接口
        
        @param request: RunBookIntroductionRequest
        @return: RunBookIntroductionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_book_introduction_with_options_async(request, runtime)

    def run_book_smart_card_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunBookSmartCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunBookSmartCardResponse:
        """
        @summary 书籍智能卡片接口
        
        @param request: RunBookSmartCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunBookSmartCardResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunBookSmartCard',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunBookSmartCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_book_smart_card_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunBookSmartCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunBookSmartCardResponse:
        """
        @summary 书籍智能卡片接口
        
        @param request: RunBookSmartCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunBookSmartCardResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunBookSmartCard',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunBookSmartCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_book_smart_card(
        self,
        request: ai_miao_bi_20230801_models.RunBookSmartCardRequest,
    ) -> ai_miao_bi_20230801_models.RunBookSmartCardResponse:
        """
        @summary 书籍智能卡片接口
        
        @param request: RunBookSmartCardRequest
        @return: RunBookSmartCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_book_smart_card_with_options(request, runtime)

    async def run_book_smart_card_async(
        self,
        request: ai_miao_bi_20230801_models.RunBookSmartCardRequest,
    ) -> ai_miao_bi_20230801_models.RunBookSmartCardResponse:
        """
        @summary 书籍智能卡片接口
        
        @param request: RunBookSmartCardRequest
        @return: RunBookSmartCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_book_smart_card_with_options_async(request, runtime)

    def run_comment_generation_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunCommentGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunCommentGenerationResponse:
        """
        @summary 客户之声预测
        
        @param tmp_req: RunCommentGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCommentGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunCommentGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.length_range):
            request.length_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.length_range, 'LengthRange', 'json')
        if not UtilClient.is_unset(tmp_req.sentiment):
            request.sentiment_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sentiment, 'Sentiment', 'json')
        if not UtilClient.is_unset(tmp_req.type):
            request.type_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.type, 'Type', 'json')
        body = {}
        if not UtilClient.is_unset(request.allow_emoji):
            body['AllowEmoji'] = request.allow_emoji
        if not UtilClient.is_unset(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.length):
            body['Length'] = request.length
        if not UtilClient.is_unset(request.length_range_shrink):
            body['LengthRange'] = request.length_range_shrink
        if not UtilClient.is_unset(request.num_comments):
            body['NumComments'] = request.num_comments
        if not UtilClient.is_unset(request.sentiment_shrink):
            body['Sentiment'] = request.sentiment_shrink
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.source_material):
            body['SourceMaterial'] = request.source_material
        if not UtilClient.is_unset(request.style):
            body['Style'] = request.style
        if not UtilClient.is_unset(request.type_shrink):
            body['Type'] = request.type_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCommentGeneration',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunCommentGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_comment_generation_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunCommentGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunCommentGenerationResponse:
        """
        @summary 客户之声预测
        
        @param tmp_req: RunCommentGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCommentGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunCommentGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.length_range):
            request.length_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.length_range, 'LengthRange', 'json')
        if not UtilClient.is_unset(tmp_req.sentiment):
            request.sentiment_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sentiment, 'Sentiment', 'json')
        if not UtilClient.is_unset(tmp_req.type):
            request.type_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.type, 'Type', 'json')
        body = {}
        if not UtilClient.is_unset(request.allow_emoji):
            body['AllowEmoji'] = request.allow_emoji
        if not UtilClient.is_unset(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.length):
            body['Length'] = request.length
        if not UtilClient.is_unset(request.length_range_shrink):
            body['LengthRange'] = request.length_range_shrink
        if not UtilClient.is_unset(request.num_comments):
            body['NumComments'] = request.num_comments
        if not UtilClient.is_unset(request.sentiment_shrink):
            body['Sentiment'] = request.sentiment_shrink
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.source_material):
            body['SourceMaterial'] = request.source_material
        if not UtilClient.is_unset(request.style):
            body['Style'] = request.style
        if not UtilClient.is_unset(request.type_shrink):
            body['Type'] = request.type_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCommentGeneration',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunCommentGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_comment_generation(
        self,
        request: ai_miao_bi_20230801_models.RunCommentGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunCommentGenerationResponse:
        """
        @summary 客户之声预测
        
        @param request: RunCommentGenerationRequest
        @return: RunCommentGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_comment_generation_with_options(request, runtime)

    async def run_comment_generation_async(
        self,
        request: ai_miao_bi_20230801_models.RunCommentGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunCommentGenerationResponse:
        """
        @summary 客户之声预测
        
        @param request: RunCommentGenerationRequest
        @return: RunCommentGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_comment_generation_with_options_async(request, runtime)

    def run_continue_content_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunContinueContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunContinueContentResponse:
        """
        @summary 内容续写
        
        @param request: RunContinueContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunContinueContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunContinueContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunContinueContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_continue_content_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunContinueContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunContinueContentResponse:
        """
        @summary 内容续写
        
        @param request: RunContinueContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunContinueContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunContinueContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunContinueContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_continue_content(
        self,
        request: ai_miao_bi_20230801_models.RunContinueContentRequest,
    ) -> ai_miao_bi_20230801_models.RunContinueContentResponse:
        """
        @summary 内容续写
        
        @param request: RunContinueContentRequest
        @return: RunContinueContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_continue_content_with_options(request, runtime)

    async def run_continue_content_async(
        self,
        request: ai_miao_bi_20230801_models.RunContinueContentRequest,
    ) -> ai_miao_bi_20230801_models.RunContinueContentResponse:
        """
        @summary 内容续写
        
        @param request: RunContinueContentRequest
        @return: RunContinueContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_continue_content_with_options_async(request, runtime)

    def run_custom_hot_topic_analysis_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisResponse:
        """
        @summary 自定义热点话题分析
        
        @param request: RunCustomHotTopicAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCustomHotTopicAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ask_user):
            body['AskUser'] = request.ask_user
        if not UtilClient.is_unset(request.force_analysis_exists_topic):
            body['ForceAnalysisExistsTopic'] = request.force_analysis_exists_topic
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.user_back):
            body['UserBack'] = request.user_back
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCustomHotTopicAnalysis',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_custom_hot_topic_analysis_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisResponse:
        """
        @summary 自定义热点话题分析
        
        @param request: RunCustomHotTopicAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCustomHotTopicAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ask_user):
            body['AskUser'] = request.ask_user
        if not UtilClient.is_unset(request.force_analysis_exists_topic):
            body['ForceAnalysisExistsTopic'] = request.force_analysis_exists_topic
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.user_back):
            body['UserBack'] = request.user_back
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCustomHotTopicAnalysis',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_custom_hot_topic_analysis(
        self,
        request: ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisRequest,
    ) -> ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisResponse:
        """
        @summary 自定义热点话题分析
        
        @param request: RunCustomHotTopicAnalysisRequest
        @return: RunCustomHotTopicAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_custom_hot_topic_analysis_with_options(request, runtime)

    async def run_custom_hot_topic_analysis_async(
        self,
        request: ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisRequest,
    ) -> ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisResponse:
        """
        @summary 自定义热点话题分析
        
        @param request: RunCustomHotTopicAnalysisRequest
        @return: RunCustomHotTopicAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_custom_hot_topic_analysis_with_options_async(request, runtime)

    def run_custom_hot_topic_view_point_analysis_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisResponse:
        """
        @summary 自定义选题视角分析
        
        @param request: RunCustomHotTopicViewPointAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCustomHotTopicViewPointAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ask_user):
            body['AskUser'] = request.ask_user
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.search_query):
            body['SearchQuery'] = request.search_query
        if not UtilClient.is_unset(request.skip_ask_user):
            body['SkipAskUser'] = request.skip_ask_user
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_id):
            body['TopicId'] = request.topic_id
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not UtilClient.is_unset(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not UtilClient.is_unset(request.user_back):
            body['UserBack'] = request.user_back
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCustomHotTopicViewPointAnalysis',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_custom_hot_topic_view_point_analysis_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisResponse:
        """
        @summary 自定义选题视角分析
        
        @param request: RunCustomHotTopicViewPointAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCustomHotTopicViewPointAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ask_user):
            body['AskUser'] = request.ask_user
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.search_query):
            body['SearchQuery'] = request.search_query
        if not UtilClient.is_unset(request.skip_ask_user):
            body['SkipAskUser'] = request.skip_ask_user
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_id):
            body['TopicId'] = request.topic_id
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not UtilClient.is_unset(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not UtilClient.is_unset(request.user_back):
            body['UserBack'] = request.user_back
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCustomHotTopicViewPointAnalysis',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_custom_hot_topic_view_point_analysis(
        self,
        request: ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisRequest,
    ) -> ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisResponse:
        """
        @summary 自定义选题视角分析
        
        @param request: RunCustomHotTopicViewPointAnalysisRequest
        @return: RunCustomHotTopicViewPointAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_custom_hot_topic_view_point_analysis_with_options(request, runtime)

    async def run_custom_hot_topic_view_point_analysis_async(
        self,
        request: ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisRequest,
    ) -> ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisResponse:
        """
        @summary 自定义选题视角分析
        
        @param request: RunCustomHotTopicViewPointAnalysisRequest
        @return: RunCustomHotTopicViewPointAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_custom_hot_topic_view_point_analysis_with_options_async(request, runtime)

    def run_doc_brainmap_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunDocBrainmapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunDocBrainmapResponse:
        """
        @summary 妙读脑图生成接口
        
        @param request: RunDocBrainmapRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDocBrainmapResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.node_number):
            body['NodeNumber'] = request.node_number
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.word_number):
            body['WordNumber'] = request.word_number
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.reference_content):
            body['referenceContent'] = request.reference_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDocBrainmap',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunDocBrainmapResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_doc_brainmap_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunDocBrainmapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunDocBrainmapResponse:
        """
        @summary 妙读脑图生成接口
        
        @param request: RunDocBrainmapRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDocBrainmapResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.node_number):
            body['NodeNumber'] = request.node_number
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.word_number):
            body['WordNumber'] = request.word_number
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.reference_content):
            body['referenceContent'] = request.reference_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDocBrainmap',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunDocBrainmapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_doc_brainmap(
        self,
        request: ai_miao_bi_20230801_models.RunDocBrainmapRequest,
    ) -> ai_miao_bi_20230801_models.RunDocBrainmapResponse:
        """
        @summary 妙读脑图生成接口
        
        @param request: RunDocBrainmapRequest
        @return: RunDocBrainmapResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_doc_brainmap_with_options(request, runtime)

    async def run_doc_brainmap_async(
        self,
        request: ai_miao_bi_20230801_models.RunDocBrainmapRequest,
    ) -> ai_miao_bi_20230801_models.RunDocBrainmapResponse:
        """
        @summary 妙读脑图生成接口
        
        @param request: RunDocBrainmapRequest
        @return: RunDocBrainmapResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_doc_brainmap_with_options_async(request, runtime)

    def run_doc_introduction_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunDocIntroductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunDocIntroductionResponse:
        """
        @summary 妙读文档导读接口
        
        @param request: RunDocIntroductionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDocIntroductionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.introduction_prompt):
            body['IntroductionPrompt'] = request.introduction_prompt
        if not UtilClient.is_unset(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.reference_content):
            body['referenceContent'] = request.reference_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDocIntroduction',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunDocIntroductionResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_doc_introduction_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunDocIntroductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunDocIntroductionResponse:
        """
        @summary 妙读文档导读接口
        
        @param request: RunDocIntroductionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDocIntroductionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.introduction_prompt):
            body['IntroductionPrompt'] = request.introduction_prompt
        if not UtilClient.is_unset(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.reference_content):
            body['referenceContent'] = request.reference_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDocIntroduction',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunDocIntroductionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_doc_introduction(
        self,
        request: ai_miao_bi_20230801_models.RunDocIntroductionRequest,
    ) -> ai_miao_bi_20230801_models.RunDocIntroductionResponse:
        """
        @summary 妙读文档导读接口
        
        @param request: RunDocIntroductionRequest
        @return: RunDocIntroductionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_doc_introduction_with_options(request, runtime)

    async def run_doc_introduction_async(
        self,
        request: ai_miao_bi_20230801_models.RunDocIntroductionRequest,
    ) -> ai_miao_bi_20230801_models.RunDocIntroductionResponse:
        """
        @summary 妙读文档导读接口
        
        @param request: RunDocIntroductionRequest
        @return: RunDocIntroductionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_doc_introduction_with_options_async(request, runtime)

    def run_doc_qa_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunDocQaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunDocQaResponse:
        """
        @summary 妙读问答接口
        
        @param tmp_req: RunDocQaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDocQaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunDocQaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.category_ids):
            request.category_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not UtilClient.is_unset(tmp_req.conversation_contexts):
            request.conversation_contexts_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.conversation_contexts, 'ConversationContexts', 'json')
        if not UtilClient.is_unset(tmp_req.doc_ids):
            request.doc_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_ids, 'DocIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.category_ids_shrink):
            body['CategoryIds'] = request.category_ids_shrink
        if not UtilClient.is_unset(request.conversation_contexts_shrink):
            body['ConversationContexts'] = request.conversation_contexts_shrink
        if not UtilClient.is_unset(request.doc_ids_shrink):
            body['DocIds'] = request.doc_ids_shrink
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not UtilClient.is_unset(request.search_source):
            body['SearchSource'] = request.search_source
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDocQa',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunDocQaResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_doc_qa_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunDocQaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunDocQaResponse:
        """
        @summary 妙读问答接口
        
        @param tmp_req: RunDocQaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDocQaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunDocQaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.category_ids):
            request.category_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not UtilClient.is_unset(tmp_req.conversation_contexts):
            request.conversation_contexts_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.conversation_contexts, 'ConversationContexts', 'json')
        if not UtilClient.is_unset(tmp_req.doc_ids):
            request.doc_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_ids, 'DocIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.category_ids_shrink):
            body['CategoryIds'] = request.category_ids_shrink
        if not UtilClient.is_unset(request.conversation_contexts_shrink):
            body['ConversationContexts'] = request.conversation_contexts_shrink
        if not UtilClient.is_unset(request.doc_ids_shrink):
            body['DocIds'] = request.doc_ids_shrink
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not UtilClient.is_unset(request.search_source):
            body['SearchSource'] = request.search_source
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDocQa',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunDocQaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_doc_qa(
        self,
        request: ai_miao_bi_20230801_models.RunDocQaRequest,
    ) -> ai_miao_bi_20230801_models.RunDocQaResponse:
        """
        @summary 妙读问答接口
        
        @param request: RunDocQaRequest
        @return: RunDocQaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_doc_qa_with_options(request, runtime)

    async def run_doc_qa_async(
        self,
        request: ai_miao_bi_20230801_models.RunDocQaRequest,
    ) -> ai_miao_bi_20230801_models.RunDocQaResponse:
        """
        @summary 妙读问答接口
        
        @param request: RunDocQaRequest
        @return: RunDocQaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_doc_qa_with_options_async(request, runtime)

    def run_doc_smart_card_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunDocSmartCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunDocSmartCardResponse:
        """
        @summary 文档智能卡片接口
        
        @param request: RunDocSmartCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDocSmartCardResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDocSmartCard',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunDocSmartCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_doc_smart_card_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunDocSmartCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunDocSmartCardResponse:
        """
        @summary 文档智能卡片接口
        
        @param request: RunDocSmartCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDocSmartCardResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDocSmartCard',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunDocSmartCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_doc_smart_card(
        self,
        request: ai_miao_bi_20230801_models.RunDocSmartCardRequest,
    ) -> ai_miao_bi_20230801_models.RunDocSmartCardResponse:
        """
        @summary 文档智能卡片接口
        
        @param request: RunDocSmartCardRequest
        @return: RunDocSmartCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_doc_smart_card_with_options(request, runtime)

    async def run_doc_smart_card_async(
        self,
        request: ai_miao_bi_20230801_models.RunDocSmartCardRequest,
    ) -> ai_miao_bi_20230801_models.RunDocSmartCardResponse:
        """
        @summary 文档智能卡片接口
        
        @param request: RunDocSmartCardRequest
        @return: RunDocSmartCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_doc_smart_card_with_options_async(request, runtime)

    def run_doc_summary_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunDocSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunDocSummaryResponse:
        """
        @summary 妙读文档总结摘要接口
        
        @param request: RunDocSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDocSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.recommend_content):
            body['RecommendContent'] = request.recommend_content
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDocSummary',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunDocSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_doc_summary_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunDocSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunDocSummaryResponse:
        """
        @summary 妙读文档总结摘要接口
        
        @param request: RunDocSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDocSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.recommend_content):
            body['RecommendContent'] = request.recommend_content
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDocSummary',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunDocSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_doc_summary(
        self,
        request: ai_miao_bi_20230801_models.RunDocSummaryRequest,
    ) -> ai_miao_bi_20230801_models.RunDocSummaryResponse:
        """
        @summary 妙读文档总结摘要接口
        
        @param request: RunDocSummaryRequest
        @return: RunDocSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_doc_summary_with_options(request, runtime)

    async def run_doc_summary_async(
        self,
        request: ai_miao_bi_20230801_models.RunDocSummaryRequest,
    ) -> ai_miao_bi_20230801_models.RunDocSummaryResponse:
        """
        @summary 妙读文档总结摘要接口
        
        @param request: RunDocSummaryRequest
        @return: RunDocSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_doc_summary_with_options_async(request, runtime)

    def run_doc_translation_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunDocTranslationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunDocTranslationResponse:
        """
        @summary 妙读文档翻译接口
        
        @param request: RunDocTranslationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDocTranslationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.recommend_content):
            body['RecommendContent'] = request.recommend_content
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.trans_type):
            body['TransType'] = request.trans_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDocTranslation',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunDocTranslationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_doc_translation_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunDocTranslationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunDocTranslationResponse:
        """
        @summary 妙读文档翻译接口
        
        @param request: RunDocTranslationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDocTranslationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.recommend_content):
            body['RecommendContent'] = request.recommend_content
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.trans_type):
            body['TransType'] = request.trans_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDocTranslation',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunDocTranslationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_doc_translation(
        self,
        request: ai_miao_bi_20230801_models.RunDocTranslationRequest,
    ) -> ai_miao_bi_20230801_models.RunDocTranslationResponse:
        """
        @summary 妙读文档翻译接口
        
        @param request: RunDocTranslationRequest
        @return: RunDocTranslationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_doc_translation_with_options(request, runtime)

    async def run_doc_translation_async(
        self,
        request: ai_miao_bi_20230801_models.RunDocTranslationRequest,
    ) -> ai_miao_bi_20230801_models.RunDocTranslationResponse:
        """
        @summary 妙读文档翻译接口
        
        @param request: RunDocTranslationRequest
        @return: RunDocTranslationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_doc_translation_with_options_async(request, runtime)

    def run_doc_washing_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunDocWashingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunDocWashingResponse:
        """
        @summary 文档改写
        
        @param request: RunDocWashingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDocWashingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.word_number):
            body['WordNumber'] = request.word_number
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.writing_type_name):
            body['WritingTypeName'] = request.writing_type_name
        if not UtilClient.is_unset(request.writing_type_ref_doc):
            body['WritingTypeRefDoc'] = request.writing_type_ref_doc
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDocWashing',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunDocWashingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_doc_washing_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunDocWashingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunDocWashingResponse:
        """
        @summary 文档改写
        
        @param request: RunDocWashingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDocWashingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.word_number):
            body['WordNumber'] = request.word_number
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.writing_type_name):
            body['WritingTypeName'] = request.writing_type_name
        if not UtilClient.is_unset(request.writing_type_ref_doc):
            body['WritingTypeRefDoc'] = request.writing_type_ref_doc
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDocWashing',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunDocWashingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_doc_washing(
        self,
        request: ai_miao_bi_20230801_models.RunDocWashingRequest,
    ) -> ai_miao_bi_20230801_models.RunDocWashingResponse:
        """
        @summary 文档改写
        
        @param request: RunDocWashingRequest
        @return: RunDocWashingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_doc_washing_with_options(request, runtime)

    async def run_doc_washing_async(
        self,
        request: ai_miao_bi_20230801_models.RunDocWashingRequest,
    ) -> ai_miao_bi_20230801_models.RunDocWashingResponse:
        """
        @summary 文档改写
        
        @param request: RunDocWashingRequest
        @return: RunDocWashingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_doc_washing_with_options_async(request, runtime)

    def run_expand_content_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunExpandContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunExpandContentResponse:
        """
        @summary 内容扩写
        
        @param request: RunExpandContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunExpandContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunExpandContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunExpandContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_expand_content_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunExpandContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunExpandContentResponse:
        """
        @summary 内容扩写
        
        @param request: RunExpandContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunExpandContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunExpandContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunExpandContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_expand_content(
        self,
        request: ai_miao_bi_20230801_models.RunExpandContentRequest,
    ) -> ai_miao_bi_20230801_models.RunExpandContentResponse:
        """
        @summary 内容扩写
        
        @param request: RunExpandContentRequest
        @return: RunExpandContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_expand_content_with_options(request, runtime)

    async def run_expand_content_async(
        self,
        request: ai_miao_bi_20230801_models.RunExpandContentRequest,
    ) -> ai_miao_bi_20230801_models.RunExpandContentResponse:
        """
        @summary 内容扩写
        
        @param request: RunExpandContentRequest
        @return: RunExpandContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_expand_content_with_options_async(request, runtime)

    def run_generate_questions_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunGenerateQuestionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunGenerateQuestionsResponse:
        """
        @summary 妙读猜你想问接口
        
        @param request: RunGenerateQuestionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunGenerateQuestionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunGenerateQuestions',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunGenerateQuestionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_generate_questions_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunGenerateQuestionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunGenerateQuestionsResponse:
        """
        @summary 妙读猜你想问接口
        
        @param request: RunGenerateQuestionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunGenerateQuestionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunGenerateQuestions',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunGenerateQuestionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_generate_questions(
        self,
        request: ai_miao_bi_20230801_models.RunGenerateQuestionsRequest,
    ) -> ai_miao_bi_20230801_models.RunGenerateQuestionsResponse:
        """
        @summary 妙读猜你想问接口
        
        @param request: RunGenerateQuestionsRequest
        @return: RunGenerateQuestionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_generate_questions_with_options(request, runtime)

    async def run_generate_questions_async(
        self,
        request: ai_miao_bi_20230801_models.RunGenerateQuestionsRequest,
    ) -> ai_miao_bi_20230801_models.RunGenerateQuestionsResponse:
        """
        @summary 妙读猜你想问接口
        
        @param request: RunGenerateQuestionsRequest
        @return: RunGenerateQuestionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_generate_questions_with_options_async(request, runtime)

    def run_hotword_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunHotwordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunHotwordResponse:
        """
        @summary 妙读文档关键词抽取接口
        
        @param request: RunHotwordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunHotwordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunHotword',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunHotwordResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_hotword_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunHotwordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunHotwordResponse:
        """
        @summary 妙读文档关键词抽取接口
        
        @param request: RunHotwordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunHotwordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_id):
            body['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunHotword',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunHotwordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_hotword(
        self,
        request: ai_miao_bi_20230801_models.RunHotwordRequest,
    ) -> ai_miao_bi_20230801_models.RunHotwordResponse:
        """
        @summary 妙读文档关键词抽取接口
        
        @param request: RunHotwordRequest
        @return: RunHotwordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_hotword_with_options(request, runtime)

    async def run_hotword_async(
        self,
        request: ai_miao_bi_20230801_models.RunHotwordRequest,
    ) -> ai_miao_bi_20230801_models.RunHotwordResponse:
        """
        @summary 妙读文档关键词抽取接口
        
        @param request: RunHotwordRequest
        @return: RunHotwordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_hotword_with_options_async(request, runtime)

    def run_keywords_extraction_generation_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationResponse:
        """
        @summary AI妙笔-创作-抽取关键词
        
        @param tmp_req: RunKeywordsExtractionGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunKeywordsExtractionGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunKeywordsExtractionGeneration',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_keywords_extraction_generation_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationResponse:
        """
        @summary AI妙笔-创作-抽取关键词
        
        @param tmp_req: RunKeywordsExtractionGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunKeywordsExtractionGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunKeywordsExtractionGeneration',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_keywords_extraction_generation(
        self,
        request: ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationResponse:
        """
        @summary AI妙笔-创作-抽取关键词
        
        @param request: RunKeywordsExtractionGenerationRequest
        @return: RunKeywordsExtractionGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_keywords_extraction_generation_with_options(request, runtime)

    async def run_keywords_extraction_generation_async(
        self,
        request: ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationResponse:
        """
        @summary AI妙笔-创作-抽取关键词
        
        @param request: RunKeywordsExtractionGenerationRequest
        @return: RunKeywordsExtractionGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_keywords_extraction_generation_with_options_async(request, runtime)

    def run_multi_doc_introduction_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunMultiDocIntroductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunMultiDocIntroductionResponse:
        """
        @summary 文档批量导读
        
        @param tmp_req: RunMultiDocIntroductionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunMultiDocIntroductionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunMultiDocIntroductionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_ids):
            request.doc_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_ids, 'DocIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.doc_ids_shrink):
            body['DocIds'] = request.doc_ids_shrink
        if not UtilClient.is_unset(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunMultiDocIntroduction',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunMultiDocIntroductionResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_multi_doc_introduction_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunMultiDocIntroductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunMultiDocIntroductionResponse:
        """
        @summary 文档批量导读
        
        @param tmp_req: RunMultiDocIntroductionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunMultiDocIntroductionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunMultiDocIntroductionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_ids):
            request.doc_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_ids, 'DocIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.doc_ids_shrink):
            body['DocIds'] = request.doc_ids_shrink
        if not UtilClient.is_unset(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunMultiDocIntroduction',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunMultiDocIntroductionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_multi_doc_introduction(
        self,
        request: ai_miao_bi_20230801_models.RunMultiDocIntroductionRequest,
    ) -> ai_miao_bi_20230801_models.RunMultiDocIntroductionResponse:
        """
        @summary 文档批量导读
        
        @param request: RunMultiDocIntroductionRequest
        @return: RunMultiDocIntroductionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_multi_doc_introduction_with_options(request, runtime)

    async def run_multi_doc_introduction_async(
        self,
        request: ai_miao_bi_20230801_models.RunMultiDocIntroductionRequest,
    ) -> ai_miao_bi_20230801_models.RunMultiDocIntroductionResponse:
        """
        @summary 文档批量导读
        
        @param request: RunMultiDocIntroductionRequest
        @return: RunMultiDocIntroductionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_multi_doc_introduction_with_options_async(request, runtime)

    def run_search_generation_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunSearchGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunSearchGenerationResponse:
        """
        @summary AI妙搜-智能搜索生成
        
        @param tmp_req: RunSearchGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSearchGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunSearchGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_context):
            request.agent_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_context, 'AgentContext', 'json')
        if not UtilClient.is_unset(tmp_req.chat_config):
            request.chat_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.chat_config, 'ChatConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.agent_context_shrink):
            body['AgentContext'] = request.agent_context_shrink
        if not UtilClient.is_unset(request.chat_config_shrink):
            body['ChatConfig'] = request.chat_config_shrink
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.original_session_id):
            body['OriginalSessionId'] = request.original_session_id
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunSearchGeneration',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunSearchGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_search_generation_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunSearchGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunSearchGenerationResponse:
        """
        @summary AI妙搜-智能搜索生成
        
        @param tmp_req: RunSearchGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSearchGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunSearchGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_context):
            request.agent_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_context, 'AgentContext', 'json')
        if not UtilClient.is_unset(tmp_req.chat_config):
            request.chat_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.chat_config, 'ChatConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.agent_context_shrink):
            body['AgentContext'] = request.agent_context_shrink
        if not UtilClient.is_unset(request.chat_config_shrink):
            body['ChatConfig'] = request.chat_config_shrink
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.original_session_id):
            body['OriginalSessionId'] = request.original_session_id
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunSearchGeneration',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunSearchGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_search_generation(
        self,
        request: ai_miao_bi_20230801_models.RunSearchGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunSearchGenerationResponse:
        """
        @summary AI妙搜-智能搜索生成
        
        @param request: RunSearchGenerationRequest
        @return: RunSearchGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_search_generation_with_options(request, runtime)

    async def run_search_generation_async(
        self,
        request: ai_miao_bi_20230801_models.RunSearchGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunSearchGenerationResponse:
        """
        @summary AI妙搜-智能搜索生成
        
        @param request: RunSearchGenerationRequest
        @return: RunSearchGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_search_generation_with_options_async(request, runtime)

    def run_search_similar_articles_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunSearchSimilarArticlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunSearchSimilarArticlesResponse:
        """
        @summary 妙搜-文搜文
        
        @param tmp_req: RunSearchSimilarArticlesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSearchSimilarArticlesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunSearchSimilarArticlesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.chat_config):
            request.chat_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.chat_config, 'ChatConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.chat_config_shrink):
            body['ChatConfig'] = request.chat_config_shrink
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunSearchSimilarArticles',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunSearchSimilarArticlesResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_search_similar_articles_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunSearchSimilarArticlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunSearchSimilarArticlesResponse:
        """
        @summary 妙搜-文搜文
        
        @param tmp_req: RunSearchSimilarArticlesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSearchSimilarArticlesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunSearchSimilarArticlesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.chat_config):
            request.chat_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.chat_config, 'ChatConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.chat_config_shrink):
            body['ChatConfig'] = request.chat_config_shrink
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunSearchSimilarArticles',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunSearchSimilarArticlesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_search_similar_articles(
        self,
        request: ai_miao_bi_20230801_models.RunSearchSimilarArticlesRequest,
    ) -> ai_miao_bi_20230801_models.RunSearchSimilarArticlesResponse:
        """
        @summary 妙搜-文搜文
        
        @param request: RunSearchSimilarArticlesRequest
        @return: RunSearchSimilarArticlesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_search_similar_articles_with_options(request, runtime)

    async def run_search_similar_articles_async(
        self,
        request: ai_miao_bi_20230801_models.RunSearchSimilarArticlesRequest,
    ) -> ai_miao_bi_20230801_models.RunSearchSimilarArticlesResponse:
        """
        @summary 妙搜-文搜文
        
        @param request: RunSearchSimilarArticlesRequest
        @return: RunSearchSimilarArticlesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_search_similar_articles_with_options_async(request, runtime)

    def run_step_by_step_writing_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunStepByStepWritingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunStepByStepWritingResponse:
        """
        @summary 创作-分步骤写作
        
        @param tmp_req: RunStepByStepWritingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunStepByStepWritingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunStepByStepWritingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        if not UtilClient.is_unset(tmp_req.writing_config):
            request.writing_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.writing_config, 'WritingConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.origin_session_id):
            body['OriginSessionId'] = request.origin_session_id
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.writing_config_shrink):
            body['WritingConfig'] = request.writing_config_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunStepByStepWriting',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunStepByStepWritingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_step_by_step_writing_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunStepByStepWritingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunStepByStepWritingResponse:
        """
        @summary 创作-分步骤写作
        
        @param tmp_req: RunStepByStepWritingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunStepByStepWritingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunStepByStepWritingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        if not UtilClient.is_unset(tmp_req.writing_config):
            request.writing_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.writing_config, 'WritingConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.origin_session_id):
            body['OriginSessionId'] = request.origin_session_id
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.writing_config_shrink):
            body['WritingConfig'] = request.writing_config_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunStepByStepWriting',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunStepByStepWritingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_step_by_step_writing(
        self,
        request: ai_miao_bi_20230801_models.RunStepByStepWritingRequest,
    ) -> ai_miao_bi_20230801_models.RunStepByStepWritingResponse:
        """
        @summary 创作-分步骤写作
        
        @param request: RunStepByStepWritingRequest
        @return: RunStepByStepWritingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_step_by_step_writing_with_options(request, runtime)

    async def run_step_by_step_writing_async(
        self,
        request: ai_miao_bi_20230801_models.RunStepByStepWritingRequest,
    ) -> ai_miao_bi_20230801_models.RunStepByStepWritingResponse:
        """
        @summary 创作-分步骤写作
        
        @param request: RunStepByStepWritingRequest
        @return: RunStepByStepWritingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_step_by_step_writing_with_options_async(request, runtime)

    def run_style_feature_analysis_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunStyleFeatureAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunStyleFeatureAnalysisResponse:
        """
        @summary 内容特点分析
        
        @param tmp_req: RunStyleFeatureAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunStyleFeatureAnalysisResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunStyleFeatureAnalysisShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contents):
            request.contents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not UtilClient.is_unset(tmp_req.material_ids):
            request.material_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.material_ids, 'MaterialIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not UtilClient.is_unset(request.material_ids_shrink):
            body['MaterialIds'] = request.material_ids_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunStyleFeatureAnalysis',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunStyleFeatureAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_style_feature_analysis_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunStyleFeatureAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunStyleFeatureAnalysisResponse:
        """
        @summary 内容特点分析
        
        @param tmp_req: RunStyleFeatureAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunStyleFeatureAnalysisResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunStyleFeatureAnalysisShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contents):
            request.contents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not UtilClient.is_unset(tmp_req.material_ids):
            request.material_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.material_ids, 'MaterialIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not UtilClient.is_unset(request.material_ids_shrink):
            body['MaterialIds'] = request.material_ids_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunStyleFeatureAnalysis',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunStyleFeatureAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_style_feature_analysis(
        self,
        request: ai_miao_bi_20230801_models.RunStyleFeatureAnalysisRequest,
    ) -> ai_miao_bi_20230801_models.RunStyleFeatureAnalysisResponse:
        """
        @summary 内容特点分析
        
        @param request: RunStyleFeatureAnalysisRequest
        @return: RunStyleFeatureAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_style_feature_analysis_with_options(request, runtime)

    async def run_style_feature_analysis_async(
        self,
        request: ai_miao_bi_20230801_models.RunStyleFeatureAnalysisRequest,
    ) -> ai_miao_bi_20230801_models.RunStyleFeatureAnalysisResponse:
        """
        @summary 内容特点分析
        
        @param request: RunStyleFeatureAnalysisRequest
        @return: RunStyleFeatureAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_style_feature_analysis_with_options_async(request, runtime)

    def run_summary_generate_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunSummaryGenerateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunSummaryGenerateResponse:
        """
        @summary 内容摘要生成
        
        @param request: RunSummaryGenerateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSummaryGenerateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunSummaryGenerate',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunSummaryGenerateResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_summary_generate_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunSummaryGenerateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunSummaryGenerateResponse:
        """
        @summary 内容摘要生成
        
        @param request: RunSummaryGenerateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSummaryGenerateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunSummaryGenerate',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunSummaryGenerateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_summary_generate(
        self,
        request: ai_miao_bi_20230801_models.RunSummaryGenerateRequest,
    ) -> ai_miao_bi_20230801_models.RunSummaryGenerateResponse:
        """
        @summary 内容摘要生成
        
        @param request: RunSummaryGenerateRequest
        @return: RunSummaryGenerateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_summary_generate_with_options(request, runtime)

    async def run_summary_generate_async(
        self,
        request: ai_miao_bi_20230801_models.RunSummaryGenerateRequest,
    ) -> ai_miao_bi_20230801_models.RunSummaryGenerateResponse:
        """
        @summary 内容摘要生成
        
        @param request: RunSummaryGenerateRequest
        @return: RunSummaryGenerateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_summary_generate_with_options_async(request, runtime)

    def run_text_polishing_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunTextPolishingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunTextPolishingResponse:
        """
        @summary 创作-文本润色
        
        @param request: RunTextPolishingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunTextPolishingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunTextPolishing',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunTextPolishingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_text_polishing_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunTextPolishingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunTextPolishingResponse:
        """
        @summary 创作-文本润色
        
        @param request: RunTextPolishingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunTextPolishingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunTextPolishing',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunTextPolishingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_text_polishing(
        self,
        request: ai_miao_bi_20230801_models.RunTextPolishingRequest,
    ) -> ai_miao_bi_20230801_models.RunTextPolishingResponse:
        """
        @summary 创作-文本润色
        
        @param request: RunTextPolishingRequest
        @return: RunTextPolishingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_text_polishing_with_options(request, runtime)

    async def run_text_polishing_async(
        self,
        request: ai_miao_bi_20230801_models.RunTextPolishingRequest,
    ) -> ai_miao_bi_20230801_models.RunTextPolishingResponse:
        """
        @summary 创作-文本润色
        
        @param request: RunTextPolishingRequest
        @return: RunTextPolishingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_text_polishing_with_options_async(request, runtime)

    def run_title_generation_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunTitleGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunTitleGenerationResponse:
        """
        @summary 妙笔：标题生成
        
        @param tmp_req: RunTitleGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunTitleGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunTitleGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.deduplicated_titles):
            request.deduplicated_titles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deduplicated_titles, 'DeduplicatedTitles', 'json')
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not UtilClient.is_unset(request.deduplicated_titles_shrink):
            body['DeduplicatedTitles'] = request.deduplicated_titles_shrink
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.title_count):
            body['TitleCount'] = request.title_count
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunTitleGeneration',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunTitleGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_title_generation_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunTitleGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunTitleGenerationResponse:
        """
        @summary 妙笔：标题生成
        
        @param tmp_req: RunTitleGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunTitleGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunTitleGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.deduplicated_titles):
            request.deduplicated_titles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deduplicated_titles, 'DeduplicatedTitles', 'json')
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not UtilClient.is_unset(request.deduplicated_titles_shrink):
            body['DeduplicatedTitles'] = request.deduplicated_titles_shrink
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.title_count):
            body['TitleCount'] = request.title_count
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunTitleGeneration',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunTitleGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_title_generation(
        self,
        request: ai_miao_bi_20230801_models.RunTitleGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunTitleGenerationResponse:
        """
        @summary 妙笔：标题生成
        
        @param request: RunTitleGenerationRequest
        @return: RunTitleGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_title_generation_with_options(request, runtime)

    async def run_title_generation_async(
        self,
        request: ai_miao_bi_20230801_models.RunTitleGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunTitleGenerationResponse:
        """
        @summary 妙笔：标题生成
        
        @param request: RunTitleGenerationRequest
        @return: RunTitleGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_title_generation_with_options_async(request, runtime)

    def run_translate_generation_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunTranslateGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunTranslateGenerationResponse:
        """
        @summary AI妙笔-创作-中英文翻译
        
        @param tmp_req: RunTranslateGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunTranslateGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunTranslateGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunTranslateGeneration',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunTranslateGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_translate_generation_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunTranslateGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunTranslateGenerationResponse:
        """
        @summary AI妙笔-创作-中英文翻译
        
        @param tmp_req: RunTranslateGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunTranslateGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunTranslateGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunTranslateGeneration',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunTranslateGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_translate_generation(
        self,
        request: ai_miao_bi_20230801_models.RunTranslateGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunTranslateGenerationResponse:
        """
        @summary AI妙笔-创作-中英文翻译
        
        @param request: RunTranslateGenerationRequest
        @return: RunTranslateGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_translate_generation_with_options(request, runtime)

    async def run_translate_generation_async(
        self,
        request: ai_miao_bi_20230801_models.RunTranslateGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunTranslateGenerationResponse:
        """
        @summary AI妙笔-创作-中英文翻译
        
        @param request: RunTranslateGenerationRequest
        @return: RunTranslateGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_translate_generation_with_options_async(request, runtime)

    def run_write_tone_generation_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunWriteToneGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunWriteToneGenerationResponse:
        """
        @summary AI妙笔-创作-文风改写
        
        @param tmp_req: RunWriteToneGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunWriteToneGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunWriteToneGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunWriteToneGeneration',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunWriteToneGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_write_tone_generation_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunWriteToneGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunWriteToneGenerationResponse:
        """
        @summary AI妙笔-创作-文风改写
        
        @param tmp_req: RunWriteToneGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunWriteToneGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunWriteToneGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunWriteToneGeneration',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunWriteToneGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_write_tone_generation(
        self,
        request: ai_miao_bi_20230801_models.RunWriteToneGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunWriteToneGenerationResponse:
        """
        @summary AI妙笔-创作-文风改写
        
        @param request: RunWriteToneGenerationRequest
        @return: RunWriteToneGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_write_tone_generation_with_options(request, runtime)

    async def run_write_tone_generation_async(
        self,
        request: ai_miao_bi_20230801_models.RunWriteToneGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunWriteToneGenerationResponse:
        """
        @summary AI妙笔-创作-文风改写
        
        @param request: RunWriteToneGenerationRequest
        @return: RunWriteToneGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_write_tone_generation_with_options_async(request, runtime)

    def run_writing_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunWritingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunWritingResponse:
        """
        @summary 直接写作
        
        @param tmp_req: RunWritingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunWritingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunWritingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        if not UtilClient.is_unset(tmp_req.writing_config):
            request.writing_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.writing_config, 'WritingConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.origin_session_id):
            body['OriginSessionId'] = request.origin_session_id
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.writing_config_shrink):
            body['WritingConfig'] = request.writing_config_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunWriting',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunWritingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_writing_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunWritingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunWritingResponse:
        """
        @summary 直接写作
        
        @param tmp_req: RunWritingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunWritingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunWritingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        if not UtilClient.is_unset(tmp_req.writing_config):
            request.writing_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.writing_config, 'WritingConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.origin_session_id):
            body['OriginSessionId'] = request.origin_session_id
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.writing_config_shrink):
            body['WritingConfig'] = request.writing_config_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunWriting',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.RunWritingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_writing(
        self,
        request: ai_miao_bi_20230801_models.RunWritingRequest,
    ) -> ai_miao_bi_20230801_models.RunWritingResponse:
        """
        @summary 直接写作
        
        @param request: RunWritingRequest
        @return: RunWritingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_writing_with_options(request, runtime)

    async def run_writing_async(
        self,
        request: ai_miao_bi_20230801_models.RunWritingRequest,
    ) -> ai_miao_bi_20230801_models.RunWritingResponse:
        """
        @summary 直接写作
        
        @param request: RunWritingRequest
        @return: RunWritingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_writing_with_options_async(request, runtime)

    def save_custom_text_with_options(
        self,
        request: ai_miao_bi_20230801_models.SaveCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SaveCustomTextResponse:
        """
        @summary 保存自定义文本
        
        @param request: SaveCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveCustomText',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SaveCustomTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_custom_text_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.SaveCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SaveCustomTextResponse:
        """
        @summary 保存自定义文本
        
        @param request: SaveCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveCustomText',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SaveCustomTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_custom_text(
        self,
        request: ai_miao_bi_20230801_models.SaveCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.SaveCustomTextResponse:
        """
        @summary 保存自定义文本
        
        @param request: SaveCustomTextRequest
        @return: SaveCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_custom_text_with_options(request, runtime)

    async def save_custom_text_async(
        self,
        request: ai_miao_bi_20230801_models.SaveCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.SaveCustomTextResponse:
        """
        @summary 保存自定义文本
        
        @param request: SaveCustomTextRequest
        @return: SaveCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_custom_text_with_options_async(request, runtime)

    def save_data_source_order_config_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SaveDataSourceOrderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SaveDataSourceOrderConfigResponse:
        """
        @summary 保存用户的信源配置
        
        @param tmp_req: SaveDataSourceOrderConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveDataSourceOrderConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SaveDataSourceOrderConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_config_data_source_list):
            request.user_config_data_source_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_config_data_source_list, 'UserConfigDataSourceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.user_config_data_source_list_shrink):
            body['UserConfigDataSourceList'] = request.user_config_data_source_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveDataSourceOrderConfig',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SaveDataSourceOrderConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_data_source_order_config_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.SaveDataSourceOrderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SaveDataSourceOrderConfigResponse:
        """
        @summary 保存用户的信源配置
        
        @param tmp_req: SaveDataSourceOrderConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveDataSourceOrderConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SaveDataSourceOrderConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_config_data_source_list):
            request.user_config_data_source_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_config_data_source_list, 'UserConfigDataSourceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.user_config_data_source_list_shrink):
            body['UserConfigDataSourceList'] = request.user_config_data_source_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveDataSourceOrderConfig',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SaveDataSourceOrderConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_data_source_order_config(
        self,
        request: ai_miao_bi_20230801_models.SaveDataSourceOrderConfigRequest,
    ) -> ai_miao_bi_20230801_models.SaveDataSourceOrderConfigResponse:
        """
        @summary 保存用户的信源配置
        
        @param request: SaveDataSourceOrderConfigRequest
        @return: SaveDataSourceOrderConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_data_source_order_config_with_options(request, runtime)

    async def save_data_source_order_config_async(
        self,
        request: ai_miao_bi_20230801_models.SaveDataSourceOrderConfigRequest,
    ) -> ai_miao_bi_20230801_models.SaveDataSourceOrderConfigResponse:
        """
        @summary 保存用户的信源配置
        
        @param request: SaveDataSourceOrderConfigRequest
        @return: SaveDataSourceOrderConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_data_source_order_config_with_options_async(request, runtime)

    def save_material_document_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SaveMaterialDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SaveMaterialDocumentResponse:
        """
        @summary 保存素材
        
        @param tmp_req: SaveMaterialDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveMaterialDocumentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SaveMaterialDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_keywords):
            request.doc_keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_keywords, 'DocKeywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.author):
            body['Author'] = request.author
        if not UtilClient.is_unset(request.both_save_private_and_share):
            body['BothSavePrivateAndShare'] = request.both_save_private_and_share
        if not UtilClient.is_unset(request.doc_keywords_shrink):
            body['DocKeywords'] = request.doc_keywords_shrink
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.external_url):
            body['ExternalUrl'] = request.external_url
        if not UtilClient.is_unset(request.html_content):
            body['HtmlContent'] = request.html_content
        if not UtilClient.is_unset(request.pub_time):
            body['PubTime'] = request.pub_time
        if not UtilClient.is_unset(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not UtilClient.is_unset(request.src_from):
            body['SrcFrom'] = request.src_from
        if not UtilClient.is_unset(request.summary):
            body['Summary'] = request.summary
        if not UtilClient.is_unset(request.text_content):
            body['TextContent'] = request.text_content
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveMaterialDocument',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SaveMaterialDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_material_document_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.SaveMaterialDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SaveMaterialDocumentResponse:
        """
        @summary 保存素材
        
        @param tmp_req: SaveMaterialDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveMaterialDocumentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SaveMaterialDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_keywords):
            request.doc_keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_keywords, 'DocKeywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.author):
            body['Author'] = request.author
        if not UtilClient.is_unset(request.both_save_private_and_share):
            body['BothSavePrivateAndShare'] = request.both_save_private_and_share
        if not UtilClient.is_unset(request.doc_keywords_shrink):
            body['DocKeywords'] = request.doc_keywords_shrink
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.external_url):
            body['ExternalUrl'] = request.external_url
        if not UtilClient.is_unset(request.html_content):
            body['HtmlContent'] = request.html_content
        if not UtilClient.is_unset(request.pub_time):
            body['PubTime'] = request.pub_time
        if not UtilClient.is_unset(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not UtilClient.is_unset(request.src_from):
            body['SrcFrom'] = request.src_from
        if not UtilClient.is_unset(request.summary):
            body['Summary'] = request.summary
        if not UtilClient.is_unset(request.text_content):
            body['TextContent'] = request.text_content
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveMaterialDocument',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SaveMaterialDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_material_document(
        self,
        request: ai_miao_bi_20230801_models.SaveMaterialDocumentRequest,
    ) -> ai_miao_bi_20230801_models.SaveMaterialDocumentResponse:
        """
        @summary 保存素材
        
        @param request: SaveMaterialDocumentRequest
        @return: SaveMaterialDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_material_document_with_options(request, runtime)

    async def save_material_document_async(
        self,
        request: ai_miao_bi_20230801_models.SaveMaterialDocumentRequest,
    ) -> ai_miao_bi_20230801_models.SaveMaterialDocumentResponse:
        """
        @summary 保存素材
        
        @param request: SaveMaterialDocumentRequest
        @return: SaveMaterialDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_material_document_with_options_async(request, runtime)

    def save_style_learning_result_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SaveStyleLearningResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SaveStyleLearningResultResponse:
        """
        @summary 保存自定义文体
        
        @param tmp_req: SaveStyleLearningResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveStyleLearningResultResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SaveStyleLearningResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_text_id_list):
            request.custom_text_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_text_id_list, 'CustomTextIdList', 'json')
        if not UtilClient.is_unset(tmp_req.material_id_list):
            request.material_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.material_id_list, 'MaterialIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.agent_key):
            body['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.aigc_result):
            body['AigcResult'] = request.aigc_result
        if not UtilClient.is_unset(request.custom_text_id_list_shrink):
            body['CustomTextIdList'] = request.custom_text_id_list_shrink
        if not UtilClient.is_unset(request.material_id_list_shrink):
            body['MaterialIdList'] = request.material_id_list_shrink
        if not UtilClient.is_unset(request.rewrite_result):
            body['RewriteResult'] = request.rewrite_result
        if not UtilClient.is_unset(request.style_name):
            body['StyleName'] = request.style_name
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveStyleLearningResult',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SaveStyleLearningResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_style_learning_result_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.SaveStyleLearningResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SaveStyleLearningResultResponse:
        """
        @summary 保存自定义文体
        
        @param tmp_req: SaveStyleLearningResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveStyleLearningResultResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SaveStyleLearningResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_text_id_list):
            request.custom_text_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_text_id_list, 'CustomTextIdList', 'json')
        if not UtilClient.is_unset(tmp_req.material_id_list):
            request.material_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.material_id_list, 'MaterialIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.agent_key):
            body['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.aigc_result):
            body['AigcResult'] = request.aigc_result
        if not UtilClient.is_unset(request.custom_text_id_list_shrink):
            body['CustomTextIdList'] = request.custom_text_id_list_shrink
        if not UtilClient.is_unset(request.material_id_list_shrink):
            body['MaterialIdList'] = request.material_id_list_shrink
        if not UtilClient.is_unset(request.rewrite_result):
            body['RewriteResult'] = request.rewrite_result
        if not UtilClient.is_unset(request.style_name):
            body['StyleName'] = request.style_name
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveStyleLearningResult',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SaveStyleLearningResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_style_learning_result(
        self,
        request: ai_miao_bi_20230801_models.SaveStyleLearningResultRequest,
    ) -> ai_miao_bi_20230801_models.SaveStyleLearningResultResponse:
        """
        @summary 保存自定义文体
        
        @param request: SaveStyleLearningResultRequest
        @return: SaveStyleLearningResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_style_learning_result_with_options(request, runtime)

    async def save_style_learning_result_async(
        self,
        request: ai_miao_bi_20230801_models.SaveStyleLearningResultRequest,
    ) -> ai_miao_bi_20230801_models.SaveStyleLearningResultResponse:
        """
        @summary 保存自定义文体
        
        @param request: SaveStyleLearningResultRequest
        @return: SaveStyleLearningResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_style_learning_result_with_options_async(request, runtime)

    def search_dataset_documents_with_options(
        self,
        request: ai_miao_bi_20230801_models.SearchDatasetDocumentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SearchDatasetDocumentsResponse:
        """
        @summary 搜索数据集文档
        
        @param request: SearchDatasetDocumentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchDatasetDocumentsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.extend_1):
            body['Extend1'] = request.extend_1
        if not UtilClient.is_unset(request.include_content):
            body['IncludeContent'] = request.include_content
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchDatasetDocuments',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SearchDatasetDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_dataset_documents_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.SearchDatasetDocumentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SearchDatasetDocumentsResponse:
        """
        @summary 搜索数据集文档
        
        @param request: SearchDatasetDocumentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchDatasetDocumentsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.extend_1):
            body['Extend1'] = request.extend_1
        if not UtilClient.is_unset(request.include_content):
            body['IncludeContent'] = request.include_content
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchDatasetDocuments',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SearchDatasetDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_dataset_documents(
        self,
        request: ai_miao_bi_20230801_models.SearchDatasetDocumentsRequest,
    ) -> ai_miao_bi_20230801_models.SearchDatasetDocumentsResponse:
        """
        @summary 搜索数据集文档
        
        @param request: SearchDatasetDocumentsRequest
        @return: SearchDatasetDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_dataset_documents_with_options(request, runtime)

    async def search_dataset_documents_async(
        self,
        request: ai_miao_bi_20230801_models.SearchDatasetDocumentsRequest,
    ) -> ai_miao_bi_20230801_models.SearchDatasetDocumentsResponse:
        """
        @summary 搜索数据集文档
        
        @param request: SearchDatasetDocumentsRequest
        @return: SearchDatasetDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_dataset_documents_with_options_async(request, runtime)

    def search_news_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SearchNewsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SearchNewsResponse:
        """
        @summary 新闻检索
        
        @param tmp_req: SearchNewsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchNewsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SearchNewsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.search_sources):
            request.search_sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.search_sources, 'SearchSources', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.filter_not_null):
            body['FilterNotNull'] = request.filter_not_null
        if not UtilClient.is_unset(request.include_content):
            body['IncludeContent'] = request.include_content
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.search_sources_shrink):
            body['SearchSources'] = request.search_sources_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchNews',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SearchNewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_news_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.SearchNewsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SearchNewsResponse:
        """
        @summary 新闻检索
        
        @param tmp_req: SearchNewsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchNewsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SearchNewsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.search_sources):
            request.search_sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.search_sources, 'SearchSources', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.filter_not_null):
            body['FilterNotNull'] = request.filter_not_null
        if not UtilClient.is_unset(request.include_content):
            body['IncludeContent'] = request.include_content
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.search_sources_shrink):
            body['SearchSources'] = request.search_sources_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchNews',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SearchNewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_news(
        self,
        request: ai_miao_bi_20230801_models.SearchNewsRequest,
    ) -> ai_miao_bi_20230801_models.SearchNewsResponse:
        """
        @summary 新闻检索
        
        @param request: SearchNewsRequest
        @return: SearchNewsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_news_with_options(request, runtime)

    async def search_news_async(
        self,
        request: ai_miao_bi_20230801_models.SearchNewsRequest,
    ) -> ai_miao_bi_20230801_models.SearchNewsResponse:
        """
        @summary 新闻检索
        
        @param request: SearchNewsRequest
        @return: SearchNewsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_news_with_options_async(request, runtime)

    def submit_async_task_with_options(
        self,
        request: ai_miao_bi_20230801_models.SubmitAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitAsyncTaskResponse:
        """
        @summary 提交异步任务
        
        @param request: SubmitAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_code):
            body['TaskCode'] = request.task_code
        if not UtilClient.is_unset(request.task_execute_time):
            body['TaskExecuteTime'] = request.task_execute_time
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_param):
            body['TaskParam'] = request.task_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitAsyncTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SubmitAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_async_task_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.SubmitAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitAsyncTaskResponse:
        """
        @summary 提交异步任务
        
        @param request: SubmitAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_code):
            body['TaskCode'] = request.task_code
        if not UtilClient.is_unset(request.task_execute_time):
            body['TaskExecuteTime'] = request.task_execute_time
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_param):
            body['TaskParam'] = request.task_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitAsyncTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SubmitAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_async_task(
        self,
        request: ai_miao_bi_20230801_models.SubmitAsyncTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitAsyncTaskResponse:
        """
        @summary 提交异步任务
        
        @param request: SubmitAsyncTaskRequest
        @return: SubmitAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_async_task_with_options(request, runtime)

    async def submit_async_task_async(
        self,
        request: ai_miao_bi_20230801_models.SubmitAsyncTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitAsyncTaskResponse:
        """
        @summary 提交异步任务
        
        @param request: SubmitAsyncTaskRequest
        @return: SubmitAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_async_task_with_options_async(request, runtime)

    def submit_custom_hot_topic_broadcast_job_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitCustomHotTopicBroadcastJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitCustomHotTopicBroadcastJobResponse:
        """
        @summary 提交自定义播报单任务
        
        @param tmp_req: SubmitCustomHotTopicBroadcastJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitCustomHotTopicBroadcastJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitCustomHotTopicBroadcastJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hot_topic_broadcast_config):
            request.hot_topic_broadcast_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hot_topic_broadcast_config, 'HotTopicBroadcastConfig', 'json')
        if not UtilClient.is_unset(tmp_req.topics):
            request.topics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        body = {}
        if not UtilClient.is_unset(request.hot_topic_broadcast_config_shrink):
            body['HotTopicBroadcastConfig'] = request.hot_topic_broadcast_config_shrink
        if not UtilClient.is_unset(request.hot_topic_version):
            body['HotTopicVersion'] = request.hot_topic_version
        if not UtilClient.is_unset(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitCustomHotTopicBroadcastJob',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SubmitCustomHotTopicBroadcastJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_custom_hot_topic_broadcast_job_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitCustomHotTopicBroadcastJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitCustomHotTopicBroadcastJobResponse:
        """
        @summary 提交自定义播报单任务
        
        @param tmp_req: SubmitCustomHotTopicBroadcastJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitCustomHotTopicBroadcastJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitCustomHotTopicBroadcastJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hot_topic_broadcast_config):
            request.hot_topic_broadcast_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hot_topic_broadcast_config, 'HotTopicBroadcastConfig', 'json')
        if not UtilClient.is_unset(tmp_req.topics):
            request.topics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        body = {}
        if not UtilClient.is_unset(request.hot_topic_broadcast_config_shrink):
            body['HotTopicBroadcastConfig'] = request.hot_topic_broadcast_config_shrink
        if not UtilClient.is_unset(request.hot_topic_version):
            body['HotTopicVersion'] = request.hot_topic_version
        if not UtilClient.is_unset(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitCustomHotTopicBroadcastJob',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SubmitCustomHotTopicBroadcastJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_custom_hot_topic_broadcast_job(
        self,
        request: ai_miao_bi_20230801_models.SubmitCustomHotTopicBroadcastJobRequest,
    ) -> ai_miao_bi_20230801_models.SubmitCustomHotTopicBroadcastJobResponse:
        """
        @summary 提交自定义播报单任务
        
        @param request: SubmitCustomHotTopicBroadcastJobRequest
        @return: SubmitCustomHotTopicBroadcastJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_custom_hot_topic_broadcast_job_with_options(request, runtime)

    async def submit_custom_hot_topic_broadcast_job_async(
        self,
        request: ai_miao_bi_20230801_models.SubmitCustomHotTopicBroadcastJobRequest,
    ) -> ai_miao_bi_20230801_models.SubmitCustomHotTopicBroadcastJobResponse:
        """
        @summary 提交自定义播报单任务
        
        @param request: SubmitCustomHotTopicBroadcastJobRequest
        @return: SubmitCustomHotTopicBroadcastJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_custom_hot_topic_broadcast_job_with_options_async(request, runtime)

    def submit_custom_topic_selection_perspective_analysis_task_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 提交自定义热点选题视角分析任务
        
        @param tmp_req: SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitCustomTopicSelectionPerspectiveAnalysisTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_custom_topic_selection_perspective_analysis_task_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 提交自定义热点选题视角分析任务
        
        @param tmp_req: SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitCustomTopicSelectionPerspectiveAnalysisTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_custom_topic_selection_perspective_analysis_task(
        self,
        request: ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 提交自定义热点选题视角分析任务
        
        @param request: SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest
        @return: SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_custom_topic_selection_perspective_analysis_task_with_options(request, runtime)

    async def submit_custom_topic_selection_perspective_analysis_task_async(
        self,
        request: ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 提交自定义热点选题视角分析任务
        
        @param request: SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest
        @return: SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_custom_topic_selection_perspective_analysis_task_with_options_async(request, runtime)

    def submit_doc_cluster_task_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitDocClusterTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitDocClusterTaskResponse:
        """
        @summary 提交文档聚合任务
        
        @param tmp_req: SubmitDocClusterTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocClusterTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitDocClusterTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.summary_length):
            body['SummaryLength'] = request.summary_length
        if not UtilClient.is_unset(request.title_length):
            body['TitleLength'] = request.title_length
        if not UtilClient.is_unset(request.topic_count):
            body['TopicCount'] = request.topic_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitDocClusterTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SubmitDocClusterTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_doc_cluster_task_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitDocClusterTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitDocClusterTaskResponse:
        """
        @summary 提交文档聚合任务
        
        @param tmp_req: SubmitDocClusterTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocClusterTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitDocClusterTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.summary_length):
            body['SummaryLength'] = request.summary_length
        if not UtilClient.is_unset(request.title_length):
            body['TitleLength'] = request.title_length
        if not UtilClient.is_unset(request.topic_count):
            body['TopicCount'] = request.topic_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitDocClusterTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SubmitDocClusterTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_doc_cluster_task(
        self,
        request: ai_miao_bi_20230801_models.SubmitDocClusterTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitDocClusterTaskResponse:
        """
        @summary 提交文档聚合任务
        
        @param request: SubmitDocClusterTaskRequest
        @return: SubmitDocClusterTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_doc_cluster_task_with_options(request, runtime)

    async def submit_doc_cluster_task_async(
        self,
        request: ai_miao_bi_20230801_models.SubmitDocClusterTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitDocClusterTaskResponse:
        """
        @summary 提交文档聚合任务
        
        @param request: SubmitDocClusterTaskRequest
        @return: SubmitDocClusterTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_doc_cluster_task_with_options_async(request, runtime)

    def submit_enterprise_voc_analysis_task_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitEnterpriseVocAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitEnterpriseVocAnalysisTaskResponse:
        """
        @summary 提交VOC异步任务
        
        @param tmp_req: SubmitEnterpriseVocAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitEnterpriseVocAnalysisTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitEnterpriseVocAnalysisTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.content_tags):
            request.content_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content_tags, 'ContentTags', 'json')
        if not UtilClient.is_unset(tmp_req.contents):
            request.contents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not UtilClient.is_unset(tmp_req.filter_tags):
            request.filter_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_tags, 'FilterTags', 'json')
        body = {}
        if not UtilClient.is_unset(request.api_key):
            body['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.content_tags_shrink):
            body['ContentTags'] = request.content_tags_shrink
        if not UtilClient.is_unset(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not UtilClient.is_unset(request.file_key):
            body['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.filter_tags_shrink):
            body['FilterTags'] = request.filter_tags_shrink
        if not UtilClient.is_unset(request.material_type):
            body['MaterialType'] = request.material_type
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.positive_sample):
            body['PositiveSample'] = request.positive_sample
        if not UtilClient.is_unset(request.positive_sample_file_key):
            body['PositiveSampleFileKey'] = request.positive_sample_file_key
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitEnterpriseVocAnalysisTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SubmitEnterpriseVocAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_enterprise_voc_analysis_task_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitEnterpriseVocAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitEnterpriseVocAnalysisTaskResponse:
        """
        @summary 提交VOC异步任务
        
        @param tmp_req: SubmitEnterpriseVocAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitEnterpriseVocAnalysisTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitEnterpriseVocAnalysisTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.content_tags):
            request.content_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content_tags, 'ContentTags', 'json')
        if not UtilClient.is_unset(tmp_req.contents):
            request.contents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not UtilClient.is_unset(tmp_req.filter_tags):
            request.filter_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_tags, 'FilterTags', 'json')
        body = {}
        if not UtilClient.is_unset(request.api_key):
            body['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.content_tags_shrink):
            body['ContentTags'] = request.content_tags_shrink
        if not UtilClient.is_unset(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not UtilClient.is_unset(request.file_key):
            body['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.filter_tags_shrink):
            body['FilterTags'] = request.filter_tags_shrink
        if not UtilClient.is_unset(request.material_type):
            body['MaterialType'] = request.material_type
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.positive_sample):
            body['PositiveSample'] = request.positive_sample
        if not UtilClient.is_unset(request.positive_sample_file_key):
            body['PositiveSampleFileKey'] = request.positive_sample_file_key
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitEnterpriseVocAnalysisTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SubmitEnterpriseVocAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_enterprise_voc_analysis_task(
        self,
        request: ai_miao_bi_20230801_models.SubmitEnterpriseVocAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitEnterpriseVocAnalysisTaskResponse:
        """
        @summary 提交VOC异步任务
        
        @param request: SubmitEnterpriseVocAnalysisTaskRequest
        @return: SubmitEnterpriseVocAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_enterprise_voc_analysis_task_with_options(request, runtime)

    async def submit_enterprise_voc_analysis_task_async(
        self,
        request: ai_miao_bi_20230801_models.SubmitEnterpriseVocAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitEnterpriseVocAnalysisTaskResponse:
        """
        @summary 提交VOC异步任务
        
        @param request: SubmitEnterpriseVocAnalysisTaskRequest
        @return: SubmitEnterpriseVocAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_enterprise_voc_analysis_task_with_options_async(request, runtime)

    def submit_smart_clip_task_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitSmartClipTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitSmartClipTaskResponse:
        """
        @summary 提交一键成片剪辑任务
        
        @param tmp_req: SubmitSmartClipTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSmartClipTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitSmartClipTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.editing_config):
            request.editing_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.editing_config, 'EditingConfig', 'json')
        if not UtilClient.is_unset(tmp_req.input_config):
            request.input_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input_config, 'InputConfig', 'json')
        if not UtilClient.is_unset(tmp_req.output_config):
            request.output_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.output_config, 'OutputConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.editing_config_shrink):
            body['EditingConfig'] = request.editing_config_shrink
        if not UtilClient.is_unset(request.extend_param):
            body['ExtendParam'] = request.extend_param
        if not UtilClient.is_unset(request.input_config_shrink):
            body['InputConfig'] = request.input_config_shrink
        if not UtilClient.is_unset(request.output_config_shrink):
            body['OutputConfig'] = request.output_config_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitSmartClipTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SubmitSmartClipTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_smart_clip_task_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitSmartClipTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitSmartClipTaskResponse:
        """
        @summary 提交一键成片剪辑任务
        
        @param tmp_req: SubmitSmartClipTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSmartClipTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitSmartClipTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.editing_config):
            request.editing_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.editing_config, 'EditingConfig', 'json')
        if not UtilClient.is_unset(tmp_req.input_config):
            request.input_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input_config, 'InputConfig', 'json')
        if not UtilClient.is_unset(tmp_req.output_config):
            request.output_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.output_config, 'OutputConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.editing_config_shrink):
            body['EditingConfig'] = request.editing_config_shrink
        if not UtilClient.is_unset(request.extend_param):
            body['ExtendParam'] = request.extend_param
        if not UtilClient.is_unset(request.input_config_shrink):
            body['InputConfig'] = request.input_config_shrink
        if not UtilClient.is_unset(request.output_config_shrink):
            body['OutputConfig'] = request.output_config_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitSmartClipTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SubmitSmartClipTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_smart_clip_task(
        self,
        request: ai_miao_bi_20230801_models.SubmitSmartClipTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitSmartClipTaskResponse:
        """
        @summary 提交一键成片剪辑任务
        
        @param request: SubmitSmartClipTaskRequest
        @return: SubmitSmartClipTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_smart_clip_task_with_options(request, runtime)

    async def submit_smart_clip_task_async(
        self,
        request: ai_miao_bi_20230801_models.SubmitSmartClipTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitSmartClipTaskResponse:
        """
        @summary 提交一键成片剪辑任务
        
        @param request: SubmitSmartClipTaskRequest
        @return: SubmitSmartClipTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_smart_clip_task_with_options_async(request, runtime)

    def submit_topic_selection_perspective_analysis_task_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 提交选题热点分析任务
        
        @param tmp_req: SubmitTopicSelectionPerspectiveAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitTopicSelectionPerspectiveAnalysisTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        if not UtilClient.is_unset(tmp_req.perspective_types):
            request.perspective_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.perspective_types, 'PerspectiveTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.perspective_types_shrink):
            body['PerspectiveTypes'] = request.perspective_types_shrink
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitTopicSelectionPerspectiveAnalysisTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_topic_selection_perspective_analysis_task_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 提交选题热点分析任务
        
        @param tmp_req: SubmitTopicSelectionPerspectiveAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitTopicSelectionPerspectiveAnalysisTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        if not UtilClient.is_unset(tmp_req.perspective_types):
            request.perspective_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.perspective_types, 'PerspectiveTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.perspective_types_shrink):
            body['PerspectiveTypes'] = request.perspective_types_shrink
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitTopicSelectionPerspectiveAnalysisTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_topic_selection_perspective_analysis_task(
        self,
        request: ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 提交选题热点分析任务
        
        @param request: SubmitTopicSelectionPerspectiveAnalysisTaskRequest
        @return: SubmitTopicSelectionPerspectiveAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_topic_selection_perspective_analysis_task_with_options(request, runtime)

    async def submit_topic_selection_perspective_analysis_task_async(
        self,
        request: ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 提交选题热点分析任务
        
        @param request: SubmitTopicSelectionPerspectiveAnalysisTaskRequest
        @return: SubmitTopicSelectionPerspectiveAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_topic_selection_perspective_analysis_task_with_options_async(request, runtime)

    def update_custom_text_with_options(
        self,
        request: ai_miao_bi_20230801_models.UpdateCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateCustomTextResponse:
        """
        @summary 更新自定义文本
        
        @param request: UpdateCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCustomText',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UpdateCustomTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_text_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.UpdateCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateCustomTextResponse:
        """
        @summary 更新自定义文本
        
        @param request: UpdateCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCustomText',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UpdateCustomTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_text(
        self,
        request: ai_miao_bi_20230801_models.UpdateCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.UpdateCustomTextResponse:
        """
        @summary 更新自定义文本
        
        @param request: UpdateCustomTextRequest
        @return: UpdateCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_custom_text_with_options(request, runtime)

    async def update_custom_text_async(
        self,
        request: ai_miao_bi_20230801_models.UpdateCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.UpdateCustomTextResponse:
        """
        @summary 更新自定义文本
        
        @param request: UpdateCustomTextRequest
        @return: UpdateCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_custom_text_with_options_async(request, runtime)

    def update_dataset_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.UpdateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateDatasetResponse:
        """
        @summary 数据集管理-更新
        
        @param tmp_req: UpdateDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UpdateDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dataset_config):
            request.dataset_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dataset_config, 'DatasetConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_config_shrink):
            body['DatasetConfig'] = request.dataset_config_shrink
        if not UtilClient.is_unset(request.dataset_description):
            body['DatasetDescription'] = request.dataset_description
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.search_dataset_enable):
            body['SearchDatasetEnable'] = request.search_dataset_enable
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataset',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UpdateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.UpdateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateDatasetResponse:
        """
        @summary 数据集管理-更新
        
        @param tmp_req: UpdateDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UpdateDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dataset_config):
            request.dataset_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dataset_config, 'DatasetConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_config_shrink):
            body['DatasetConfig'] = request.dataset_config_shrink
        if not UtilClient.is_unset(request.dataset_description):
            body['DatasetDescription'] = request.dataset_description
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.search_dataset_enable):
            body['SearchDatasetEnable'] = request.search_dataset_enable
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataset',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UpdateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset(
        self,
        request: ai_miao_bi_20230801_models.UpdateDatasetRequest,
    ) -> ai_miao_bi_20230801_models.UpdateDatasetResponse:
        """
        @summary 数据集管理-更新
        
        @param request: UpdateDatasetRequest
        @return: UpdateDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dataset_with_options(request, runtime)

    async def update_dataset_async(
        self,
        request: ai_miao_bi_20230801_models.UpdateDatasetRequest,
    ) -> ai_miao_bi_20230801_models.UpdateDatasetResponse:
        """
        @summary 数据集管理-更新
        
        @param request: UpdateDatasetRequest
        @return: UpdateDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dataset_with_options_async(request, runtime)

    def update_dataset_document_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.UpdateDatasetDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateDatasetDocumentResponse:
        """
        @summary 修改数据集文档
        
        @param tmp_req: UpdateDatasetDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetDocumentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UpdateDatasetDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.document):
            request.document_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document, 'Document', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.document_shrink):
            body['Document'] = request.document_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatasetDocument',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UpdateDatasetDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_document_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.UpdateDatasetDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateDatasetDocumentResponse:
        """
        @summary 修改数据集文档
        
        @param tmp_req: UpdateDatasetDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetDocumentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UpdateDatasetDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.document):
            request.document_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document, 'Document', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.document_shrink):
            body['Document'] = request.document_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatasetDocument',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UpdateDatasetDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset_document(
        self,
        request: ai_miao_bi_20230801_models.UpdateDatasetDocumentRequest,
    ) -> ai_miao_bi_20230801_models.UpdateDatasetDocumentResponse:
        """
        @summary 修改数据集文档
        
        @param request: UpdateDatasetDocumentRequest
        @return: UpdateDatasetDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dataset_document_with_options(request, runtime)

    async def update_dataset_document_async(
        self,
        request: ai_miao_bi_20230801_models.UpdateDatasetDocumentRequest,
    ) -> ai_miao_bi_20230801_models.UpdateDatasetDocumentResponse:
        """
        @summary 修改数据集文档
        
        @param request: UpdateDatasetDocumentRequest
        @return: UpdateDatasetDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dataset_document_with_options_async(request, runtime)

    def update_generated_content_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.UpdateGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateGeneratedContentResponse:
        """
        @summary 文档管理-更新。
        
        @param tmp_req: UpdateGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGeneratedContentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UpdateGeneratedContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.keywords):
            request.keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_text):
            body['ContentText'] = request.content_text
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UpdateGeneratedContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_generated_content_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.UpdateGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateGeneratedContentResponse:
        """
        @summary 文档管理-更新。
        
        @param tmp_req: UpdateGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGeneratedContentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UpdateGeneratedContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.keywords):
            request.keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_text):
            body['ContentText'] = request.content_text
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UpdateGeneratedContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_generated_content(
        self,
        request: ai_miao_bi_20230801_models.UpdateGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.UpdateGeneratedContentResponse:
        """
        @summary 文档管理-更新。
        
        @param request: UpdateGeneratedContentRequest
        @return: UpdateGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_generated_content_with_options(request, runtime)

    async def update_generated_content_async(
        self,
        request: ai_miao_bi_20230801_models.UpdateGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.UpdateGeneratedContentResponse:
        """
        @summary 文档管理-更新。
        
        @param request: UpdateGeneratedContentRequest
        @return: UpdateGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_generated_content_with_options_async(request, runtime)

    def update_material_document_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.UpdateMaterialDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateMaterialDocumentResponse:
        """
        @summary 根据ID更新素材
        
        @param tmp_req: UpdateMaterialDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMaterialDocumentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UpdateMaterialDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_keywords):
            request.doc_keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_keywords, 'DocKeywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.author):
            body['Author'] = request.author
        if not UtilClient.is_unset(request.doc_keywords_shrink):
            body['DocKeywords'] = request.doc_keywords_shrink
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.external_url):
            body['ExternalUrl'] = request.external_url
        if not UtilClient.is_unset(request.html_content):
            body['HtmlContent'] = request.html_content
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.pub_time):
            body['PubTime'] = request.pub_time
        if not UtilClient.is_unset(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not UtilClient.is_unset(request.src_from):
            body['SrcFrom'] = request.src_from
        if not UtilClient.is_unset(request.summary):
            body['Summary'] = request.summary
        if not UtilClient.is_unset(request.text_content):
            body['TextContent'] = request.text_content
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMaterialDocument',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UpdateMaterialDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_material_document_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.UpdateMaterialDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateMaterialDocumentResponse:
        """
        @summary 根据ID更新素材
        
        @param tmp_req: UpdateMaterialDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMaterialDocumentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UpdateMaterialDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_keywords):
            request.doc_keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_keywords, 'DocKeywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.author):
            body['Author'] = request.author
        if not UtilClient.is_unset(request.doc_keywords_shrink):
            body['DocKeywords'] = request.doc_keywords_shrink
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.external_url):
            body['ExternalUrl'] = request.external_url
        if not UtilClient.is_unset(request.html_content):
            body['HtmlContent'] = request.html_content
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.pub_time):
            body['PubTime'] = request.pub_time
        if not UtilClient.is_unset(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not UtilClient.is_unset(request.src_from):
            body['SrcFrom'] = request.src_from
        if not UtilClient.is_unset(request.summary):
            body['Summary'] = request.summary
        if not UtilClient.is_unset(request.text_content):
            body['TextContent'] = request.text_content
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMaterialDocument',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UpdateMaterialDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_material_document(
        self,
        request: ai_miao_bi_20230801_models.UpdateMaterialDocumentRequest,
    ) -> ai_miao_bi_20230801_models.UpdateMaterialDocumentResponse:
        """
        @summary 根据ID更新素材
        
        @param request: UpdateMaterialDocumentRequest
        @return: UpdateMaterialDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_material_document_with_options(request, runtime)

    async def update_material_document_async(
        self,
        request: ai_miao_bi_20230801_models.UpdateMaterialDocumentRequest,
    ) -> ai_miao_bi_20230801_models.UpdateMaterialDocumentResponse:
        """
        @summary 根据ID更新素材
        
        @param request: UpdateMaterialDocumentRequest
        @return: UpdateMaterialDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_material_document_with_options_async(request, runtime)

    def upload_book_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.UploadBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UploadBookResponse:
        """
        @summary 妙读上传书籍
        
        @param tmp_req: UploadBookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadBookResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UploadBookShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.docs):
            request.docs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.docs, 'Docs', 'json')
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.docs_shrink):
            body['Docs'] = request.docs_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadBook',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UploadBookResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_book_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.UploadBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UploadBookResponse:
        """
        @summary 妙读上传书籍
        
        @param tmp_req: UploadBookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadBookResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UploadBookShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.docs):
            request.docs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.docs, 'Docs', 'json')
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.docs_shrink):
            body['Docs'] = request.docs_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadBook',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UploadBookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_book(
        self,
        request: ai_miao_bi_20230801_models.UploadBookRequest,
    ) -> ai_miao_bi_20230801_models.UploadBookResponse:
        """
        @summary 妙读上传书籍
        
        @param request: UploadBookRequest
        @return: UploadBookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_book_with_options(request, runtime)

    async def upload_book_async(
        self,
        request: ai_miao_bi_20230801_models.UploadBookRequest,
    ) -> ai_miao_bi_20230801_models.UploadBookResponse:
        """
        @summary 妙读上传书籍
        
        @param request: UploadBookRequest
        @return: UploadBookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_book_with_options_async(request, runtime)

    def upload_doc_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.UploadDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UploadDocResponse:
        """
        @summary 妙读上传文档接口
        
        @param tmp_req: UploadDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadDocResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UploadDocShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.docs):
            request.docs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.docs, 'Docs', 'json')
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.docs_shrink):
            body['Docs'] = request.docs_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadDoc',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UploadDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_doc_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.UploadDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UploadDocResponse:
        """
        @summary 妙读上传文档接口
        
        @param tmp_req: UploadDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadDocResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UploadDocShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.docs):
            request.docs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.docs, 'Docs', 'json')
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.docs_shrink):
            body['Docs'] = request.docs_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadDoc',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UploadDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_doc(
        self,
        request: ai_miao_bi_20230801_models.UploadDocRequest,
    ) -> ai_miao_bi_20230801_models.UploadDocResponse:
        """
        @summary 妙读上传文档接口
        
        @param request: UploadDocRequest
        @return: UploadDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_doc_with_options(request, runtime)

    async def upload_doc_async(
        self,
        request: ai_miao_bi_20230801_models.UploadDocRequest,
    ) -> ai_miao_bi_20230801_models.UploadDocResponse:
        """
        @summary 妙读上传文档接口
        
        @param request: UploadDocRequest
        @return: UploadDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_doc_with_options_async(request, runtime)

    def validate_upload_template_with_options(
        self,
        request: ai_miao_bi_20230801_models.ValidateUploadTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ValidateUploadTemplateResponse:
        """
        @summary 校验企业VOC上传模板
        
        @param request: ValidateUploadTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateUploadTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_key):
            body['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateUploadTemplate',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ValidateUploadTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_upload_template_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ValidateUploadTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ValidateUploadTemplateResponse:
        """
        @summary 校验企业VOC上传模板
        
        @param request: ValidateUploadTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateUploadTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_key):
            body['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateUploadTemplate',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ValidateUploadTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_upload_template(
        self,
        request: ai_miao_bi_20230801_models.ValidateUploadTemplateRequest,
    ) -> ai_miao_bi_20230801_models.ValidateUploadTemplateResponse:
        """
        @summary 校验企业VOC上传模板
        
        @param request: ValidateUploadTemplateRequest
        @return: ValidateUploadTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.validate_upload_template_with_options(request, runtime)

    async def validate_upload_template_async(
        self,
        request: ai_miao_bi_20230801_models.ValidateUploadTemplateRequest,
    ) -> ai_miao_bi_20230801_models.ValidateUploadTemplateResponse:
        """
        @summary 校验企业VOC上传模板
        
        @param request: ValidateUploadTemplateRequest
        @return: ValidateUploadTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.validate_upload_template_with_options_async(request, runtime)
