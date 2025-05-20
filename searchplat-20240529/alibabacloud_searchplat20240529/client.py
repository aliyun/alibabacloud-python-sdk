# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_pop.client import Client as GatewayClientClient
from alibabacloud_searchplat20240529 import models as searchplat_20240529_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
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
        self._product_id = 'Searchplat'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = ''

    def create_document_analyze_task_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.CreateDocumentAnalyzeTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.CreateDocumentAnalyzeTaskResponse:
        """
        @summary 创建文档解析异步提取任务
        
        @param request: CreateDocumentAnalyzeTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDocumentAnalyzeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.document):
            body['document'] = request.document
        if not UtilClient.is_unset(request.output):
            body['output'] = request.output
        if not UtilClient.is_unset(request.strategy):
            body['strategy'] = request.strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDocumentAnalyzeTask',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/document-analyze/{service_id}/async',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.CreateDocumentAnalyzeTaskResponse(),
            self.execute(params, req, runtime)
        )

    async def create_document_analyze_task_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.CreateDocumentAnalyzeTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.CreateDocumentAnalyzeTaskResponse:
        """
        @summary 创建文档解析异步提取任务
        
        @param request: CreateDocumentAnalyzeTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDocumentAnalyzeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.document):
            body['document'] = request.document
        if not UtilClient.is_unset(request.output):
            body['output'] = request.output
        if not UtilClient.is_unset(request.strategy):
            body['strategy'] = request.strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDocumentAnalyzeTask',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/document-analyze/{service_id}/async',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.CreateDocumentAnalyzeTaskResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_document_analyze_task(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.CreateDocumentAnalyzeTaskRequest,
    ) -> searchplat_20240529_models.CreateDocumentAnalyzeTaskResponse:
        """
        @summary 创建文档解析异步提取任务
        
        @param request: CreateDocumentAnalyzeTaskRequest
        @return: CreateDocumentAnalyzeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_document_analyze_task_with_options(workspace_name, service_id, request, headers, runtime)

    async def create_document_analyze_task_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.CreateDocumentAnalyzeTaskRequest,
    ) -> searchplat_20240529_models.CreateDocumentAnalyzeTaskResponse:
        """
        @summary 创建文档解析异步提取任务
        
        @param request: CreateDocumentAnalyzeTaskRequest
        @return: CreateDocumentAnalyzeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_document_analyze_task_with_options_async(workspace_name, service_id, request, headers, runtime)

    def create_image_analyze_task_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.CreateImageAnalyzeTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.CreateImageAnalyzeTaskResponse:
        """
        @summary 创建图片解析异步提取任务
        
        @param request: CreateImageAnalyzeTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageAnalyzeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.document):
            body['document'] = request.document
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateImageAnalyzeTask',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/image-analyze/{service_id}/async',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.CreateImageAnalyzeTaskResponse(),
            self.execute(params, req, runtime)
        )

    async def create_image_analyze_task_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.CreateImageAnalyzeTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.CreateImageAnalyzeTaskResponse:
        """
        @summary 创建图片解析异步提取任务
        
        @param request: CreateImageAnalyzeTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageAnalyzeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.document):
            body['document'] = request.document
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateImageAnalyzeTask',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/image-analyze/{service_id}/async',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.CreateImageAnalyzeTaskResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_image_analyze_task(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.CreateImageAnalyzeTaskRequest,
    ) -> searchplat_20240529_models.CreateImageAnalyzeTaskResponse:
        """
        @summary 创建图片解析异步提取任务
        
        @param request: CreateImageAnalyzeTaskRequest
        @return: CreateImageAnalyzeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_image_analyze_task_with_options(workspace_name, service_id, request, headers, runtime)

    async def create_image_analyze_task_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.CreateImageAnalyzeTaskRequest,
    ) -> searchplat_20240529_models.CreateImageAnalyzeTaskResponse:
        """
        @summary 创建图片解析异步提取任务
        
        @param request: CreateImageAnalyzeTaskRequest
        @return: CreateImageAnalyzeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_image_analyze_task_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_document_analyze_task_status_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetDocumentAnalyzeTaskStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetDocumentAnalyzeTaskStatusResponse:
        """
        @summary 获取文档解析异步提取任务状态
        
        @param request: GetDocumentAnalyzeTaskStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentAnalyzeTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocumentAnalyzeTaskStatus',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/document-analyze/{service_id}/async/task-status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetDocumentAnalyzeTaskStatusResponse(),
            self.execute(params, req, runtime)
        )

    async def get_document_analyze_task_status_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetDocumentAnalyzeTaskStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetDocumentAnalyzeTaskStatusResponse:
        """
        @summary 获取文档解析异步提取任务状态
        
        @param request: GetDocumentAnalyzeTaskStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentAnalyzeTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocumentAnalyzeTaskStatus',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/document-analyze/{service_id}/async/task-status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetDocumentAnalyzeTaskStatusResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_document_analyze_task_status(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetDocumentAnalyzeTaskStatusRequest,
    ) -> searchplat_20240529_models.GetDocumentAnalyzeTaskStatusResponse:
        """
        @summary 获取文档解析异步提取任务状态
        
        @param request: GetDocumentAnalyzeTaskStatusRequest
        @return: GetDocumentAnalyzeTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_document_analyze_task_status_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_document_analyze_task_status_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetDocumentAnalyzeTaskStatusRequest,
    ) -> searchplat_20240529_models.GetDocumentAnalyzeTaskStatusResponse:
        """
        @summary 获取文档解析异步提取任务状态
        
        @param request: GetDocumentAnalyzeTaskStatusRequest
        @return: GetDocumentAnalyzeTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_document_analyze_task_status_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_document_rank_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetDocumentRankRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetDocumentRankResponse:
        """
        @summary 文档相关性打分
        
        @param request: GetDocumentRankRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentRankResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.docs):
            body['docs'] = request.docs
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocumentRank',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/ranker/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetDocumentRankResponse(),
            self.execute(params, req, runtime)
        )

    async def get_document_rank_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetDocumentRankRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetDocumentRankResponse:
        """
        @summary 文档相关性打分
        
        @param request: GetDocumentRankRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentRankResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.docs):
            body['docs'] = request.docs
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocumentRank',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/ranker/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetDocumentRankResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_document_rank(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetDocumentRankRequest,
    ) -> searchplat_20240529_models.GetDocumentRankResponse:
        """
        @summary 文档相关性打分
        
        @param request: GetDocumentRankRequest
        @return: GetDocumentRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_document_rank_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_document_rank_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetDocumentRankRequest,
    ) -> searchplat_20240529_models.GetDocumentRankResponse:
        """
        @summary 文档相关性打分
        
        @param request: GetDocumentRankRequest
        @return: GetDocumentRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_document_rank_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_document_split_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetDocumentSplitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetDocumentSplitResponse:
        """
        @summary 文档切片
        
        @param request: GetDocumentSplitRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentSplitResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.document):
            body['document'] = request.document
        if not UtilClient.is_unset(request.strategy):
            body['strategy'] = request.strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocumentSplit',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/document-split/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetDocumentSplitResponse(),
            self.execute(params, req, runtime)
        )

    async def get_document_split_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetDocumentSplitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetDocumentSplitResponse:
        """
        @summary 文档切片
        
        @param request: GetDocumentSplitRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentSplitResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.document):
            body['document'] = request.document
        if not UtilClient.is_unset(request.strategy):
            body['strategy'] = request.strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocumentSplit',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/document-split/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetDocumentSplitResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_document_split(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetDocumentSplitRequest,
    ) -> searchplat_20240529_models.GetDocumentSplitResponse:
        """
        @summary 文档切片
        
        @param request: GetDocumentSplitRequest
        @return: GetDocumentSplitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_document_split_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_document_split_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetDocumentSplitRequest,
    ) -> searchplat_20240529_models.GetDocumentSplitResponse:
        """
        @summary 文档切片
        
        @param request: GetDocumentSplitRequest
        @return: GetDocumentSplitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_document_split_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_embedding_tuning_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetEmbeddingTuningRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetEmbeddingTuningResponse:
        """
        @summary 向量微调
        
        @param request: GetEmbeddingTuningRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEmbeddingTuningResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input):
            body['input'] = request.input
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEmbeddingTuning',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/embedding-tuning/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetEmbeddingTuningResponse(),
            self.execute(params, req, runtime)
        )

    async def get_embedding_tuning_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetEmbeddingTuningRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetEmbeddingTuningResponse:
        """
        @summary 向量微调
        
        @param request: GetEmbeddingTuningRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEmbeddingTuningResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input):
            body['input'] = request.input
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEmbeddingTuning',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/embedding-tuning/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetEmbeddingTuningResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_embedding_tuning(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetEmbeddingTuningRequest,
    ) -> searchplat_20240529_models.GetEmbeddingTuningResponse:
        """
        @summary 向量微调
        
        @param request: GetEmbeddingTuningRequest
        @return: GetEmbeddingTuningResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_embedding_tuning_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_embedding_tuning_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetEmbeddingTuningRequest,
    ) -> searchplat_20240529_models.GetEmbeddingTuningResponse:
        """
        @summary 向量微调
        
        @param request: GetEmbeddingTuningRequest
        @return: GetEmbeddingTuningResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_embedding_tuning_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_image_analyze_task_status_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetImageAnalyzeTaskStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetImageAnalyzeTaskStatusResponse:
        """
        @summary 获取图片解析异步提取任务状态
        
        @param request: GetImageAnalyzeTaskStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageAnalyzeTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageAnalyzeTaskStatus',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/image-analyze/{service_id}/async/task-status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetImageAnalyzeTaskStatusResponse(),
            self.execute(params, req, runtime)
        )

    async def get_image_analyze_task_status_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetImageAnalyzeTaskStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetImageAnalyzeTaskStatusResponse:
        """
        @summary 获取图片解析异步提取任务状态
        
        @param request: GetImageAnalyzeTaskStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageAnalyzeTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageAnalyzeTaskStatus',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/image-analyze/{service_id}/async/task-status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetImageAnalyzeTaskStatusResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_image_analyze_task_status(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetImageAnalyzeTaskStatusRequest,
    ) -> searchplat_20240529_models.GetImageAnalyzeTaskStatusResponse:
        """
        @summary 获取图片解析异步提取任务状态
        
        @param request: GetImageAnalyzeTaskStatusRequest
        @return: GetImageAnalyzeTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_image_analyze_task_status_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_image_analyze_task_status_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetImageAnalyzeTaskStatusRequest,
    ) -> searchplat_20240529_models.GetImageAnalyzeTaskStatusResponse:
        """
        @summary 获取图片解析异步提取任务状态
        
        @param request: GetImageAnalyzeTaskStatusRequest
        @return: GetImageAnalyzeTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_image_analyze_task_status_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_multi_modal_embedding_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetMultiModalEmbeddingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetMultiModalEmbeddingResponse:
        """
        @summary 多模态向量化
        
        @param request: GetMultiModalEmbeddingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMultiModalEmbeddingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input):
            body['input'] = request.input
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMultiModalEmbedding',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/multi-modal-embedding/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetMultiModalEmbeddingResponse(),
            self.execute(params, req, runtime)
        )

    async def get_multi_modal_embedding_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetMultiModalEmbeddingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetMultiModalEmbeddingResponse:
        """
        @summary 多模态向量化
        
        @param request: GetMultiModalEmbeddingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMultiModalEmbeddingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input):
            body['input'] = request.input
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMultiModalEmbedding',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/multi-modal-embedding/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetMultiModalEmbeddingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_multi_modal_embedding(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetMultiModalEmbeddingRequest,
    ) -> searchplat_20240529_models.GetMultiModalEmbeddingResponse:
        """
        @summary 多模态向量化
        
        @param request: GetMultiModalEmbeddingRequest
        @return: GetMultiModalEmbeddingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_multi_modal_embedding_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_multi_modal_embedding_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetMultiModalEmbeddingRequest,
    ) -> searchplat_20240529_models.GetMultiModalEmbeddingResponse:
        """
        @summary 多模态向量化
        
        @param request: GetMultiModalEmbeddingRequest
        @return: GetMultiModalEmbeddingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_multi_modal_embedding_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_prediction_with_options(
        self,
        deployment_id: str,
        request: searchplat_20240529_models.GetPredictionRequest,
        headers: searchplat_20240529_models.GetPredictionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetPredictionResponse:
        """
        @summary 获取推理结果
        
        @param request: GetPredictionRequest
        @param headers: GetPredictionHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPredictionResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.token):
            real_headers['Token'] = UtilClient.to_jsonstring(headers.token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='GetPrediction',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/deployments/{deployment_id}/predict',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetPredictionResponse(),
            self.execute(params, req, runtime)
        )

    async def get_prediction_with_options_async(
        self,
        deployment_id: str,
        request: searchplat_20240529_models.GetPredictionRequest,
        headers: searchplat_20240529_models.GetPredictionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetPredictionResponse:
        """
        @summary 获取推理结果
        
        @param request: GetPredictionRequest
        @param headers: GetPredictionHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPredictionResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.token):
            real_headers['Token'] = UtilClient.to_jsonstring(headers.token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='GetPrediction',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/deployments/{deployment_id}/predict',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetPredictionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_prediction(
        self,
        deployment_id: str,
        request: searchplat_20240529_models.GetPredictionRequest,
    ) -> searchplat_20240529_models.GetPredictionResponse:
        """
        @summary 获取推理结果
        
        @param request: GetPredictionRequest
        @return: GetPredictionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = searchplat_20240529_models.GetPredictionHeaders()
        return self.get_prediction_with_options(deployment_id, request, headers, runtime)

    async def get_prediction_async(
        self,
        deployment_id: str,
        request: searchplat_20240529_models.GetPredictionRequest,
    ) -> searchplat_20240529_models.GetPredictionResponse:
        """
        @summary 获取推理结果
        
        @param request: GetPredictionRequest
        @return: GetPredictionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = searchplat_20240529_models.GetPredictionHeaders()
        return await self.get_prediction_with_options_async(deployment_id, request, headers, runtime)

    def get_query_analysis_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetQueryAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetQueryAnalysisResponse:
        """
        @summary 获取query分析结果
        
        @param request: GetQueryAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.functions):
            body['functions'] = request.functions
        if not UtilClient.is_unset(request.history):
            body['history'] = request.history
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQueryAnalysis',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/query-analyze/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetQueryAnalysisResponse(),
            self.execute(params, req, runtime)
        )

    async def get_query_analysis_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetQueryAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetQueryAnalysisResponse:
        """
        @summary 获取query分析结果
        
        @param request: GetQueryAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.functions):
            body['functions'] = request.functions
        if not UtilClient.is_unset(request.history):
            body['history'] = request.history
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQueryAnalysis',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/query-analyze/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetQueryAnalysisResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_query_analysis(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetQueryAnalysisRequest,
    ) -> searchplat_20240529_models.GetQueryAnalysisResponse:
        """
        @summary 获取query分析结果
        
        @param request: GetQueryAnalysisRequest
        @return: GetQueryAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_query_analysis_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_query_analysis_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetQueryAnalysisRequest,
    ) -> searchplat_20240529_models.GetQueryAnalysisResponse:
        """
        @summary 获取query分析结果
        
        @param request: GetQueryAnalysisRequest
        @return: GetQueryAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_query_analysis_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_text_embedding_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetTextEmbeddingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetTextEmbeddingResponse:
        """
        @summary 文本向量化
        
        @param request: GetTextEmbeddingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTextEmbeddingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input):
            body['input'] = request.input
        if not UtilClient.is_unset(request.input_type):
            body['input_type'] = request.input_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTextEmbedding',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/text-embedding/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetTextEmbeddingResponse(),
            self.execute(params, req, runtime)
        )

    async def get_text_embedding_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetTextEmbeddingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetTextEmbeddingResponse:
        """
        @summary 文本向量化
        
        @param request: GetTextEmbeddingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTextEmbeddingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input):
            body['input'] = request.input
        if not UtilClient.is_unset(request.input_type):
            body['input_type'] = request.input_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTextEmbedding',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/text-embedding/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetTextEmbeddingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_text_embedding(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetTextEmbeddingRequest,
    ) -> searchplat_20240529_models.GetTextEmbeddingResponse:
        """
        @summary 文本向量化
        
        @param request: GetTextEmbeddingRequest
        @return: GetTextEmbeddingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_text_embedding_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_text_embedding_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetTextEmbeddingRequest,
    ) -> searchplat_20240529_models.GetTextEmbeddingResponse:
        """
        @summary 文本向量化
        
        @param request: GetTextEmbeddingRequest
        @return: GetTextEmbeddingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_text_embedding_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_text_generation_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetTextGenerationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetTextGenerationResponse:
        """
        @summary 大模型问答
        
        @param request: GetTextGenerationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTextGenerationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.csi_level):
            body['csi_level'] = request.csi_level
        if not UtilClient.is_unset(request.enable_search):
            body['enable_search'] = request.enable_search
        if not UtilClient.is_unset(request.messages):
            body['messages'] = request.messages
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTextGeneration',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/text-generation/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetTextGenerationResponse(),
            self.execute(params, req, runtime)
        )

    async def get_text_generation_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetTextGenerationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetTextGenerationResponse:
        """
        @summary 大模型问答
        
        @param request: GetTextGenerationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTextGenerationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.csi_level):
            body['csi_level'] = request.csi_level
        if not UtilClient.is_unset(request.enable_search):
            body['enable_search'] = request.enable_search
        if not UtilClient.is_unset(request.messages):
            body['messages'] = request.messages
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTextGeneration',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/text-generation/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetTextGenerationResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_text_generation(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetTextGenerationRequest,
    ) -> searchplat_20240529_models.GetTextGenerationResponse:
        """
        @summary 大模型问答
        
        @param request: GetTextGenerationRequest
        @return: GetTextGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_text_generation_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_text_generation_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetTextGenerationRequest,
    ) -> searchplat_20240529_models.GetTextGenerationResponse:
        """
        @summary 大模型问答
        
        @param request: GetTextGenerationRequest
        @return: GetTextGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_text_generation_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_text_sparse_embedding_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetTextSparseEmbeddingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetTextSparseEmbeddingResponse:
        """
        @summary 文本稀疏向量化
        
        @param request: GetTextSparseEmbeddingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTextSparseEmbeddingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input):
            body['input'] = request.input
        if not UtilClient.is_unset(request.input_type):
            body['input_type'] = request.input_type
        if not UtilClient.is_unset(request.return_token):
            body['return_token'] = request.return_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTextSparseEmbedding',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/text-sparse-embedding/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetTextSparseEmbeddingResponse(),
            self.execute(params, req, runtime)
        )

    async def get_text_sparse_embedding_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetTextSparseEmbeddingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetTextSparseEmbeddingResponse:
        """
        @summary 文本稀疏向量化
        
        @param request: GetTextSparseEmbeddingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTextSparseEmbeddingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input):
            body['input'] = request.input
        if not UtilClient.is_unset(request.input_type):
            body['input_type'] = request.input_type
        if not UtilClient.is_unset(request.return_token):
            body['return_token'] = request.return_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTextSparseEmbedding',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/text-sparse-embedding/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetTextSparseEmbeddingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_text_sparse_embedding(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetTextSparseEmbeddingRequest,
    ) -> searchplat_20240529_models.GetTextSparseEmbeddingResponse:
        """
        @summary 文本稀疏向量化
        
        @param request: GetTextSparseEmbeddingRequest
        @return: GetTextSparseEmbeddingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_text_sparse_embedding_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_text_sparse_embedding_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetTextSparseEmbeddingRequest,
    ) -> searchplat_20240529_models.GetTextSparseEmbeddingResponse:
        """
        @summary 文本稀疏向量化
        
        @param request: GetTextSparseEmbeddingRequest
        @return: GetTextSparseEmbeddingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_text_sparse_embedding_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_web_search_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetWebSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetWebSearchResponse:
        """
        @summary 联网搜索
        
        @param request: GetWebSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWebSearchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.top_k):
            body['top_k'] = request.top_k
        if not UtilClient.is_unset(request.way):
            body['way'] = request.way
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWebSearch',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/web-search/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetWebSearchResponse(),
            self.execute(params, req, runtime)
        )

    async def get_web_search_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetWebSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchplat_20240529_models.GetWebSearchResponse:
        """
        @summary 联网搜索
        
        @param request: GetWebSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWebSearchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.top_k):
            body['top_k'] = request.top_k
        if not UtilClient.is_unset(request.way):
            body['way'] = request.way
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWebSearch',
            version='2024-05-29',
            protocol='HTTPS',
            pathname=f'/v3/openapi/workspaces/{workspace_name}/web-search/{service_id}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchplat_20240529_models.GetWebSearchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_web_search(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetWebSearchRequest,
    ) -> searchplat_20240529_models.GetWebSearchResponse:
        """
        @summary 联网搜索
        
        @param request: GetWebSearchRequest
        @return: GetWebSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_web_search_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_web_search_async(
        self,
        workspace_name: str,
        service_id: str,
        request: searchplat_20240529_models.GetWebSearchRequest,
    ) -> searchplat_20240529_models.GetWebSearchResponse:
        """
        @summary 联网搜索
        
        @param request: GetWebSearchRequest
        @return: GetWebSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_web_search_with_options_async(workspace_name, service_id, request, headers, runtime)
