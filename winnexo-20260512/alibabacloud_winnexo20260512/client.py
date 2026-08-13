# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_tea_openapi import exceptions as open_api_exceptions
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_winnexo20260512 import models as main_models
from darabonba.core import DaraCore
from darabonba.core import DaraCore as DaraCore
from darabonba.exceptions import UnretryableException
from darabonba.policy.retry import RetryPolicyContext
from darabonba.request import DaraRequest
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL
from darabonba.utils.form import FileField
from darabonba.utils.form import Form as DaraForm
from darabonba.utils.stream import Stream as DaraStream
from darabonba.utils.xml import XML as DaraXML

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
        self._endpoint = self.get_endpoint('winnexo', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def _post_ossobject(
        self,
        bucket_name: str,
        form: dict,
        runtime: RuntimeOptions,
    ) -> dict:
        _runtime = {
            'key': runtime.key or self._key,
            'cert': runtime.cert or self._cert,
            'ca': runtime.ca or self._ca,
            'readTimeout': DaraCore.to_number(runtime.read_timeout or self._read_timeout),
            'connectTimeout': DaraCore.to_number(runtime.connect_timeout or self._connect_timeout),
            'httpProxy': runtime.http_proxy or self._http_proxy,
            'httpsProxy': runtime.https_proxy or self._https_proxy,
            'noProxy': runtime.no_proxy or self._no_proxy,
            'socks5Proxy': runtime.socks_5proxy or self._socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work or self._socks_5net_work,
            'maxIdleConns': DaraCore.to_number(runtime.max_idle_conns or self._max_idle_conns),
            'retryOptions': self._retry_options,
            'ignoreSSL': bool(runtime.ignore_ssl or False),
            'tlsMinVersion': self._tls_min_version,
        }
        _last_request = None
        _last_response = None
        _retries_attempted = 0
        _context = RetryPolicyContext(
            retries_attempted= _retries_attempted
        )
        while DaraCore.should_retry(_runtime.get('retryOptions'), _context):
            if _retries_attempted > 0:
                _backoff_time = DaraCore.get_backoff_time(_runtime.get('retryOptions'), _context)
                if _backoff_time > 0:
                    DaraCore.sleep(_backoff_time)
            _retries_attempted = _retries_attempted + 1
            try:
                _request = DaraRequest()
                boundary = DaraForm.get_boundary()
                tmp = str(form.get("host"))
                host = f'{bucket_name}.{tmp}'
                _request.protocol = 'HTTPS'
                _request.method = 'POST'
                _request.pathname = f'/'
                _request.headers = {
                    'host': host,
                    'date': Utils.get_date_utcstring(),
                    'user-agent': Utils.get_user_agent('')
                }
                _request.headers["content-type"] = f'multipart/form-data; boundary={boundary}'
                _request.body = DaraForm.to_file_form(form, boundary)
                _last_request = _request
                _response = DaraCore.do_action(_request, _runtime)
                _last_response = _response
                resp_map = None
                body_str = DaraStream.read_as_string(_response.body)
                if (_response.status_code >= 400) and (_response.status_code < 600):
                    resp_map = DaraXML.parse_xml(body_str, None)
                    err = resp_map.get("Error")
                    raise open_api_exceptions.ClientException(
                        code = str(err.get("Code")),
                        message = str(err.get("Message")),
                        data = {
                            'httpCode': _response.status_code,
                            'requestId': str(err.get("RequestId")),
                            'hostId': str(err.get("HostId"))
                        }
                    )
                resp_map = DaraXML.parse_xml(body_str, None)
                return DaraCore.merge({}, resp_map)
            except Exception as e:
                _context = RetryPolicyContext(
                    retries_attempted= _retries_attempted,
                    http_request = _last_request,
                    http_response = _last_response,
                    exception = e
                )
                continue
        raise UnretryableException(_context)

    async def _post_ossobject_async(
        self,
        bucket_name: str,
        form: dict,
        runtime: RuntimeOptions,
    ) -> dict:
        _runtime = {
            'key': runtime.key or self._key,
            'cert': runtime.cert or self._cert,
            'ca': runtime.ca or self._ca,
            'readTimeout': DaraCore.to_number(runtime.read_timeout or self._read_timeout),
            'connectTimeout': DaraCore.to_number(runtime.connect_timeout or self._connect_timeout),
            'httpProxy': runtime.http_proxy or self._http_proxy,
            'httpsProxy': runtime.https_proxy or self._https_proxy,
            'noProxy': runtime.no_proxy or self._no_proxy,
            'socks5Proxy': runtime.socks_5proxy or self._socks_5proxy,
            'socks5NetWork': runtime.socks_5net_work or self._socks_5net_work,
            'maxIdleConns': DaraCore.to_number(runtime.max_idle_conns or self._max_idle_conns),
            'retryOptions': self._retry_options,
            'ignoreSSL': bool(runtime.ignore_ssl or False),
            'tlsMinVersion': self._tls_min_version,
        }
        _last_request = None
        _last_response = None
        _retries_attempted = 0
        _context = RetryPolicyContext(
            retries_attempted= _retries_attempted
        )
        while DaraCore.should_retry(_runtime.get('retryOptions'), _context):
            if _retries_attempted > 0:
                _backoff_time = DaraCore.get_backoff_time(_runtime.get('retryOptions'), _context)
                if _backoff_time > 0:
                    DaraCore.sleep(_backoff_time)
            _retries_attempted = _retries_attempted + 1
            try:
                _request = DaraRequest()
                boundary = DaraForm.get_boundary()
                tmp = str(form.get("host"))
                host = f'{bucket_name}.{tmp}'
                _request.protocol = 'HTTPS'
                _request.method = 'POST'
                _request.pathname = f'/'
                _request.headers = {
                    'host': host,
                    'date': Utils.get_date_utcstring(),
                    'user-agent': Utils.get_user_agent('')
                }
                _request.headers["content-type"] = f'multipart/form-data; boundary={boundary}'
                _request.body = DaraForm.to_file_form(form, boundary)
                _last_request = _request
                _response = await DaraCore.async_do_action(_request, _runtime)
                _last_response = _response
                resp_map = None
                body_str = await DaraStream.read_as_string_async(_response.body)
                if (_response.status_code >= 400) and (_response.status_code < 600):
                    resp_map = DaraXML.parse_xml(body_str, None)
                    err = resp_map.get("Error")
                    raise open_api_exceptions.ClientException(
                        code = str(err.get("Code")),
                        message = str(err.get("Message")),
                        data = {
                            'httpCode': _response.status_code,
                            'requestId': str(err.get("RequestId")),
                            'hostId': str(err.get("HostId"))
                        }
                    )
                resp_map = DaraXML.parse_xml(body_str, None)
                return DaraCore.merge({}, resp_map)
            except Exception as e:
                _context = RetryPolicyContext(
                    retries_attempted= _retries_attempted,
                    http_request = _last_request,
                    http_response = _last_response,
                    exception = e
                )
                continue
        raise UnretryableException(_context)

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

    def check_health_with_options(
        self,
        request: main_models.CheckHealthRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckHealthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckHealth',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/checkHealth',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckHealthResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_health_with_options_async(
        self,
        request: main_models.CheckHealthRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckHealthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckHealth',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/checkHealth',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckHealthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_health(
        self,
        request: main_models.CheckHealthRequest,
    ) -> main_models.CheckHealthResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.check_health_with_options(request, headers, runtime)

    async def check_health_async(
        self,
        request: main_models.CheckHealthRequest,
    ) -> main_models.CheckHealthResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.check_health_with_options_async(request, headers, runtime)

    def create_conversation_with_options(
        self,
        tmp_req: main_models.CreateConversationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConversationResponse:
        tmp_req.validate()
        request = main_models.CreateConversationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operating_object_name):
            request.operating_object_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.operating_object_name, 'operatingObjectName', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.metadata):
            body['metadata'] = request.metadata
        if not DaraCore.is_null(request.object_id):
            body['objectId'] = request.object_id
        if not DaraCore.is_null(request.operating_object_name_shrink):
            body['operatingObjectName'] = request.operating_object_name_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConversation',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createConversation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_conversation_with_options_async(
        self,
        tmp_req: main_models.CreateConversationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConversationResponse:
        tmp_req.validate()
        request = main_models.CreateConversationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operating_object_name):
            request.operating_object_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.operating_object_name, 'operatingObjectName', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.metadata):
            body['metadata'] = request.metadata
        if not DaraCore.is_null(request.object_id):
            body['objectId'] = request.object_id
        if not DaraCore.is_null(request.operating_object_name_shrink):
            body['operatingObjectName'] = request.operating_object_name_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConversation',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createConversation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_conversation(
        self,
        request: main_models.CreateConversationRequest,
    ) -> main_models.CreateConversationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_conversation_with_options(request, headers, runtime)

    async def create_conversation_async(
        self,
        request: main_models.CreateConversationRequest,
    ) -> main_models.CreateConversationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_conversation_with_options_async(request, headers, runtime)

    def create_custom_org_with_options(
        self,
        request: main_models.CreateCustomOrgRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomOrgResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.corp_id):
            body['corpId'] = request.corp_id
        if not DaraCore.is_null(request.corp_name):
            body['corpName'] = request.corp_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomOrg',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createCustomOrg',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomOrgResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_org_with_options_async(
        self,
        request: main_models.CreateCustomOrgRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomOrgResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.corp_id):
            body['corpId'] = request.corp_id
        if not DaraCore.is_null(request.corp_name):
            body['corpName'] = request.corp_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomOrg',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createCustomOrg',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomOrgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_org(
        self,
        request: main_models.CreateCustomOrgRequest,
    ) -> main_models.CreateCustomOrgResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_custom_org_with_options(request, headers, runtime)

    async def create_custom_org_async(
        self,
        request: main_models.CreateCustomOrgRequest,
    ) -> main_models.CreateCustomOrgResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_custom_org_with_options_async(request, headers, runtime)

    def create_knowledge_base_ali_ding_doc_with_options(
        self,
        request: main_models.CreateKnowledgeBaseAliDingDocRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKnowledgeBaseAliDingDocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.file_public_url):
            body['filePublicUrl'] = request.file_public_url
        if not DaraCore.is_null(request.knowledge_id):
            body['knowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.source_tags):
            body['sourceTags'] = request.source_tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKnowledgeBaseAliDingDoc',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createKnowledgeBaseAlidingDoc',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKnowledgeBaseAliDingDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_knowledge_base_ali_ding_doc_with_options_async(
        self,
        request: main_models.CreateKnowledgeBaseAliDingDocRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKnowledgeBaseAliDingDocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.file_public_url):
            body['filePublicUrl'] = request.file_public_url
        if not DaraCore.is_null(request.knowledge_id):
            body['knowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.source_tags):
            body['sourceTags'] = request.source_tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKnowledgeBaseAliDingDoc',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createKnowledgeBaseAlidingDoc',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKnowledgeBaseAliDingDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_knowledge_base_ali_ding_doc(
        self,
        request: main_models.CreateKnowledgeBaseAliDingDocRequest,
    ) -> main_models.CreateKnowledgeBaseAliDingDocResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_knowledge_base_ali_ding_doc_with_options(request, headers, runtime)

    async def create_knowledge_base_ali_ding_doc_async(
        self,
        request: main_models.CreateKnowledgeBaseAliDingDocRequest,
    ) -> main_models.CreateKnowledgeBaseAliDingDocResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_knowledge_base_ali_ding_doc_with_options_async(request, headers, runtime)

    def create_knowledge_base_directory_with_options(
        self,
        request: main_models.CreateKnowledgeBaseDirectoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKnowledgeBaseDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.parent_directory_id):
            body['parentDirectoryId'] = request.parent_directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKnowledgeBaseDirectory',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createKnowledgeBaseDirectory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKnowledgeBaseDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_knowledge_base_directory_with_options_async(
        self,
        request: main_models.CreateKnowledgeBaseDirectoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKnowledgeBaseDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.parent_directory_id):
            body['parentDirectoryId'] = request.parent_directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKnowledgeBaseDirectory',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createKnowledgeBaseDirectory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKnowledgeBaseDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_knowledge_base_directory(
        self,
        request: main_models.CreateKnowledgeBaseDirectoryRequest,
    ) -> main_models.CreateKnowledgeBaseDirectoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_knowledge_base_directory_with_options(request, headers, runtime)

    async def create_knowledge_base_directory_async(
        self,
        request: main_models.CreateKnowledgeBaseDirectoryRequest,
    ) -> main_models.CreateKnowledgeBaseDirectoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_knowledge_base_directory_with_options_async(request, headers, runtime)

    def create_knowledge_base_file_with_options(
        self,
        request: main_models.CreateKnowledgeBaseFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKnowledgeBaseFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.file_ext):
            body['fileExt'] = request.file_ext
        if not DaraCore.is_null(request.file_name):
            body['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_path):
            body['filePath'] = request.file_path
        if not DaraCore.is_null(request.file_public_url):
            body['filePublicUrl'] = request.file_public_url
        if not DaraCore.is_null(request.file_record_id):
            body['fileRecordId'] = request.file_record_id
        if not DaraCore.is_null(request.knowledge_id):
            body['knowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.source_tags):
            body['sourceTags'] = request.source_tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKnowledgeBaseFile',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createKnowledgeBaseFile',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKnowledgeBaseFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_knowledge_base_file_with_options_async(
        self,
        request: main_models.CreateKnowledgeBaseFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKnowledgeBaseFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.file_ext):
            body['fileExt'] = request.file_ext
        if not DaraCore.is_null(request.file_name):
            body['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_path):
            body['filePath'] = request.file_path
        if not DaraCore.is_null(request.file_public_url):
            body['filePublicUrl'] = request.file_public_url
        if not DaraCore.is_null(request.file_record_id):
            body['fileRecordId'] = request.file_record_id
        if not DaraCore.is_null(request.knowledge_id):
            body['knowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.source_tags):
            body['sourceTags'] = request.source_tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKnowledgeBaseFile',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createKnowledgeBaseFile',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKnowledgeBaseFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_knowledge_base_file(
        self,
        request: main_models.CreateKnowledgeBaseFileRequest,
    ) -> main_models.CreateKnowledgeBaseFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_knowledge_base_file_with_options(request, headers, runtime)

    async def create_knowledge_base_file_async(
        self,
        request: main_models.CreateKnowledgeBaseFileRequest,
    ) -> main_models.CreateKnowledgeBaseFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_knowledge_base_file_with_options_async(request, headers, runtime)

    def create_knowledge_base_text_with_options(
        self,
        request: main_models.CreateKnowledgeBaseTextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKnowledgeBaseTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.knowledge_id):
            body['knowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.source_tags):
            body['sourceTags'] = request.source_tags
        if not DaraCore.is_null(request.text_content):
            body['textContent'] = request.text_content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKnowledgeBaseText',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createKnowledgeBaseText',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKnowledgeBaseTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_knowledge_base_text_with_options_async(
        self,
        request: main_models.CreateKnowledgeBaseTextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKnowledgeBaseTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.knowledge_id):
            body['knowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.source_tags):
            body['sourceTags'] = request.source_tags
        if not DaraCore.is_null(request.text_content):
            body['textContent'] = request.text_content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKnowledgeBaseText',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createKnowledgeBaseText',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKnowledgeBaseTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_knowledge_base_text(
        self,
        request: main_models.CreateKnowledgeBaseTextRequest,
    ) -> main_models.CreateKnowledgeBaseTextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_knowledge_base_text_with_options(request, headers, runtime)

    async def create_knowledge_base_text_async(
        self,
        request: main_models.CreateKnowledgeBaseTextRequest,
    ) -> main_models.CreateKnowledgeBaseTextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_knowledge_base_text_with_options_async(request, headers, runtime)

    def create_personal_ali_ding_meeting_with_options(
        self,
        request: main_models.CreatePersonalAliDingMeetingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalAliDingMeetingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.notes):
            body['notes'] = request.notes
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.shanji_url):
            body['shanjiUrl'] = request.shanji_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalAliDingMeeting',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalAliDingMeeting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalAliDingMeetingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_personal_ali_ding_meeting_with_options_async(
        self,
        request: main_models.CreatePersonalAliDingMeetingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalAliDingMeetingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.notes):
            body['notes'] = request.notes
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.shanji_url):
            body['shanjiUrl'] = request.shanji_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalAliDingMeeting',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalAliDingMeeting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalAliDingMeetingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_personal_ali_ding_meeting(
        self,
        request: main_models.CreatePersonalAliDingMeetingRequest,
    ) -> main_models.CreatePersonalAliDingMeetingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_personal_ali_ding_meeting_with_options(request, headers, runtime)

    async def create_personal_ali_ding_meeting_async(
        self,
        request: main_models.CreatePersonalAliDingMeetingRequest,
    ) -> main_models.CreatePersonalAliDingMeetingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_personal_ali_ding_meeting_with_options_async(request, headers, runtime)

    def create_personal_aliding_doc_with_options(
        self,
        request: main_models.CreatePersonalAlidingDocRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalAlidingDocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.file_public_url):
            body['filePublicUrl'] = request.file_public_url
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalAlidingDoc',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalAliDingDoc',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalAlidingDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_personal_aliding_doc_with_options_async(
        self,
        request: main_models.CreatePersonalAlidingDocRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalAlidingDocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.file_public_url):
            body['filePublicUrl'] = request.file_public_url
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalAlidingDoc',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalAliDingDoc',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalAlidingDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_personal_aliding_doc(
        self,
        request: main_models.CreatePersonalAlidingDocRequest,
    ) -> main_models.CreatePersonalAlidingDocResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_personal_aliding_doc_with_options(request, headers, runtime)

    async def create_personal_aliding_doc_async(
        self,
        request: main_models.CreatePersonalAlidingDocRequest,
    ) -> main_models.CreatePersonalAlidingDocResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_personal_aliding_doc_with_options_async(request, headers, runtime)

    def create_personal_aliding_knowledge_base_with_options(
        self,
        tmp_req: main_models.CreatePersonalAlidingKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalAlidingKnowledgeBaseResponse:
        tmp_req.validate()
        request = main_models.CreatePersonalAlidingKnowledgeBaseShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.object_bindings):
            request.object_bindings_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_bindings, 'objectBindings', 'json')
        if not DaraCore.is_null(tmp_req.sync_config):
            request.sync_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.sync_config, 'syncConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.kb_name):
            body['kbName'] = request.kb_name
        if not DaraCore.is_null(request.kb_url):
            body['kbUrl'] = request.kb_url
        if not DaraCore.is_null(request.object_bindings_shrink):
            body['objectBindings'] = request.object_bindings_shrink
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.sync_config_shrink):
            body['syncConfig'] = request.sync_config_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalAlidingKnowledgeBase',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalAliDingKnowledgeBase',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalAlidingKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_personal_aliding_knowledge_base_with_options_async(
        self,
        tmp_req: main_models.CreatePersonalAlidingKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalAlidingKnowledgeBaseResponse:
        tmp_req.validate()
        request = main_models.CreatePersonalAlidingKnowledgeBaseShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.object_bindings):
            request.object_bindings_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_bindings, 'objectBindings', 'json')
        if not DaraCore.is_null(tmp_req.sync_config):
            request.sync_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.sync_config, 'syncConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.kb_name):
            body['kbName'] = request.kb_name
        if not DaraCore.is_null(request.kb_url):
            body['kbUrl'] = request.kb_url
        if not DaraCore.is_null(request.object_bindings_shrink):
            body['objectBindings'] = request.object_bindings_shrink
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.sync_config_shrink):
            body['syncConfig'] = request.sync_config_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalAlidingKnowledgeBase',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalAliDingKnowledgeBase',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalAlidingKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_personal_aliding_knowledge_base(
        self,
        request: main_models.CreatePersonalAlidingKnowledgeBaseRequest,
    ) -> main_models.CreatePersonalAlidingKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_personal_aliding_knowledge_base_with_options(request, headers, runtime)

    async def create_personal_aliding_knowledge_base_async(
        self,
        request: main_models.CreatePersonalAlidingKnowledgeBaseRequest,
    ) -> main_models.CreatePersonalAlidingKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_personal_aliding_knowledge_base_with_options_async(request, headers, runtime)

    def create_personal_dingtalk_meeting_with_options(
        self,
        request: main_models.CreatePersonalDingtalkMeetingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalDingtalkMeetingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.credential_id):
            body['credentialId'] = request.credential_id
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.notes):
            body['notes'] = request.notes
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.room_code):
            body['roomCode'] = request.room_code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalDingtalkMeeting',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalDingtalkMeeting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalDingtalkMeetingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_personal_dingtalk_meeting_with_options_async(
        self,
        request: main_models.CreatePersonalDingtalkMeetingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalDingtalkMeetingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.credential_id):
            body['credentialId'] = request.credential_id
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.notes):
            body['notes'] = request.notes
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.room_code):
            body['roomCode'] = request.room_code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalDingtalkMeeting',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalDingtalkMeeting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalDingtalkMeetingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_personal_dingtalk_meeting(
        self,
        request: main_models.CreatePersonalDingtalkMeetingRequest,
    ) -> main_models.CreatePersonalDingtalkMeetingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_personal_dingtalk_meeting_with_options(request, headers, runtime)

    async def create_personal_dingtalk_meeting_async(
        self,
        request: main_models.CreatePersonalDingtalkMeetingRequest,
    ) -> main_models.CreatePersonalDingtalkMeetingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_personal_dingtalk_meeting_with_options_async(request, headers, runtime)

    def create_personal_directory_with_options(
        self,
        request: main_models.CreatePersonalDirectoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.parent_directory_id):
            body['parentDirectoryId'] = request.parent_directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalDirectory',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalDirectory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_personal_directory_with_options_async(
        self,
        request: main_models.CreatePersonalDirectoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.parent_directory_id):
            body['parentDirectoryId'] = request.parent_directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalDirectory',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalDirectory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_personal_directory(
        self,
        request: main_models.CreatePersonalDirectoryRequest,
    ) -> main_models.CreatePersonalDirectoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_personal_directory_with_options(request, headers, runtime)

    async def create_personal_directory_async(
        self,
        request: main_models.CreatePersonalDirectoryRequest,
    ) -> main_models.CreatePersonalDirectoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_personal_directory_with_options_async(request, headers, runtime)

    def create_personal_feishu_minute_with_options(
        self,
        request: main_models.CreatePersonalFeishuMinuteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalFeishuMinuteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.credential_id):
            body['credentialId'] = request.credential_id
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.minute_token):
            body['minuteToken'] = request.minute_token
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalFeishuMinute',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalFeishuMinute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalFeishuMinuteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_personal_feishu_minute_with_options_async(
        self,
        request: main_models.CreatePersonalFeishuMinuteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalFeishuMinuteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.credential_id):
            body['credentialId'] = request.credential_id
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.minute_token):
            body['minuteToken'] = request.minute_token
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalFeishuMinute',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalFeishuMinute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalFeishuMinuteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_personal_feishu_minute(
        self,
        request: main_models.CreatePersonalFeishuMinuteRequest,
    ) -> main_models.CreatePersonalFeishuMinuteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_personal_feishu_minute_with_options(request, headers, runtime)

    async def create_personal_feishu_minute_async(
        self,
        request: main_models.CreatePersonalFeishuMinuteRequest,
    ) -> main_models.CreatePersonalFeishuMinuteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_personal_feishu_minute_with_options_async(request, headers, runtime)

    def create_personal_file_with_options(
        self,
        request: main_models.CreatePersonalFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.file_ext):
            body['fileExt'] = request.file_ext
        if not DaraCore.is_null(request.file_name):
            body['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_path):
            body['filePath'] = request.file_path
        if not DaraCore.is_null(request.file_public_url):
            body['filePublicUrl'] = request.file_public_url
        if not DaraCore.is_null(request.file_record_id):
            body['fileRecordId'] = request.file_record_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalFile',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalFile',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_personal_file_with_options_async(
        self,
        request: main_models.CreatePersonalFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.file_ext):
            body['fileExt'] = request.file_ext
        if not DaraCore.is_null(request.file_name):
            body['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_path):
            body['filePath'] = request.file_path
        if not DaraCore.is_null(request.file_public_url):
            body['filePublicUrl'] = request.file_public_url
        if not DaraCore.is_null(request.file_record_id):
            body['fileRecordId'] = request.file_record_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalFile',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalFile',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_personal_file(
        self,
        request: main_models.CreatePersonalFileRequest,
    ) -> main_models.CreatePersonalFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_personal_file_with_options(request, headers, runtime)

    async def create_personal_file_async(
        self,
        request: main_models.CreatePersonalFileRequest,
    ) -> main_models.CreatePersonalFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_personal_file_with_options_async(request, headers, runtime)

    def create_personal_text_with_options(
        self,
        request: main_models.CreatePersonalTextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.text_content):
            body['textContent'] = request.text_content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalText',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalText',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_personal_text_with_options_async(
        self,
        request: main_models.CreatePersonalTextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.text_content):
            body['textContent'] = request.text_content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalText',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalText',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_personal_text(
        self,
        request: main_models.CreatePersonalTextRequest,
    ) -> main_models.CreatePersonalTextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_personal_text_with_options(request, headers, runtime)

    async def create_personal_text_async(
        self,
        request: main_models.CreatePersonalTextRequest,
    ) -> main_models.CreatePersonalTextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_personal_text_with_options_async(request, headers, runtime)

    def create_personal_voice_meeting_with_options(
        self,
        request: main_models.CreatePersonalVoiceMeetingRequest,
        headers: main_models.CreatePersonalVoiceMeetingHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalVoiceMeetingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.file_url):
            body['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.request_id):
            real_headers['requestId'] = str(headers.request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalVoiceMeeting',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalVoiceMeeting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalVoiceMeetingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_personal_voice_meeting_with_options_async(
        self,
        request: main_models.CreatePersonalVoiceMeetingRequest,
        headers: main_models.CreatePersonalVoiceMeetingHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePersonalVoiceMeetingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.file_url):
            body['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.request_id):
            real_headers['requestId'] = str(headers.request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePersonalVoiceMeeting',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createPersonalVoiceMeeting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePersonalVoiceMeetingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_personal_voice_meeting(
        self,
        request: main_models.CreatePersonalVoiceMeetingRequest,
    ) -> main_models.CreatePersonalVoiceMeetingResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreatePersonalVoiceMeetingHeaders()
        return self.create_personal_voice_meeting_with_options(request, headers, runtime)

    async def create_personal_voice_meeting_async(
        self,
        request: main_models.CreatePersonalVoiceMeetingRequest,
    ) -> main_models.CreatePersonalVoiceMeetingResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreatePersonalVoiceMeetingHeaders()
        return await self.create_personal_voice_meeting_with_options_async(request, headers, runtime)

    def create_scheduled_task_with_options(
        self,
        tmp_req: main_models.CreateScheduledTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduledTaskResponse:
        tmp_req.validate()
        request = main_models.CreateScheduledTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.description):
            request.description_shrink = Utils.array_to_string_with_specified_style(tmp_req.description, 'description', 'json')
        if not DaraCore.is_null(tmp_req.digital_employee_name):
            request.digital_employee_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.digital_employee_name, 'digitalEmployeeName', 'json')
        if not DaraCore.is_null(tmp_req.segments):
            request.segments_shrink = Utils.array_to_string_with_specified_style(tmp_req.segments, 'segments', 'json')
        if not DaraCore.is_null(tmp_req.task_detail):
            request.task_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_detail, 'taskDetail', 'json')
        if not DaraCore.is_null(tmp_req.trigger_config):
            request.trigger_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger_config, 'triggerConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.collaboration_group_id):
            body['collaborationGroupId'] = request.collaboration_group_id
        if not DaraCore.is_null(request.description_shrink):
            body['description'] = request.description_shrink
        if not DaraCore.is_null(request.digital_employee_name_shrink):
            body['digitalEmployeeName'] = request.digital_employee_name_shrink
        if not DaraCore.is_null(request.is_open):
            body['isOpen'] = request.is_open
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.segments_shrink):
            body['segments'] = request.segments_shrink
        if not DaraCore.is_null(request.task_detail_shrink):
            body['taskDetail'] = request.task_detail_shrink
        if not DaraCore.is_null(request.trigger_config_shrink):
            body['triggerConfig'] = request.trigger_config_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateScheduledTask',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createScheduledTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheduled_task_with_options_async(
        self,
        tmp_req: main_models.CreateScheduledTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduledTaskResponse:
        tmp_req.validate()
        request = main_models.CreateScheduledTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.description):
            request.description_shrink = Utils.array_to_string_with_specified_style(tmp_req.description, 'description', 'json')
        if not DaraCore.is_null(tmp_req.digital_employee_name):
            request.digital_employee_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.digital_employee_name, 'digitalEmployeeName', 'json')
        if not DaraCore.is_null(tmp_req.segments):
            request.segments_shrink = Utils.array_to_string_with_specified_style(tmp_req.segments, 'segments', 'json')
        if not DaraCore.is_null(tmp_req.task_detail):
            request.task_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_detail, 'taskDetail', 'json')
        if not DaraCore.is_null(tmp_req.trigger_config):
            request.trigger_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger_config, 'triggerConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.collaboration_group_id):
            body['collaborationGroupId'] = request.collaboration_group_id
        if not DaraCore.is_null(request.description_shrink):
            body['description'] = request.description_shrink
        if not DaraCore.is_null(request.digital_employee_name_shrink):
            body['digitalEmployeeName'] = request.digital_employee_name_shrink
        if not DaraCore.is_null(request.is_open):
            body['isOpen'] = request.is_open
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.segments_shrink):
            body['segments'] = request.segments_shrink
        if not DaraCore.is_null(request.task_detail_shrink):
            body['taskDetail'] = request.task_detail_shrink
        if not DaraCore.is_null(request.trigger_config_shrink):
            body['triggerConfig'] = request.trigger_config_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateScheduledTask',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createScheduledTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheduled_task(
        self,
        request: main_models.CreateScheduledTaskRequest,
    ) -> main_models.CreateScheduledTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_scheduled_task_with_options(request, headers, runtime)

    async def create_scheduled_task_async(
        self,
        request: main_models.CreateScheduledTaskRequest,
    ) -> main_models.CreateScheduledTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_scheduled_task_with_options_async(request, headers, runtime)

    def create_tenant_directory_with_options(
        self,
        request: main_models.CreateTenantDirectoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTenantDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.parent_id):
            body['parentId'] = request.parent_id
        if not DaraCore.is_null(request.path):
            body['path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTenantDirectory',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createTenantDirectory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTenantDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tenant_directory_with_options_async(
        self,
        request: main_models.CreateTenantDirectoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTenantDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.parent_id):
            body['parentId'] = request.parent_id
        if not DaraCore.is_null(request.path):
            body['path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTenantDirectory',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createTenantDirectory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTenantDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tenant_directory(
        self,
        request: main_models.CreateTenantDirectoryRequest,
    ) -> main_models.CreateTenantDirectoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_tenant_directory_with_options(request, headers, runtime)

    async def create_tenant_directory_async(
        self,
        request: main_models.CreateTenantDirectoryRequest,
    ) -> main_models.CreateTenantDirectoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_tenant_directory_with_options_async(request, headers, runtime)

    def create_user_with_options(
        self,
        tmp_req: main_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        tmp_req.validate()
        request = main_models.CreateUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_codes):
            request.role_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_codes, 'roleCodes', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.password_encrypted):
            body['passwordEncrypted'] = request.password_encrypted
        if not DaraCore.is_null(request.role_codes_shrink):
            body['roleCodes'] = request.role_codes_shrink
        if not DaraCore.is_null(request.wn_account_id):
            body['wnAccountId'] = request.wn_account_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createUser',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        tmp_req: main_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        tmp_req.validate()
        request = main_models.CreateUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_codes):
            request.role_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_codes, 'roleCodes', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.password_encrypted):
            body['passwordEncrypted'] = request.password_encrypted
        if not DaraCore.is_null(request.role_codes_shrink):
            body['roleCodes'] = request.role_codes_shrink
        if not DaraCore.is_null(request.wn_account_id):
            body['wnAccountId'] = request.wn_account_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/createUser',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_user_with_options(request, headers, runtime)

    async def create_user_async(
        self,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_user_with_options_async(request, headers, runtime)

    def delete_chat_session_with_options(
        self,
        request: main_models.DeleteChatSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChatSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChatSession',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/deleteChatSession',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChatSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chat_session_with_options_async(
        self,
        request: main_models.DeleteChatSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChatSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChatSession',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/deleteChatSession',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChatSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chat_session(
        self,
        request: main_models.DeleteChatSessionRequest,
    ) -> main_models.DeleteChatSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_chat_session_with_options(request, headers, runtime)

    async def delete_chat_session_async(
        self,
        request: main_models.DeleteChatSessionRequest,
    ) -> main_models.DeleteChatSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_chat_session_with_options_async(request, headers, runtime)

    def delete_source_with_options(
        self,
        request: main_models.DeleteSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/deleteSource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_source_with_options_async(
        self,
        request: main_models.DeleteSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/deleteSource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_source(
        self,
        request: main_models.DeleteSourceRequest,
    ) -> main_models.DeleteSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_source_with_options(request, headers, runtime)

    async def delete_source_async(
        self,
        request: main_models.DeleteSourceRequest,
    ) -> main_models.DeleteSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_source_with_options_async(request, headers, runtime)

    def delete_tenant_directory_with_options(
        self,
        request: main_models.DeleteTenantDirectoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTenantDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_mode):
            body['deleteMode'] = request.delete_mode
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTenantDirectory',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/deleteTenantDirectory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTenantDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tenant_directory_with_options_async(
        self,
        request: main_models.DeleteTenantDirectoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTenantDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_mode):
            body['deleteMode'] = request.delete_mode
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTenantDirectory',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/deleteTenantDirectory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTenantDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tenant_directory(
        self,
        request: main_models.DeleteTenantDirectoryRequest,
    ) -> main_models.DeleteTenantDirectoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_tenant_directory_with_options(request, headers, runtime)

    async def delete_tenant_directory_async(
        self,
        request: main_models.DeleteTenantDirectoryRequest,
    ) -> main_models.DeleteTenantDirectoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_tenant_directory_with_options_async(request, headers, runtime)

    def disable_token_with_options(
        self,
        request: main_models.DisableTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.wn_user_id):
            body['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableToken',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/disableToken',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_token_with_options_async(
        self,
        request: main_models.DisableTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.wn_user_id):
            body['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableToken',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/disableToken',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_token(
        self,
        request: main_models.DisableTokenRequest,
    ) -> main_models.DisableTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.disable_token_with_options(request, headers, runtime)

    async def disable_token_async(
        self,
        request: main_models.DisableTokenRequest,
    ) -> main_models.DisableTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.disable_token_with_options_async(request, headers, runtime)

    def enable_token_with_options(
        self,
        request: main_models.EnableTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.wn_user_id):
            body['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableToken',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/enableToken',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_token_with_options_async(
        self,
        request: main_models.EnableTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.wn_user_id):
            body['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableToken',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/enableToken',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_token(
        self,
        request: main_models.EnableTokenRequest,
    ) -> main_models.EnableTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.enable_token_with_options(request, headers, runtime)

    async def enable_token_async(
        self,
        request: main_models.EnableTokenRequest,
    ) -> main_models.EnableTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.enable_token_with_options_async(request, headers, runtime)

    def get_chat_session_with_options(
        self,
        request: main_models.GetChatSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetChatSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatSession',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getChatSession',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_session_with_options_async(
        self,
        request: main_models.GetChatSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetChatSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatSession',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getChatSession',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat_session(
        self,
        request: main_models.GetChatSessionRequest,
    ) -> main_models.GetChatSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_chat_session_with_options(request, headers, runtime)

    async def get_chat_session_async(
        self,
        request: main_models.GetChatSessionRequest,
    ) -> main_models.GetChatSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_chat_session_with_options_async(request, headers, runtime)

    def get_graph_schema_with_options(
        self,
        request: main_models.GetGraphSchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGraphSchemaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.graph_name):
            body['graphName'] = request.graph_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGraphSchema',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getGraphSchema',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGraphSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_graph_schema_with_options_async(
        self,
        request: main_models.GetGraphSchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGraphSchemaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.graph_name):
            body['graphName'] = request.graph_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGraphSchema',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getGraphSchema',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGraphSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_graph_schema(
        self,
        request: main_models.GetGraphSchemaRequest,
    ) -> main_models.GetGraphSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_graph_schema_with_options(request, headers, runtime)

    async def get_graph_schema_async(
        self,
        request: main_models.GetGraphSchemaRequest,
    ) -> main_models.GetGraphSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_graph_schema_with_options_async(request, headers, runtime)

    def get_instance_expire_time_with_options(
        self,
        request: main_models.GetInstanceExpireTimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceExpireTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceExpireTime',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getInstanceExpireTime',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceExpireTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_expire_time_with_options_async(
        self,
        request: main_models.GetInstanceExpireTimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceExpireTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceExpireTime',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getInstanceExpireTime',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceExpireTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_expire_time(
        self,
        request: main_models.GetInstanceExpireTimeRequest,
    ) -> main_models.GetInstanceExpireTimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_expire_time_with_options(request, headers, runtime)

    async def get_instance_expire_time_async(
        self,
        request: main_models.GetInstanceExpireTimeRequest,
    ) -> main_models.GetInstanceExpireTimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_expire_time_with_options_async(request, headers, runtime)

    def get_knowledge_base_source_with_options(
        self,
        request: main_models.GetKnowledgeBaseSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKnowledgeBaseSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetKnowledgeBaseSource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getKnowledgeBaseSource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKnowledgeBaseSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_knowledge_base_source_with_options_async(
        self,
        request: main_models.GetKnowledgeBaseSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKnowledgeBaseSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetKnowledgeBaseSource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getKnowledgeBaseSource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKnowledgeBaseSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_knowledge_base_source(
        self,
        request: main_models.GetKnowledgeBaseSourceRequest,
    ) -> main_models.GetKnowledgeBaseSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_knowledge_base_source_with_options(request, headers, runtime)

    async def get_knowledge_base_source_async(
        self,
        request: main_models.GetKnowledgeBaseSourceRequest,
    ) -> main_models.GetKnowledgeBaseSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_knowledge_base_source_with_options_async(request, headers, runtime)

    def get_scheduled_task_execution_detail_with_options(
        self,
        request: main_models.GetScheduledTaskExecutionDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetScheduledTaskExecutionDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.execution_id):
            query['executionId'] = request.execution_id
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScheduledTaskExecutionDetail',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getScheduledTaskExecutionDetail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScheduledTaskExecutionDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scheduled_task_execution_detail_with_options_async(
        self,
        request: main_models.GetScheduledTaskExecutionDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetScheduledTaskExecutionDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.execution_id):
            query['executionId'] = request.execution_id
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScheduledTaskExecutionDetail',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getScheduledTaskExecutionDetail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScheduledTaskExecutionDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scheduled_task_execution_detail(
        self,
        request: main_models.GetScheduledTaskExecutionDetailRequest,
    ) -> main_models.GetScheduledTaskExecutionDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_scheduled_task_execution_detail_with_options(request, headers, runtime)

    async def get_scheduled_task_execution_detail_async(
        self,
        request: main_models.GetScheduledTaskExecutionDetailRequest,
    ) -> main_models.GetScheduledTaskExecutionDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_scheduled_task_execution_detail_with_options_async(request, headers, runtime)

    def get_scheduled_task_execution_records_with_options(
        self,
        request: main_models.GetScheduledTaskExecutionRecordsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetScheduledTaskExecutionRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collaboration_group_id):
            query['collaborationGroupId'] = request.collaboration_group_id
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScheduledTaskExecutionRecords',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getScheduledTaskExecutionRecords',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScheduledTaskExecutionRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scheduled_task_execution_records_with_options_async(
        self,
        request: main_models.GetScheduledTaskExecutionRecordsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetScheduledTaskExecutionRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collaboration_group_id):
            query['collaborationGroupId'] = request.collaboration_group_id
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScheduledTaskExecutionRecords',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getScheduledTaskExecutionRecords',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScheduledTaskExecutionRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scheduled_task_execution_records(
        self,
        request: main_models.GetScheduledTaskExecutionRecordsRequest,
    ) -> main_models.GetScheduledTaskExecutionRecordsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_scheduled_task_execution_records_with_options(request, headers, runtime)

    async def get_scheduled_task_execution_records_async(
        self,
        request: main_models.GetScheduledTaskExecutionRecordsRequest,
    ) -> main_models.GetScheduledTaskExecutionRecordsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_scheduled_task_execution_records_with_options_async(request, headers, runtime)

    def get_scheduled_task_understand_detail_with_options(
        self,
        tmp_req: main_models.GetScheduledTaskUnderstandDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetScheduledTaskUnderstandDetailResponse:
        tmp_req.validate()
        request = main_models.GetScheduledTaskUnderstandDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.digital_employee_name):
            request.digital_employee_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.digital_employee_name, 'digitalEmployeeName', 'json')
        if not DaraCore.is_null(tmp_req.segments):
            request.segments_shrink = Utils.array_to_string_with_specified_style(tmp_req.segments, 'segments', 'json')
        query = {}
        if not DaraCore.is_null(request.collaboration_group_id):
            query['collaborationGroupId'] = request.collaboration_group_id
        if not DaraCore.is_null(request.digital_employee_name_shrink):
            query['digitalEmployeeName'] = request.digital_employee_name_shrink
        if not DaraCore.is_null(request.segments_shrink):
            query['segments'] = request.segments_shrink
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not DaraCore.is_null(request.user_input):
            query['userInput'] = request.user_input
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScheduledTaskUnderstandDetail',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getScheduledTaskUnderstandDetail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScheduledTaskUnderstandDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scheduled_task_understand_detail_with_options_async(
        self,
        tmp_req: main_models.GetScheduledTaskUnderstandDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetScheduledTaskUnderstandDetailResponse:
        tmp_req.validate()
        request = main_models.GetScheduledTaskUnderstandDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.digital_employee_name):
            request.digital_employee_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.digital_employee_name, 'digitalEmployeeName', 'json')
        if not DaraCore.is_null(tmp_req.segments):
            request.segments_shrink = Utils.array_to_string_with_specified_style(tmp_req.segments, 'segments', 'json')
        query = {}
        if not DaraCore.is_null(request.collaboration_group_id):
            query['collaborationGroupId'] = request.collaboration_group_id
        if not DaraCore.is_null(request.digital_employee_name_shrink):
            query['digitalEmployeeName'] = request.digital_employee_name_shrink
        if not DaraCore.is_null(request.segments_shrink):
            query['segments'] = request.segments_shrink
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not DaraCore.is_null(request.user_input):
            query['userInput'] = request.user_input
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScheduledTaskUnderstandDetail',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getScheduledTaskUnderstandDetail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScheduledTaskUnderstandDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scheduled_task_understand_detail(
        self,
        request: main_models.GetScheduledTaskUnderstandDetailRequest,
    ) -> main_models.GetScheduledTaskUnderstandDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_scheduled_task_understand_detail_with_options(request, headers, runtime)

    async def get_scheduled_task_understand_detail_async(
        self,
        request: main_models.GetScheduledTaskUnderstandDetailRequest,
    ) -> main_models.GetScheduledTaskUnderstandDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_scheduled_task_understand_detail_with_options_async(request, headers, runtime)

    def get_skill_with_options(
        self,
        request: main_models.GetSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.include_skill_files):
            body['includeSkillFiles'] = request.include_skill_files
        if not DaraCore.is_null(request.skill_code):
            body['skillCode'] = request.skill_code
        if not DaraCore.is_null(request.skill_name):
            body['skillName'] = request.skill_name
        if not DaraCore.is_null(request.view_mode):
            body['viewMode'] = request.view_mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSkill',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getSkill',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_with_options_async(
        self,
        request: main_models.GetSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.include_skill_files):
            body['includeSkillFiles'] = request.include_skill_files
        if not DaraCore.is_null(request.skill_code):
            body['skillCode'] = request.skill_code
        if not DaraCore.is_null(request.skill_name):
            body['skillName'] = request.skill_name
        if not DaraCore.is_null(request.view_mode):
            body['viewMode'] = request.view_mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSkill',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getSkill',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill(
        self,
        request: main_models.GetSkillRequest,
    ) -> main_models.GetSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_skill_with_options(request, headers, runtime)

    async def get_skill_async(
        self,
        request: main_models.GetSkillRequest,
    ) -> main_models.GetSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_skill_with_options_async(request, headers, runtime)

    def get_skill_run_with_options(
        self,
        request: main_models.GetSkillRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillRunResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.include_logs):
            body['includeLogs'] = request.include_logs
        if not DaraCore.is_null(request.run_id):
            body['runId'] = request.run_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillRun',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getSkillRun',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_run_with_options_async(
        self,
        request: main_models.GetSkillRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillRunResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.include_logs):
            body['includeLogs'] = request.include_logs
        if not DaraCore.is_null(request.run_id):
            body['runId'] = request.run_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillRun',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getSkillRun',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_run(
        self,
        request: main_models.GetSkillRunRequest,
    ) -> main_models.GetSkillRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_skill_run_with_options(request, headers, runtime)

    async def get_skill_run_async(
        self,
        request: main_models.GetSkillRunRequest,
    ) -> main_models.GetSkillRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_skill_run_with_options_async(request, headers, runtime)

    def get_source_with_options(
        self,
        request: main_models.GetSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.include_details):
            body['includeDetails'] = request.include_details
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getSource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_source_with_options_async(
        self,
        request: main_models.GetSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.include_details):
            body['includeDetails'] = request.include_details
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getSource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_source(
        self,
        request: main_models.GetSourceRequest,
    ) -> main_models.GetSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_source_with_options(request, headers, runtime)

    async def get_source_async(
        self,
        request: main_models.GetSourceRequest,
    ) -> main_models.GetSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_source_with_options_async(request, headers, runtime)

    def get_source_upload_signature_with_options(
        self,
        request: main_models.GetSourceUploadSignatureRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSourceUploadSignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.content_type):
            body['contentType'] = request.content_type
        if not DaraCore.is_null(request.expires):
            body['expires'] = request.expires
        if not DaraCore.is_null(request.filename):
            body['filename'] = request.filename
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.scope):
            body['scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSourceUploadSignature',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getSourceUploadSignature',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSourceUploadSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_source_upload_signature_with_options_async(
        self,
        request: main_models.GetSourceUploadSignatureRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSourceUploadSignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.content_type):
            body['contentType'] = request.content_type
        if not DaraCore.is_null(request.expires):
            body['expires'] = request.expires
        if not DaraCore.is_null(request.filename):
            body['filename'] = request.filename
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.scope):
            body['scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSourceUploadSignature',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getSourceUploadSignature',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSourceUploadSignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_source_upload_signature(
        self,
        request: main_models.GetSourceUploadSignatureRequest,
    ) -> main_models.GetSourceUploadSignatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_source_upload_signature_with_options(request, headers, runtime)

    async def get_source_upload_signature_async(
        self,
        request: main_models.GetSourceUploadSignatureRequest,
    ) -> main_models.GetSourceUploadSignatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_source_upload_signature_with_options_async(request, headers, runtime)

    def get_token_info_with_options(
        self,
        request: main_models.GetTokenInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.wn_user_id):
            body['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTokenInfo',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getTokenInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_info_with_options_async(
        self,
        request: main_models.GetTokenInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.wn_user_id):
            body['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTokenInfo',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getTokenInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token_info(
        self,
        request: main_models.GetTokenInfoRequest,
    ) -> main_models.GetTokenInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_token_info_with_options(request, headers, runtime)

    async def get_token_info_async(
        self,
        request: main_models.GetTokenInfoRequest,
    ) -> main_models.GetTokenInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_token_info_with_options_async(request, headers, runtime)

    def get_user_with_options(
        self,
        request: main_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not DaraCore.is_null(request.wn_account_id):
            query['wnAccountId'] = request.wn_account_id
        if not DaraCore.is_null(request.wn_user_id):
            query['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getUser',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: main_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not DaraCore.is_null(request.wn_account_id):
            query['wnAccountId'] = request.wn_account_id
        if not DaraCore.is_null(request.wn_user_id):
            query['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getUser',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_user_with_options(request, headers, runtime)

    async def get_user_async(
        self,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_user_with_options_async(request, headers, runtime)

    def get_user_credit_usage_with_options(
        self,
        request: main_models.GetUserCreditUsageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserCreditUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserCreditUsage',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getUserCreditUsage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserCreditUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_credit_usage_with_options_async(
        self,
        request: main_models.GetUserCreditUsageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserCreditUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserCreditUsage',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getUserCreditUsage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserCreditUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_credit_usage(
        self,
        request: main_models.GetUserCreditUsageRequest,
    ) -> main_models.GetUserCreditUsageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_user_credit_usage_with_options(request, headers, runtime)

    async def get_user_credit_usage_async(
        self,
        request: main_models.GetUserCreditUsageRequest,
    ) -> main_models.GetUserCreditUsageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_user_credit_usage_with_options_async(request, headers, runtime)

    def get_user_info_with_options(
        self,
        request: main_models.GetUserInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserInfo',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getUserInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_info_with_options_async(
        self,
        request: main_models.GetUserInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserInfo',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/getUserInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_info(
        self,
        request: main_models.GetUserInfoRequest,
    ) -> main_models.GetUserInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_user_info_with_options(request, headers, runtime)

    async def get_user_info_async(
        self,
        request: main_models.GetUserInfoRequest,
    ) -> main_models.GetUserInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_user_info_with_options_async(request, headers, runtime)

    def grant_agent_users_with_options(
        self,
        tmp_req: main_models.GrantAgentUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GrantAgentUsersResponse:
        tmp_req.validate()
        request = main_models.GrantAgentUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.permissions):
            request.permissions_shrink = Utils.array_to_string_with_specified_style(tmp_req.permissions, 'permissions', 'json')
        if not DaraCore.is_null(tmp_req.user_group_ids):
            request.user_group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_group_ids, 'userGroupIds', 'json')
        if not DaraCore.is_null(tmp_req.user_ids):
            request.user_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_ids, 'userIds', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.expire_date):
            body['expireDate'] = request.expire_date
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.permissions_shrink):
            body['permissions'] = request.permissions_shrink
        if not DaraCore.is_null(request.user_group_ids_shrink):
            body['userGroupIds'] = request.user_group_ids_shrink
        if not DaraCore.is_null(request.user_ids_shrink):
            body['userIds'] = request.user_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantAgentUsers',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/grantAgentUsers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantAgentUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_agent_users_with_options_async(
        self,
        tmp_req: main_models.GrantAgentUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GrantAgentUsersResponse:
        tmp_req.validate()
        request = main_models.GrantAgentUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.permissions):
            request.permissions_shrink = Utils.array_to_string_with_specified_style(tmp_req.permissions, 'permissions', 'json')
        if not DaraCore.is_null(tmp_req.user_group_ids):
            request.user_group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_group_ids, 'userGroupIds', 'json')
        if not DaraCore.is_null(tmp_req.user_ids):
            request.user_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_ids, 'userIds', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.expire_date):
            body['expireDate'] = request.expire_date
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.permissions_shrink):
            body['permissions'] = request.permissions_shrink
        if not DaraCore.is_null(request.user_group_ids_shrink):
            body['userGroupIds'] = request.user_group_ids_shrink
        if not DaraCore.is_null(request.user_ids_shrink):
            body['userIds'] = request.user_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantAgentUsers',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/grantAgentUsers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantAgentUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_agent_users(
        self,
        request: main_models.GrantAgentUsersRequest,
    ) -> main_models.GrantAgentUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.grant_agent_users_with_options(request, headers, runtime)

    async def grant_agent_users_async(
        self,
        request: main_models.GrantAgentUsersRequest,
    ) -> main_models.GrantAgentUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.grant_agent_users_with_options_async(request, headers, runtime)

    def list_admin_knowledge_bases_with_options(
        self,
        tmp_req: main_models.ListAdminKnowledgeBasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAdminKnowledgeBasesResponse:
        tmp_req.validate()
        request = main_models.ListAdminKnowledgeBasesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.source_types):
            request.source_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_types, 'sourceTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.keyword):
            body['keyword'] = request.keyword
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_field):
            body['sortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            body['sortOrder'] = request.sort_order
        if not DaraCore.is_null(request.source_types_shrink):
            body['sourceTypes'] = request.source_types_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAdminKnowledgeBases',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listAdminKnowledgeBases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAdminKnowledgeBasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_admin_knowledge_bases_with_options_async(
        self,
        tmp_req: main_models.ListAdminKnowledgeBasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAdminKnowledgeBasesResponse:
        tmp_req.validate()
        request = main_models.ListAdminKnowledgeBasesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.source_types):
            request.source_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_types, 'sourceTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.keyword):
            body['keyword'] = request.keyword
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_field):
            body['sortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            body['sortOrder'] = request.sort_order
        if not DaraCore.is_null(request.source_types_shrink):
            body['sourceTypes'] = request.source_types_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAdminKnowledgeBases',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listAdminKnowledgeBases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAdminKnowledgeBasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_admin_knowledge_bases(
        self,
        request: main_models.ListAdminKnowledgeBasesRequest,
    ) -> main_models.ListAdminKnowledgeBasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_admin_knowledge_bases_with_options(request, headers, runtime)

    async def list_admin_knowledge_bases_async(
        self,
        request: main_models.ListAdminKnowledgeBasesRequest,
    ) -> main_models.ListAdminKnowledgeBasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_admin_knowledge_bases_with_options_async(request, headers, runtime)

    def list_agents_with_options(
        self,
        request: main_models.ListAgentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgents',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listAgents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agents_with_options_async(
        self,
        request: main_models.ListAgentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgents',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listAgents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agents(
        self,
        request: main_models.ListAgentsRequest,
    ) -> main_models.ListAgentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_agents_with_options(request, headers, runtime)

    async def list_agents_async(
        self,
        request: main_models.ListAgentsRequest,
    ) -> main_models.ListAgentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_agents_with_options_async(request, headers, runtime)

    def list_authorized_agents_with_options(
        self,
        request: main_models.ListAuthorizedAgentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthorizedAgentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.permission):
            body['permission'] = request.permission
        if not DaraCore.is_null(request.target_user_id):
            body['targetUserId'] = request.target_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAuthorizedAgents',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listAuthorizedAgents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthorizedAgentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_authorized_agents_with_options_async(
        self,
        request: main_models.ListAuthorizedAgentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthorizedAgentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.permission):
            body['permission'] = request.permission
        if not DaraCore.is_null(request.target_user_id):
            body['targetUserId'] = request.target_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAuthorizedAgents',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listAuthorizedAgents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthorizedAgentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_authorized_agents(
        self,
        request: main_models.ListAuthorizedAgentsRequest,
    ) -> main_models.ListAuthorizedAgentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_authorized_agents_with_options(request, headers, runtime)

    async def list_authorized_agents_async(
        self,
        request: main_models.ListAuthorizedAgentsRequest,
    ) -> main_models.ListAuthorizedAgentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_authorized_agents_with_options_async(request, headers, runtime)

    def list_authorized_users_with_options(
        self,
        request: main_models.ListAuthorizedUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthorizedUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.grantee_type):
            body['granteeType'] = request.grantee_type
        if not DaraCore.is_null(request.keyword):
            body['keyword'] = request.keyword
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.permission):
            body['permission'] = request.permission
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAuthorizedUsers',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listAuthorizedUsers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthorizedUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_authorized_users_with_options_async(
        self,
        request: main_models.ListAuthorizedUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthorizedUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.grantee_type):
            body['granteeType'] = request.grantee_type
        if not DaraCore.is_null(request.keyword):
            body['keyword'] = request.keyword
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.permission):
            body['permission'] = request.permission
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAuthorizedUsers',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listAuthorizedUsers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthorizedUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_authorized_users(
        self,
        request: main_models.ListAuthorizedUsersRequest,
    ) -> main_models.ListAuthorizedUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_authorized_users_with_options(request, headers, runtime)

    async def list_authorized_users_async(
        self,
        request: main_models.ListAuthorizedUsersRequest,
    ) -> main_models.ListAuthorizedUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_authorized_users_with_options_async(request, headers, runtime)

    def list_available_configs_with_options(
        self,
        request: main_models.ListAvailableConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableConfigs',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listAvailableConfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_configs_with_options_async(
        self,
        request: main_models.ListAvailableConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableConfigs',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listAvailableConfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_configs(
        self,
        request: main_models.ListAvailableConfigsRequest,
    ) -> main_models.ListAvailableConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_available_configs_with_options(request, headers, runtime)

    async def list_available_configs_async(
        self,
        request: main_models.ListAvailableConfigsRequest,
    ) -> main_models.ListAvailableConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_available_configs_with_options_async(request, headers, runtime)

    def list_billing_with_options(
        self,
        request: main_models.ListBillingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBillingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['bizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            body['bizType'] = request.biz_type
        if not DaraCore.is_null(request.end_time):
            body['endTime'] = request.end_time
        if not DaraCore.is_null(request.ignore_zero):
            body['ignoreZero'] = request.ignore_zero
        if not DaraCore.is_null(request.operation):
            body['operation'] = request.operation
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['startTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.wn_user_id):
            body['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListBilling',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listBilling',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBillingResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_billing_with_options_async(
        self,
        request: main_models.ListBillingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBillingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['bizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            body['bizType'] = request.biz_type
        if not DaraCore.is_null(request.end_time):
            body['endTime'] = request.end_time
        if not DaraCore.is_null(request.ignore_zero):
            body['ignoreZero'] = request.ignore_zero
        if not DaraCore.is_null(request.operation):
            body['operation'] = request.operation
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['startTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.wn_user_id):
            body['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListBilling',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listBilling',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBillingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_billing(
        self,
        request: main_models.ListBillingRequest,
    ) -> main_models.ListBillingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_billing_with_options(request, headers, runtime)

    async def list_billing_async(
        self,
        request: main_models.ListBillingRequest,
    ) -> main_models.ListBillingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_billing_with_options_async(request, headers, runtime)

    def list_chat_sessions_with_options(
        self,
        request: main_models.ListChatSessionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListChatSessionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.digital_employee_name):
            query['digitalEmployeeName'] = request.digital_employee_name
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatSessions',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listChatSessions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chat_sessions_with_options_async(
        self,
        request: main_models.ListChatSessionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListChatSessionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.digital_employee_name):
            query['digitalEmployeeName'] = request.digital_employee_name
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatSessions',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listChatSessions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatSessionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chat_sessions(
        self,
        request: main_models.ListChatSessionsRequest,
    ) -> main_models.ListChatSessionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_chat_sessions_with_options(request, headers, runtime)

    async def list_chat_sessions_async(
        self,
        request: main_models.ListChatSessionsRequest,
    ) -> main_models.ListChatSessionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_chat_sessions_with_options_async(request, headers, runtime)

    def list_graphs_with_options(
        self,
        request: main_models.ListGraphsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGraphsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGraphs',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listGraphs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGraphsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_graphs_with_options_async(
        self,
        request: main_models.ListGraphsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGraphsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGraphs',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listGraphs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGraphsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_graphs(
        self,
        request: main_models.ListGraphsRequest,
    ) -> main_models.ListGraphsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_graphs_with_options(request, headers, runtime)

    async def list_graphs_async(
        self,
        request: main_models.ListGraphsRequest,
    ) -> main_models.ListGraphsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_graphs_with_options_async(request, headers, runtime)

    def list_knowledge_base_directories_with_options(
        self,
        request: main_models.ListKnowledgeBaseDirectoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKnowledgeBaseDirectoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.sort_field):
            body['sortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            body['sortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListKnowledgeBaseDirectories',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listKnowledgeBaseDirectories',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKnowledgeBaseDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_knowledge_base_directories_with_options_async(
        self,
        request: main_models.ListKnowledgeBaseDirectoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKnowledgeBaseDirectoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.sort_field):
            body['sortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            body['sortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListKnowledgeBaseDirectories',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listKnowledgeBaseDirectories',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKnowledgeBaseDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_knowledge_base_directories(
        self,
        request: main_models.ListKnowledgeBaseDirectoriesRequest,
    ) -> main_models.ListKnowledgeBaseDirectoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_knowledge_base_directories_with_options(request, headers, runtime)

    async def list_knowledge_base_directories_async(
        self,
        request: main_models.ListKnowledgeBaseDirectoriesRequest,
    ) -> main_models.ListKnowledgeBaseDirectoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_knowledge_base_directories_with_options_async(request, headers, runtime)

    def list_output_files_with_options(
        self,
        request: main_models.ListOutputFilesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOutputFilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.item_type):
            body['itemType'] = request.item_type
        if not DaraCore.is_null(request.keyword):
            body['keyword'] = request.keyword
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.shared_only):
            body['sharedOnly'] = request.shared_only
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListOutputFiles',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listOutputFiles',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOutputFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_output_files_with_options_async(
        self,
        request: main_models.ListOutputFilesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOutputFilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.item_type):
            body['itemType'] = request.item_type
        if not DaraCore.is_null(request.keyword):
            body['keyword'] = request.keyword
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.shared_only):
            body['sharedOnly'] = request.shared_only
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListOutputFiles',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listOutputFiles',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOutputFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_output_files(
        self,
        request: main_models.ListOutputFilesRequest,
    ) -> main_models.ListOutputFilesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_output_files_with_options(request, headers, runtime)

    async def list_output_files_async(
        self,
        request: main_models.ListOutputFilesRequest,
    ) -> main_models.ListOutputFilesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_output_files_with_options_async(request, headers, runtime)

    def list_personal_directory_contents_with_options(
        self,
        tmp_req: main_models.ListPersonalDirectoryContentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPersonalDirectoryContentsResponse:
        tmp_req.validate()
        request = main_models.ListPersonalDirectoryContentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.source_types):
            request.source_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_types, 'sourceTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_field):
            body['sortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            body['sortOrder'] = request.sort_order
        if not DaraCore.is_null(request.source_types_shrink):
            body['sourceTypes'] = request.source_types_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPersonalDirectoryContents',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listPersonalDirectoryContents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPersonalDirectoryContentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_personal_directory_contents_with_options_async(
        self,
        tmp_req: main_models.ListPersonalDirectoryContentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPersonalDirectoryContentsResponse:
        tmp_req.validate()
        request = main_models.ListPersonalDirectoryContentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.source_types):
            request.source_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_types, 'sourceTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_field):
            body['sortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            body['sortOrder'] = request.sort_order
        if not DaraCore.is_null(request.source_types_shrink):
            body['sourceTypes'] = request.source_types_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPersonalDirectoryContents',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listPersonalDirectoryContents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPersonalDirectoryContentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_personal_directory_contents(
        self,
        request: main_models.ListPersonalDirectoryContentsRequest,
    ) -> main_models.ListPersonalDirectoryContentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_personal_directory_contents_with_options(request, headers, runtime)

    async def list_personal_directory_contents_async(
        self,
        request: main_models.ListPersonalDirectoryContentsRequest,
    ) -> main_models.ListPersonalDirectoryContentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_personal_directory_contents_with_options_async(request, headers, runtime)

    def list_roles_with_options(
        self,
        request: main_models.ListRolesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listRoles',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: main_models.ListRolesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listRoles',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        request: main_models.ListRolesRequest,
    ) -> main_models.ListRolesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_roles_with_options(request, headers, runtime)

    async def list_roles_async(
        self,
        request: main_models.ListRolesRequest,
    ) -> main_models.ListRolesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_roles_with_options_async(request, headers, runtime)

    def list_scheduled_tasks_with_options(
        self,
        request: main_models.ListScheduledTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListScheduledTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collaboration_group_id):
            query['collaborationGroupId'] = request.collaboration_group_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheduledTasks',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listScheduledTasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScheduledTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scheduled_tasks_with_options_async(
        self,
        request: main_models.ListScheduledTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListScheduledTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.collaboration_group_id):
            query['collaborationGroupId'] = request.collaboration_group_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheduledTasks',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listScheduledTasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScheduledTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scheduled_tasks(
        self,
        request: main_models.ListScheduledTasksRequest,
    ) -> main_models.ListScheduledTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_scheduled_tasks_with_options(request, headers, runtime)

    async def list_scheduled_tasks_async(
        self,
        request: main_models.ListScheduledTasksRequest,
    ) -> main_models.ListScheduledTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_scheduled_tasks_with_options_async(request, headers, runtime)

    def list_skills_with_options(
        self,
        tmp_req: main_models.ListSkillsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillsResponse:
        tmp_req.validate()
        request = main_models.ListSkillsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.bind_status):
            body['bindStatus'] = request.bind_status
        if not DaraCore.is_null(request.filter_type):
            body['filterType'] = request.filter_type
        if not DaraCore.is_null(request.keyword):
            body['keyword'] = request.keyword
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSkills',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listSkills',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skills_with_options_async(
        self,
        tmp_req: main_models.ListSkillsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillsResponse:
        tmp_req.validate()
        request = main_models.ListSkillsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.bind_status):
            body['bindStatus'] = request.bind_status
        if not DaraCore.is_null(request.filter_type):
            body['filterType'] = request.filter_type
        if not DaraCore.is_null(request.keyword):
            body['keyword'] = request.keyword
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSkills',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listSkills',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skills(
        self,
        request: main_models.ListSkillsRequest,
    ) -> main_models.ListSkillsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_skills_with_options(request, headers, runtime)

    async def list_skills_async(
        self,
        request: main_models.ListSkillsRequest,
    ) -> main_models.ListSkillsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_skills_with_options_async(request, headers, runtime)

    def list_tenant_directory_with_options(
        self,
        request: main_models.ListTenantDirectoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTenantDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_field):
            body['sortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            body['sortOrder'] = request.sort_order
        if not DaraCore.is_null(request.source_types):
            body['sourceTypes'] = request.source_types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTenantDirectory',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listTenantDirectory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTenantDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tenant_directory_with_options_async(
        self,
        request: main_models.ListTenantDirectoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTenantDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_field):
            body['sortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            body['sortOrder'] = request.sort_order
        if not DaraCore.is_null(request.source_types):
            body['sourceTypes'] = request.source_types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTenantDirectory',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listTenantDirectory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTenantDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tenant_directory(
        self,
        request: main_models.ListTenantDirectoryRequest,
    ) -> main_models.ListTenantDirectoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tenant_directory_with_options(request, headers, runtime)

    async def list_tenant_directory_async(
        self,
        request: main_models.ListTenantDirectoryRequest,
    ) -> main_models.ListTenantDirectoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tenant_directory_with_options_async(request, headers, runtime)

    def list_user_visible_knowledge_base_contents_with_options(
        self,
        request: main_models.ListUserVisibleKnowledgeBaseContentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserVisibleKnowledgeBaseContentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.keyword):
            body['keyword'] = request.keyword
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_field):
            body['sortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            body['sortOrder'] = request.sort_order
        if not DaraCore.is_null(request.source_types):
            body['sourceTypes'] = request.source_types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUserVisibleKnowledgeBaseContents',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listUserVisibleKnowledgeBaseContents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserVisibleKnowledgeBaseContentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_visible_knowledge_base_contents_with_options_async(
        self,
        request: main_models.ListUserVisibleKnowledgeBaseContentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserVisibleKnowledgeBaseContentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.keyword):
            body['keyword'] = request.keyword
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_field):
            body['sortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            body['sortOrder'] = request.sort_order
        if not DaraCore.is_null(request.source_types):
            body['sourceTypes'] = request.source_types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUserVisibleKnowledgeBaseContents',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listUserVisibleKnowledgeBaseContents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserVisibleKnowledgeBaseContentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_visible_knowledge_base_contents(
        self,
        request: main_models.ListUserVisibleKnowledgeBaseContentsRequest,
    ) -> main_models.ListUserVisibleKnowledgeBaseContentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_user_visible_knowledge_base_contents_with_options(request, headers, runtime)

    async def list_user_visible_knowledge_base_contents_async(
        self,
        request: main_models.ListUserVisibleKnowledgeBaseContentsRequest,
    ) -> main_models.ListUserVisibleKnowledgeBaseContentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_user_visible_knowledge_base_contents_with_options_async(request, headers, runtime)

    def list_user_visible_knowledge_bases_with_options(
        self,
        request: main_models.ListUserVisibleKnowledgeBasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserVisibleKnowledgeBasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.keyword):
            body['keyword'] = request.keyword
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUserVisibleKnowledgeBases',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listUserVisibleKnowledgeBases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserVisibleKnowledgeBasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_visible_knowledge_bases_with_options_async(
        self,
        request: main_models.ListUserVisibleKnowledgeBasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserVisibleKnowledgeBasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.keyword):
            body['keyword'] = request.keyword
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUserVisibleKnowledgeBases',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listUserVisibleKnowledgeBases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserVisibleKnowledgeBasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_visible_knowledge_bases(
        self,
        request: main_models.ListUserVisibleKnowledgeBasesRequest,
    ) -> main_models.ListUserVisibleKnowledgeBasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_user_visible_knowledge_bases_with_options(request, headers, runtime)

    async def list_user_visible_knowledge_bases_async(
        self,
        request: main_models.ListUserVisibleKnowledgeBasesRequest,
    ) -> main_models.ListUserVisibleKnowledgeBasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_user_visible_knowledge_bases_with_options_async(request, headers, runtime)

    def list_users_with_options(
        self,
        tmp_req: main_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        tmp_req.validate()
        request = main_models.ListUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'accountIds', 'json')
        if not DaraCore.is_null(tmp_req.role_codes):
            request.role_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_codes, 'roleCodes', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            body['accountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.is_active):
            body['isActive'] = request.is_active
        if not DaraCore.is_null(request.keyword):
            body['keyword'] = request.keyword
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.role_codes_shrink):
            body['roleCodes'] = request.role_codes_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listUsers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        tmp_req: main_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        tmp_req.validate()
        request = main_models.ListUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'accountIds', 'json')
        if not DaraCore.is_null(tmp_req.role_codes):
            request.role_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_codes, 'roleCodes', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            body['accountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.is_active):
            body['isActive'] = request.is_active
        if not DaraCore.is_null(request.keyword):
            body['keyword'] = request.keyword
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.role_codes_shrink):
            body['roleCodes'] = request.role_codes_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listUsers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_users_with_options(request, headers, runtime)

    async def list_users_async(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_users_with_options_async(request, headers, runtime)

    def list_visible_knowledge_base_contents_with_options(
        self,
        tmp_req: main_models.ListVisibleKnowledgeBaseContentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVisibleKnowledgeBaseContentsResponse:
        tmp_req.validate()
        request = main_models.ListVisibleKnowledgeBaseContentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.source_types):
            request.source_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_types, 'sourceTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_field):
            body['sortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            body['sortOrder'] = request.sort_order
        if not DaraCore.is_null(request.source_types_shrink):
            body['sourceTypes'] = request.source_types_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVisibleKnowledgeBaseContents',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listVisibleKnowledgeBaseContents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVisibleKnowledgeBaseContentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_visible_knowledge_base_contents_with_options_async(
        self,
        tmp_req: main_models.ListVisibleKnowledgeBaseContentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVisibleKnowledgeBaseContentsResponse:
        tmp_req.validate()
        request = main_models.ListVisibleKnowledgeBaseContentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.source_types):
            request.source_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_types, 'sourceTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_field):
            body['sortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            body['sortOrder'] = request.sort_order
        if not DaraCore.is_null(request.source_types_shrink):
            body['sourceTypes'] = request.source_types_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVisibleKnowledgeBaseContents',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listVisibleKnowledgeBaseContents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVisibleKnowledgeBaseContentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_visible_knowledge_base_contents(
        self,
        request: main_models.ListVisibleKnowledgeBaseContentsRequest,
    ) -> main_models.ListVisibleKnowledgeBaseContentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_visible_knowledge_base_contents_with_options(request, headers, runtime)

    async def list_visible_knowledge_base_contents_async(
        self,
        request: main_models.ListVisibleKnowledgeBaseContentsRequest,
    ) -> main_models.ListVisibleKnowledgeBaseContentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_visible_knowledge_base_contents_with_options_async(request, headers, runtime)

    def list_visible_knowledge_bases_with_options(
        self,
        request: main_models.ListVisibleKnowledgeBasesRequest,
        headers: main_models.ListVisibleKnowledgeBasesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListVisibleKnowledgeBasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.request_id):
            real_headers['requestId'] = str(headers.request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVisibleKnowledgeBases',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listVisibleKnowledgeBases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVisibleKnowledgeBasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_visible_knowledge_bases_with_options_async(
        self,
        request: main_models.ListVisibleKnowledgeBasesRequest,
        headers: main_models.ListVisibleKnowledgeBasesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListVisibleKnowledgeBasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.request_id):
            real_headers['requestId'] = str(headers.request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVisibleKnowledgeBases',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/listVisibleKnowledgeBases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVisibleKnowledgeBasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_visible_knowledge_bases(
        self,
        request: main_models.ListVisibleKnowledgeBasesRequest,
    ) -> main_models.ListVisibleKnowledgeBasesResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListVisibleKnowledgeBasesHeaders()
        return self.list_visible_knowledge_bases_with_options(request, headers, runtime)

    async def list_visible_knowledge_bases_async(
        self,
        request: main_models.ListVisibleKnowledgeBasesRequest,
    ) -> main_models.ListVisibleKnowledgeBasesResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListVisibleKnowledgeBasesHeaders()
        return await self.list_visible_knowledge_bases_with_options_async(request, headers, runtime)

    def move_knowledge_base_resource_with_options(
        self,
        request: main_models.MoveKnowledgeBaseResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MoveKnowledgeBaseResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.knowledge_id):
            body['knowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.source_directory_id):
            body['sourceDirectoryId'] = request.source_directory_id
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        if not DaraCore.is_null(request.target_directory_id):
            body['targetDirectoryId'] = request.target_directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveKnowledgeBaseResource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/moveKnowledgeBaseResource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveKnowledgeBaseResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_knowledge_base_resource_with_options_async(
        self,
        request: main_models.MoveKnowledgeBaseResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MoveKnowledgeBaseResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.knowledge_id):
            body['knowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.source_directory_id):
            body['sourceDirectoryId'] = request.source_directory_id
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        if not DaraCore.is_null(request.target_directory_id):
            body['targetDirectoryId'] = request.target_directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveKnowledgeBaseResource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/moveKnowledgeBaseResource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveKnowledgeBaseResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_knowledge_base_resource(
        self,
        request: main_models.MoveKnowledgeBaseResourceRequest,
    ) -> main_models.MoveKnowledgeBaseResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.move_knowledge_base_resource_with_options(request, headers, runtime)

    async def move_knowledge_base_resource_async(
        self,
        request: main_models.MoveKnowledgeBaseResourceRequest,
    ) -> main_models.MoveKnowledgeBaseResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.move_knowledge_base_resource_with_options_async(request, headers, runtime)

    def move_resource_with_options(
        self,
        request: main_models.MoveResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.source_directory_id):
            body['sourceDirectoryId'] = request.source_directory_id
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        if not DaraCore.is_null(request.target_directory_id):
            body['targetDirectoryId'] = request.target_directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveResource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/moveResource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_with_options_async(
        self,
        request: main_models.MoveResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.source_directory_id):
            body['sourceDirectoryId'] = request.source_directory_id
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        if not DaraCore.is_null(request.target_directory_id):
            body['targetDirectoryId'] = request.target_directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveResource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/moveResource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource(
        self,
        request: main_models.MoveResourceRequest,
    ) -> main_models.MoveResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.move_resource_with_options(request, headers, runtime)

    async def move_resource_async(
        self,
        request: main_models.MoveResourceRequest,
    ) -> main_models.MoveResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.move_resource_with_options_async(request, headers, runtime)

    def preview_knowledge_base_source_with_options(
        self,
        request: main_models.PreviewKnowledgeBaseSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PreviewKnowledgeBaseSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PreviewKnowledgeBaseSource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/previewKnowledgeBaseSource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviewKnowledgeBaseSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def preview_knowledge_base_source_with_options_async(
        self,
        request: main_models.PreviewKnowledgeBaseSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PreviewKnowledgeBaseSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PreviewKnowledgeBaseSource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/previewKnowledgeBaseSource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviewKnowledgeBaseSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preview_knowledge_base_source(
        self,
        request: main_models.PreviewKnowledgeBaseSourceRequest,
    ) -> main_models.PreviewKnowledgeBaseSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.preview_knowledge_base_source_with_options(request, headers, runtime)

    async def preview_knowledge_base_source_async(
        self,
        request: main_models.PreviewKnowledgeBaseSourceRequest,
    ) -> main_models.PreviewKnowledgeBaseSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.preview_knowledge_base_source_with_options_async(request, headers, runtime)

    def preview_personal_source_with_options(
        self,
        request: main_models.PreviewPersonalSourceRequest,
        headers: main_models.PreviewPersonalSourceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PreviewPersonalSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.request_id):
            real_headers['requestId'] = str(headers.request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PreviewPersonalSource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/previewPersonalSource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviewPersonalSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def preview_personal_source_with_options_async(
        self,
        request: main_models.PreviewPersonalSourceRequest,
        headers: main_models.PreviewPersonalSourceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PreviewPersonalSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.request_id):
            real_headers['requestId'] = str(headers.request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PreviewPersonalSource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/previewPersonalSource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviewPersonalSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preview_personal_source(
        self,
        request: main_models.PreviewPersonalSourceRequest,
    ) -> main_models.PreviewPersonalSourceResponse:
        runtime = RuntimeOptions()
        headers = main_models.PreviewPersonalSourceHeaders()
        return self.preview_personal_source_with_options(request, headers, runtime)

    async def preview_personal_source_async(
        self,
        request: main_models.PreviewPersonalSourceRequest,
    ) -> main_models.PreviewPersonalSourceResponse:
        runtime = RuntimeOptions()
        headers = main_models.PreviewPersonalSourceHeaders()
        return await self.preview_personal_source_with_options_async(request, headers, runtime)

    def query_primary_object_data_with_options(
        self,
        request: main_models.QueryPrimaryObjectDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryPrimaryObjectDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.keyword):
            body['keyword'] = request.keyword
        if not DaraCore.is_null(request.only_favorites):
            body['onlyFavorites'] = request.only_favorites
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryPrimaryObjectData',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/queryPrimaryObjectData',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPrimaryObjectDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_primary_object_data_with_options_async(
        self,
        request: main_models.QueryPrimaryObjectDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryPrimaryObjectDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.keyword):
            body['keyword'] = request.keyword
        if not DaraCore.is_null(request.only_favorites):
            body['onlyFavorites'] = request.only_favorites
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryPrimaryObjectData',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/queryPrimaryObjectData',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPrimaryObjectDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_primary_object_data(
        self,
        request: main_models.QueryPrimaryObjectDataRequest,
    ) -> main_models.QueryPrimaryObjectDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_primary_object_data_with_options(request, headers, runtime)

    async def query_primary_object_data_async(
        self,
        request: main_models.QueryPrimaryObjectDataRequest,
    ) -> main_models.QueryPrimaryObjectDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_primary_object_data_with_options_async(request, headers, runtime)

    def query_semantic_knowledge_with_options(
        self,
        request: main_models.QuerySemanticKnowledgeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QuerySemanticKnowledgeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.graph_name):
            body['graphName'] = request.graph_name
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QuerySemanticKnowledge',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/querySemanticKnowledge',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySemanticKnowledgeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_semantic_knowledge_with_options_async(
        self,
        request: main_models.QuerySemanticKnowledgeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QuerySemanticKnowledgeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.graph_name):
            body['graphName'] = request.graph_name
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QuerySemanticKnowledge',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/querySemanticKnowledge',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySemanticKnowledgeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_semantic_knowledge(
        self,
        request: main_models.QuerySemanticKnowledgeRequest,
    ) -> main_models.QuerySemanticKnowledgeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_semantic_knowledge_with_options(request, headers, runtime)

    async def query_semantic_knowledge_async(
        self,
        request: main_models.QuerySemanticKnowledgeRequest,
    ) -> main_models.QuerySemanticKnowledgeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_semantic_knowledge_with_options_async(request, headers, runtime)

    def query_sync_result_with_options(
        self,
        request: main_models.QuerySyncResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QuerySyncResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QuerySyncResult',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/querySyncResult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sync_result_with_options_async(
        self,
        request: main_models.QuerySyncResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QuerySyncResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QuerySyncResult',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/querySyncResult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySyncResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sync_result(
        self,
        request: main_models.QuerySyncResultRequest,
    ) -> main_models.QuerySyncResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_sync_result_with_options(request, headers, runtime)

    async def query_sync_result_async(
        self,
        request: main_models.QuerySyncResultRequest,
    ) -> main_models.QuerySyncResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_sync_result_with_options_async(request, headers, runtime)

    def remove_user_with_options(
        self,
        request: main_models.RemoveUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not DaraCore.is_null(request.wn_user_id):
            query['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUser',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/removeUser',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_with_options_async(
        self,
        request: main_models.RemoveUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not DaraCore.is_null(request.wn_user_id):
            query['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUser',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/removeUser',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user(
        self,
        request: main_models.RemoveUserRequest,
    ) -> main_models.RemoveUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_user_with_options(request, headers, runtime)

    async def remove_user_async(
        self,
        request: main_models.RemoveUserRequest,
    ) -> main_models.RemoveUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_user_with_options_async(request, headers, runtime)

    def rename_knowledge_base_source_with_options(
        self,
        request: main_models.RenameKnowledgeBaseSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenameKnowledgeBaseSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.new_name):
            body['newName'] = request.new_name
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenameKnowledgeBaseSource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/renameKnowledgeBaseSource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenameKnowledgeBaseSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_knowledge_base_source_with_options_async(
        self,
        request: main_models.RenameKnowledgeBaseSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenameKnowledgeBaseSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.new_name):
            body['newName'] = request.new_name
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenameKnowledgeBaseSource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/renameKnowledgeBaseSource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenameKnowledgeBaseSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_knowledge_base_source(
        self,
        request: main_models.RenameKnowledgeBaseSourceRequest,
    ) -> main_models.RenameKnowledgeBaseSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.rename_knowledge_base_source_with_options(request, headers, runtime)

    async def rename_knowledge_base_source_async(
        self,
        request: main_models.RenameKnowledgeBaseSourceRequest,
    ) -> main_models.RenameKnowledgeBaseSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.rename_knowledge_base_source_with_options_async(request, headers, runtime)

    def rename_source_with_options(
        self,
        request: main_models.RenameSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenameSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.new_name):
            body['newName'] = request.new_name
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenameSource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/renameSource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenameSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_source_with_options_async(
        self,
        request: main_models.RenameSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenameSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.new_name):
            body['newName'] = request.new_name
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenameSource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/renameSource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenameSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_source(
        self,
        request: main_models.RenameSourceRequest,
    ) -> main_models.RenameSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.rename_source_with_options(request, headers, runtime)

    async def rename_source_async(
        self,
        request: main_models.RenameSourceRequest,
    ) -> main_models.RenameSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.rename_source_with_options_async(request, headers, runtime)

    def reparse_source_with_options(
        self,
        request: main_models.ReparseSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReparseSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.force_sync):
            body['forceSync'] = request.force_sync
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReparseSource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/reparseSource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReparseSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reparse_source_with_options_async(
        self,
        request: main_models.ReparseSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReparseSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.force_sync):
            body['forceSync'] = request.force_sync
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReparseSource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/reparseSource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReparseSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reparse_source(
        self,
        request: main_models.ReparseSourceRequest,
    ) -> main_models.ReparseSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.reparse_source_with_options(request, headers, runtime)

    async def reparse_source_async(
        self,
        request: main_models.ReparseSourceRequest,
    ) -> main_models.ReparseSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.reparse_source_with_options_async(request, headers, runtime)

    def replace_knowledge_base_source_file_with_options(
        self,
        request: main_models.ReplaceKnowledgeBaseSourceFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceKnowledgeBaseSourceFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_path):
            body['filePath'] = request.file_path
        if not DaraCore.is_null(request.file_public_url):
            body['filePublicUrl'] = request.file_public_url
        if not DaraCore.is_null(request.file_record_id):
            body['fileRecordId'] = request.file_record_id
        if not DaraCore.is_null(request.force_sync):
            body['forceSync'] = request.force_sync
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceKnowledgeBaseSourceFile',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/replaceKnowledgeBaseSourceFile',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceKnowledgeBaseSourceFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_knowledge_base_source_file_with_options_async(
        self,
        request: main_models.ReplaceKnowledgeBaseSourceFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceKnowledgeBaseSourceFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_path):
            body['filePath'] = request.file_path
        if not DaraCore.is_null(request.file_public_url):
            body['filePublicUrl'] = request.file_public_url
        if not DaraCore.is_null(request.file_record_id):
            body['fileRecordId'] = request.file_record_id
        if not DaraCore.is_null(request.force_sync):
            body['forceSync'] = request.force_sync
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceKnowledgeBaseSourceFile',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/replaceKnowledgeBaseSourceFile',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceKnowledgeBaseSourceFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_knowledge_base_source_file(
        self,
        request: main_models.ReplaceKnowledgeBaseSourceFileRequest,
    ) -> main_models.ReplaceKnowledgeBaseSourceFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.replace_knowledge_base_source_file_with_options(request, headers, runtime)

    async def replace_knowledge_base_source_file_async(
        self,
        request: main_models.ReplaceKnowledgeBaseSourceFileRequest,
    ) -> main_models.ReplaceKnowledgeBaseSourceFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.replace_knowledge_base_source_file_with_options_async(request, headers, runtime)

    def replace_object_bindings_with_options(
        self,
        tmp_req: main_models.ReplaceObjectBindingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceObjectBindingsResponse:
        tmp_req.validate()
        request = main_models.ReplaceObjectBindingsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.object_bindings):
            request.object_bindings_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_bindings, 'objectBindings', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.object_bindings_shrink):
            body['objectBindings'] = request.object_bindings_shrink
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceObjectBindings',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/replaceObjectBindings',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceObjectBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_object_bindings_with_options_async(
        self,
        tmp_req: main_models.ReplaceObjectBindingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceObjectBindingsResponse:
        tmp_req.validate()
        request = main_models.ReplaceObjectBindingsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.object_bindings):
            request.object_bindings_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_bindings, 'objectBindings', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.object_bindings_shrink):
            body['objectBindings'] = request.object_bindings_shrink
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceObjectBindings',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/replaceObjectBindings',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceObjectBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_object_bindings(
        self,
        request: main_models.ReplaceObjectBindingsRequest,
    ) -> main_models.ReplaceObjectBindingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.replace_object_bindings_with_options(request, headers, runtime)

    async def replace_object_bindings_async(
        self,
        request: main_models.ReplaceObjectBindingsRequest,
    ) -> main_models.ReplaceObjectBindingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.replace_object_bindings_with_options_async(request, headers, runtime)

    def replace_source_file_with_options(
        self,
        request: main_models.ReplaceSourceFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceSourceFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_path):
            body['filePath'] = request.file_path
        if not DaraCore.is_null(request.file_public_url):
            body['filePublicUrl'] = request.file_public_url
        if not DaraCore.is_null(request.file_record_id):
            body['fileRecordId'] = request.file_record_id
        if not DaraCore.is_null(request.force_sync):
            body['forceSync'] = request.force_sync
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceSourceFile',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/replaceSourceFile',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceSourceFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_source_file_with_options_async(
        self,
        request: main_models.ReplaceSourceFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceSourceFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_path):
            body['filePath'] = request.file_path
        if not DaraCore.is_null(request.file_public_url):
            body['filePublicUrl'] = request.file_public_url
        if not DaraCore.is_null(request.file_record_id):
            body['fileRecordId'] = request.file_record_id
        if not DaraCore.is_null(request.force_sync):
            body['forceSync'] = request.force_sync
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceSourceFile',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/replaceSourceFile',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceSourceFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_source_file(
        self,
        request: main_models.ReplaceSourceFileRequest,
    ) -> main_models.ReplaceSourceFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.replace_source_file_with_options(request, headers, runtime)

    async def replace_source_file_async(
        self,
        request: main_models.ReplaceSourceFileRequest,
    ) -> main_models.ReplaceSourceFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.replace_source_file_with_options_async(request, headers, runtime)

    def reset_password_with_options(
        self,
        request: main_models.ResetPasswordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.password_encrypted):
            body['passwordEncrypted'] = request.password_encrypted
        if not DaraCore.is_null(request.wn_user_id):
            body['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetPassword',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/resetPassword',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_password_with_options_async(
        self,
        request: main_models.ResetPasswordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.password_encrypted):
            body['passwordEncrypted'] = request.password_encrypted
        if not DaraCore.is_null(request.wn_user_id):
            body['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetPassword',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/resetPassword',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_password(
        self,
        request: main_models.ResetPasswordRequest,
    ) -> main_models.ResetPasswordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.reset_password_with_options(request, headers, runtime)

    async def reset_password_async(
        self,
        request: main_models.ResetPasswordRequest,
    ) -> main_models.ResetPasswordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.reset_password_with_options_async(request, headers, runtime)

    def reset_token_with_options(
        self,
        request: main_models.ResetTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.wn_user_id):
            body['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetToken',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/resetToken',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_token_with_options_async(
        self,
        request: main_models.ResetTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.wn_user_id):
            body['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetToken',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/resetToken',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_token(
        self,
        request: main_models.ResetTokenRequest,
    ) -> main_models.ResetTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.reset_token_with_options(request, headers, runtime)

    async def reset_token_async(
        self,
        request: main_models.ResetTokenRequest,
    ) -> main_models.ResetTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.reset_token_with_options_async(request, headers, runtime)

    def retry_directory_failed_sources_with_options(
        self,
        request: main_models.RetryDirectoryFailedSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RetryDirectoryFailedSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RetryDirectoryFailedSources',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/retryDirectoryFailedSources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryDirectoryFailedSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_directory_failed_sources_with_options_async(
        self,
        request: main_models.RetryDirectoryFailedSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RetryDirectoryFailedSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RetryDirectoryFailedSources',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/retryDirectoryFailedSources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryDirectoryFailedSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_directory_failed_sources(
        self,
        request: main_models.RetryDirectoryFailedSourcesRequest,
    ) -> main_models.RetryDirectoryFailedSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.retry_directory_failed_sources_with_options(request, headers, runtime)

    async def retry_directory_failed_sources_async(
        self,
        request: main_models.RetryDirectoryFailedSourcesRequest,
    ) -> main_models.RetryDirectoryFailedSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.retry_directory_failed_sources_with_options_async(request, headers, runtime)

    def retry_knowledge_base_failed_sources_with_options(
        self,
        request: main_models.RetryKnowledgeBaseFailedSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RetryKnowledgeBaseFailedSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RetryKnowledgeBaseFailedSources',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/retryKnowledgeBaseFailedSources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryKnowledgeBaseFailedSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_knowledge_base_failed_sources_with_options_async(
        self,
        request: main_models.RetryKnowledgeBaseFailedSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RetryKnowledgeBaseFailedSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RetryKnowledgeBaseFailedSources',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/retryKnowledgeBaseFailedSources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryKnowledgeBaseFailedSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_knowledge_base_failed_sources(
        self,
        request: main_models.RetryKnowledgeBaseFailedSourcesRequest,
    ) -> main_models.RetryKnowledgeBaseFailedSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.retry_knowledge_base_failed_sources_with_options(request, headers, runtime)

    async def retry_knowledge_base_failed_sources_async(
        self,
        request: main_models.RetryKnowledgeBaseFailedSourcesRequest,
    ) -> main_models.RetryKnowledgeBaseFailedSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.retry_knowledge_base_failed_sources_with_options_async(request, headers, runtime)

    def revoke_agent_users_with_options(
        self,
        tmp_req: main_models.RevokeAgentUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeAgentUsersResponse:
        tmp_req.validate()
        request = main_models.RevokeAgentUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_group_ids):
            request.user_group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_group_ids, 'userGroupIds', 'json')
        if not DaraCore.is_null(tmp_req.user_ids):
            request.user_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_ids, 'userIds', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.user_group_ids_shrink):
            body['userGroupIds'] = request.user_group_ids_shrink
        if not DaraCore.is_null(request.user_ids_shrink):
            body['userIds'] = request.user_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeAgentUsers',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/revokeAgentUsers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeAgentUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_agent_users_with_options_async(
        self,
        tmp_req: main_models.RevokeAgentUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeAgentUsersResponse:
        tmp_req.validate()
        request = main_models.RevokeAgentUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_group_ids):
            request.user_group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_group_ids, 'userGroupIds', 'json')
        if not DaraCore.is_null(tmp_req.user_ids):
            request.user_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_ids, 'userIds', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.user_group_ids_shrink):
            body['userGroupIds'] = request.user_group_ids_shrink
        if not DaraCore.is_null(request.user_ids_shrink):
            body['userIds'] = request.user_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeAgentUsers',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/revokeAgentUsers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeAgentUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_agent_users(
        self,
        request: main_models.RevokeAgentUsersRequest,
    ) -> main_models.RevokeAgentUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.revoke_agent_users_with_options(request, headers, runtime)

    async def revoke_agent_users_async(
        self,
        request: main_models.RevokeAgentUsersRequest,
    ) -> main_models.RevokeAgentUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.revoke_agent_users_with_options_async(request, headers, runtime)

    def run_skill_with_options(
        self,
        tmp_req: main_models.RunSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunSkillResponse:
        tmp_req.validate()
        request = main_models.RunSkillShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.arguments):
            request.arguments_shrink = Utils.array_to_string_with_specified_style(tmp_req.arguments, 'arguments', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.arguments_shrink):
            body['arguments'] = request.arguments_shrink
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.skill_code):
            body['skillCode'] = request.skill_code
        if not DaraCore.is_null(request.skill_name):
            body['skillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSkill',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/runSkill',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_skill_with_options_async(
        self,
        tmp_req: main_models.RunSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunSkillResponse:
        tmp_req.validate()
        request = main_models.RunSkillShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.arguments):
            request.arguments_shrink = Utils.array_to_string_with_specified_style(tmp_req.arguments, 'arguments', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.arguments_shrink):
            body['arguments'] = request.arguments_shrink
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        if not DaraCore.is_null(request.skill_code):
            body['skillCode'] = request.skill_code
        if not DaraCore.is_null(request.skill_name):
            body['skillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSkill',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/runSkill',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_skill(
        self,
        request: main_models.RunSkillRequest,
    ) -> main_models.RunSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_skill_with_options(request, headers, runtime)

    async def run_skill_async(
        self,
        request: main_models.RunSkillRequest,
    ) -> main_models.RunSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_skill_with_options_async(request, headers, runtime)

    def save_output_file_to_resource_with_options(
        self,
        tmp_req: main_models.SaveOutputFileToResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SaveOutputFileToResourceResponse:
        tmp_req.validate()
        request = main_models.SaveOutputFileToResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.item_ids):
            request.item_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.item_ids, 'itemIds', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.item_ids_shrink):
            body['itemIds'] = request.item_ids_shrink
        if not DaraCore.is_null(request.mode):
            body['mode'] = request.mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveOutputFileToResource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/saveOutputFileToResource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveOutputFileToResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_output_file_to_resource_with_options_async(
        self,
        tmp_req: main_models.SaveOutputFileToResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SaveOutputFileToResourceResponse:
        tmp_req.validate()
        request = main_models.SaveOutputFileToResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.item_ids):
            request.item_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.item_ids, 'itemIds', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.item_ids_shrink):
            body['itemIds'] = request.item_ids_shrink
        if not DaraCore.is_null(request.mode):
            body['mode'] = request.mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveOutputFileToResource',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/saveOutputFileToResource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveOutputFileToResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_output_file_to_resource(
        self,
        request: main_models.SaveOutputFileToResourceRequest,
    ) -> main_models.SaveOutputFileToResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.save_output_file_to_resource_with_options(request, headers, runtime)

    async def save_output_file_to_resource_async(
        self,
        request: main_models.SaveOutputFileToResourceRequest,
    ) -> main_models.SaveOutputFileToResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.save_output_file_to_resource_with_options_async(request, headers, runtime)

    def send_async_chat_message_with_options(
        self,
        tmp_req: main_models.SendAsyncChatMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendAsyncChatMessageResponse:
        tmp_req.validate()
        request = main_models.SendAsyncChatMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.digital_employee_name):
            request.digital_employee_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.digital_employee_name, 'digitalEmployeeName', 'json')
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'files', 'json')
        if not DaraCore.is_null(tmp_req.task_execution):
            request.task_execution_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_execution, 'taskExecution', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.content_type):
            body['contentType'] = request.content_type
        if not DaraCore.is_null(request.digital_employee_name_shrink):
            body['digitalEmployeeName'] = request.digital_employee_name_shrink
        if not DaraCore.is_null(request.direct_chat):
            body['directChat'] = request.direct_chat
        if not DaraCore.is_null(request.files_shrink):
            body['files'] = request.files_shrink
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.reuse_last_session):
            body['reuseLastSession'] = request.reuse_last_session
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.task_execution_shrink):
            body['taskExecution'] = request.task_execution_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendAsyncChatMessage',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/sendAsyncChatMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendAsyncChatMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_async_chat_message_with_options_async(
        self,
        tmp_req: main_models.SendAsyncChatMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendAsyncChatMessageResponse:
        tmp_req.validate()
        request = main_models.SendAsyncChatMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.digital_employee_name):
            request.digital_employee_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.digital_employee_name, 'digitalEmployeeName', 'json')
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'files', 'json')
        if not DaraCore.is_null(tmp_req.task_execution):
            request.task_execution_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_execution, 'taskExecution', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.content_type):
            body['contentType'] = request.content_type
        if not DaraCore.is_null(request.digital_employee_name_shrink):
            body['digitalEmployeeName'] = request.digital_employee_name_shrink
        if not DaraCore.is_null(request.direct_chat):
            body['directChat'] = request.direct_chat
        if not DaraCore.is_null(request.files_shrink):
            body['files'] = request.files_shrink
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.reuse_last_session):
            body['reuseLastSession'] = request.reuse_last_session
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.task_execution_shrink):
            body['taskExecution'] = request.task_execution_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendAsyncChatMessage',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/sendAsyncChatMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendAsyncChatMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_async_chat_message(
        self,
        request: main_models.SendAsyncChatMessageRequest,
    ) -> main_models.SendAsyncChatMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.send_async_chat_message_with_options(request, headers, runtime)

    async def send_async_chat_message_async(
        self,
        request: main_models.SendAsyncChatMessageRequest,
    ) -> main_models.SendAsyncChatMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.send_async_chat_message_with_options_async(request, headers, runtime)

    def send_chat_message_with_sse(
        self,
        tmp_req: main_models.SendChatMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.SendChatMessageResponse, None, None]:
        tmp_req.validate()
        request = main_models.SendChatMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.digital_employee_name):
            request.digital_employee_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.digital_employee_name, 'digitalEmployeeName', 'json')
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'files', 'json')
        if not DaraCore.is_null(tmp_req.task_execution):
            request.task_execution_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_execution, 'taskExecution', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.content_type):
            body['contentType'] = request.content_type
        if not DaraCore.is_null(request.digital_employee_name_shrink):
            body['digitalEmployeeName'] = request.digital_employee_name_shrink
        if not DaraCore.is_null(request.direct_chat):
            body['directChat'] = request.direct_chat
        if not DaraCore.is_null(request.files_shrink):
            body['files'] = request.files_shrink
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.reuse_last_session):
            body['reuseLastSession'] = request.reuse_last_session
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.task_execution_shrink):
            body['taskExecution'] = request.task_execution_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendChatMessage',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/sendChatMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.SendChatMessageResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def send_chat_message_with_sse_async(
        self,
        tmp_req: main_models.SendChatMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.SendChatMessageResponse, None, None]:
        tmp_req.validate()
        request = main_models.SendChatMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.digital_employee_name):
            request.digital_employee_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.digital_employee_name, 'digitalEmployeeName', 'json')
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'files', 'json')
        if not DaraCore.is_null(tmp_req.task_execution):
            request.task_execution_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_execution, 'taskExecution', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.content_type):
            body['contentType'] = request.content_type
        if not DaraCore.is_null(request.digital_employee_name_shrink):
            body['digitalEmployeeName'] = request.digital_employee_name_shrink
        if not DaraCore.is_null(request.direct_chat):
            body['directChat'] = request.direct_chat
        if not DaraCore.is_null(request.files_shrink):
            body['files'] = request.files_shrink
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.reuse_last_session):
            body['reuseLastSession'] = request.reuse_last_session
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.task_execution_shrink):
            body['taskExecution'] = request.task_execution_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendChatMessage',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/sendChatMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.SendChatMessageResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def send_chat_message_with_options(
        self,
        tmp_req: main_models.SendChatMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendChatMessageResponse:
        tmp_req.validate()
        request = main_models.SendChatMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.digital_employee_name):
            request.digital_employee_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.digital_employee_name, 'digitalEmployeeName', 'json')
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'files', 'json')
        if not DaraCore.is_null(tmp_req.task_execution):
            request.task_execution_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_execution, 'taskExecution', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.content_type):
            body['contentType'] = request.content_type
        if not DaraCore.is_null(request.digital_employee_name_shrink):
            body['digitalEmployeeName'] = request.digital_employee_name_shrink
        if not DaraCore.is_null(request.direct_chat):
            body['directChat'] = request.direct_chat
        if not DaraCore.is_null(request.files_shrink):
            body['files'] = request.files_shrink
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.reuse_last_session):
            body['reuseLastSession'] = request.reuse_last_session
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.task_execution_shrink):
            body['taskExecution'] = request.task_execution_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendChatMessage',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/sendChatMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendChatMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_chat_message_with_options_async(
        self,
        tmp_req: main_models.SendChatMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendChatMessageResponse:
        tmp_req.validate()
        request = main_models.SendChatMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.digital_employee_name):
            request.digital_employee_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.digital_employee_name, 'digitalEmployeeName', 'json')
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'files', 'json')
        if not DaraCore.is_null(tmp_req.task_execution):
            request.task_execution_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_execution, 'taskExecution', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.content_type):
            body['contentType'] = request.content_type
        if not DaraCore.is_null(request.digital_employee_name_shrink):
            body['digitalEmployeeName'] = request.digital_employee_name_shrink
        if not DaraCore.is_null(request.direct_chat):
            body['directChat'] = request.direct_chat
        if not DaraCore.is_null(request.files_shrink):
            body['files'] = request.files_shrink
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.reuse_last_session):
            body['reuseLastSession'] = request.reuse_last_session
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.task_execution_shrink):
            body['taskExecution'] = request.task_execution_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendChatMessage',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/sendChatMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendChatMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_chat_message(
        self,
        request: main_models.SendChatMessageRequest,
    ) -> main_models.SendChatMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.send_chat_message_with_options(request, headers, runtime)

    async def send_chat_message_async(
        self,
        request: main_models.SendChatMessageRequest,
    ) -> main_models.SendChatMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.send_chat_message_with_options_async(request, headers, runtime)

    def stop_chat_message_with_options(
        self,
        request: main_models.StopChatMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopChatMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopChatMessage',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/stopChatMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopChatMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_chat_message_with_options_async(
        self,
        request: main_models.StopChatMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopChatMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopChatMessage',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/stopChatMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopChatMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_chat_message(
        self,
        request: main_models.StopChatMessageRequest,
    ) -> main_models.StopChatMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_chat_message_with_options(request, headers, runtime)

    async def stop_chat_message_async(
        self,
        request: main_models.StopChatMessageRequest,
    ) -> main_models.StopChatMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_chat_message_with_options_async(request, headers, runtime)

    def stream_chat_message_with_sse(
        self,
        message_id: str,
        request: main_models.StreamChatMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.StreamChatMessageResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.last_event_id):
            query['lastEventId'] = request.last_event_id
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StreamChatMessage',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/streamChatMessage/{DaraURL.percent_encode(message_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.StreamChatMessageResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def stream_chat_message_with_sse_async(
        self,
        message_id: str,
        request: main_models.StreamChatMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.StreamChatMessageResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.last_event_id):
            query['lastEventId'] = request.last_event_id
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StreamChatMessage',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/streamChatMessage/{DaraURL.percent_encode(message_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.StreamChatMessageResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def stream_chat_message_with_options(
        self,
        message_id: str,
        request: main_models.StreamChatMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StreamChatMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.last_event_id):
            query['lastEventId'] = request.last_event_id
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StreamChatMessage',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/streamChatMessage/{DaraURL.percent_encode(message_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StreamChatMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def stream_chat_message_with_options_async(
        self,
        message_id: str,
        request: main_models.StreamChatMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StreamChatMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.last_event_id):
            query['lastEventId'] = request.last_event_id
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StreamChatMessage',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/streamChatMessage/{DaraURL.percent_encode(message_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StreamChatMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stream_chat_message(
        self,
        message_id: str,
        request: main_models.StreamChatMessageRequest,
    ) -> main_models.StreamChatMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stream_chat_message_with_options(message_id, request, headers, runtime)

    async def stream_chat_message_async(
        self,
        message_id: str,
        request: main_models.StreamChatMessageRequest,
    ) -> main_models.StreamChatMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stream_chat_message_with_options_async(message_id, request, headers, runtime)

    def sync_org_structure_with_options(
        self,
        tmp_req: main_models.SyncOrgStructureRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SyncOrgStructureResponse:
        tmp_req.validate()
        request = main_models.SyncOrgStructureShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.departments):
            request.departments_shrink = Utils.array_to_string_with_specified_style(tmp_req.departments, 'departments', 'json')
        if not DaraCore.is_null(tmp_req.members):
            request.members_shrink = Utils.array_to_string_with_specified_style(tmp_req.members, 'members', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.corp_id):
            body['corpId'] = request.corp_id
        if not DaraCore.is_null(request.departments_shrink):
            body['departments'] = request.departments_shrink
        if not DaraCore.is_null(request.members_shrink):
            body['members'] = request.members_shrink
        if not DaraCore.is_null(request.platform_type):
            body['platformType'] = request.platform_type
        if not DaraCore.is_null(request.sso_settings_id):
            body['ssoSettingsId'] = request.sso_settings_id
        if not DaraCore.is_null(request.sync_members):
            body['syncMembers'] = request.sync_members
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncOrgStructure',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/syncOrgStructure',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncOrgStructureResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_org_structure_with_options_async(
        self,
        tmp_req: main_models.SyncOrgStructureRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SyncOrgStructureResponse:
        tmp_req.validate()
        request = main_models.SyncOrgStructureShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.departments):
            request.departments_shrink = Utils.array_to_string_with_specified_style(tmp_req.departments, 'departments', 'json')
        if not DaraCore.is_null(tmp_req.members):
            request.members_shrink = Utils.array_to_string_with_specified_style(tmp_req.members, 'members', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.corp_id):
            body['corpId'] = request.corp_id
        if not DaraCore.is_null(request.departments_shrink):
            body['departments'] = request.departments_shrink
        if not DaraCore.is_null(request.members_shrink):
            body['members'] = request.members_shrink
        if not DaraCore.is_null(request.platform_type):
            body['platformType'] = request.platform_type
        if not DaraCore.is_null(request.sso_settings_id):
            body['ssoSettingsId'] = request.sso_settings_id
        if not DaraCore.is_null(request.sync_members):
            body['syncMembers'] = request.sync_members
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncOrgStructure',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/syncOrgStructure',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncOrgStructureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_org_structure(
        self,
        request: main_models.SyncOrgStructureRequest,
    ) -> main_models.SyncOrgStructureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.sync_org_structure_with_options(request, headers, runtime)

    async def sync_org_structure_async(
        self,
        request: main_models.SyncOrgStructureRequest,
    ) -> main_models.SyncOrgStructureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.sync_org_structure_with_options_async(request, headers, runtime)

    def toggle_primary_object_favorite_with_options(
        self,
        tmp_req: main_models.TogglePrimaryObjectFavoriteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TogglePrimaryObjectFavoriteResponse:
        tmp_req.validate()
        request = main_models.TogglePrimaryObjectFavoriteShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.object_ids):
            request.object_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_ids, 'objectIds', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.object_ids_shrink):
            body['objectIds'] = request.object_ids_shrink
        if not DaraCore.is_null(request.object_type):
            body['objectType'] = request.object_type
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TogglePrimaryObjectFavorite',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/togglePrimaryObjectFavorite',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TogglePrimaryObjectFavoriteResponse(),
            self.call_api(params, req, runtime)
        )

    async def toggle_primary_object_favorite_with_options_async(
        self,
        tmp_req: main_models.TogglePrimaryObjectFavoriteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TogglePrimaryObjectFavoriteResponse:
        tmp_req.validate()
        request = main_models.TogglePrimaryObjectFavoriteShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.object_ids):
            request.object_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_ids, 'objectIds', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.object_ids_shrink):
            body['objectIds'] = request.object_ids_shrink
        if not DaraCore.is_null(request.object_type):
            body['objectType'] = request.object_type
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TogglePrimaryObjectFavorite',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/togglePrimaryObjectFavorite',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TogglePrimaryObjectFavoriteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def toggle_primary_object_favorite(
        self,
        request: main_models.TogglePrimaryObjectFavoriteRequest,
    ) -> main_models.TogglePrimaryObjectFavoriteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.toggle_primary_object_favorite_with_options(request, headers, runtime)

    async def toggle_primary_object_favorite_async(
        self,
        request: main_models.TogglePrimaryObjectFavoriteRequest,
    ) -> main_models.TogglePrimaryObjectFavoriteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.toggle_primary_object_favorite_with_options_async(request, headers, runtime)

    def update_agent_auth_mode_with_options(
        self,
        request: main_models.UpdateAgentAuthModeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentAuthModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.auth_mode):
            body['authMode'] = request.auth_mode
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentAuthMode',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateAgentAuthMode',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentAuthModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_auth_mode_with_options_async(
        self,
        request: main_models.UpdateAgentAuthModeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentAuthModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.auth_mode):
            body['authMode'] = request.auth_mode
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentAuthMode',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateAgentAuthMode',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentAuthModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent_auth_mode(
        self,
        request: main_models.UpdateAgentAuthModeRequest,
    ) -> main_models.UpdateAgentAuthModeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_agent_auth_mode_with_options(request, headers, runtime)

    async def update_agent_auth_mode_async(
        self,
        request: main_models.UpdateAgentAuthModeRequest,
    ) -> main_models.UpdateAgentAuthModeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_agent_auth_mode_with_options_async(request, headers, runtime)

    def update_chat_session_with_options(
        self,
        request: main_models.UpdateChatSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChatSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChatSession',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateChatSession',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChatSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_chat_session_with_options_async(
        self,
        request: main_models.UpdateChatSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChatSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChatSession',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateChatSession',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChatSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_chat_session(
        self,
        request: main_models.UpdateChatSessionRequest,
    ) -> main_models.UpdateChatSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_chat_session_with_options(request, headers, runtime)

    async def update_chat_session_async(
        self,
        request: main_models.UpdateChatSessionRequest,
    ) -> main_models.UpdateChatSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_chat_session_with_options_async(request, headers, runtime)

    def update_directory_with_options(
        self,
        request: main_models.UpdateDirectoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.parent_id):
            body['parentId'] = request.parent_id
        if not DaraCore.is_null(request.path):
            body['path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDirectory',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateDirectory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_directory_with_options_async(
        self,
        request: main_models.UpdateDirectoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.parent_id):
            body['parentId'] = request.parent_id
        if not DaraCore.is_null(request.path):
            body['path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDirectory',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateDirectory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_directory(
        self,
        request: main_models.UpdateDirectoryRequest,
    ) -> main_models.UpdateDirectoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_directory_with_options(request, headers, runtime)

    async def update_directory_async(
        self,
        request: main_models.UpdateDirectoryRequest,
    ) -> main_models.UpdateDirectoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_directory_with_options_async(request, headers, runtime)

    def update_knowledge_base_directory_with_options(
        self,
        request: main_models.UpdateKnowledgeBaseDirectoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKnowledgeBaseDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.parent_directory_id):
            body['parentDirectoryId'] = request.parent_directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKnowledgeBaseDirectory',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateKnowledgeBaseDirectory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKnowledgeBaseDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_knowledge_base_directory_with_options_async(
        self,
        request: main_models.UpdateKnowledgeBaseDirectoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKnowledgeBaseDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.parent_directory_id):
            body['parentDirectoryId'] = request.parent_directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKnowledgeBaseDirectory',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateKnowledgeBaseDirectory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKnowledgeBaseDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_knowledge_base_directory(
        self,
        request: main_models.UpdateKnowledgeBaseDirectoryRequest,
    ) -> main_models.UpdateKnowledgeBaseDirectoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_knowledge_base_directory_with_options(request, headers, runtime)

    async def update_knowledge_base_directory_async(
        self,
        request: main_models.UpdateKnowledgeBaseDirectoryRequest,
    ) -> main_models.UpdateKnowledgeBaseDirectoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_knowledge_base_directory_with_options_async(request, headers, runtime)

    def update_knowledge_base_source_content_with_options(
        self,
        request: main_models.UpdateKnowledgeBaseSourceContentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKnowledgeBaseSourceContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.force_sync):
            body['forceSync'] = request.force_sync
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKnowledgeBaseSourceContent',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateKnowledgeBaseSourceContent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKnowledgeBaseSourceContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_knowledge_base_source_content_with_options_async(
        self,
        request: main_models.UpdateKnowledgeBaseSourceContentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKnowledgeBaseSourceContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.force_sync):
            body['forceSync'] = request.force_sync
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKnowledgeBaseSourceContent',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateKnowledgeBaseSourceContent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKnowledgeBaseSourceContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_knowledge_base_source_content(
        self,
        request: main_models.UpdateKnowledgeBaseSourceContentRequest,
    ) -> main_models.UpdateKnowledgeBaseSourceContentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_knowledge_base_source_content_with_options(request, headers, runtime)

    async def update_knowledge_base_source_content_async(
        self,
        request: main_models.UpdateKnowledgeBaseSourceContentRequest,
    ) -> main_models.UpdateKnowledgeBaseSourceContentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_knowledge_base_source_content_with_options_async(request, headers, runtime)

    def update_knowledge_base_source_tags_with_options(
        self,
        request: main_models.UpdateKnowledgeBaseSourceTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKnowledgeBaseSourceTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        if not DaraCore.is_null(request.source_tags):
            body['sourceTags'] = request.source_tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKnowledgeBaseSourceTags',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateKnowledgeBaseSourceTags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKnowledgeBaseSourceTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_knowledge_base_source_tags_with_options_async(
        self,
        request: main_models.UpdateKnowledgeBaseSourceTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKnowledgeBaseSourceTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        if not DaraCore.is_null(request.source_tags):
            body['sourceTags'] = request.source_tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKnowledgeBaseSourceTags',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateKnowledgeBaseSourceTags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKnowledgeBaseSourceTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_knowledge_base_source_tags(
        self,
        request: main_models.UpdateKnowledgeBaseSourceTagsRequest,
    ) -> main_models.UpdateKnowledgeBaseSourceTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_knowledge_base_source_tags_with_options(request, headers, runtime)

    async def update_knowledge_base_source_tags_async(
        self,
        request: main_models.UpdateKnowledgeBaseSourceTagsRequest,
    ) -> main_models.UpdateKnowledgeBaseSourceTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_knowledge_base_source_tags_with_options_async(request, headers, runtime)

    def update_scheduled_task_with_options(
        self,
        tmp_req: main_models.UpdateScheduledTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateScheduledTaskResponse:
        tmp_req.validate()
        request = main_models.UpdateScheduledTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.description):
            request.description_shrink = Utils.array_to_string_with_specified_style(tmp_req.description, 'description', 'json')
        if not DaraCore.is_null(tmp_req.digital_employee_name):
            request.digital_employee_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.digital_employee_name, 'digitalEmployeeName', 'json')
        if not DaraCore.is_null(tmp_req.segments):
            request.segments_shrink = Utils.array_to_string_with_specified_style(tmp_req.segments, 'segments', 'json')
        if not DaraCore.is_null(tmp_req.task_detail):
            request.task_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_detail, 'taskDetail', 'json')
        if not DaraCore.is_null(tmp_req.trigger_config):
            request.trigger_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger_config, 'triggerConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description_shrink):
            body['description'] = request.description_shrink
        if not DaraCore.is_null(request.digital_employee_name_shrink):
            body['digitalEmployeeName'] = request.digital_employee_name_shrink
        if not DaraCore.is_null(request.is_open):
            body['isOpen'] = request.is_open
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.segments_shrink):
            body['segments'] = request.segments_shrink
        if not DaraCore.is_null(request.task_detail_shrink):
            body['taskDetail'] = request.task_detail_shrink
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.trigger_config_shrink):
            body['triggerConfig'] = request.trigger_config_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScheduledTask',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateScheduledTask',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scheduled_task_with_options_async(
        self,
        tmp_req: main_models.UpdateScheduledTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateScheduledTaskResponse:
        tmp_req.validate()
        request = main_models.UpdateScheduledTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.description):
            request.description_shrink = Utils.array_to_string_with_specified_style(tmp_req.description, 'description', 'json')
        if not DaraCore.is_null(tmp_req.digital_employee_name):
            request.digital_employee_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.digital_employee_name, 'digitalEmployeeName', 'json')
        if not DaraCore.is_null(tmp_req.segments):
            request.segments_shrink = Utils.array_to_string_with_specified_style(tmp_req.segments, 'segments', 'json')
        if not DaraCore.is_null(tmp_req.task_detail):
            request.task_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_detail, 'taskDetail', 'json')
        if not DaraCore.is_null(tmp_req.trigger_config):
            request.trigger_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.trigger_config, 'triggerConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description_shrink):
            body['description'] = request.description_shrink
        if not DaraCore.is_null(request.digital_employee_name_shrink):
            body['digitalEmployeeName'] = request.digital_employee_name_shrink
        if not DaraCore.is_null(request.is_open):
            body['isOpen'] = request.is_open
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.segments_shrink):
            body['segments'] = request.segments_shrink
        if not DaraCore.is_null(request.task_detail_shrink):
            body['taskDetail'] = request.task_detail_shrink
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.trigger_config_shrink):
            body['triggerConfig'] = request.trigger_config_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScheduledTask',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateScheduledTask',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scheduled_task(
        self,
        request: main_models.UpdateScheduledTaskRequest,
    ) -> main_models.UpdateScheduledTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_scheduled_task_with_options(request, headers, runtime)

    async def update_scheduled_task_async(
        self,
        request: main_models.UpdateScheduledTaskRequest,
    ) -> main_models.UpdateScheduledTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_scheduled_task_with_options_async(request, headers, runtime)

    def update_source_content_with_options(
        self,
        request: main_models.UpdateSourceContentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSourceContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.force_sync):
            body['forceSync'] = request.force_sync
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSourceContent',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateSourceContent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSourceContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_source_content_with_options_async(
        self,
        request: main_models.UpdateSourceContentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSourceContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.force_sync):
            body['forceSync'] = request.force_sync
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSourceContent',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateSourceContent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSourceContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_source_content(
        self,
        request: main_models.UpdateSourceContentRequest,
    ) -> main_models.UpdateSourceContentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_source_content_with_options(request, headers, runtime)

    async def update_source_content_async(
        self,
        request: main_models.UpdateSourceContentRequest,
    ) -> main_models.UpdateSourceContentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_source_content_with_options_async(request, headers, runtime)

    def update_tenant_directory_with_options(
        self,
        request: main_models.UpdateTenantDirectoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTenantDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.parent_id):
            body['parentId'] = request.parent_id
        if not DaraCore.is_null(request.path):
            body['path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTenantDirectory',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateTenantDirectory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTenantDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tenant_directory_with_options_async(
        self,
        request: main_models.UpdateTenantDirectoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTenantDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.parent_id):
            body['parentId'] = request.parent_id
        if not DaraCore.is_null(request.path):
            body['path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTenantDirectory',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateTenantDirectory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTenantDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_tenant_directory(
        self,
        request: main_models.UpdateTenantDirectoryRequest,
    ) -> main_models.UpdateTenantDirectoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_tenant_directory_with_options(request, headers, runtime)

    async def update_tenant_directory_async(
        self,
        request: main_models.UpdateTenantDirectoryRequest,
    ) -> main_models.UpdateTenantDirectoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_tenant_directory_with_options_async(request, headers, runtime)

    def update_user_with_options(
        self,
        tmp_req: main_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        tmp_req.validate()
        request = main_models.UpdateUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_codes):
            request.role_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_codes, 'roleCodes', 'json')
        if not DaraCore.is_null(tmp_req.user_group_ids):
            request.user_group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_group_ids, 'userGroupIds', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.is_active):
            body['isActive'] = request.is_active
        if not DaraCore.is_null(request.role_codes_shrink):
            body['roleCodes'] = request.role_codes_shrink
        if not DaraCore.is_null(request.user_group_ids_shrink):
            body['userGroupIds'] = request.user_group_ids_shrink
        if not DaraCore.is_null(request.wn_user_id):
            body['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateUser',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        tmp_req: main_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        tmp_req.validate()
        request = main_models.UpdateUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_codes):
            request.role_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_codes, 'roleCodes', 'json')
        if not DaraCore.is_null(tmp_req.user_group_ids):
            request.user_group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_group_ids, 'userGroupIds', 'json')
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.is_active):
            body['isActive'] = request.is_active
        if not DaraCore.is_null(request.role_codes_shrink):
            body['roleCodes'] = request.role_codes_shrink
        if not DaraCore.is_null(request.user_group_ids_shrink):
            body['userGroupIds'] = request.user_group_ids_shrink
        if not DaraCore.is_null(request.wn_user_id):
            body['wnUserId'] = request.wn_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateUser',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_user_with_options(request, headers, runtime)

    async def update_user_async(
        self,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_user_with_options_async(request, headers, runtime)

    def update_user_info_with_options(
        self,
        request: main_models.UpdateUserInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.avatar):
            body['avatar'] = request.avatar
        if not DaraCore.is_null(request.language_preference):
            body['languagePreference'] = request.language_preference
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.offering):
            body['offering'] = request.offering
        if not DaraCore.is_null(request.profile_role_info):
            body['profileRoleInfo'] = request.profile_role_info
        if not DaraCore.is_null(request.self_introduction):
            body['selfIntroduction'] = request.self_introduction
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserInfo',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateUserInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_info_with_options_async(
        self,
        request: main_models.UpdateUserInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.avatar):
            body['avatar'] = request.avatar
        if not DaraCore.is_null(request.language_preference):
            body['languagePreference'] = request.language_preference
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.offering):
            body['offering'] = request.offering
        if not DaraCore.is_null(request.profile_role_info):
            body['profileRoleInfo'] = request.profile_role_info
        if not DaraCore.is_null(request.self_introduction):
            body['selfIntroduction'] = request.self_introduction
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserInfo',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/updateUserInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_info(
        self,
        request: main_models.UpdateUserInfoRequest,
    ) -> main_models.UpdateUserInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_user_info_with_options(request, headers, runtime)

    async def update_user_info_async(
        self,
        request: main_models.UpdateUserInfoRequest,
    ) -> main_models.UpdateUserInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_user_info_with_options_async(request, headers, runtime)

    def upload_chat_file_with_options(
        self,
        request: main_models.UploadChatFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadChatFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.content_type):
            body['contentType'] = request.content_type
        if not DaraCore.is_null(request.file_name):
            body['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            body['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadChatFile',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/uploadChatFile',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadChatFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_chat_file_with_options_async(
        self,
        request: main_models.UploadChatFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadChatFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.content_type):
            body['contentType'] = request.content_type
        if not DaraCore.is_null(request.file_name):
            body['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            body['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.operating_object_name):
            body['operatingObjectName'] = request.operating_object_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadChatFile',
            version = '2026-05-12',
            protocol = 'HTTPS',
            pathname = f'/openapi/uploadChatFile',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadChatFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_chat_file(
        self,
        request: main_models.UploadChatFileRequest,
    ) -> main_models.UploadChatFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upload_chat_file_with_options(request, headers, runtime)

    async def upload_chat_file_async(
        self,
        request: main_models.UploadChatFileRequest,
    ) -> main_models.UploadChatFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upload_chat_file_with_options_async(request, headers, runtime)

    def upload_chat_file_advance(
        self,
        request: main_models.UploadChatFileAdvanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadChatFileResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'WinNexo',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        upload_chat_file_req = main_models.UploadChatFileRequest()
        Utils.convert(request, upload_chat_file_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type),
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            upload_chat_file_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        upload_chat_file_resp = self.upload_chat_file_with_options(upload_chat_file_req, headers, runtime)
        return upload_chat_file_resp

    async def upload_chat_file_advance_async(
        self,
        request: main_models.UploadChatFileAdvanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadChatFileResponse:
        # Step 0: init client
        if DaraCore.is_null(self._credential):
            raise open_api_exceptions.ClientException(
                code = 'InvalidCredentials',
                message = 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            )
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if DaraCore.is_null(open_platform_endpoint) or open_platform_endpoint == '':
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if DaraCore.is_null(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_util_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret,
            security_token = security_token,
            type = credential_type,
            endpoint = open_platform_endpoint,
            protocol = self._protocol,
            region_id = self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'WinNexo',
            'RegionId': self._region_id
        }
        auth_req = open_api_util_models.OpenApiRequest(
            query = Utils.query(auth_request)
        )
        auth_params = open_api_util_models.Params(
            action = 'AuthorizeFileUpload',
            version = '2019-12-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        auth_response = {}
        file_obj = FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        upload_chat_file_req = main_models.UploadChatFileRequest()
        Utils.convert(request, upload_chat_file_req)
        if not DaraCore.is_null(request.file_url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_url_object,
                content_type = ''
            )
            oss_header = {
                'host': Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type),
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            upload_chat_file_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        upload_chat_file_resp = await self.upload_chat_file_with_options_async(upload_chat_file_req, headers, runtime)
        return upload_chat_file_resp
