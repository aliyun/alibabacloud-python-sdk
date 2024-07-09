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
        if not UtilClient.is_unset(tmp_req.document_ids):
            request.document_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.category_ids_shrink):
            query['CategoryIds'] = request.category_ids_shrink
        if not UtilClient.is_unset(request.chunk_size):
            query['ChunkSize'] = request.chunk_size
        if not UtilClient.is_unset(request.columns_shrink):
            query['Columns'] = request.columns_shrink
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
        if not UtilClient.is_unset(tmp_req.document_ids):
            request.document_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.category_ids_shrink):
            query['CategoryIds'] = request.category_ids_shrink
        if not UtilClient.is_unset(request.chunk_size):
            query['ChunkSize'] = request.chunk_size
        if not UtilClient.is_unset(request.columns_shrink):
            query['Columns'] = request.columns_shrink
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
        if not UtilClient.is_unset(tmp_req.rerank):
            request.rerank_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rerank, 'Rerank', 'json')
        if not UtilClient.is_unset(tmp_req.rewrite):
            request.rewrite_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rewrite, 'Rewrite', 'json')
        query = {}
        if not UtilClient.is_unset(request.dense_similarity_top_k):
            query['DenseSimilarityTopK'] = request.dense_similarity_top_k
        if not UtilClient.is_unset(request.enable_reranking):
            query['EnableReranking'] = request.enable_reranking
        if not UtilClient.is_unset(request.enable_rewrite):
            query['EnableRewrite'] = request.enable_rewrite
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
        if not UtilClient.is_unset(tmp_req.rerank):
            request.rerank_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rerank, 'Rerank', 'json')
        if not UtilClient.is_unset(tmp_req.rewrite):
            request.rewrite_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rewrite, 'Rewrite', 'json')
        query = {}
        if not UtilClient.is_unset(request.dense_similarity_top_k):
            query['DenseSimilarityTopK'] = request.dense_similarity_top_k
        if not UtilClient.is_unset(request.enable_reranking):
            query['EnableReranking'] = request.enable_reranking
        if not UtilClient.is_unset(request.enable_rewrite):
            query['EnableRewrite'] = request.enable_rewrite
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
