# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_realtranslationagent20260622 import models as main_models
from alibabacloud_tea_openapi import exceptions as open_api_exceptions
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore
from darabonba.core import DaraCore as DaraCore
from darabonba.exceptions import UnretryableException
from darabonba.policy.retry import RetryPolicyContext
from darabonba.request import DaraRequest
from darabonba.runtime import RuntimeOptions
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
        self._endpoint = self.get_endpoint('realtranslationagent', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_translation_task_with_options(
        self,
        request: main_models.CancelTranslationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelTranslationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apikey):
            query['APIKey'] = request.apikey
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelTranslationTask',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelTranslationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_translation_task_with_options_async(
        self,
        request: main_models.CancelTranslationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelTranslationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apikey):
            query['APIKey'] = request.apikey
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelTranslationTask',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelTranslationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_translation_task(
        self,
        request: main_models.CancelTranslationTaskRequest,
    ) -> main_models.CancelTranslationTaskResponse:
        runtime = RuntimeOptions()
        return self.cancel_translation_task_with_options(request, runtime)

    async def cancel_translation_task_async(
        self,
        request: main_models.CancelTranslationTaskRequest,
    ) -> main_models.CancelTranslationTaskResponse:
        runtime = RuntimeOptions()
        return await self.cancel_translation_task_with_options_async(request, runtime)

    def get_original_file_url_with_options(
        self,
        request: main_models.GetOriginalFileUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOriginalFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apikey):
            query['APIKey'] = request.apikey
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOriginalFileUrl',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOriginalFileUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_original_file_url_with_options_async(
        self,
        request: main_models.GetOriginalFileUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOriginalFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apikey):
            query['APIKey'] = request.apikey
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOriginalFileUrl',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOriginalFileUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_original_file_url(
        self,
        request: main_models.GetOriginalFileUrlRequest,
    ) -> main_models.GetOriginalFileUrlResponse:
        runtime = RuntimeOptions()
        return self.get_original_file_url_with_options(request, runtime)

    async def get_original_file_url_async(
        self,
        request: main_models.GetOriginalFileUrlRequest,
    ) -> main_models.GetOriginalFileUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_original_file_url_with_options_async(request, runtime)

    def get_translated_file_url_with_options(
        self,
        request: main_models.GetTranslatedFileUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTranslatedFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apikey):
            query['APIKey'] = request.apikey
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTranslatedFileUrl',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTranslatedFileUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_translated_file_url_with_options_async(
        self,
        request: main_models.GetTranslatedFileUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTranslatedFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apikey):
            query['APIKey'] = request.apikey
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTranslatedFileUrl',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTranslatedFileUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_translated_file_url(
        self,
        request: main_models.GetTranslatedFileUrlRequest,
    ) -> main_models.GetTranslatedFileUrlResponse:
        runtime = RuntimeOptions()
        return self.get_translated_file_url_with_options(request, runtime)

    async def get_translated_file_url_async(
        self,
        request: main_models.GetTranslatedFileUrlRequest,
    ) -> main_models.GetTranslatedFileUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_translated_file_url_with_options_async(request, runtime)

    def get_translation_task_with_options(
        self,
        request: main_models.GetTranslationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTranslationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apikey):
            query['APIKey'] = request.apikey
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTranslationTask',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTranslationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_translation_task_with_options_async(
        self,
        request: main_models.GetTranslationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTranslationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apikey):
            query['APIKey'] = request.apikey
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTranslationTask',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTranslationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_translation_task(
        self,
        request: main_models.GetTranslationTaskRequest,
    ) -> main_models.GetTranslationTaskResponse:
        runtime = RuntimeOptions()
        return self.get_translation_task_with_options(request, runtime)

    async def get_translation_task_async(
        self,
        request: main_models.GetTranslationTaskRequest,
    ) -> main_models.GetTranslationTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_translation_task_with_options_async(request, runtime)

    def list_translation_tasks_with_options(
        self,
        request: main_models.ListTranslationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTranslationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apikey):
            query['APIKey'] = request.apikey
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.original_file_name):
            query['OriginalFileName'] = request.original_file_name
        if not DaraCore.is_null(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.target_language):
            query['TargetLanguage'] = request.target_language
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTranslationTasks',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTranslationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_translation_tasks_with_options_async(
        self,
        request: main_models.ListTranslationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTranslationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apikey):
            query['APIKey'] = request.apikey
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.original_file_name):
            query['OriginalFileName'] = request.original_file_name
        if not DaraCore.is_null(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.target_language):
            query['TargetLanguage'] = request.target_language
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTranslationTasks',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTranslationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_translation_tasks(
        self,
        request: main_models.ListTranslationTasksRequest,
    ) -> main_models.ListTranslationTasksResponse:
        runtime = RuntimeOptions()
        return self.list_translation_tasks_with_options(request, runtime)

    async def list_translation_tasks_async(
        self,
        request: main_models.ListTranslationTasksRequest,
    ) -> main_models.ListTranslationTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_translation_tasks_with_options_async(request, runtime)

    def submit_translation_task_with_options(
        self,
        tmp_req: main_models.SubmitTranslationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTranslationTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitTranslationTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config):
            request.config_shrink = Utils.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        if not DaraCore.is_null(tmp_req.custom_terms):
            request.custom_terms_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_terms, 'CustomTerms', 'json')
        query = {}
        if not DaraCore.is_null(request.apikey):
            query['APIKey'] = request.apikey
        if not DaraCore.is_null(request.custom_terms_shrink):
            query['CustomTerms'] = request.custom_terms_shrink
        body = {}
        if not DaraCore.is_null(request.base_task_id):
            body['BaseTaskId'] = request.base_task_id
        if not DaraCore.is_null(request.config_shrink):
            body['Config'] = request.config_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTranslationTask',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTranslationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_translation_task_with_options_async(
        self,
        tmp_req: main_models.SubmitTranslationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTranslationTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitTranslationTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config):
            request.config_shrink = Utils.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        if not DaraCore.is_null(tmp_req.custom_terms):
            request.custom_terms_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_terms, 'CustomTerms', 'json')
        query = {}
        if not DaraCore.is_null(request.apikey):
            query['APIKey'] = request.apikey
        if not DaraCore.is_null(request.custom_terms_shrink):
            query['CustomTerms'] = request.custom_terms_shrink
        body = {}
        if not DaraCore.is_null(request.base_task_id):
            body['BaseTaskId'] = request.base_task_id
        if not DaraCore.is_null(request.config_shrink):
            body['Config'] = request.config_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTranslationTask',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTranslationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_translation_task(
        self,
        request: main_models.SubmitTranslationTaskRequest,
    ) -> main_models.SubmitTranslationTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_translation_task_with_options(request, runtime)

    async def submit_translation_task_async(
        self,
        request: main_models.SubmitTranslationTaskRequest,
    ) -> main_models.SubmitTranslationTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_translation_task_with_options_async(request, runtime)

    def upload_translation_file_with_options(
        self,
        request: main_models.UploadTranslationFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadTranslationFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apikey):
            query['APIKey'] = request.apikey
        if not DaraCore.is_null(request.file):
            query['File'] = request.file
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadTranslationFile',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadTranslationFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_translation_file_with_options_async(
        self,
        request: main_models.UploadTranslationFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadTranslationFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apikey):
            query['APIKey'] = request.apikey
        if not DaraCore.is_null(request.file):
            query['File'] = request.file
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadTranslationFile',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadTranslationFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_translation_file(
        self,
        request: main_models.UploadTranslationFileRequest,
    ) -> main_models.UploadTranslationFileResponse:
        runtime = RuntimeOptions()
        return self.upload_translation_file_with_options(request, runtime)

    async def upload_translation_file_async(
        self,
        request: main_models.UploadTranslationFileRequest,
    ) -> main_models.UploadTranslationFileResponse:
        runtime = RuntimeOptions()
        return await self.upload_translation_file_with_options_async(request, runtime)

    def upload_translation_file_advance(
        self,
        request: main_models.UploadTranslationFileAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadTranslationFileResponse:
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
            'Product': 'RealTranslationAgent',
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
        upload_translation_file_req = main_models.UploadTranslationFileRequest()
        Utils.convert(request, upload_translation_file_req)
        if not DaraCore.is_null(request.file_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_object,
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
            upload_translation_file_req.file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        upload_translation_file_resp = self.upload_translation_file_with_options(upload_translation_file_req, runtime)
        return upload_translation_file_resp

    async def upload_translation_file_advance_async(
        self,
        request: main_models.UploadTranslationFileAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadTranslationFileResponse:
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
            'Product': 'RealTranslationAgent',
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
        upload_translation_file_req = main_models.UploadTranslationFileRequest()
        Utils.convert(request, upload_translation_file_req)
        if not DaraCore.is_null(request.file_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.file_object,
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
            upload_translation_file_req.file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        upload_translation_file_resp = await self.upload_translation_file_with_options_async(upload_translation_file_req, runtime)
        return upload_translation_file_resp
