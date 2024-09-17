# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_bailian20231229 import models as bailian_20231229_models
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
        self._endpoint = self.get_endpoint('bailian', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_category_with_options(
        self,
        workspace_id: str,
        request: bailian_20231229_models.AddCategoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.AddCategoryResponse:
        """
        @param request: AddCategoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCategoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_name):
            body['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.category_type):
            body['CategoryType'] = request.category_type
        if not UtilClient.is_unset(request.parent_category_id):
            body['ParentCategoryId'] = request.parent_category_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCategory',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/category/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.AddCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_category_with_options_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.AddCategoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.AddCategoryResponse:
        """
        @param request: AddCategoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCategoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_name):
            body['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.category_type):
            body['CategoryType'] = request.category_type
        if not UtilClient.is_unset(request.parent_category_id):
            body['ParentCategoryId'] = request.parent_category_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCategory',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/category/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.AddCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_category(
        self,
        workspace_id: str,
        request: bailian_20231229_models.AddCategoryRequest,
    ) -> bailian_20231229_models.AddCategoryResponse:
        """
        @param request: AddCategoryRequest
        @return: AddCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_category_with_options(workspace_id, request, headers, runtime)

    async def add_category_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.AddCategoryRequest,
    ) -> bailian_20231229_models.AddCategoryResponse:
        """
        @param request: AddCategoryRequest
        @return: AddCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_category_with_options_async(workspace_id, request, headers, runtime)

    def add_file_with_options(
        self,
        workspace_id: str,
        request: bailian_20231229_models.AddFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.AddFileResponse:
        """
        @summary 将临时上传的文档导入百炼数据中心，导入成功之后会自动触发文档解析。
        
        @param request: AddFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.lease_id):
            body['LeaseId'] = request.lease_id
        if not UtilClient.is_unset(request.parser):
            body['Parser'] = request.parser
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFile',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/file',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.AddFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_file_with_options_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.AddFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.AddFileResponse:
        """
        @summary 将临时上传的文档导入百炼数据中心，导入成功之后会自动触发文档解析。
        
        @param request: AddFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.lease_id):
            body['LeaseId'] = request.lease_id
        if not UtilClient.is_unset(request.parser):
            body['Parser'] = request.parser
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFile',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/file',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.AddFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_file(
        self,
        workspace_id: str,
        request: bailian_20231229_models.AddFileRequest,
    ) -> bailian_20231229_models.AddFileResponse:
        """
        @summary 将临时上传的文档导入百炼数据中心，导入成功之后会自动触发文档解析。
        
        @param request: AddFileRequest
        @return: AddFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_file_with_options(workspace_id, request, headers, runtime)

    async def add_file_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.AddFileRequest,
    ) -> bailian_20231229_models.AddFileResponse:
        """
        @summary 将临时上传的文档导入百炼数据中心，导入成功之后会自动触发文档解析。
        
        @param request: AddFileRequest
        @return: AddFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_file_with_options_async(workspace_id, request, headers, runtime)

    def apply_file_upload_lease_with_options(
        self,
        category_id: str,
        workspace_id: str,
        request: bailian_20231229_models.ApplyFileUploadLeaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ApplyFileUploadLeaseResponse:
        """
        @summary 请求文档上传租约，进行文档上传。
        
        @param request: ApplyFileUploadLeaseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyFileUploadLeaseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.md_5):
            body['Md5'] = request.md_5
        if not UtilClient.is_unset(request.size_in_bytes):
            body['SizeInBytes'] = request.size_in_bytes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyFileUploadLease',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/category/{OpenApiUtilClient.get_encode_param(category_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ApplyFileUploadLeaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_file_upload_lease_with_options_async(
        self,
        category_id: str,
        workspace_id: str,
        request: bailian_20231229_models.ApplyFileUploadLeaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ApplyFileUploadLeaseResponse:
        """
        @summary 请求文档上传租约，进行文档上传。
        
        @param request: ApplyFileUploadLeaseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyFileUploadLeaseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.md_5):
            body['Md5'] = request.md_5
        if not UtilClient.is_unset(request.size_in_bytes):
            body['SizeInBytes'] = request.size_in_bytes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyFileUploadLease',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/category/{OpenApiUtilClient.get_encode_param(category_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ApplyFileUploadLeaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_file_upload_lease(
        self,
        category_id: str,
        workspace_id: str,
        request: bailian_20231229_models.ApplyFileUploadLeaseRequest,
    ) -> bailian_20231229_models.ApplyFileUploadLeaseResponse:
        """
        @summary 请求文档上传租约，进行文档上传。
        
        @param request: ApplyFileUploadLeaseRequest
        @return: ApplyFileUploadLeaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.apply_file_upload_lease_with_options(category_id, workspace_id, request, headers, runtime)

    async def apply_file_upload_lease_async(
        self,
        category_id: str,
        workspace_id: str,
        request: bailian_20231229_models.ApplyFileUploadLeaseRequest,
    ) -> bailian_20231229_models.ApplyFileUploadLeaseResponse:
        """
        @summary 请求文档上传租约，进行文档上传。
        
        @param request: ApplyFileUploadLeaseRequest
        @return: ApplyFileUploadLeaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.apply_file_upload_lease_with_options_async(category_id, workspace_id, request, headers, runtime)

    def create_and_pulish_agent_with_options(
        self,
        workspace_id: str,
        tmp_req: bailian_20231229_models.CreateAndPulishAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.CreateAndPulishAgentResponse:
        """
        @summary 创建并发布智能体应用
        
        @param tmp_req: CreateAndPulishAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAndPulishAgentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bailian_20231229_models.CreateAndPulishAgentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_config):
            request.application_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_config, 'applicationConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_config_shrink):
            body['applicationConfig'] = request.application_config_shrink
        if not UtilClient.is_unset(request.instructions):
            body['instructions'] = request.instructions
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAndPulishAgent',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/application/agents',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.CreateAndPulishAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_and_pulish_agent_with_options_async(
        self,
        workspace_id: str,
        tmp_req: bailian_20231229_models.CreateAndPulishAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.CreateAndPulishAgentResponse:
        """
        @summary 创建并发布智能体应用
        
        @param tmp_req: CreateAndPulishAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAndPulishAgentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bailian_20231229_models.CreateAndPulishAgentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_config):
            request.application_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_config, 'applicationConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_config_shrink):
            body['applicationConfig'] = request.application_config_shrink
        if not UtilClient.is_unset(request.instructions):
            body['instructions'] = request.instructions
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAndPulishAgent',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/application/agents',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.CreateAndPulishAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_and_pulish_agent(
        self,
        workspace_id: str,
        request: bailian_20231229_models.CreateAndPulishAgentRequest,
    ) -> bailian_20231229_models.CreateAndPulishAgentResponse:
        """
        @summary 创建并发布智能体应用
        
        @param request: CreateAndPulishAgentRequest
        @return: CreateAndPulishAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_and_pulish_agent_with_options(workspace_id, request, headers, runtime)

    async def create_and_pulish_agent_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.CreateAndPulishAgentRequest,
    ) -> bailian_20231229_models.CreateAndPulishAgentResponse:
        """
        @summary 创建并发布智能体应用
        
        @param request: CreateAndPulishAgentRequest
        @return: CreateAndPulishAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_and_pulish_agent_with_options_async(workspace_id, request, headers, runtime)

    def create_index_with_options(
        self,
        workspace_id: str,
        tmp_req: bailian_20231229_models.CreateIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.CreateIndexResponse:
        """
        @summary 创建并运行pipeline
        
        @param tmp_req: CreateIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIndexResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bailian_20231229_models.CreateIndexShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.category_ids):
            request.category_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not UtilClient.is_unset(tmp_req.columns):
            request.columns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.columns, 'Columns', 'json')
        if not UtilClient.is_unset(tmp_req.data_source):
            request.data_source_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source, 'DataSource', 'json')
        if not UtilClient.is_unset(tmp_req.document_ids):
            request.document_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.category_ids_shrink):
            query['CategoryIds'] = request.category_ids_shrink
        if not UtilClient.is_unset(request.chunk_size):
            query['ChunkSize'] = request.chunk_size
        if not UtilClient.is_unset(request.columns_shrink):
            query['Columns'] = request.columns_shrink
        if not UtilClient.is_unset(request.data_source_shrink):
            query['DataSource'] = request.data_source_shrink
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.document_ids_shrink):
            query['DocumentIds'] = request.document_ids_shrink
        if not UtilClient.is_unset(request.embedding_model_name):
            query['EmbeddingModelName'] = request.embedding_model_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.overlap_size):
            query['OverlapSize'] = request.overlap_size
        if not UtilClient.is_unset(request.rerank_min_score):
            query['RerankMinScore'] = request.rerank_min_score
        if not UtilClient.is_unset(request.rerank_model_name):
            query['RerankModelName'] = request.rerank_model_name
        if not UtilClient.is_unset(request.separator):
            query['Separator'] = request.separator
        if not UtilClient.is_unset(request.sink_instance_id):
            query['SinkInstanceId'] = request.sink_instance_id
        if not UtilClient.is_unset(request.sink_region):
            query['SinkRegion'] = request.sink_region
        if not UtilClient.is_unset(request.sink_type):
            query['SinkType'] = request.sink_type
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.structure_type):
            query['StructureType'] = request.structure_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIndex',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.CreateIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_index_with_options_async(
        self,
        workspace_id: str,
        tmp_req: bailian_20231229_models.CreateIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.CreateIndexResponse:
        """
        @summary 创建并运行pipeline
        
        @param tmp_req: CreateIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIndexResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bailian_20231229_models.CreateIndexShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.category_ids):
            request.category_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not UtilClient.is_unset(tmp_req.columns):
            request.columns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.columns, 'Columns', 'json')
        if not UtilClient.is_unset(tmp_req.data_source):
            request.data_source_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source, 'DataSource', 'json')
        if not UtilClient.is_unset(tmp_req.document_ids):
            request.document_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.category_ids_shrink):
            query['CategoryIds'] = request.category_ids_shrink
        if not UtilClient.is_unset(request.chunk_size):
            query['ChunkSize'] = request.chunk_size
        if not UtilClient.is_unset(request.columns_shrink):
            query['Columns'] = request.columns_shrink
        if not UtilClient.is_unset(request.data_source_shrink):
            query['DataSource'] = request.data_source_shrink
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.document_ids_shrink):
            query['DocumentIds'] = request.document_ids_shrink
        if not UtilClient.is_unset(request.embedding_model_name):
            query['EmbeddingModelName'] = request.embedding_model_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.overlap_size):
            query['OverlapSize'] = request.overlap_size
        if not UtilClient.is_unset(request.rerank_min_score):
            query['RerankMinScore'] = request.rerank_min_score
        if not UtilClient.is_unset(request.rerank_model_name):
            query['RerankModelName'] = request.rerank_model_name
        if not UtilClient.is_unset(request.separator):
            query['Separator'] = request.separator
        if not UtilClient.is_unset(request.sink_instance_id):
            query['SinkInstanceId'] = request.sink_instance_id
        if not UtilClient.is_unset(request.sink_region):
            query['SinkRegion'] = request.sink_region
        if not UtilClient.is_unset(request.sink_type):
            query['SinkType'] = request.sink_type
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.structure_type):
            query['StructureType'] = request.structure_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIndex',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.CreateIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_index(
        self,
        workspace_id: str,
        request: bailian_20231229_models.CreateIndexRequest,
    ) -> bailian_20231229_models.CreateIndexResponse:
        """
        @summary 创建并运行pipeline
        
        @param request: CreateIndexRequest
        @return: CreateIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_index_with_options(workspace_id, request, headers, runtime)

    async def create_index_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.CreateIndexRequest,
    ) -> bailian_20231229_models.CreateIndexResponse:
        """
        @summary 创建并运行pipeline
        
        @param request: CreateIndexRequest
        @return: CreateIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_index_with_options_async(workspace_id, request, headers, runtime)

    def create_memory_with_options(
        self,
        workspace_id: str,
        request: bailian_20231229_models.CreateMemoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.CreateMemoryResponse:
        """
        @summary 创建Memory
        
        @param request: CreateMemoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMemoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMemory',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.CreateMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_memory_with_options_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.CreateMemoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.CreateMemoryResponse:
        """
        @summary 创建Memory
        
        @param request: CreateMemoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMemoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMemory',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.CreateMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_memory(
        self,
        workspace_id: str,
        request: bailian_20231229_models.CreateMemoryRequest,
    ) -> bailian_20231229_models.CreateMemoryResponse:
        """
        @summary 创建Memory
        
        @param request: CreateMemoryRequest
        @return: CreateMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_memory_with_options(workspace_id, request, headers, runtime)

    async def create_memory_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.CreateMemoryRequest,
    ) -> bailian_20231229_models.CreateMemoryResponse:
        """
        @summary 创建Memory
        
        @param request: CreateMemoryRequest
        @return: CreateMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_memory_with_options_async(workspace_id, request, headers, runtime)

    def create_memory_node_with_options(
        self,
        workspace_id: str,
        memory_id: str,
        request: bailian_20231229_models.CreateMemoryNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.CreateMemoryNodeResponse:
        """
        @summary 创建记忆Node
        
        @param request: CreateMemoryNodeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMemoryNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['content'] = request.content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMemoryNode',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories/{OpenApiUtilClient.get_encode_param(memory_id)}/memoryNodes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.CreateMemoryNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_memory_node_with_options_async(
        self,
        workspace_id: str,
        memory_id: str,
        request: bailian_20231229_models.CreateMemoryNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.CreateMemoryNodeResponse:
        """
        @summary 创建记忆Node
        
        @param request: CreateMemoryNodeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMemoryNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['content'] = request.content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMemoryNode',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories/{OpenApiUtilClient.get_encode_param(memory_id)}/memoryNodes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.CreateMemoryNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_memory_node(
        self,
        workspace_id: str,
        memory_id: str,
        request: bailian_20231229_models.CreateMemoryNodeRequest,
    ) -> bailian_20231229_models.CreateMemoryNodeResponse:
        """
        @summary 创建记忆Node
        
        @param request: CreateMemoryNodeRequest
        @return: CreateMemoryNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_memory_node_with_options(workspace_id, memory_id, request, headers, runtime)

    async def create_memory_node_async(
        self,
        workspace_id: str,
        memory_id: str,
        request: bailian_20231229_models.CreateMemoryNodeRequest,
    ) -> bailian_20231229_models.CreateMemoryNodeResponse:
        """
        @summary 创建记忆Node
        
        @param request: CreateMemoryNodeRequest
        @return: CreateMemoryNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_memory_node_with_options_async(workspace_id, memory_id, request, headers, runtime)

    def delete_agent_with_options(
        self,
        workspace_id: str,
        app_code: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DeleteAgentResponse:
        """
        @summary 删除智能体
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAgentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAgent',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/application/agents/{OpenApiUtilClient.get_encode_param(app_code)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DeleteAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_with_options_async(
        self,
        workspace_id: str,
        app_code: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DeleteAgentResponse:
        """
        @summary 删除智能体
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAgentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAgent',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/application/agents/{OpenApiUtilClient.get_encode_param(app_code)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DeleteAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent(
        self,
        workspace_id: str,
        app_code: str,
    ) -> bailian_20231229_models.DeleteAgentResponse:
        """
        @summary 删除智能体
        
        @return: DeleteAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_agent_with_options(workspace_id, app_code, headers, runtime)

    async def delete_agent_async(
        self,
        workspace_id: str,
        app_code: str,
    ) -> bailian_20231229_models.DeleteAgentResponse:
        """
        @summary 删除智能体
        
        @return: DeleteAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_agent_with_options_async(workspace_id, app_code, headers, runtime)

    def delete_category_with_options(
        self,
        category_id: str,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DeleteCategoryResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCategoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCategory',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/category/{OpenApiUtilClient.get_encode_param(category_id)}/',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DeleteCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_category_with_options_async(
        self,
        category_id: str,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DeleteCategoryResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCategoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCategory',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/category/{OpenApiUtilClient.get_encode_param(category_id)}/',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DeleteCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_category(
        self,
        category_id: str,
        workspace_id: str,
    ) -> bailian_20231229_models.DeleteCategoryResponse:
        """
        @return: DeleteCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_category_with_options(category_id, workspace_id, headers, runtime)

    async def delete_category_async(
        self,
        category_id: str,
        workspace_id: str,
    ) -> bailian_20231229_models.DeleteCategoryResponse:
        """
        @return: DeleteCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_category_with_options_async(category_id, workspace_id, headers, runtime)

    def delete_file_with_options(
        self,
        file_id: str,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DeleteFileResponse:
        """
        @summary 删除文档
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFileResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/file/{OpenApiUtilClient.get_encode_param(file_id)}/',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DeleteFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_with_options_async(
        self,
        file_id: str,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DeleteFileResponse:
        """
        @summary 删除文档
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFileResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/file/{OpenApiUtilClient.get_encode_param(file_id)}/',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DeleteFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_file(
        self,
        file_id: str,
        workspace_id: str,
    ) -> bailian_20231229_models.DeleteFileResponse:
        """
        @summary 删除文档
        
        @return: DeleteFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_file_with_options(file_id, workspace_id, headers, runtime)

    async def delete_file_async(
        self,
        file_id: str,
        workspace_id: str,
    ) -> bailian_20231229_models.DeleteFileResponse:
        """
        @summary 删除文档
        
        @return: DeleteFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_file_with_options_async(file_id, workspace_id, headers, runtime)

    def delete_index_with_options(
        self,
        workspace_id: str,
        request: bailian_20231229_models.DeleteIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DeleteIndexResponse:
        """
        @summary 删除Index
        
        @param request: DeleteIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIndexResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIndex',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DeleteIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_index_with_options_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.DeleteIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DeleteIndexResponse:
        """
        @summary 删除Index
        
        @param request: DeleteIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIndexResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIndex',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DeleteIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_index(
        self,
        workspace_id: str,
        request: bailian_20231229_models.DeleteIndexRequest,
    ) -> bailian_20231229_models.DeleteIndexResponse:
        """
        @summary 删除Index
        
        @param request: DeleteIndexRequest
        @return: DeleteIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_index_with_options(workspace_id, request, headers, runtime)

    async def delete_index_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.DeleteIndexRequest,
    ) -> bailian_20231229_models.DeleteIndexResponse:
        """
        @summary 删除Index
        
        @param request: DeleteIndexRequest
        @return: DeleteIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_index_with_options_async(workspace_id, request, headers, runtime)

    def delete_index_document_with_options(
        self,
        workspace_id: str,
        tmp_req: bailian_20231229_models.DeleteIndexDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DeleteIndexDocumentResponse:
        """
        @summary 删除index doc
        
        @param tmp_req: DeleteIndexDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIndexDocumentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bailian_20231229_models.DeleteIndexDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.document_ids):
            request.document_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.document_ids_shrink):
            query['DocumentIds'] = request.document_ids_shrink
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIndexDocument',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/delete_index_document',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DeleteIndexDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_index_document_with_options_async(
        self,
        workspace_id: str,
        tmp_req: bailian_20231229_models.DeleteIndexDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DeleteIndexDocumentResponse:
        """
        @summary 删除index doc
        
        @param tmp_req: DeleteIndexDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIndexDocumentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bailian_20231229_models.DeleteIndexDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.document_ids):
            request.document_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.document_ids_shrink):
            query['DocumentIds'] = request.document_ids_shrink
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIndexDocument',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/delete_index_document',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DeleteIndexDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_index_document(
        self,
        workspace_id: str,
        request: bailian_20231229_models.DeleteIndexDocumentRequest,
    ) -> bailian_20231229_models.DeleteIndexDocumentResponse:
        """
        @summary 删除index doc
        
        @param request: DeleteIndexDocumentRequest
        @return: DeleteIndexDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_index_document_with_options(workspace_id, request, headers, runtime)

    async def delete_index_document_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.DeleteIndexDocumentRequest,
    ) -> bailian_20231229_models.DeleteIndexDocumentResponse:
        """
        @summary 删除index doc
        
        @param request: DeleteIndexDocumentRequest
        @return: DeleteIndexDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_index_document_with_options_async(workspace_id, request, headers, runtime)

    def delete_memory_with_options(
        self,
        workspace_id: str,
        memory_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DeleteMemoryResponse:
        """
        @summary 删除memory
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMemoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMemory',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories/{OpenApiUtilClient.get_encode_param(memory_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DeleteMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_memory_with_options_async(
        self,
        workspace_id: str,
        memory_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DeleteMemoryResponse:
        """
        @summary 删除memory
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMemoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMemory',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories/{OpenApiUtilClient.get_encode_param(memory_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DeleteMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_memory(
        self,
        workspace_id: str,
        memory_id: str,
    ) -> bailian_20231229_models.DeleteMemoryResponse:
        """
        @summary 删除memory
        
        @return: DeleteMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_memory_with_options(workspace_id, memory_id, headers, runtime)

    async def delete_memory_async(
        self,
        workspace_id: str,
        memory_id: str,
    ) -> bailian_20231229_models.DeleteMemoryResponse:
        """
        @summary 删除memory
        
        @return: DeleteMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_memory_with_options_async(workspace_id, memory_id, headers, runtime)

    def delete_memory_node_with_options(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DeleteMemoryNodeResponse:
        """
        @summary 删除记忆Node
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMemoryNodeResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMemoryNode',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories/{OpenApiUtilClient.get_encode_param(memory_id)}/memoryNodes/{OpenApiUtilClient.get_encode_param(memory_node_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DeleteMemoryNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_memory_node_with_options_async(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DeleteMemoryNodeResponse:
        """
        @summary 删除记忆Node
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMemoryNodeResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMemoryNode',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories/{OpenApiUtilClient.get_encode_param(memory_id)}/memoryNodes/{OpenApiUtilClient.get_encode_param(memory_node_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DeleteMemoryNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_memory_node(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
    ) -> bailian_20231229_models.DeleteMemoryNodeResponse:
        """
        @summary 删除记忆Node
        
        @return: DeleteMemoryNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_memory_node_with_options(workspace_id, memory_id, memory_node_id, headers, runtime)

    async def delete_memory_node_async(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
    ) -> bailian_20231229_models.DeleteMemoryNodeResponse:
        """
        @summary 删除记忆Node
        
        @return: DeleteMemoryNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_memory_node_with_options_async(workspace_id, memory_id, memory_node_id, headers, runtime)

    def describe_file_with_options(
        self,
        workspace_id: str,
        file_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DescribeFileResponse:
        """
        @summary 获取文档基本信息，包括文档名称、类型、状态等。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFileResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeFile',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/file/{OpenApiUtilClient.get_encode_param(file_id)}/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DescribeFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_file_with_options_async(
        self,
        workspace_id: str,
        file_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.DescribeFileResponse:
        """
        @summary 获取文档基本信息，包括文档名称、类型、状态等。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFileResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeFile',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/file/{OpenApiUtilClient.get_encode_param(file_id)}/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.DescribeFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_file(
        self,
        workspace_id: str,
        file_id: str,
    ) -> bailian_20231229_models.DescribeFileResponse:
        """
        @summary 获取文档基本信息，包括文档名称、类型、状态等。
        
        @return: DescribeFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_file_with_options(workspace_id, file_id, headers, runtime)

    async def describe_file_async(
        self,
        workspace_id: str,
        file_id: str,
    ) -> bailian_20231229_models.DescribeFileResponse:
        """
        @summary 获取文档基本信息，包括文档名称、类型、状态等。
        
        @return: DescribeFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_file_with_options_async(workspace_id, file_id, headers, runtime)

    def get_index_job_status_with_options(
        self,
        workspace_id: str,
        request: bailian_20231229_models.GetIndexJobStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.GetIndexJobStatusResponse:
        """
        @summary 获取Index运行状态
        
        @param request: GetIndexJobStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIndexJobStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIndexJobStatus',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/job/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.GetIndexJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_index_job_status_with_options_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.GetIndexJobStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.GetIndexJobStatusResponse:
        """
        @summary 获取Index运行状态
        
        @param request: GetIndexJobStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIndexJobStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIndexJobStatus',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/job/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.GetIndexJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_index_job_status(
        self,
        workspace_id: str,
        request: bailian_20231229_models.GetIndexJobStatusRequest,
    ) -> bailian_20231229_models.GetIndexJobStatusResponse:
        """
        @summary 获取Index运行状态
        
        @param request: GetIndexJobStatusRequest
        @return: GetIndexJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_index_job_status_with_options(workspace_id, request, headers, runtime)

    async def get_index_job_status_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.GetIndexJobStatusRequest,
    ) -> bailian_20231229_models.GetIndexJobStatusResponse:
        """
        @summary 获取Index运行状态
        
        @param request: GetIndexJobStatusRequest
        @return: GetIndexJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_index_job_status_with_options_async(workspace_id, request, headers, runtime)

    def get_memory_with_options(
        self,
        workspace_id: str,
        memory_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.GetMemoryResponse:
        """
        @summary 获取memory
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMemoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMemory',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories/{OpenApiUtilClient.get_encode_param(memory_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.GetMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_memory_with_options_async(
        self,
        workspace_id: str,
        memory_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.GetMemoryResponse:
        """
        @summary 获取memory
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMemoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMemory',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories/{OpenApiUtilClient.get_encode_param(memory_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.GetMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_memory(
        self,
        workspace_id: str,
        memory_id: str,
    ) -> bailian_20231229_models.GetMemoryResponse:
        """
        @summary 获取memory
        
        @return: GetMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_memory_with_options(workspace_id, memory_id, headers, runtime)

    async def get_memory_async(
        self,
        workspace_id: str,
        memory_id: str,
    ) -> bailian_20231229_models.GetMemoryResponse:
        """
        @summary 获取memory
        
        @return: GetMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_memory_with_options_async(workspace_id, memory_id, headers, runtime)

    def get_memory_node_with_options(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.GetMemoryNodeResponse:
        """
        @summary 获取记忆Node
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMemoryNodeResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMemoryNode',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories/{OpenApiUtilClient.get_encode_param(memory_id)}/memoryNodes/{OpenApiUtilClient.get_encode_param(memory_node_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.GetMemoryNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_memory_node_with_options_async(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.GetMemoryNodeResponse:
        """
        @summary 获取记忆Node
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMemoryNodeResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMemoryNode',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories/{OpenApiUtilClient.get_encode_param(memory_id)}/memoryNodes/{OpenApiUtilClient.get_encode_param(memory_node_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.GetMemoryNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_memory_node(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
    ) -> bailian_20231229_models.GetMemoryNodeResponse:
        """
        @summary 获取记忆Node
        
        @return: GetMemoryNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_memory_node_with_options(workspace_id, memory_id, memory_node_id, headers, runtime)

    async def get_memory_node_async(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
    ) -> bailian_20231229_models.GetMemoryNodeResponse:
        """
        @summary 获取记忆Node
        
        @return: GetMemoryNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_memory_node_with_options_async(workspace_id, memory_id, memory_node_id, headers, runtime)

    def get_published_agent_with_options(
        self,
        workspace_id: str,
        app_code: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.GetPublishedAgentResponse:
        """
        @summary 获取发布态智能体应用
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPublishedAgentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPublishedAgent',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/application/agents/{OpenApiUtilClient.get_encode_param(app_code)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.GetPublishedAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_published_agent_with_options_async(
        self,
        workspace_id: str,
        app_code: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.GetPublishedAgentResponse:
        """
        @summary 获取发布态智能体应用
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPublishedAgentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPublishedAgent',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/application/agents/{OpenApiUtilClient.get_encode_param(app_code)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.GetPublishedAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_published_agent(
        self,
        workspace_id: str,
        app_code: str,
    ) -> bailian_20231229_models.GetPublishedAgentResponse:
        """
        @summary 获取发布态智能体应用
        
        @return: GetPublishedAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_published_agent_with_options(workspace_id, app_code, headers, runtime)

    async def get_published_agent_async(
        self,
        workspace_id: str,
        app_code: str,
    ) -> bailian_20231229_models.GetPublishedAgentResponse:
        """
        @summary 获取发布态智能体应用
        
        @return: GetPublishedAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_published_agent_with_options_async(workspace_id, app_code, headers, runtime)

    def list_category_with_options(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListCategoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ListCategoryResponse:
        """
        @summary ListCategory
        
        @param request: ListCategoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCategoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_type):
            body['CategoryType'] = request.category_type
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.parent_category_id):
            body['ParentCategoryId'] = request.parent_category_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCategory',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/categories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ListCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_category_with_options_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListCategoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ListCategoryResponse:
        """
        @summary ListCategory
        
        @param request: ListCategoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCategoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_type):
            body['CategoryType'] = request.category_type
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.parent_category_id):
            body['ParentCategoryId'] = request.parent_category_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCategory',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/categories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ListCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_category(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListCategoryRequest,
    ) -> bailian_20231229_models.ListCategoryResponse:
        """
        @summary ListCategory
        
        @param request: ListCategoryRequest
        @return: ListCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_category_with_options(workspace_id, request, headers, runtime)

    async def list_category_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListCategoryRequest,
    ) -> bailian_20231229_models.ListCategoryResponse:
        """
        @summary ListCategory
        
        @param request: ListCategoryRequest
        @return: ListCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_category_with_options_async(workspace_id, request, headers, runtime)

    def list_chunks_with_options(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListChunksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ListChunksResponse:
        """
        @summary Chunk
        
        @param request: ListChunksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChunksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.filed):
            body['Filed'] = request.filed
        if not UtilClient.is_unset(request.index_id):
            body['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListChunks',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/list_chunks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ListChunksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chunks_with_options_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListChunksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ListChunksResponse:
        """
        @summary Chunk
        
        @param request: ListChunksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChunksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.filed):
            body['Filed'] = request.filed
        if not UtilClient.is_unset(request.index_id):
            body['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListChunks',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/list_chunks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ListChunksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chunks(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListChunksRequest,
    ) -> bailian_20231229_models.ListChunksResponse:
        """
        @summary Chunk
        
        @param request: ListChunksRequest
        @return: ListChunksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_chunks_with_options(workspace_id, request, headers, runtime)

    async def list_chunks_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListChunksRequest,
    ) -> bailian_20231229_models.ListChunksResponse:
        """
        @summary Chunk
        
        @param request: ListChunksRequest
        @return: ListChunksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_chunks_with_options_async(workspace_id, request, headers, runtime)

    def list_file_with_options(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ListFileResponse:
        """
        @summary 获取文档列表
        
        @param request: ListFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFile',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/files',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ListFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_file_with_options_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ListFileResponse:
        """
        @summary 获取文档列表
        
        @param request: ListFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFile',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/datacenter/files',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ListFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_file(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListFileRequest,
    ) -> bailian_20231229_models.ListFileResponse:
        """
        @summary 获取文档列表
        
        @param request: ListFileRequest
        @return: ListFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_file_with_options(workspace_id, request, headers, runtime)

    async def list_file_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListFileRequest,
    ) -> bailian_20231229_models.ListFileResponse:
        """
        @summary 获取文档列表
        
        @param request: ListFileRequest
        @return: ListFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_file_with_options_async(workspace_id, request, headers, runtime)

    def list_index_documents_with_options(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListIndexDocumentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ListIndexDocumentsResponse:
        """
        @summary 查询Index文件
        
        @param request: ListIndexDocumentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIndexDocumentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.document_name):
            query['DocumentName'] = request.document_name
        if not UtilClient.is_unset(request.document_status):
            query['DocumentStatus'] = request.document_status
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIndexDocuments',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/list_index_documents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ListIndexDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_index_documents_with_options_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListIndexDocumentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ListIndexDocumentsResponse:
        """
        @summary 查询Index文件
        
        @param request: ListIndexDocumentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIndexDocumentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.document_name):
            query['DocumentName'] = request.document_name
        if not UtilClient.is_unset(request.document_status):
            query['DocumentStatus'] = request.document_status
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIndexDocuments',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/list_index_documents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ListIndexDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_index_documents(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListIndexDocumentsRequest,
    ) -> bailian_20231229_models.ListIndexDocumentsResponse:
        """
        @summary 查询Index文件
        
        @param request: ListIndexDocumentsRequest
        @return: ListIndexDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_index_documents_with_options(workspace_id, request, headers, runtime)

    async def list_index_documents_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListIndexDocumentsRequest,
    ) -> bailian_20231229_models.ListIndexDocumentsResponse:
        """
        @summary 查询Index文件
        
        @param request: ListIndexDocumentsRequest
        @return: ListIndexDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_index_documents_with_options_async(workspace_id, request, headers, runtime)

    def list_indices_with_options(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListIndicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ListIndicesResponse:
        """
        @summary 查询pipeline
        
        @param request: ListIndicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIndicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.index_name):
            query['IndexName'] = request.index_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIndices',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/list_indices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ListIndicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_indices_with_options_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListIndicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ListIndicesResponse:
        """
        @summary 查询pipeline
        
        @param request: ListIndicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIndicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.index_name):
            query['IndexName'] = request.index_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIndices',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/list_indices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ListIndicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_indices(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListIndicesRequest,
    ) -> bailian_20231229_models.ListIndicesResponse:
        """
        @summary 查询pipeline
        
        @param request: ListIndicesRequest
        @return: ListIndicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_indices_with_options(workspace_id, request, headers, runtime)

    async def list_indices_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListIndicesRequest,
    ) -> bailian_20231229_models.ListIndicesResponse:
        """
        @summary 查询pipeline
        
        @param request: ListIndicesRequest
        @return: ListIndicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_indices_with_options_async(workspace_id, request, headers, runtime)

    def list_memories_with_options(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListMemoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ListMemoriesResponse:
        """
        @summary 获取memory
        
        @param request: ListMemoriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMemoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMemories',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ListMemoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_memories_with_options_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListMemoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ListMemoriesResponse:
        """
        @summary 获取memory
        
        @param request: ListMemoriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMemoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMemories',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ListMemoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_memories(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListMemoriesRequest,
    ) -> bailian_20231229_models.ListMemoriesResponse:
        """
        @summary 获取memory
        
        @param request: ListMemoriesRequest
        @return: ListMemoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_memories_with_options(workspace_id, request, headers, runtime)

    async def list_memories_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListMemoriesRequest,
    ) -> bailian_20231229_models.ListMemoriesResponse:
        """
        @summary 获取memory
        
        @param request: ListMemoriesRequest
        @return: ListMemoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_memories_with_options_async(workspace_id, request, headers, runtime)

    def list_memory_nodes_with_options(
        self,
        workspace_id: str,
        memory_id: str,
        request: bailian_20231229_models.ListMemoryNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ListMemoryNodesResponse:
        """
        @summary 获取记忆Node列表
        
        @param request: ListMemoryNodesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMemoryNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMemoryNodes',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories/{OpenApiUtilClient.get_encode_param(memory_id)}/memoryNodes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ListMemoryNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_memory_nodes_with_options_async(
        self,
        workspace_id: str,
        memory_id: str,
        request: bailian_20231229_models.ListMemoryNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ListMemoryNodesResponse:
        """
        @summary 获取记忆Node列表
        
        @param request: ListMemoryNodesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMemoryNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMemoryNodes',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories/{OpenApiUtilClient.get_encode_param(memory_id)}/memoryNodes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ListMemoryNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_memory_nodes(
        self,
        workspace_id: str,
        memory_id: str,
        request: bailian_20231229_models.ListMemoryNodesRequest,
    ) -> bailian_20231229_models.ListMemoryNodesResponse:
        """
        @summary 获取记忆Node列表
        
        @param request: ListMemoryNodesRequest
        @return: ListMemoryNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_memory_nodes_with_options(workspace_id, memory_id, request, headers, runtime)

    async def list_memory_nodes_async(
        self,
        workspace_id: str,
        memory_id: str,
        request: bailian_20231229_models.ListMemoryNodesRequest,
    ) -> bailian_20231229_models.ListMemoryNodesResponse:
        """
        @summary 获取记忆Node列表
        
        @param request: ListMemoryNodesRequest
        @return: ListMemoryNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_memory_nodes_with_options_async(workspace_id, memory_id, request, headers, runtime)

    def list_published_agent_with_options(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListPublishedAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ListPublishedAgentResponse:
        """
        @summary 查询已发布的智能体应用列表
        
        @param request: ListPublishedAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublishedAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['pageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishedAgent',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/application/agents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ListPublishedAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_published_agent_with_options_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListPublishedAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.ListPublishedAgentResponse:
        """
        @summary 查询已发布的智能体应用列表
        
        @param request: ListPublishedAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublishedAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['pageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishedAgent',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/application/agents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.ListPublishedAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_published_agent(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListPublishedAgentRequest,
    ) -> bailian_20231229_models.ListPublishedAgentResponse:
        """
        @summary 查询已发布的智能体应用列表
        
        @param request: ListPublishedAgentRequest
        @return: ListPublishedAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_published_agent_with_options(workspace_id, request, headers, runtime)

    async def list_published_agent_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.ListPublishedAgentRequest,
    ) -> bailian_20231229_models.ListPublishedAgentResponse:
        """
        @summary 查询已发布的智能体应用列表
        
        @param request: ListPublishedAgentRequest
        @return: ListPublishedAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_published_agent_with_options_async(workspace_id, request, headers, runtime)

    def retrieve_with_options(
        self,
        workspace_id: str,
        tmp_req: bailian_20231229_models.RetrieveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.RetrieveResponse:
        """
        @summary 召回测试
        
        @param tmp_req: RetrieveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetrieveResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bailian_20231229_models.RetrieveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.images):
            request.images_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.images, 'Images', 'simple')
        if not UtilClient.is_unset(tmp_req.rerank):
            request.rerank_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rerank, 'Rerank', 'json')
        if not UtilClient.is_unset(tmp_req.rewrite):
            request.rewrite_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rewrite, 'Rewrite', 'json')
        if not UtilClient.is_unset(tmp_req.search_filters):
            request.search_filters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.search_filters, 'SearchFilters', 'json')
        query = {}
        if not UtilClient.is_unset(request.dense_similarity_top_k):
            query['DenseSimilarityTopK'] = request.dense_similarity_top_k
        if not UtilClient.is_unset(request.enable_reranking):
            query['EnableReranking'] = request.enable_reranking
        if not UtilClient.is_unset(request.enable_rewrite):
            query['EnableRewrite'] = request.enable_rewrite
        if not UtilClient.is_unset(request.images_shrink):
            query['Images'] = request.images_shrink
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.rerank_shrink):
            query['Rerank'] = request.rerank_shrink
        if not UtilClient.is_unset(request.rerank_min_score):
            query['RerankMinScore'] = request.rerank_min_score
        if not UtilClient.is_unset(request.rerank_top_n):
            query['RerankTopN'] = request.rerank_top_n
        if not UtilClient.is_unset(request.rewrite_shrink):
            query['Rewrite'] = request.rewrite_shrink
        if not UtilClient.is_unset(request.save_retriever_history):
            query['SaveRetrieverHistory'] = request.save_retriever_history
        if not UtilClient.is_unset(request.search_filters_shrink):
            query['SearchFilters'] = request.search_filters_shrink
        if not UtilClient.is_unset(request.sparse_similarity_top_k):
            query['SparseSimilarityTopK'] = request.sparse_similarity_top_k
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Retrieve',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/retrieve',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.RetrieveResponse(),
            self.call_api(params, req, runtime)
        )

    async def retrieve_with_options_async(
        self,
        workspace_id: str,
        tmp_req: bailian_20231229_models.RetrieveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.RetrieveResponse:
        """
        @summary 召回测试
        
        @param tmp_req: RetrieveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetrieveResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bailian_20231229_models.RetrieveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.images):
            request.images_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.images, 'Images', 'simple')
        if not UtilClient.is_unset(tmp_req.rerank):
            request.rerank_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rerank, 'Rerank', 'json')
        if not UtilClient.is_unset(tmp_req.rewrite):
            request.rewrite_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rewrite, 'Rewrite', 'json')
        if not UtilClient.is_unset(tmp_req.search_filters):
            request.search_filters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.search_filters, 'SearchFilters', 'json')
        query = {}
        if not UtilClient.is_unset(request.dense_similarity_top_k):
            query['DenseSimilarityTopK'] = request.dense_similarity_top_k
        if not UtilClient.is_unset(request.enable_reranking):
            query['EnableReranking'] = request.enable_reranking
        if not UtilClient.is_unset(request.enable_rewrite):
            query['EnableRewrite'] = request.enable_rewrite
        if not UtilClient.is_unset(request.images_shrink):
            query['Images'] = request.images_shrink
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.rerank_shrink):
            query['Rerank'] = request.rerank_shrink
        if not UtilClient.is_unset(request.rerank_min_score):
            query['RerankMinScore'] = request.rerank_min_score
        if not UtilClient.is_unset(request.rerank_top_n):
            query['RerankTopN'] = request.rerank_top_n
        if not UtilClient.is_unset(request.rewrite_shrink):
            query['Rewrite'] = request.rewrite_shrink
        if not UtilClient.is_unset(request.save_retriever_history):
            query['SaveRetrieverHistory'] = request.save_retriever_history
        if not UtilClient.is_unset(request.search_filters_shrink):
            query['SearchFilters'] = request.search_filters_shrink
        if not UtilClient.is_unset(request.sparse_similarity_top_k):
            query['SparseSimilarityTopK'] = request.sparse_similarity_top_k
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Retrieve',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/retrieve',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.RetrieveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retrieve(
        self,
        workspace_id: str,
        request: bailian_20231229_models.RetrieveRequest,
    ) -> bailian_20231229_models.RetrieveResponse:
        """
        @summary 召回测试
        
        @param request: RetrieveRequest
        @return: RetrieveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.retrieve_with_options(workspace_id, request, headers, runtime)

    async def retrieve_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.RetrieveRequest,
    ) -> bailian_20231229_models.RetrieveResponse:
        """
        @summary 召回测试
        
        @param request: RetrieveRequest
        @return: RetrieveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.retrieve_with_options_async(workspace_id, request, headers, runtime)

    def submit_index_add_documents_job_with_options(
        self,
        workspace_id: str,
        tmp_req: bailian_20231229_models.SubmitIndexAddDocumentsJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.SubmitIndexAddDocumentsJobResponse:
        """
        @summary 知识索引
        
        @param tmp_req: SubmitIndexAddDocumentsJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitIndexAddDocumentsJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bailian_20231229_models.SubmitIndexAddDocumentsJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.category_ids):
            request.category_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not UtilClient.is_unset(tmp_req.document_ids):
            request.document_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.category_ids_shrink):
            query['CategoryIds'] = request.category_ids_shrink
        if not UtilClient.is_unset(request.document_ids_shrink):
            query['DocumentIds'] = request.document_ids_shrink
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIndexAddDocumentsJob',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/add_documents_to_index',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.SubmitIndexAddDocumentsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_index_add_documents_job_with_options_async(
        self,
        workspace_id: str,
        tmp_req: bailian_20231229_models.SubmitIndexAddDocumentsJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.SubmitIndexAddDocumentsJobResponse:
        """
        @summary 知识索引
        
        @param tmp_req: SubmitIndexAddDocumentsJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitIndexAddDocumentsJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bailian_20231229_models.SubmitIndexAddDocumentsJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.category_ids):
            request.category_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not UtilClient.is_unset(tmp_req.document_ids):
            request.document_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.category_ids_shrink):
            query['CategoryIds'] = request.category_ids_shrink
        if not UtilClient.is_unset(request.document_ids_shrink):
            query['DocumentIds'] = request.document_ids_shrink
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIndexAddDocumentsJob',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/add_documents_to_index',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.SubmitIndexAddDocumentsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_index_add_documents_job(
        self,
        workspace_id: str,
        request: bailian_20231229_models.SubmitIndexAddDocumentsJobRequest,
    ) -> bailian_20231229_models.SubmitIndexAddDocumentsJobResponse:
        """
        @summary 知识索引
        
        @param request: SubmitIndexAddDocumentsJobRequest
        @return: SubmitIndexAddDocumentsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_index_add_documents_job_with_options(workspace_id, request, headers, runtime)

    async def submit_index_add_documents_job_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.SubmitIndexAddDocumentsJobRequest,
    ) -> bailian_20231229_models.SubmitIndexAddDocumentsJobResponse:
        """
        @summary 知识索引
        
        @param request: SubmitIndexAddDocumentsJobRequest
        @return: SubmitIndexAddDocumentsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_index_add_documents_job_with_options_async(workspace_id, request, headers, runtime)

    def submit_index_job_with_options(
        self,
        workspace_id: str,
        request: bailian_20231229_models.SubmitIndexJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.SubmitIndexJobResponse:
        """
        @summary 提交索引任务
        
        @param request: SubmitIndexJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitIndexJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIndexJob',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/submit_index_job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.SubmitIndexJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_index_job_with_options_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.SubmitIndexJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.SubmitIndexJobResponse:
        """
        @summary 提交索引任务
        
        @param request: SubmitIndexJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitIndexJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIndexJob',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/index/submit_index_job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.SubmitIndexJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_index_job(
        self,
        workspace_id: str,
        request: bailian_20231229_models.SubmitIndexJobRequest,
    ) -> bailian_20231229_models.SubmitIndexJobResponse:
        """
        @summary 提交索引任务
        
        @param request: SubmitIndexJobRequest
        @return: SubmitIndexJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_index_job_with_options(workspace_id, request, headers, runtime)

    async def submit_index_job_async(
        self,
        workspace_id: str,
        request: bailian_20231229_models.SubmitIndexJobRequest,
    ) -> bailian_20231229_models.SubmitIndexJobResponse:
        """
        @summary 提交索引任务
        
        @param request: SubmitIndexJobRequest
        @return: SubmitIndexJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_index_job_with_options_async(workspace_id, request, headers, runtime)

    def update_and_publish_agent_with_options(
        self,
        workspace_id: str,
        app_code: str,
        tmp_req: bailian_20231229_models.UpdateAndPublishAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.UpdateAndPublishAgentResponse:
        """
        @summary 更新并发布智能体应用
        
        @param tmp_req: UpdateAndPublishAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAndPublishAgentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bailian_20231229_models.UpdateAndPublishAgentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_config):
            request.application_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_config, 'applicationConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_config_shrink):
            body['applicationConfig'] = request.application_config_shrink
        if not UtilClient.is_unset(request.instructions):
            body['instructions'] = request.instructions
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAndPublishAgent',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/application/agents/{OpenApiUtilClient.get_encode_param(app_code)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.UpdateAndPublishAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_and_publish_agent_with_options_async(
        self,
        workspace_id: str,
        app_code: str,
        tmp_req: bailian_20231229_models.UpdateAndPublishAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.UpdateAndPublishAgentResponse:
        """
        @summary 更新并发布智能体应用
        
        @param tmp_req: UpdateAndPublishAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAndPublishAgentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bailian_20231229_models.UpdateAndPublishAgentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_config):
            request.application_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_config, 'applicationConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_config_shrink):
            body['applicationConfig'] = request.application_config_shrink
        if not UtilClient.is_unset(request.instructions):
            body['instructions'] = request.instructions
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAndPublishAgent',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/application/agents/{OpenApiUtilClient.get_encode_param(app_code)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.UpdateAndPublishAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_and_publish_agent(
        self,
        workspace_id: str,
        app_code: str,
        request: bailian_20231229_models.UpdateAndPublishAgentRequest,
    ) -> bailian_20231229_models.UpdateAndPublishAgentResponse:
        """
        @summary 更新并发布智能体应用
        
        @param request: UpdateAndPublishAgentRequest
        @return: UpdateAndPublishAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_and_publish_agent_with_options(workspace_id, app_code, request, headers, runtime)

    async def update_and_publish_agent_async(
        self,
        workspace_id: str,
        app_code: str,
        request: bailian_20231229_models.UpdateAndPublishAgentRequest,
    ) -> bailian_20231229_models.UpdateAndPublishAgentResponse:
        """
        @summary 更新并发布智能体应用
        
        @param request: UpdateAndPublishAgentRequest
        @return: UpdateAndPublishAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_and_publish_agent_with_options_async(workspace_id, app_code, request, headers, runtime)

    def update_memory_with_options(
        self,
        workspace_id: str,
        memory_id: str,
        request: bailian_20231229_models.UpdateMemoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.UpdateMemoryResponse:
        """
        @summary 更新memory
        
        @param request: UpdateMemoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMemoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMemory',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories/{OpenApiUtilClient.get_encode_param(memory_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.UpdateMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_memory_with_options_async(
        self,
        workspace_id: str,
        memory_id: str,
        request: bailian_20231229_models.UpdateMemoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.UpdateMemoryResponse:
        """
        @summary 更新memory
        
        @param request: UpdateMemoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMemoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMemory',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories/{OpenApiUtilClient.get_encode_param(memory_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.UpdateMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_memory(
        self,
        workspace_id: str,
        memory_id: str,
        request: bailian_20231229_models.UpdateMemoryRequest,
    ) -> bailian_20231229_models.UpdateMemoryResponse:
        """
        @summary 更新memory
        
        @param request: UpdateMemoryRequest
        @return: UpdateMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_memory_with_options(workspace_id, memory_id, request, headers, runtime)

    async def update_memory_async(
        self,
        workspace_id: str,
        memory_id: str,
        request: bailian_20231229_models.UpdateMemoryRequest,
    ) -> bailian_20231229_models.UpdateMemoryResponse:
        """
        @summary 更新memory
        
        @param request: UpdateMemoryRequest
        @return: UpdateMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_memory_with_options_async(workspace_id, memory_id, request, headers, runtime)

    def update_memory_node_with_options(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
        request: bailian_20231229_models.UpdateMemoryNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.UpdateMemoryNodeResponse:
        """
        @summary 更新记忆Node
        
        @param request: UpdateMemoryNodeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMemoryNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['content'] = request.content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMemoryNode',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories/{OpenApiUtilClient.get_encode_param(memory_id)}/memoryNodes/{OpenApiUtilClient.get_encode_param(memory_node_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.UpdateMemoryNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_memory_node_with_options_async(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
        request: bailian_20231229_models.UpdateMemoryNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20231229_models.UpdateMemoryNodeResponse:
        """
        @summary 更新记忆Node
        
        @param request: UpdateMemoryNodeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMemoryNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['content'] = request.content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMemoryNode',
            version='2023-12-29',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/memories/{OpenApiUtilClient.get_encode_param(memory_id)}/memoryNodes/{OpenApiUtilClient.get_encode_param(memory_node_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20231229_models.UpdateMemoryNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_memory_node(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
        request: bailian_20231229_models.UpdateMemoryNodeRequest,
    ) -> bailian_20231229_models.UpdateMemoryNodeResponse:
        """
        @summary 更新记忆Node
        
        @param request: UpdateMemoryNodeRequest
        @return: UpdateMemoryNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_memory_node_with_options(workspace_id, memory_id, memory_node_id, request, headers, runtime)

    async def update_memory_node_async(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
        request: bailian_20231229_models.UpdateMemoryNodeRequest,
    ) -> bailian_20231229_models.UpdateMemoryNodeResponse:
        """
        @summary 更新记忆Node
        
        @param request: UpdateMemoryNodeRequest
        @return: UpdateMemoryNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_memory_node_with_options_async(workspace_id, memory_id, memory_node_id, request, headers, runtime)
