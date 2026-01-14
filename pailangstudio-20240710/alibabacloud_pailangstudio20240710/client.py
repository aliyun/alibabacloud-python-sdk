# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_pailangstudio20240710 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('pailangstudio', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_knowledge_base_with_options(
        self,
        request: main_models.CreateKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKnowledgeBaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.chunk_config):
            body['ChunkConfig'] = request.chunk_config
        if not DaraCore.is_null(request.data_sources):
            body['DataSources'] = request.data_sources
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.embedding_config):
            body['EmbeddingConfig'] = request.embedding_config
        if not DaraCore.is_null(request.index_column_config):
            body['IndexColumnConfig'] = request.index_column_config
        if not DaraCore.is_null(request.knowledge_base_type):
            body['KnowledgeBaseType'] = request.knowledge_base_type
        if not DaraCore.is_null(request.meta_data_config):
            body['MetaDataConfig'] = request.meta_data_config
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.output_dir):
            body['OutputDir'] = request.output_dir
        if not DaraCore.is_null(request.runtime_id):
            body['RuntimeId'] = request.runtime_id
        if not DaraCore.is_null(request.vector_dbconfig):
            body['VectorDBConfig'] = request.vector_dbconfig
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKnowledgeBase',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_knowledge_base_with_options_async(
        self,
        request: main_models.CreateKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKnowledgeBaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.chunk_config):
            body['ChunkConfig'] = request.chunk_config
        if not DaraCore.is_null(request.data_sources):
            body['DataSources'] = request.data_sources
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.embedding_config):
            body['EmbeddingConfig'] = request.embedding_config
        if not DaraCore.is_null(request.index_column_config):
            body['IndexColumnConfig'] = request.index_column_config
        if not DaraCore.is_null(request.knowledge_base_type):
            body['KnowledgeBaseType'] = request.knowledge_base_type
        if not DaraCore.is_null(request.meta_data_config):
            body['MetaDataConfig'] = request.meta_data_config
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.output_dir):
            body['OutputDir'] = request.output_dir
        if not DaraCore.is_null(request.runtime_id):
            body['RuntimeId'] = request.runtime_id
        if not DaraCore.is_null(request.vector_dbconfig):
            body['VectorDBConfig'] = request.vector_dbconfig
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKnowledgeBase',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_knowledge_base(
        self,
        request: main_models.CreateKnowledgeBaseRequest,
    ) -> main_models.CreateKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_knowledge_base_with_options(request, headers, runtime)

    async def create_knowledge_base_async(
        self,
        request: main_models.CreateKnowledgeBaseRequest,
    ) -> main_models.CreateKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_knowledge_base_with_options_async(request, headers, runtime)

    def create_knowledge_base_job_with_options(
        self,
        knowledge_base_id: str,
        request: main_models.CreateKnowledgeBaseJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKnowledgeBaseJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.ecs_specs):
            body['EcsSpecs'] = request.ecs_specs
        if not DaraCore.is_null(request.embedding_config):
            body['EmbeddingConfig'] = request.embedding_config
        if not DaraCore.is_null(request.job_action):
            body['JobAction'] = request.job_action
        if not DaraCore.is_null(request.max_running_time_in_seconds):
            body['MaxRunningTimeInSeconds'] = request.max_running_time_in_seconds
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKnowledgeBaseJob',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}/knowledgebasejobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKnowledgeBaseJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_knowledge_base_job_with_options_async(
        self,
        knowledge_base_id: str,
        request: main_models.CreateKnowledgeBaseJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKnowledgeBaseJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.ecs_specs):
            body['EcsSpecs'] = request.ecs_specs
        if not DaraCore.is_null(request.embedding_config):
            body['EmbeddingConfig'] = request.embedding_config
        if not DaraCore.is_null(request.job_action):
            body['JobAction'] = request.job_action
        if not DaraCore.is_null(request.max_running_time_in_seconds):
            body['MaxRunningTimeInSeconds'] = request.max_running_time_in_seconds
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKnowledgeBaseJob',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}/knowledgebasejobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKnowledgeBaseJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_knowledge_base_job(
        self,
        knowledge_base_id: str,
        request: main_models.CreateKnowledgeBaseJobRequest,
    ) -> main_models.CreateKnowledgeBaseJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_knowledge_base_job_with_options(knowledge_base_id, request, headers, runtime)

    async def create_knowledge_base_job_async(
        self,
        knowledge_base_id: str,
        request: main_models.CreateKnowledgeBaseJobRequest,
    ) -> main_models.CreateKnowledgeBaseJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_knowledge_base_job_with_options_async(knowledge_base_id, request, headers, runtime)

    def delete_knowledge_base_with_options(
        self,
        knowledge_base_id: str,
        request: main_models.DeleteKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKnowledgeBaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKnowledgeBase',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_knowledge_base_with_options_async(
        self,
        knowledge_base_id: str,
        request: main_models.DeleteKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKnowledgeBaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKnowledgeBase',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_knowledge_base(
        self,
        knowledge_base_id: str,
        request: main_models.DeleteKnowledgeBaseRequest,
    ) -> main_models.DeleteKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_knowledge_base_with_options(knowledge_base_id, request, headers, runtime)

    async def delete_knowledge_base_async(
        self,
        knowledge_base_id: str,
        request: main_models.DeleteKnowledgeBaseRequest,
    ) -> main_models.DeleteKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_knowledge_base_with_options_async(knowledge_base_id, request, headers, runtime)

    def delete_knowledge_base_job_with_options(
        self,
        knowledge_base_id: str,
        knowledge_base_job_id: str,
        request: main_models.DeleteKnowledgeBaseJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKnowledgeBaseJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKnowledgeBaseJob',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}/knowledgebasejobs/{DaraURL.percent_encode(knowledge_base_job_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKnowledgeBaseJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_knowledge_base_job_with_options_async(
        self,
        knowledge_base_id: str,
        knowledge_base_job_id: str,
        request: main_models.DeleteKnowledgeBaseJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKnowledgeBaseJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKnowledgeBaseJob',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}/knowledgebasejobs/{DaraURL.percent_encode(knowledge_base_job_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKnowledgeBaseJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_knowledge_base_job(
        self,
        knowledge_base_id: str,
        knowledge_base_job_id: str,
        request: main_models.DeleteKnowledgeBaseJobRequest,
    ) -> main_models.DeleteKnowledgeBaseJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_knowledge_base_job_with_options(knowledge_base_id, knowledge_base_job_id, request, headers, runtime)

    async def delete_knowledge_base_job_async(
        self,
        knowledge_base_id: str,
        knowledge_base_job_id: str,
        request: main_models.DeleteKnowledgeBaseJobRequest,
    ) -> main_models.DeleteKnowledgeBaseJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_knowledge_base_job_with_options_async(knowledge_base_id, knowledge_base_job_id, request, headers, runtime)

    def get_knowledge_base_with_options(
        self,
        knowledge_base_id: str,
        request: main_models.GetKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKnowledgeBaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKnowledgeBase',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_knowledge_base_with_options_async(
        self,
        knowledge_base_id: str,
        request: main_models.GetKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKnowledgeBaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKnowledgeBase',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_knowledge_base(
        self,
        knowledge_base_id: str,
        request: main_models.GetKnowledgeBaseRequest,
    ) -> main_models.GetKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_knowledge_base_with_options(knowledge_base_id, request, headers, runtime)

    async def get_knowledge_base_async(
        self,
        knowledge_base_id: str,
        request: main_models.GetKnowledgeBaseRequest,
    ) -> main_models.GetKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_knowledge_base_with_options_async(knowledge_base_id, request, headers, runtime)

    def get_knowledge_base_job_with_options(
        self,
        knowledge_base_id: str,
        knowledge_base_job_id: str,
        request: main_models.GetKnowledgeBaseJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKnowledgeBaseJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKnowledgeBaseJob',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}/knowledgebasejobs/{DaraURL.percent_encode(knowledge_base_job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKnowledgeBaseJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_knowledge_base_job_with_options_async(
        self,
        knowledge_base_id: str,
        knowledge_base_job_id: str,
        request: main_models.GetKnowledgeBaseJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKnowledgeBaseJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKnowledgeBaseJob',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}/knowledgebasejobs/{DaraURL.percent_encode(knowledge_base_job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKnowledgeBaseJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_knowledge_base_job(
        self,
        knowledge_base_id: str,
        knowledge_base_job_id: str,
        request: main_models.GetKnowledgeBaseJobRequest,
    ) -> main_models.GetKnowledgeBaseJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_knowledge_base_job_with_options(knowledge_base_id, knowledge_base_job_id, request, headers, runtime)

    async def get_knowledge_base_job_async(
        self,
        knowledge_base_id: str,
        knowledge_base_job_id: str,
        request: main_models.GetKnowledgeBaseJobRequest,
    ) -> main_models.GetKnowledgeBaseJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_knowledge_base_job_with_options_async(knowledge_base_id, knowledge_base_job_id, request, headers, runtime)

    def list_knowledge_base_chunks_with_options(
        self,
        knowledge_base_id: str,
        request: main_models.ListKnowledgeBaseChunksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKnowledgeBaseChunksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chunk_status):
            query['ChunkStatus'] = request.chunk_status
        if not DaraCore.is_null(request.meta_data):
            query['MetaData'] = request.meta_data
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKnowledgeBaseChunks',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}/knowledgebasechunks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKnowledgeBaseChunksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_knowledge_base_chunks_with_options_async(
        self,
        knowledge_base_id: str,
        request: main_models.ListKnowledgeBaseChunksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKnowledgeBaseChunksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chunk_status):
            query['ChunkStatus'] = request.chunk_status
        if not DaraCore.is_null(request.meta_data):
            query['MetaData'] = request.meta_data
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKnowledgeBaseChunks',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}/knowledgebasechunks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKnowledgeBaseChunksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_knowledge_base_chunks(
        self,
        knowledge_base_id: str,
        request: main_models.ListKnowledgeBaseChunksRequest,
    ) -> main_models.ListKnowledgeBaseChunksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_knowledge_base_chunks_with_options(knowledge_base_id, request, headers, runtime)

    async def list_knowledge_base_chunks_async(
        self,
        knowledge_base_id: str,
        request: main_models.ListKnowledgeBaseChunksRequest,
    ) -> main_models.ListKnowledgeBaseChunksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_knowledge_base_chunks_with_options_async(knowledge_base_id, request, headers, runtime)

    def list_knowledge_base_jobs_with_options(
        self,
        knowledge_base_id: str,
        request: main_models.ListKnowledgeBaseJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKnowledgeBaseJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_action):
            query['JobAction'] = request.job_action
        if not DaraCore.is_null(request.knowledge_base_job_id):
            query['KnowledgeBaseJobId'] = request.knowledge_base_job_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKnowledgeBaseJobs',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}/knowledgebasejobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKnowledgeBaseJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_knowledge_base_jobs_with_options_async(
        self,
        knowledge_base_id: str,
        request: main_models.ListKnowledgeBaseJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKnowledgeBaseJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_action):
            query['JobAction'] = request.job_action
        if not DaraCore.is_null(request.knowledge_base_job_id):
            query['KnowledgeBaseJobId'] = request.knowledge_base_job_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKnowledgeBaseJobs',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}/knowledgebasejobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKnowledgeBaseJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_knowledge_base_jobs(
        self,
        knowledge_base_id: str,
        request: main_models.ListKnowledgeBaseJobsRequest,
    ) -> main_models.ListKnowledgeBaseJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_knowledge_base_jobs_with_options(knowledge_base_id, request, headers, runtime)

    async def list_knowledge_base_jobs_async(
        self,
        knowledge_base_id: str,
        request: main_models.ListKnowledgeBaseJobsRequest,
    ) -> main_models.ListKnowledgeBaseJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_knowledge_base_jobs_with_options_async(knowledge_base_id, request, headers, runtime)

    def list_knowledge_bases_with_options(
        self,
        request: main_models.ListKnowledgeBasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKnowledgeBasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator):
            query['Creator'] = request.creator
        if not DaraCore.is_null(request.knowledge_base_id):
            query['KnowledgeBaseId'] = request.knowledge_base_id
        if not DaraCore.is_null(request.knowledge_base_type):
            query['KnowledgeBaseType'] = request.knowledge_base_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKnowledgeBases',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKnowledgeBasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_knowledge_bases_with_options_async(
        self,
        request: main_models.ListKnowledgeBasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKnowledgeBasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator):
            query['Creator'] = request.creator
        if not DaraCore.is_null(request.knowledge_base_id):
            query['KnowledgeBaseId'] = request.knowledge_base_id
        if not DaraCore.is_null(request.knowledge_base_type):
            query['KnowledgeBaseType'] = request.knowledge_base_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKnowledgeBases',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKnowledgeBasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_knowledge_bases(
        self,
        request: main_models.ListKnowledgeBasesRequest,
    ) -> main_models.ListKnowledgeBasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_knowledge_bases_with_options(request, headers, runtime)

    async def list_knowledge_bases_async(
        self,
        request: main_models.ListKnowledgeBasesRequest,
    ) -> main_models.ListKnowledgeBasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_knowledge_bases_with_options_async(request, headers, runtime)

    def retrieve_knowledge_base_with_options(
        self,
        knowledge_base_id: str,
        request: main_models.RetrieveKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RetrieveKnowledgeBaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hybrid_strategy_config):
            body['HybridStrategyConfig'] = request.hybrid_strategy_config
        if not DaraCore.is_null(request.meta_data_filter_conditions):
            body['MetaDataFilterConditions'] = request.meta_data_filter_conditions
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.query_mode):
            body['QueryMode'] = request.query_mode
        if not DaraCore.is_null(request.rerank_config):
            body['RerankConfig'] = request.rerank_config
        if not DaraCore.is_null(request.rewrite_config):
            body['RewriteConfig'] = request.rewrite_config
        if not DaraCore.is_null(request.score_threshold):
            body['ScoreThreshold'] = request.score_threshold
        if not DaraCore.is_null(request.top_k):
            body['TopK'] = request.top_k
        if not DaraCore.is_null(request.version_name):
            body['VersionName'] = request.version_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RetrieveKnowledgeBase',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}/action/retrieve',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetrieveKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def retrieve_knowledge_base_with_options_async(
        self,
        knowledge_base_id: str,
        request: main_models.RetrieveKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RetrieveKnowledgeBaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hybrid_strategy_config):
            body['HybridStrategyConfig'] = request.hybrid_strategy_config
        if not DaraCore.is_null(request.meta_data_filter_conditions):
            body['MetaDataFilterConditions'] = request.meta_data_filter_conditions
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.query_mode):
            body['QueryMode'] = request.query_mode
        if not DaraCore.is_null(request.rerank_config):
            body['RerankConfig'] = request.rerank_config
        if not DaraCore.is_null(request.rewrite_config):
            body['RewriteConfig'] = request.rewrite_config
        if not DaraCore.is_null(request.score_threshold):
            body['ScoreThreshold'] = request.score_threshold
        if not DaraCore.is_null(request.top_k):
            body['TopK'] = request.top_k
        if not DaraCore.is_null(request.version_name):
            body['VersionName'] = request.version_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RetrieveKnowledgeBase',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}/action/retrieve',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetrieveKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retrieve_knowledge_base(
        self,
        knowledge_base_id: str,
        request: main_models.RetrieveKnowledgeBaseRequest,
    ) -> main_models.RetrieveKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.retrieve_knowledge_base_with_options(knowledge_base_id, request, headers, runtime)

    async def retrieve_knowledge_base_async(
        self,
        knowledge_base_id: str,
        request: main_models.RetrieveKnowledgeBaseRequest,
    ) -> main_models.RetrieveKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.retrieve_knowledge_base_with_options_async(knowledge_base_id, request, headers, runtime)

    def update_knowledge_base_with_options(
        self,
        knowledge_base_id: str,
        request: main_models.UpdateKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKnowledgeBaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_update_config):
            body['AutoUpdateConfig'] = request.auto_update_config
        if not DaraCore.is_null(request.bind_runtime):
            body['BindRuntime'] = request.bind_runtime
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.meta_data_config):
            body['MetaDataConfig'] = request.meta_data_config
        if not DaraCore.is_null(request.runtime_id):
            body['RuntimeId'] = request.runtime_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKnowledgeBase',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_knowledge_base_with_options_async(
        self,
        knowledge_base_id: str,
        request: main_models.UpdateKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKnowledgeBaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_update_config):
            body['AutoUpdateConfig'] = request.auto_update_config
        if not DaraCore.is_null(request.bind_runtime):
            body['BindRuntime'] = request.bind_runtime
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.meta_data_config):
            body['MetaDataConfig'] = request.meta_data_config
        if not DaraCore.is_null(request.runtime_id):
            body['RuntimeId'] = request.runtime_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKnowledgeBase',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_knowledge_base(
        self,
        knowledge_base_id: str,
        request: main_models.UpdateKnowledgeBaseRequest,
    ) -> main_models.UpdateKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_knowledge_base_with_options(knowledge_base_id, request, headers, runtime)

    async def update_knowledge_base_async(
        self,
        knowledge_base_id: str,
        request: main_models.UpdateKnowledgeBaseRequest,
    ) -> main_models.UpdateKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_knowledge_base_with_options_async(knowledge_base_id, request, headers, runtime)

    def update_knowledge_base_chunk_with_options(
        self,
        knowledge_base_id: str,
        knowledge_base_chunk_id: str,
        request: main_models.UpdateKnowledgeBaseChunkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKnowledgeBaseChunkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chunk_content):
            body['ChunkContent'] = request.chunk_content
        if not DaraCore.is_null(request.chunk_status):
            body['ChunkStatus'] = request.chunk_status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKnowledgeBaseChunk',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}/knowledgebasechunks/{DaraURL.percent_encode(knowledge_base_chunk_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKnowledgeBaseChunkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_knowledge_base_chunk_with_options_async(
        self,
        knowledge_base_id: str,
        knowledge_base_chunk_id: str,
        request: main_models.UpdateKnowledgeBaseChunkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKnowledgeBaseChunkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chunk_content):
            body['ChunkContent'] = request.chunk_content
        if not DaraCore.is_null(request.chunk_status):
            body['ChunkStatus'] = request.chunk_status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKnowledgeBaseChunk',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}/knowledgebasechunks/{DaraURL.percent_encode(knowledge_base_chunk_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKnowledgeBaseChunkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_knowledge_base_chunk(
        self,
        knowledge_base_id: str,
        knowledge_base_chunk_id: str,
        request: main_models.UpdateKnowledgeBaseChunkRequest,
    ) -> main_models.UpdateKnowledgeBaseChunkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_knowledge_base_chunk_with_options(knowledge_base_id, knowledge_base_chunk_id, request, headers, runtime)

    async def update_knowledge_base_chunk_async(
        self,
        knowledge_base_id: str,
        knowledge_base_chunk_id: str,
        request: main_models.UpdateKnowledgeBaseChunkRequest,
    ) -> main_models.UpdateKnowledgeBaseChunkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_knowledge_base_chunk_with_options_async(knowledge_base_id, knowledge_base_chunk_id, request, headers, runtime)

    def update_knowledge_base_job_with_options(
        self,
        knowledge_base_id: str,
        knowledge_base_job_id: str,
        request: main_models.UpdateKnowledgeBaseJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKnowledgeBaseJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKnowledgeBaseJob',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}/knowledgebasejobs/{DaraURL.percent_encode(knowledge_base_job_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKnowledgeBaseJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_knowledge_base_job_with_options_async(
        self,
        knowledge_base_id: str,
        knowledge_base_job_id: str,
        request: main_models.UpdateKnowledgeBaseJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKnowledgeBaseJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKnowledgeBaseJob',
            version = '2024-07-10',
            protocol = 'HTTPS',
            pathname = f'/api/v1/langstudio/knowledgebases/{DaraURL.percent_encode(knowledge_base_id)}/knowledgebasejobs/{DaraURL.percent_encode(knowledge_base_job_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKnowledgeBaseJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_knowledge_base_job(
        self,
        knowledge_base_id: str,
        knowledge_base_job_id: str,
        request: main_models.UpdateKnowledgeBaseJobRequest,
    ) -> main_models.UpdateKnowledgeBaseJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_knowledge_base_job_with_options(knowledge_base_id, knowledge_base_job_id, request, headers, runtime)

    async def update_knowledge_base_job_async(
        self,
        knowledge_base_id: str,
        knowledge_base_job_id: str,
        request: main_models.UpdateKnowledgeBaseJobRequest,
    ) -> main_models.UpdateKnowledgeBaseJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_knowledge_base_job_with_options_async(knowledge_base_id, knowledge_base_job_id, request, headers, runtime)
