# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_milvusknowledgebase20260604 import models as main_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('milvusknowledgebase', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_documents_with_options(
        self,
        dataset_id: str,
        request: main_models.AddDocumentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddDocumentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dedup):
            body['Dedup'] = request.dedup
        if not DaraCore.is_null(request.documents):
            body['Documents'] = request.documents
        if not DaraCore.is_null(request.import_type):
            body['ImportType'] = request.import_type
        if not DaraCore.is_null(request.knowledge_base_id):
            body['KnowledgeBaseId'] = request.knowledge_base_id
        if not DaraCore.is_null(request.meta_fields):
            body['MetaFields'] = request.meta_fields
        if not DaraCore.is_null(request.strategy_id):
            body['StrategyId'] = request.strategy_id
        if not DaraCore.is_null(request.ding_talk_configuration):
            body['dingTalkConfiguration'] = request.ding_talk_configuration
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDocuments',
            version = '2026-06-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/documents/addDocuments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_documents_with_options_async(
        self,
        dataset_id: str,
        request: main_models.AddDocumentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddDocumentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dedup):
            body['Dedup'] = request.dedup
        if not DaraCore.is_null(request.documents):
            body['Documents'] = request.documents
        if not DaraCore.is_null(request.import_type):
            body['ImportType'] = request.import_type
        if not DaraCore.is_null(request.knowledge_base_id):
            body['KnowledgeBaseId'] = request.knowledge_base_id
        if not DaraCore.is_null(request.meta_fields):
            body['MetaFields'] = request.meta_fields
        if not DaraCore.is_null(request.strategy_id):
            body['StrategyId'] = request.strategy_id
        if not DaraCore.is_null(request.ding_talk_configuration):
            body['dingTalkConfiguration'] = request.ding_talk_configuration
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDocuments',
            version = '2026-06-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/documents/addDocuments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_documents(
        self,
        dataset_id: str,
        request: main_models.AddDocumentsRequest,
    ) -> main_models.AddDocumentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_documents_with_options(dataset_id, request, headers, runtime)

    async def add_documents_async(
        self,
        dataset_id: str,
        request: main_models.AddDocumentsRequest,
    ) -> main_models.AddDocumentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_documents_with_options_async(dataset_id, request, headers, runtime)

    def get_knowledge_base_pre_signed_url_with_options(
        self,
        dataset_id: str,
        request: main_models.GetKnowledgeBasePreSignedUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKnowledgeBasePreSignedUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.documents):
            body['Documents'] = request.documents
        if not DaraCore.is_null(request.expires_in):
            body['ExpiresIn'] = request.expires_in
        if not DaraCore.is_null(request.knowledge_base_id):
            body['KnowledgeBaseId'] = request.knowledge_base_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetKnowledgeBasePreSignedUrl',
            version = '2026-06-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/getKnowledgeBasePreSignedUrl',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKnowledgeBasePreSignedUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_knowledge_base_pre_signed_url_with_options_async(
        self,
        dataset_id: str,
        request: main_models.GetKnowledgeBasePreSignedUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKnowledgeBasePreSignedUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.documents):
            body['Documents'] = request.documents
        if not DaraCore.is_null(request.expires_in):
            body['ExpiresIn'] = request.expires_in
        if not DaraCore.is_null(request.knowledge_base_id):
            body['KnowledgeBaseId'] = request.knowledge_base_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetKnowledgeBasePreSignedUrl',
            version = '2026-06-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/datasets/{DaraURL.percent_encode(dataset_id)}/getKnowledgeBasePreSignedUrl',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKnowledgeBasePreSignedUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_knowledge_base_pre_signed_url(
        self,
        dataset_id: str,
        request: main_models.GetKnowledgeBasePreSignedUrlRequest,
    ) -> main_models.GetKnowledgeBasePreSignedUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_knowledge_base_pre_signed_url_with_options(dataset_id, request, headers, runtime)

    async def get_knowledge_base_pre_signed_url_async(
        self,
        dataset_id: str,
        request: main_models.GetKnowledgeBasePreSignedUrlRequest,
    ) -> main_models.GetKnowledgeBasePreSignedUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_knowledge_base_pre_signed_url_with_options_async(dataset_id, request, headers, runtime)

    def search_knowledge_base_with_options(
        self,
        knowledge_base_id: str,
        request: main_models.SearchKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchKnowledgeBaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_ids):
            body['documentIds'] = request.document_ids
        if not DaraCore.is_null(request.enable_knowledge_graph):
            body['enableKnowledgeGraph'] = request.enable_knowledge_graph
        if not DaraCore.is_null(request.image):
            body['image'] = request.image
        if not DaraCore.is_null(request.page_number):
            body['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.rerank_model_id):
            body['rerankModelId'] = request.rerank_model_id
        if not DaraCore.is_null(request.rerank_model_name):
            body['rerankModelName'] = request.rerank_model_name
        if not DaraCore.is_null(request.retrieval_config):
            body['retrievalConfig'] = request.retrieval_config
        if not DaraCore.is_null(request.tag_filter):
            body['tagFilter'] = request.tag_filter
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchKnowledgeBase',
            version = '2026-06-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/knowledge-bases/{DaraURL.percent_encode(knowledge_base_id)}/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_knowledge_base_with_options_async(
        self,
        knowledge_base_id: str,
        request: main_models.SearchKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchKnowledgeBaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_ids):
            body['documentIds'] = request.document_ids
        if not DaraCore.is_null(request.enable_knowledge_graph):
            body['enableKnowledgeGraph'] = request.enable_knowledge_graph
        if not DaraCore.is_null(request.image):
            body['image'] = request.image
        if not DaraCore.is_null(request.page_number):
            body['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.rerank_model_id):
            body['rerankModelId'] = request.rerank_model_id
        if not DaraCore.is_null(request.rerank_model_name):
            body['rerankModelName'] = request.rerank_model_name
        if not DaraCore.is_null(request.retrieval_config):
            body['retrievalConfig'] = request.retrieval_config
        if not DaraCore.is_null(request.tag_filter):
            body['tagFilter'] = request.tag_filter
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchKnowledgeBase',
            version = '2026-06-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/knowledge-bases/{DaraURL.percent_encode(knowledge_base_id)}/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_knowledge_base(
        self,
        knowledge_base_id: str,
        request: main_models.SearchKnowledgeBaseRequest,
    ) -> main_models.SearchKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_knowledge_base_with_options(knowledge_base_id, request, headers, runtime)

    async def search_knowledge_base_async(
        self,
        knowledge_base_id: str,
        request: main_models.SearchKnowledgeBaseRequest,
    ) -> main_models.SearchKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_knowledge_base_with_options_async(knowledge_base_id, request, headers, runtime)
