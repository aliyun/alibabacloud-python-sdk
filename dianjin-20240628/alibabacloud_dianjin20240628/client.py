# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_dianjin20240628 import models as main_models
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
        self._endpoint = self.get_endpoint('dianjin', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
                _request.protocol = 'HTTPS'
                _request.method = 'POST'
                _request.pathname = f'/'
                _request.headers = {
                    'host': str(form.get("host")),
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
                _request.protocol = 'HTTPS'
                _request.method = 'POST'
                _request.pathname = f'/'
                _request.headers = {
                    'host': str(form.get("host")),
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

    def create_annual_doc_summary_task_with_options(
        self,
        workspace_id: str,
        request: main_models.CreateAnnualDocSummaryTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnnualDocSummaryTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ana_years):
            body['anaYears'] = request.ana_years
        if not DaraCore.is_null(request.doc_infos):
            body['docInfos'] = request.doc_infos
        if not DaraCore.is_null(request.enable_table):
            body['enableTable'] = request.enable_table
        if not DaraCore.is_null(request.instruction):
            body['instruction'] = request.instruction
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnnualDocSummaryTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/summary/doc/annual',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAnnualDocSummaryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_annual_doc_summary_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreateAnnualDocSummaryTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnnualDocSummaryTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ana_years):
            body['anaYears'] = request.ana_years
        if not DaraCore.is_null(request.doc_infos):
            body['docInfos'] = request.doc_infos
        if not DaraCore.is_null(request.enable_table):
            body['enableTable'] = request.enable_table
        if not DaraCore.is_null(request.instruction):
            body['instruction'] = request.instruction
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnnualDocSummaryTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/summary/doc/annual',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAnnualDocSummaryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_annual_doc_summary_task(
        self,
        workspace_id: str,
        request: main_models.CreateAnnualDocSummaryTaskRequest,
    ) -> main_models.CreateAnnualDocSummaryTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_annual_doc_summary_task_with_options(workspace_id, request, headers, runtime)

    async def create_annual_doc_summary_task_async(
        self,
        workspace_id: str,
        request: main_models.CreateAnnualDocSummaryTaskRequest,
    ) -> main_models.CreateAnnualDocSummaryTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_annual_doc_summary_task_with_options_async(workspace_id, request, headers, runtime)

    def create_dialog_with_options(
        self,
        workspace_id: str,
        request: main_models.CreateDialogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDialogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel):
            body['channel'] = request.channel
        if not DaraCore.is_null(request.enable_library):
            body['enableLibrary'] = request.enable_library
        if not DaraCore.is_null(request.meta_data):
            body['metaData'] = request.meta_data
        if not DaraCore.is_null(request.play_code):
            body['playCode'] = request.play_code
        if not DaraCore.is_null(request.qa_library_list):
            body['qaLibraryList'] = request.qa_library_list
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.self_directed):
            body['selfDirected'] = request.self_directed
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDialog',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/dialog/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDialogResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dialog_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreateDialogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDialogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel):
            body['channel'] = request.channel
        if not DaraCore.is_null(request.enable_library):
            body['enableLibrary'] = request.enable_library
        if not DaraCore.is_null(request.meta_data):
            body['metaData'] = request.meta_data
        if not DaraCore.is_null(request.play_code):
            body['playCode'] = request.play_code
        if not DaraCore.is_null(request.qa_library_list):
            body['qaLibraryList'] = request.qa_library_list
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.self_directed):
            body['selfDirected'] = request.self_directed
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDialog',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/dialog/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDialogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dialog(
        self,
        workspace_id: str,
        request: main_models.CreateDialogRequest,
    ) -> main_models.CreateDialogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_dialog_with_options(workspace_id, request, headers, runtime)

    async def create_dialog_async(
        self,
        workspace_id: str,
        request: main_models.CreateDialogRequest,
    ) -> main_models.CreateDialogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_dialog_with_options_async(workspace_id, request, headers, runtime)

    def create_dialog_analysis_task_with_options(
        self,
        workspace_id: str,
        request: main_models.CreateDialogAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDialogAnalysisTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.analysis_nodes):
            body['analysisNodes'] = request.analysis_nodes
        if not DaraCore.is_null(request.conversation_list):
            body['conversationList'] = request.conversation_list
        if not DaraCore.is_null(request.meta_data):
            body['metaData'] = request.meta_data
        if not DaraCore.is_null(request.play_code):
            body['playCode'] = request.play_code
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDialogAnalysisTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/dialog/analysis/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDialogAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dialog_analysis_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreateDialogAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDialogAnalysisTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.analysis_nodes):
            body['analysisNodes'] = request.analysis_nodes
        if not DaraCore.is_null(request.conversation_list):
            body['conversationList'] = request.conversation_list
        if not DaraCore.is_null(request.meta_data):
            body['metaData'] = request.meta_data
        if not DaraCore.is_null(request.play_code):
            body['playCode'] = request.play_code
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDialogAnalysisTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/dialog/analysis/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDialogAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dialog_analysis_task(
        self,
        workspace_id: str,
        request: main_models.CreateDialogAnalysisTaskRequest,
    ) -> main_models.CreateDialogAnalysisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_dialog_analysis_task_with_options(workspace_id, request, headers, runtime)

    async def create_dialog_analysis_task_async(
        self,
        workspace_id: str,
        request: main_models.CreateDialogAnalysisTaskRequest,
    ) -> main_models.CreateDialogAnalysisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_dialog_analysis_task_with_options_async(workspace_id, request, headers, runtime)

    def create_docs_summary_task_with_options(
        self,
        workspace_id: str,
        request: main_models.CreateDocsSummaryTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDocsSummaryTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_infos):
            body['docInfos'] = request.doc_infos
        if not DaraCore.is_null(request.enable_table):
            body['enableTable'] = request.enable_table
        if not DaraCore.is_null(request.instruction):
            body['instruction'] = request.instruction
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDocsSummaryTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/summary/docs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDocsSummaryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_docs_summary_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreateDocsSummaryTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDocsSummaryTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_infos):
            body['docInfos'] = request.doc_infos
        if not DaraCore.is_null(request.enable_table):
            body['enableTable'] = request.enable_table
        if not DaraCore.is_null(request.instruction):
            body['instruction'] = request.instruction
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDocsSummaryTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/summary/docs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDocsSummaryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_docs_summary_task(
        self,
        workspace_id: str,
        request: main_models.CreateDocsSummaryTaskRequest,
    ) -> main_models.CreateDocsSummaryTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_docs_summary_task_with_options(workspace_id, request, headers, runtime)

    async def create_docs_summary_task_async(
        self,
        workspace_id: str,
        request: main_models.CreateDocsSummaryTaskRequest,
    ) -> main_models.CreateDocsSummaryTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_docs_summary_task_with_options_async(workspace_id, request, headers, runtime)

    def create_fin_report_summary_task_with_options(
        self,
        workspace_id: str,
        request: main_models.CreateFinReportSummaryTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFinReportSummaryTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['docId'] = request.doc_id
        if not DaraCore.is_null(request.enable_table):
            body['enableTable'] = request.enable_table
        if not DaraCore.is_null(request.end_page):
            body['endPage'] = request.end_page
        if not DaraCore.is_null(request.instruction):
            body['instruction'] = request.instruction
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.start_page):
            body['startPage'] = request.start_page
        if not DaraCore.is_null(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFinReportSummaryTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/summary',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFinReportSummaryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fin_report_summary_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreateFinReportSummaryTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFinReportSummaryTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['docId'] = request.doc_id
        if not DaraCore.is_null(request.enable_table):
            body['enableTable'] = request.enable_table
        if not DaraCore.is_null(request.end_page):
            body['endPage'] = request.end_page
        if not DaraCore.is_null(request.instruction):
            body['instruction'] = request.instruction
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.start_page):
            body['startPage'] = request.start_page
        if not DaraCore.is_null(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFinReportSummaryTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/summary',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFinReportSummaryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fin_report_summary_task(
        self,
        workspace_id: str,
        request: main_models.CreateFinReportSummaryTaskRequest,
    ) -> main_models.CreateFinReportSummaryTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_fin_report_summary_task_with_options(workspace_id, request, headers, runtime)

    async def create_fin_report_summary_task_async(
        self,
        workspace_id: str,
        request: main_models.CreateFinReportSummaryTaskRequest,
    ) -> main_models.CreateFinReportSummaryTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_fin_report_summary_task_with_options_async(workspace_id, request, headers, runtime)

    def create_image_detection_task_with_options(
        self,
        workspace_id: str,
        request: main_models.CreateImageDetectionTaskRequest,
        headers: main_models.CreateImageDetectionTaskHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageDetectionTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_info):
            body['fileInfo'] = request.file_info
        if not DaraCore.is_null(request.file_url):
            body['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_load_test):
            real_headers['X-Load-Test'] = DaraCore.to_json_string(headers.x_load_test)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageDetectionTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/imageDetect/task/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageDetectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_detection_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreateImageDetectionTaskRequest,
        headers: main_models.CreateImageDetectionTaskHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageDetectionTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_info):
            body['fileInfo'] = request.file_info
        if not DaraCore.is_null(request.file_url):
            body['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_load_test):
            real_headers['X-Load-Test'] = DaraCore.to_json_string(headers.x_load_test)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageDetectionTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/imageDetect/task/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageDetectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_detection_task(
        self,
        workspace_id: str,
        request: main_models.CreateImageDetectionTaskRequest,
    ) -> main_models.CreateImageDetectionTaskResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateImageDetectionTaskHeaders()
        return self.create_image_detection_task_with_options(workspace_id, request, headers, runtime)

    async def create_image_detection_task_async(
        self,
        workspace_id: str,
        request: main_models.CreateImageDetectionTaskRequest,
    ) -> main_models.CreateImageDetectionTaskResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateImageDetectionTaskHeaders()
        return await self.create_image_detection_task_with_options_async(workspace_id, request, headers, runtime)

    def create_library_with_options(
        self,
        workspace_id: str,
        request: main_models.CreateLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLibraryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.index_setting):
            body['indexSetting'] = request.index_setting
        if not DaraCore.is_null(request.library_name):
            body['libraryName'] = request.library_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLibrary',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_library_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreateLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLibraryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.index_setting):
            body['indexSetting'] = request.index_setting
        if not DaraCore.is_null(request.library_name):
            body['libraryName'] = request.library_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLibrary',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_library(
        self,
        workspace_id: str,
        request: main_models.CreateLibraryRequest,
    ) -> main_models.CreateLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_library_with_options(workspace_id, request, headers, runtime)

    async def create_library_async(
        self,
        workspace_id: str,
        request: main_models.CreateLibraryRequest,
    ) -> main_models.CreateLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_library_with_options_async(workspace_id, request, headers, runtime)

    def create_pdf_translate_task_with_options(
        self,
        workspace_id: str,
        request: main_models.CreatePdfTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePdfTranslateTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['docId'] = request.doc_id
        if not DaraCore.is_null(request.knowledge):
            body['knowledge'] = request.knowledge
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.translate_to):
            body['translateTo'] = request.translate_to
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePdfTranslateTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/pdfTranslate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePdfTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pdf_translate_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreatePdfTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePdfTranslateTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['docId'] = request.doc_id
        if not DaraCore.is_null(request.knowledge):
            body['knowledge'] = request.knowledge
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.translate_to):
            body['translateTo'] = request.translate_to
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePdfTranslateTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/pdfTranslate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePdfTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pdf_translate_task(
        self,
        workspace_id: str,
        request: main_models.CreatePdfTranslateTaskRequest,
    ) -> main_models.CreatePdfTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_pdf_translate_task_with_options(workspace_id, request, headers, runtime)

    async def create_pdf_translate_task_async(
        self,
        workspace_id: str,
        request: main_models.CreatePdfTranslateTaskRequest,
    ) -> main_models.CreatePdfTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_pdf_translate_task_with_options_async(workspace_id, request, headers, runtime)

    def create_predefined_document_with_options(
        self,
        workspace_id: str,
        request: main_models.CreatePredefinedDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePredefinedDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chunks):
            body['chunks'] = request.chunks
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.metadata):
            body['metadata'] = request.metadata
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePredefinedDocument',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/document/createPredefinedDocument',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePredefinedDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_predefined_document_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreatePredefinedDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePredefinedDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chunks):
            body['chunks'] = request.chunks
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.metadata):
            body['metadata'] = request.metadata
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePredefinedDocument',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/document/createPredefinedDocument',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePredefinedDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_predefined_document(
        self,
        workspace_id: str,
        request: main_models.CreatePredefinedDocumentRequest,
    ) -> main_models.CreatePredefinedDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_predefined_document_with_options(workspace_id, request, headers, runtime)

    async def create_predefined_document_async(
        self,
        workspace_id: str,
        request: main_models.CreatePredefinedDocumentRequest,
    ) -> main_models.CreatePredefinedDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_predefined_document_with_options_async(workspace_id, request, headers, runtime)

    def create_quality_check_task_with_options(
        self,
        workspace_id: str,
        request: main_models.CreateQualityCheckTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateQualityCheckTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.conversation_list):
            body['conversationList'] = request.conversation_list
        if not DaraCore.is_null(request.gmt_service):
            body['gmtService'] = request.gmt_service
        if not DaraCore.is_null(request.meta_data):
            body['metaData'] = request.meta_data
        if not DaraCore.is_null(request.quality_group):
            body['qualityGroup'] = request.quality_group
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.scene_code):
            body['sceneCode'] = request.scene_code
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateQualityCheckTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/qualitycheck/task/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQualityCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quality_check_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreateQualityCheckTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateQualityCheckTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.conversation_list):
            body['conversationList'] = request.conversation_list
        if not DaraCore.is_null(request.gmt_service):
            body['gmtService'] = request.gmt_service
        if not DaraCore.is_null(request.meta_data):
            body['metaData'] = request.meta_data
        if not DaraCore.is_null(request.quality_group):
            body['qualityGroup'] = request.quality_group
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.scene_code):
            body['sceneCode'] = request.scene_code
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateQualityCheckTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/qualitycheck/task/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQualityCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quality_check_task(
        self,
        workspace_id: str,
        request: main_models.CreateQualityCheckTaskRequest,
    ) -> main_models.CreateQualityCheckTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_quality_check_task_with_options(workspace_id, request, headers, runtime)

    async def create_quality_check_task_async(
        self,
        workspace_id: str,
        request: main_models.CreateQualityCheckTaskRequest,
    ) -> main_models.CreateQualityCheckTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_quality_check_task_with_options_async(workspace_id, request, headers, runtime)

    def create_video_creation_task_with_options(
        self,
        workspace_id: str,
        request: main_models.CreateVideoCreationTaskRequest,
        headers: main_models.CreateVideoCreationTaskHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVideoCreationTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.creation_instruction):
            body['creationInstruction'] = request.creation_instruction
        if not DaraCore.is_null(request.file_info):
            body['fileInfo'] = request.file_info
        if not DaraCore.is_null(request.image_detection_task_id):
            body['imageDetectionTaskId'] = request.image_detection_task_id
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_load_test):
            real_headers['X-Load-Test'] = DaraCore.to_json_string(headers.x_load_test)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVideoCreationTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/videoCreation/task/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVideoCreationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_video_creation_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreateVideoCreationTaskRequest,
        headers: main_models.CreateVideoCreationTaskHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVideoCreationTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.creation_instruction):
            body['creationInstruction'] = request.creation_instruction
        if not DaraCore.is_null(request.file_info):
            body['fileInfo'] = request.file_info
        if not DaraCore.is_null(request.image_detection_task_id):
            body['imageDetectionTaskId'] = request.image_detection_task_id
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_load_test):
            real_headers['X-Load-Test'] = DaraCore.to_json_string(headers.x_load_test)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVideoCreationTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/videoCreation/task/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVideoCreationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_video_creation_task(
        self,
        workspace_id: str,
        request: main_models.CreateVideoCreationTaskRequest,
    ) -> main_models.CreateVideoCreationTaskResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateVideoCreationTaskHeaders()
        return self.create_video_creation_task_with_options(workspace_id, request, headers, runtime)

    async def create_video_creation_task_async(
        self,
        workspace_id: str,
        request: main_models.CreateVideoCreationTaskRequest,
    ) -> main_models.CreateVideoCreationTaskResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateVideoCreationTaskHeaders()
        return await self.create_video_creation_task_with_options_async(workspace_id, request, headers, runtime)

    def dashscope_async_task_finish_event_with_options(
        self,
        workspace_id: str,
        request: main_models.DashscopeAsyncTaskFinishEventRequest,
        headers: main_models.DashscopeAsyncTaskFinishEventHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DashscopeAsyncTaskFinishEventResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.body):
            body['body'] = request.body
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_load_test):
            real_headers['X-Load-Test'] = DaraCore.to_json_string(headers.x_load_test)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DashscopeAsyncTaskFinishEvent',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/event/dashscopeAsyncTaskFinish',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DashscopeAsyncTaskFinishEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def dashscope_async_task_finish_event_with_options_async(
        self,
        workspace_id: str,
        request: main_models.DashscopeAsyncTaskFinishEventRequest,
        headers: main_models.DashscopeAsyncTaskFinishEventHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DashscopeAsyncTaskFinishEventResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.body):
            body['body'] = request.body
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_load_test):
            real_headers['X-Load-Test'] = DaraCore.to_json_string(headers.x_load_test)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DashscopeAsyncTaskFinishEvent',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/event/dashscopeAsyncTaskFinish',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DashscopeAsyncTaskFinishEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dashscope_async_task_finish_event(
        self,
        workspace_id: str,
        request: main_models.DashscopeAsyncTaskFinishEventRequest,
    ) -> main_models.DashscopeAsyncTaskFinishEventResponse:
        runtime = RuntimeOptions()
        headers = main_models.DashscopeAsyncTaskFinishEventHeaders()
        return self.dashscope_async_task_finish_event_with_options(workspace_id, request, headers, runtime)

    async def dashscope_async_task_finish_event_async(
        self,
        workspace_id: str,
        request: main_models.DashscopeAsyncTaskFinishEventRequest,
    ) -> main_models.DashscopeAsyncTaskFinishEventResponse:
        runtime = RuntimeOptions()
        headers = main_models.DashscopeAsyncTaskFinishEventHeaders()
        return await self.dashscope_async_task_finish_event_with_options_async(workspace_id, request, headers, runtime)

    def delete_document_with_options(
        self,
        workspace_id: str,
        request: main_models.DeleteDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_ids):
            body['docIds'] = request.doc_ids
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocument',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/document/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_document_with_options_async(
        self,
        workspace_id: str,
        request: main_models.DeleteDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_ids):
            body['docIds'] = request.doc_ids
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocument',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/document/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_document(
        self,
        workspace_id: str,
        request: main_models.DeleteDocumentRequest,
    ) -> main_models.DeleteDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_document_with_options(workspace_id, request, headers, runtime)

    async def delete_document_async(
        self,
        workspace_id: str,
        request: main_models.DeleteDocumentRequest,
    ) -> main_models.DeleteDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_document_with_options_async(workspace_id, request, headers, runtime)

    def delete_library_with_options(
        self,
        workspace_id: str,
        request: main_models.DeleteLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLibraryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.library_id):
            query['libraryId'] = request.library_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLibrary',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/delete',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_library_with_options_async(
        self,
        workspace_id: str,
        request: main_models.DeleteLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLibraryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.library_id):
            query['libraryId'] = request.library_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLibrary',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/delete',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_library(
        self,
        workspace_id: str,
        request: main_models.DeleteLibraryRequest,
    ) -> main_models.DeleteLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_library_with_options(workspace_id, request, headers, runtime)

    async def delete_library_async(
        self,
        workspace_id: str,
        request: main_models.DeleteLibraryRequest,
    ) -> main_models.DeleteLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_library_with_options_async(workspace_id, request, headers, runtime)

    def end_to_end_real_time_dialog_with_options(
        self,
        workspace_id: str,
        request: main_models.EndToEndRealTimeDialogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EndToEndRealTimeDialogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asr_model_id):
            query['asrModelId'] = request.asr_model_id
        if not DaraCore.is_null(request.input_format):
            query['inputFormat'] = request.input_format
        if not DaraCore.is_null(request.output_format):
            query['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.pitch_rate):
            query['pitchRate'] = request.pitch_rate
        if not DaraCore.is_null(request.sample_rate):
            query['sampleRate'] = request.sample_rate
        if not DaraCore.is_null(request.speech_rate):
            query['speechRate'] = request.speech_rate
        if not DaraCore.is_null(request.tts_model_id):
            query['ttsModelId'] = request.tts_model_id
        if not DaraCore.is_null(request.voice_code):
            query['voiceCode'] = request.voice_code
        if not DaraCore.is_null(request.volume):
            query['volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EndToEndRealTimeDialog',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ws/realtime/dialog',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EndToEndRealTimeDialogResponse(),
            self.call_api(params, req, runtime)
        )

    async def end_to_end_real_time_dialog_with_options_async(
        self,
        workspace_id: str,
        request: main_models.EndToEndRealTimeDialogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EndToEndRealTimeDialogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asr_model_id):
            query['asrModelId'] = request.asr_model_id
        if not DaraCore.is_null(request.input_format):
            query['inputFormat'] = request.input_format
        if not DaraCore.is_null(request.output_format):
            query['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.pitch_rate):
            query['pitchRate'] = request.pitch_rate
        if not DaraCore.is_null(request.sample_rate):
            query['sampleRate'] = request.sample_rate
        if not DaraCore.is_null(request.speech_rate):
            query['speechRate'] = request.speech_rate
        if not DaraCore.is_null(request.tts_model_id):
            query['ttsModelId'] = request.tts_model_id
        if not DaraCore.is_null(request.voice_code):
            query['voiceCode'] = request.voice_code
        if not DaraCore.is_null(request.volume):
            query['volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EndToEndRealTimeDialog',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ws/realtime/dialog',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EndToEndRealTimeDialogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def end_to_end_real_time_dialog(
        self,
        workspace_id: str,
        request: main_models.EndToEndRealTimeDialogRequest,
    ) -> main_models.EndToEndRealTimeDialogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.end_to_end_real_time_dialog_with_options(workspace_id, request, headers, runtime)

    async def end_to_end_real_time_dialog_async(
        self,
        workspace_id: str,
        request: main_models.EndToEndRealTimeDialogRequest,
    ) -> main_models.EndToEndRealTimeDialogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.end_to_end_real_time_dialog_with_options_async(workspace_id, request, headers, runtime)

    def evict_task_with_options(
        self,
        workspace_id: str,
        request: main_models.EvictTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EvictTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EvictTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/evict',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EvictTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def evict_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.EvictTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EvictTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EvictTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/evict',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EvictTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def evict_task(
        self,
        workspace_id: str,
        request: main_models.EvictTaskRequest,
    ) -> main_models.EvictTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.evict_task_with_options(workspace_id, request, headers, runtime)

    async def evict_task_async(
        self,
        workspace_id: str,
        request: main_models.EvictTaskRequest,
    ) -> main_models.EvictTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.evict_task_with_options_async(workspace_id, request, headers, runtime)

    def gen_doc_qa_result_with_options(
        self,
        workspace_id: str,
        request: main_models.GenDocQaResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenDocQaResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['docId'] = request.doc_id
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenDocQaResult',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/qa/parse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenDocQaResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def gen_doc_qa_result_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GenDocQaResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenDocQaResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['docId'] = request.doc_id
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenDocQaResult',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/qa/parse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenDocQaResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def gen_doc_qa_result(
        self,
        workspace_id: str,
        request: main_models.GenDocQaResultRequest,
    ) -> main_models.GenDocQaResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.gen_doc_qa_result_with_options(workspace_id, request, headers, runtime)

    async def gen_doc_qa_result_async(
        self,
        workspace_id: str,
        request: main_models.GenDocQaResultRequest,
    ) -> main_models.GenDocQaResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.gen_doc_qa_result_with_options_async(workspace_id, request, headers, runtime)

    def get_app_config_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAppConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAppConfig',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/app/config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_config_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAppConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAppConfig',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/app/config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_config(
        self,
        workspace_id: str,
    ) -> main_models.GetAppConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_app_config_with_options(workspace_id, headers, runtime)

    async def get_app_config_async(
        self,
        workspace_id: str,
    ) -> main_models.GetAppConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_app_config_with_options_async(workspace_id, headers, runtime)

    def get_chat_question_resp_with_options(
        self,
        workspace_id: str,
        request: main_models.GetChatQuestionRespRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetChatQuestionRespResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.batch_id):
            body['batchId'] = request.batch_id
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetChatQuestionResp',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/chat/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatQuestionRespResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_question_resp_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetChatQuestionRespRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetChatQuestionRespResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.batch_id):
            body['batchId'] = request.batch_id
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetChatQuestionResp',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/chat/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatQuestionRespResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat_question_resp(
        self,
        workspace_id: str,
        request: main_models.GetChatQuestionRespRequest,
    ) -> main_models.GetChatQuestionRespResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_chat_question_resp_with_options(workspace_id, request, headers, runtime)

    async def get_chat_question_resp_async(
        self,
        workspace_id: str,
        request: main_models.GetChatQuestionRespRequest,
    ) -> main_models.GetChatQuestionRespResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_chat_question_resp_with_options_async(workspace_id, request, headers, runtime)

    def get_dialog_analysis_result_with_options(
        self,
        workspace_id: str,
        request: main_models.GetDialogAnalysisResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDialogAnalysisResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.asc):
            body['asc'] = request.asc
        if not DaraCore.is_null(request.end_time):
            body['endTime'] = request.end_time
        if not DaraCore.is_null(request.session_ids):
            body['sessionIds'] = request.session_ids
        if not DaraCore.is_null(request.start_time):
            body['startTime'] = request.start_time
        if not DaraCore.is_null(request.use_url):
            body['useUrl'] = request.use_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDialogAnalysisResult',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/dialog/analysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDialogAnalysisResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dialog_analysis_result_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetDialogAnalysisResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDialogAnalysisResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.asc):
            body['asc'] = request.asc
        if not DaraCore.is_null(request.end_time):
            body['endTime'] = request.end_time
        if not DaraCore.is_null(request.session_ids):
            body['sessionIds'] = request.session_ids
        if not DaraCore.is_null(request.start_time):
            body['startTime'] = request.start_time
        if not DaraCore.is_null(request.use_url):
            body['useUrl'] = request.use_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDialogAnalysisResult',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/dialog/analysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDialogAnalysisResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dialog_analysis_result(
        self,
        workspace_id: str,
        request: main_models.GetDialogAnalysisResultRequest,
    ) -> main_models.GetDialogAnalysisResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_dialog_analysis_result_with_options(workspace_id, request, headers, runtime)

    async def get_dialog_analysis_result_async(
        self,
        workspace_id: str,
        request: main_models.GetDialogAnalysisResultRequest,
    ) -> main_models.GetDialogAnalysisResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_dialog_analysis_result_with_options_async(workspace_id, request, headers, runtime)

    def get_dialog_detail_with_options(
        self,
        workspace_id: str,
        request: main_models.GetDialogDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDialogDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDialogDetail',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/dialog/detail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDialogDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dialog_detail_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetDialogDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDialogDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDialogDetail',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/dialog/detail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDialogDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dialog_detail(
        self,
        workspace_id: str,
        request: main_models.GetDialogDetailRequest,
    ) -> main_models.GetDialogDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_dialog_detail_with_options(workspace_id, request, headers, runtime)

    async def get_dialog_detail_async(
        self,
        workspace_id: str,
        request: main_models.GetDialogDetailRequest,
    ) -> main_models.GetDialogDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_dialog_detail_with_options_async(workspace_id, request, headers, runtime)

    def get_dialog_log_with_options(
        self,
        workspace_id: str,
        request: main_models.GetDialogLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDialogLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDialogLog',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/dialog/log',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDialogLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dialog_log_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetDialogLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDialogLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDialogLog',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/dialog/log',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDialogLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dialog_log(
        self,
        workspace_id: str,
        request: main_models.GetDialogLogRequest,
    ) -> main_models.GetDialogLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_dialog_log_with_options(workspace_id, request, headers, runtime)

    async def get_dialog_log_async(
        self,
        workspace_id: str,
        request: main_models.GetDialogLogRequest,
    ) -> main_models.GetDialogLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_dialog_log_with_options_async(workspace_id, request, headers, runtime)

    def get_document_chunk_list_with_options(
        self,
        workspace_id: str,
        request: main_models.GetDocumentChunkListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentChunkListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chunk_id_list):
            body['chunkIdList'] = request.chunk_id_list
        if not DaraCore.is_null(request.doc_id):
            body['docId'] = request.doc_id
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.order):
            body['order'] = request.order
        if not DaraCore.is_null(request.order_by):
            body['orderBy'] = request.order_by
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.search_query):
            body['searchQuery'] = request.search_query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentChunkList',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/getDocumentChunk',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentChunkListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_chunk_list_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetDocumentChunkListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentChunkListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chunk_id_list):
            body['chunkIdList'] = request.chunk_id_list
        if not DaraCore.is_null(request.doc_id):
            body['docId'] = request.doc_id
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.order):
            body['order'] = request.order
        if not DaraCore.is_null(request.order_by):
            body['orderBy'] = request.order_by
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.search_query):
            body['searchQuery'] = request.search_query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentChunkList',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/getDocumentChunk',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentChunkListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_chunk_list(
        self,
        workspace_id: str,
        request: main_models.GetDocumentChunkListRequest,
    ) -> main_models.GetDocumentChunkListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_document_chunk_list_with_options(workspace_id, request, headers, runtime)

    async def get_document_chunk_list_async(
        self,
        workspace_id: str,
        request: main_models.GetDocumentChunkListRequest,
    ) -> main_models.GetDocumentChunkListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_document_chunk_list_with_options_async(workspace_id, request, headers, runtime)

    def get_document_list_with_options(
        self,
        workspace_id: str,
        request: main_models.GetDocumentListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.library_id):
            query['libraryId'] = request.library_id
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentList',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/listDocument',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_list_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetDocumentListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.library_id):
            query['libraryId'] = request.library_id
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentList',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/listDocument',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_list(
        self,
        workspace_id: str,
        request: main_models.GetDocumentListRequest,
    ) -> main_models.GetDocumentListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_document_list_with_options(workspace_id, request, headers, runtime)

    async def get_document_list_async(
        self,
        workspace_id: str,
        request: main_models.GetDocumentListRequest,
    ) -> main_models.GetDocumentListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_document_list_with_options_async(workspace_id, request, headers, runtime)

    def get_document_url_with_options(
        self,
        workspace_id: str,
        request: main_models.GetDocumentUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.document_id):
            query['documentId'] = request.document_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentUrl',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/document/url',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_url_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetDocumentUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.document_id):
            query['documentId'] = request.document_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentUrl',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/document/url',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_url(
        self,
        workspace_id: str,
        request: main_models.GetDocumentUrlRequest,
    ) -> main_models.GetDocumentUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_document_url_with_options(workspace_id, request, headers, runtime)

    async def get_document_url_async(
        self,
        workspace_id: str,
        request: main_models.GetDocumentUrlRequest,
    ) -> main_models.GetDocumentUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_document_url_with_options_async(workspace_id, request, headers, runtime)

    def get_filter_document_list_with_options(
        self,
        workspace_id: str,
        request: main_models.GetFilterDocumentListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFilterDocumentListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.and_):
            body['and'] = request.and_
        if not DaraCore.is_null(request.doc_id_list):
            body['docIdList'] = request.doc_id_list
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.or_):
            body['or'] = request.or_
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFilterDocumentList',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/filterDocument',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFilterDocumentListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_filter_document_list_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetFilterDocumentListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFilterDocumentListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.and_):
            body['and'] = request.and_
        if not DaraCore.is_null(request.doc_id_list):
            body['docIdList'] = request.doc_id_list
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.or_):
            body['or'] = request.or_
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFilterDocumentList',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/filterDocument',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFilterDocumentListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_filter_document_list(
        self,
        workspace_id: str,
        request: main_models.GetFilterDocumentListRequest,
    ) -> main_models.GetFilterDocumentListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_filter_document_list_with_options(workspace_id, request, headers, runtime)

    async def get_filter_document_list_async(
        self,
        workspace_id: str,
        request: main_models.GetFilterDocumentListRequest,
    ) -> main_models.GetFilterDocumentListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_filter_document_list_with_options_async(workspace_id, request, headers, runtime)

    def get_history_list_by_biz_type_with_options(
        self,
        workspace_id: str,
        request: main_models.GetHistoryListByBizTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHistoryListByBizTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['bizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['bizType'] = request.biz_type
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHistoryListByBizType',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/history/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHistoryListByBizTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_history_list_by_biz_type_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetHistoryListByBizTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHistoryListByBizTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['bizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['bizType'] = request.biz_type
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHistoryListByBizType',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/history/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHistoryListByBizTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_history_list_by_biz_type(
        self,
        workspace_id: str,
        request: main_models.GetHistoryListByBizTypeRequest,
    ) -> main_models.GetHistoryListByBizTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_history_list_by_biz_type_with_options(workspace_id, request, headers, runtime)

    async def get_history_list_by_biz_type_async(
        self,
        workspace_id: str,
        request: main_models.GetHistoryListByBizTypeRequest,
    ) -> main_models.GetHistoryListByBizTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_history_list_by_biz_type_with_options_async(workspace_id, request, headers, runtime)

    def get_image_detection_task_result_with_options(
        self,
        workspace_id: str,
        request: main_models.GetImageDetectionTaskResultRequest,
        headers: main_models.GetImageDetectionTaskResultHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageDetectionTaskResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_load_test):
            real_headers['X-Load-Test'] = DaraCore.to_json_string(headers.x_load_test)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetImageDetectionTaskResult',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/imageDetect/task/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageDetectionTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_detection_task_result_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetImageDetectionTaskResultRequest,
        headers: main_models.GetImageDetectionTaskResultHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageDetectionTaskResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_load_test):
            real_headers['X-Load-Test'] = DaraCore.to_json_string(headers.x_load_test)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetImageDetectionTaskResult',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/imageDetect/task/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageDetectionTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_detection_task_result(
        self,
        workspace_id: str,
        request: main_models.GetImageDetectionTaskResultRequest,
    ) -> main_models.GetImageDetectionTaskResultResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetImageDetectionTaskResultHeaders()
        return self.get_image_detection_task_result_with_options(workspace_id, request, headers, runtime)

    async def get_image_detection_task_result_async(
        self,
        workspace_id: str,
        request: main_models.GetImageDetectionTaskResultRequest,
    ) -> main_models.GetImageDetectionTaskResultResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetImageDetectionTaskResultHeaders()
        return await self.get_image_detection_task_result_with_options_async(workspace_id, request, headers, runtime)

    def get_library_with_options(
        self,
        workspace_id: str,
        request: main_models.GetLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLibraryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.library_id):
            query['libraryId'] = request.library_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLibrary',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_library_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLibraryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.library_id):
            query['libraryId'] = request.library_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLibrary',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_library(
        self,
        workspace_id: str,
        request: main_models.GetLibraryRequest,
    ) -> main_models.GetLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_library_with_options(workspace_id, request, headers, runtime)

    async def get_library_async(
        self,
        workspace_id: str,
        request: main_models.GetLibraryRequest,
    ) -> main_models.GetLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_library_with_options_async(workspace_id, request, headers, runtime)

    def get_library_list_with_options(
        self,
        workspace_id: str,
        request: main_models.GetLibraryListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLibraryListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLibraryList',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLibraryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_library_list_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetLibraryListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLibraryListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLibraryList',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLibraryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_library_list(
        self,
        workspace_id: str,
        request: main_models.GetLibraryListRequest,
    ) -> main_models.GetLibraryListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_library_list_with_options(workspace_id, request, headers, runtime)

    async def get_library_list_async(
        self,
        workspace_id: str,
        request: main_models.GetLibraryListRequest,
    ) -> main_models.GetLibraryListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_library_list_with_options_async(workspace_id, request, headers, runtime)

    def get_parse_result_with_options(
        self,
        workspace_id: str,
        request: main_models.GetParseResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetParseResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['docId'] = request.doc_id
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.use_url_result):
            body['useUrlResult'] = request.use_url_result
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetParseResult',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/document/getParseResult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetParseResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_parse_result_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetParseResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetParseResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['docId'] = request.doc_id
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.use_url_result):
            body['useUrlResult'] = request.use_url_result
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetParseResult',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/document/getParseResult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetParseResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_parse_result(
        self,
        workspace_id: str,
        request: main_models.GetParseResultRequest,
    ) -> main_models.GetParseResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_parse_result_with_options(workspace_id, request, headers, runtime)

    async def get_parse_result_async(
        self,
        workspace_id: str,
        request: main_models.GetParseResultRequest,
    ) -> main_models.GetParseResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_parse_result_with_options_async(workspace_id, request, headers, runtime)

    def get_quality_check_task_result_with_options(
        self,
        workspace_id: str,
        request: main_models.GetQualityCheckTaskResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityCheckTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityCheckTaskResult',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/qualitycheck/task/query',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityCheckTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_check_task_result_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetQualityCheckTaskResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityCheckTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityCheckTaskResult',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/qualitycheck/task/query',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityCheckTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_check_task_result(
        self,
        workspace_id: str,
        request: main_models.GetQualityCheckTaskResultRequest,
    ) -> main_models.GetQualityCheckTaskResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_quality_check_task_result_with_options(workspace_id, request, headers, runtime)

    async def get_quality_check_task_result_async(
        self,
        workspace_id: str,
        request: main_models.GetQualityCheckTaskResultRequest,
    ) -> main_models.GetQualityCheckTaskResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_quality_check_task_result_with_options_async(workspace_id, request, headers, runtime)

    def get_summary_task_result_with_options(
        self,
        workspace_id: str,
        request: main_models.GetSummaryTaskResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSummaryTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSummaryTaskResult',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/summary/result',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSummaryTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_summary_task_result_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetSummaryTaskResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSummaryTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSummaryTaskResult',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/summary/result',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSummaryTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_summary_task_result(
        self,
        workspace_id: str,
        request: main_models.GetSummaryTaskResultRequest,
    ) -> main_models.GetSummaryTaskResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_summary_task_result_with_options(workspace_id, request, headers, runtime)

    async def get_summary_task_result_async(
        self,
        workspace_id: str,
        request: main_models.GetSummaryTaskResultRequest,
    ) -> main_models.GetSummaryTaskResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_summary_task_result_with_options_async(workspace_id, request, headers, runtime)

    def get_task_result_with_options(
        self,
        workspace_id: str,
        request: main_models.GetTaskResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskResult',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/result',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_result_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetTaskResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskResult',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/result',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_result(
        self,
        workspace_id: str,
        request: main_models.GetTaskResultRequest,
    ) -> main_models.GetTaskResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_task_result_with_options(workspace_id, request, headers, runtime)

    async def get_task_result_async(
        self,
        workspace_id: str,
        request: main_models.GetTaskResultRequest,
    ) -> main_models.GetTaskResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_task_result_with_options_async(workspace_id, request, headers, runtime)

    def get_task_status_with_options(
        self,
        workspace_id: str,
        request: main_models.GetTaskStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskStatus',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_status_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetTaskStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskStatus',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_status(
        self,
        workspace_id: str,
        request: main_models.GetTaskStatusRequest,
    ) -> main_models.GetTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_task_status_with_options(workspace_id, request, headers, runtime)

    async def get_task_status_async(
        self,
        workspace_id: str,
        request: main_models.GetTaskStatusRequest,
    ) -> main_models.GetTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_task_status_with_options_async(workspace_id, request, headers, runtime)

    def get_video_creation_task_result_with_options(
        self,
        workspace_id: str,
        request: main_models.GetVideoCreationTaskResultRequest,
        headers: main_models.GetVideoCreationTaskResultHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoCreationTaskResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_load_test):
            real_headers['X-Load-Test'] = DaraCore.to_json_string(headers.x_load_test)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoCreationTaskResult',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/videoCreation/task/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoCreationTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_creation_task_result_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetVideoCreationTaskResultRequest,
        headers: main_models.GetVideoCreationTaskResultHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoCreationTaskResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_load_test):
            real_headers['X-Load-Test'] = DaraCore.to_json_string(headers.x_load_test)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoCreationTaskResult',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/videoCreation/task/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoCreationTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_creation_task_result(
        self,
        workspace_id: str,
        request: main_models.GetVideoCreationTaskResultRequest,
    ) -> main_models.GetVideoCreationTaskResultResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetVideoCreationTaskResultHeaders()
        return self.get_video_creation_task_result_with_options(workspace_id, request, headers, runtime)

    async def get_video_creation_task_result_async(
        self,
        workspace_id: str,
        request: main_models.GetVideoCreationTaskResultRequest,
    ) -> main_models.GetVideoCreationTaskResultResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetVideoCreationTaskResultHeaders()
        return await self.get_video_creation_task_result_with_options_async(workspace_id, request, headers, runtime)

    def invoke_plugin_with_options(
        self,
        workspace_id: str,
        request: main_models.InvokePluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InvokePluginResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        if not DaraCore.is_null(request.plugin_id):
            body['pluginId'] = request.plugin_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InvokePlugin',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/plugin/invoke',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokePluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoke_plugin_with_options_async(
        self,
        workspace_id: str,
        request: main_models.InvokePluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InvokePluginResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        if not DaraCore.is_null(request.plugin_id):
            body['pluginId'] = request.plugin_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InvokePlugin',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/plugin/invoke',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokePluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoke_plugin(
        self,
        workspace_id: str,
        request: main_models.InvokePluginRequest,
    ) -> main_models.InvokePluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.invoke_plugin_with_options(workspace_id, request, headers, runtime)

    async def invoke_plugin_async(
        self,
        workspace_id: str,
        request: main_models.InvokePluginRequest,
    ) -> main_models.InvokePluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.invoke_plugin_with_options_async(workspace_id, request, headers, runtime)

    def preview_document_with_options(
        self,
        workspace_id: str,
        request: main_models.PreviewDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PreviewDocumentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.document_id):
            query['documentId'] = request.document_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreviewDocument',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/document/preview',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviewDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def preview_document_with_options_async(
        self,
        workspace_id: str,
        request: main_models.PreviewDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PreviewDocumentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.document_id):
            query['documentId'] = request.document_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreviewDocument',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/document/preview',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviewDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preview_document(
        self,
        workspace_id: str,
        request: main_models.PreviewDocumentRequest,
    ) -> main_models.PreviewDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.preview_document_with_options(workspace_id, request, headers, runtime)

    async def preview_document_async(
        self,
        workspace_id: str,
        request: main_models.PreviewDocumentRequest,
    ) -> main_models.PreviewDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.preview_document_with_options_async(workspace_id, request, headers, runtime)

    def re_index_with_options(
        self,
        workspace_id: str,
        request: main_models.ReIndexRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.document_id):
            query['documentId'] = request.document_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReIndex',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/document/reIndex',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def re_index_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ReIndexRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.document_id):
            query['documentId'] = request.document_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReIndex',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/document/reIndex',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def re_index(
        self,
        workspace_id: str,
        request: main_models.ReIndexRequest,
    ) -> main_models.ReIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.re_index_with_options(workspace_id, request, headers, runtime)

    async def re_index_async(
        self,
        workspace_id: str,
        request: main_models.ReIndexRequest,
    ) -> main_models.ReIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.re_index_with_options_async(workspace_id, request, headers, runtime)

    def real_time_dialog_with_sse(
        self,
        workspace_id: str,
        request: main_models.RealTimeDialogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RealTimeDialogResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.analysis):
            body['analysis'] = request.analysis
        if not DaraCore.is_null(request.biz_type):
            body['bizType'] = request.biz_type
        if not DaraCore.is_null(request.conversation_model):
            body['conversationModel'] = request.conversation_model
        if not DaraCore.is_null(request.dialog_memory_turns):
            body['dialogMemoryTurns'] = request.dialog_memory_turns
        if not DaraCore.is_null(request.meta_data):
            body['metaData'] = request.meta_data
        if not DaraCore.is_null(request.op_type):
            body['opType'] = request.op_type
        if not DaraCore.is_null(request.recommend):
            body['recommend'] = request.recommend
        if not DaraCore.is_null(request.script_content_played):
            body['scriptContentPlayed'] = request.script_content_played
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.user_vad):
            body['userVad'] = request.user_vad
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RealTimeDialog',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/realtime/dialog/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RealTimeDialogResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def real_time_dialog_with_sse_async(
        self,
        workspace_id: str,
        request: main_models.RealTimeDialogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RealTimeDialogResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.analysis):
            body['analysis'] = request.analysis
        if not DaraCore.is_null(request.biz_type):
            body['bizType'] = request.biz_type
        if not DaraCore.is_null(request.conversation_model):
            body['conversationModel'] = request.conversation_model
        if not DaraCore.is_null(request.dialog_memory_turns):
            body['dialogMemoryTurns'] = request.dialog_memory_turns
        if not DaraCore.is_null(request.meta_data):
            body['metaData'] = request.meta_data
        if not DaraCore.is_null(request.op_type):
            body['opType'] = request.op_type
        if not DaraCore.is_null(request.recommend):
            body['recommend'] = request.recommend
        if not DaraCore.is_null(request.script_content_played):
            body['scriptContentPlayed'] = request.script_content_played
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.user_vad):
            body['userVad'] = request.user_vad
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RealTimeDialog',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/realtime/dialog/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RealTimeDialogResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def real_time_dialog_with_options(
        self,
        workspace_id: str,
        request: main_models.RealTimeDialogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RealTimeDialogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.analysis):
            body['analysis'] = request.analysis
        if not DaraCore.is_null(request.biz_type):
            body['bizType'] = request.biz_type
        if not DaraCore.is_null(request.conversation_model):
            body['conversationModel'] = request.conversation_model
        if not DaraCore.is_null(request.dialog_memory_turns):
            body['dialogMemoryTurns'] = request.dialog_memory_turns
        if not DaraCore.is_null(request.meta_data):
            body['metaData'] = request.meta_data
        if not DaraCore.is_null(request.op_type):
            body['opType'] = request.op_type
        if not DaraCore.is_null(request.recommend):
            body['recommend'] = request.recommend
        if not DaraCore.is_null(request.script_content_played):
            body['scriptContentPlayed'] = request.script_content_played
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.user_vad):
            body['userVad'] = request.user_vad
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RealTimeDialog',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/realtime/dialog/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RealTimeDialogResponse(),
            self.call_api(params, req, runtime)
        )

    async def real_time_dialog_with_options_async(
        self,
        workspace_id: str,
        request: main_models.RealTimeDialogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RealTimeDialogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.analysis):
            body['analysis'] = request.analysis
        if not DaraCore.is_null(request.biz_type):
            body['bizType'] = request.biz_type
        if not DaraCore.is_null(request.conversation_model):
            body['conversationModel'] = request.conversation_model
        if not DaraCore.is_null(request.dialog_memory_turns):
            body['dialogMemoryTurns'] = request.dialog_memory_turns
        if not DaraCore.is_null(request.meta_data):
            body['metaData'] = request.meta_data
        if not DaraCore.is_null(request.op_type):
            body['opType'] = request.op_type
        if not DaraCore.is_null(request.recommend):
            body['recommend'] = request.recommend
        if not DaraCore.is_null(request.script_content_played):
            body['scriptContentPlayed'] = request.script_content_played
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.user_vad):
            body['userVad'] = request.user_vad
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RealTimeDialog',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/realtime/dialog/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RealTimeDialogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def real_time_dialog(
        self,
        workspace_id: str,
        request: main_models.RealTimeDialogRequest,
    ) -> main_models.RealTimeDialogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.real_time_dialog_with_options(workspace_id, request, headers, runtime)

    async def real_time_dialog_async(
        self,
        workspace_id: str,
        request: main_models.RealTimeDialogRequest,
    ) -> main_models.RealTimeDialogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.real_time_dialog_with_options_async(workspace_id, request, headers, runtime)

    def realtime_dialog_assist_with_options(
        self,
        workspace_id: str,
        request: main_models.RealtimeDialogAssistRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RealtimeDialogAssistResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.analysis):
            body['analysis'] = request.analysis
        if not DaraCore.is_null(request.biz_type):
            body['bizType'] = request.biz_type
        if not DaraCore.is_null(request.conversation_model):
            body['conversationModel'] = request.conversation_model
        if not DaraCore.is_null(request.dialog_memory_turns):
            body['dialogMemoryTurns'] = request.dialog_memory_turns
        if not DaraCore.is_null(request.hang_up_dialog):
            body['hangUpDialog'] = request.hang_up_dialog
        if not DaraCore.is_null(request.meta_data):
            body['metaData'] = request.meta_data
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.script_content_played):
            body['scriptContentPlayed'] = request.script_content_played
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.user_vad):
            body['userVad'] = request.user_vad
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RealtimeDialogAssist',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/realtime/dialog/assist',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RealtimeDialogAssistResponse(),
            self.call_api(params, req, runtime)
        )

    async def realtime_dialog_assist_with_options_async(
        self,
        workspace_id: str,
        request: main_models.RealtimeDialogAssistRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RealtimeDialogAssistResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.analysis):
            body['analysis'] = request.analysis
        if not DaraCore.is_null(request.biz_type):
            body['bizType'] = request.biz_type
        if not DaraCore.is_null(request.conversation_model):
            body['conversationModel'] = request.conversation_model
        if not DaraCore.is_null(request.dialog_memory_turns):
            body['dialogMemoryTurns'] = request.dialog_memory_turns
        if not DaraCore.is_null(request.hang_up_dialog):
            body['hangUpDialog'] = request.hang_up_dialog
        if not DaraCore.is_null(request.meta_data):
            body['metaData'] = request.meta_data
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.script_content_played):
            body['scriptContentPlayed'] = request.script_content_played
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.user_vad):
            body['userVad'] = request.user_vad
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RealtimeDialogAssist',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/realtime/dialog/assist',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RealtimeDialogAssistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def realtime_dialog_assist(
        self,
        workspace_id: str,
        request: main_models.RealtimeDialogAssistRequest,
    ) -> main_models.RealtimeDialogAssistResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.realtime_dialog_assist_with_options(workspace_id, request, headers, runtime)

    async def realtime_dialog_assist_async(
        self,
        workspace_id: str,
        request: main_models.RealtimeDialogAssistRequest,
    ) -> main_models.RealtimeDialogAssistResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.realtime_dialog_assist_with_options_async(workspace_id, request, headers, runtime)

    def rebuild_task_with_options(
        self,
        workspace_id: str,
        request: main_models.RebuildTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RebuildTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_ids):
            body['taskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RebuildTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/rebuild',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebuildTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebuild_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.RebuildTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RebuildTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_ids):
            body['taskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RebuildTask',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/task/rebuild',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebuildTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebuild_task(
        self,
        workspace_id: str,
        request: main_models.RebuildTaskRequest,
    ) -> main_models.RebuildTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.rebuild_task_with_options(workspace_id, request, headers, runtime)

    async def rebuild_task_async(
        self,
        workspace_id: str,
        request: main_models.RebuildTaskRequest,
    ) -> main_models.RebuildTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.rebuild_task_with_options_async(workspace_id, request, headers, runtime)

    def recall_document_with_options(
        self,
        workspace_id: str,
        request: main_models.RecallDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RecallDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.filters):
            body['filters'] = request.filters
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.rearrangement):
            body['rearrangement'] = request.rearrangement
        if not DaraCore.is_null(request.top_k):
            body['topK'] = request.top_k
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RecallDocument',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/recallDocument',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecallDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def recall_document_with_options_async(
        self,
        workspace_id: str,
        request: main_models.RecallDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RecallDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.filters):
            body['filters'] = request.filters
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.rearrangement):
            body['rearrangement'] = request.rearrangement
        if not DaraCore.is_null(request.top_k):
            body['topK'] = request.top_k
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RecallDocument',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/recallDocument',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecallDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recall_document(
        self,
        workspace_id: str,
        request: main_models.RecallDocumentRequest,
    ) -> main_models.RecallDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.recall_document_with_options(workspace_id, request, headers, runtime)

    async def recall_document_async(
        self,
        workspace_id: str,
        request: main_models.RecallDocumentRequest,
    ) -> main_models.RecallDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.recall_document_with_options_async(workspace_id, request, headers, runtime)

    def recognize_intention_with_options(
        self,
        workspace_id: str,
        request: main_models.RecognizeIntentionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RecognizeIntentionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.analysis):
            body['analysis'] = request.analysis
        if not DaraCore.is_null(request.biz_type):
            body['bizType'] = request.biz_type
        if not DaraCore.is_null(request.conversation):
            body['conversation'] = request.conversation
        if not DaraCore.is_null(request.global_intention_list):
            body['globalIntentionList'] = request.global_intention_list
        if not DaraCore.is_null(request.hierarchical_intention_list):
            body['hierarchicalIntentionList'] = request.hierarchical_intention_list
        if not DaraCore.is_null(request.intention_domain_code):
            body['intentionDomainCode'] = request.intention_domain_code
        if not DaraCore.is_null(request.intention_list):
            body['intentionList'] = request.intention_list
        if not DaraCore.is_null(request.op_type):
            body['opType'] = request.op_type
        if not DaraCore.is_null(request.recommend):
            body['recommend'] = request.recommend
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RecognizeIntention',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/recog/intent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecognizeIntentionResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_intention_with_options_async(
        self,
        workspace_id: str,
        request: main_models.RecognizeIntentionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RecognizeIntentionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.analysis):
            body['analysis'] = request.analysis
        if not DaraCore.is_null(request.biz_type):
            body['bizType'] = request.biz_type
        if not DaraCore.is_null(request.conversation):
            body['conversation'] = request.conversation
        if not DaraCore.is_null(request.global_intention_list):
            body['globalIntentionList'] = request.global_intention_list
        if not DaraCore.is_null(request.hierarchical_intention_list):
            body['hierarchicalIntentionList'] = request.hierarchical_intention_list
        if not DaraCore.is_null(request.intention_domain_code):
            body['intentionDomainCode'] = request.intention_domain_code
        if not DaraCore.is_null(request.intention_list):
            body['intentionList'] = request.intention_list
        if not DaraCore.is_null(request.op_type):
            body['opType'] = request.op_type
        if not DaraCore.is_null(request.recommend):
            body['recommend'] = request.recommend
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RecognizeIntention',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/recog/intent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecognizeIntentionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_intention(
        self,
        workspace_id: str,
        request: main_models.RecognizeIntentionRequest,
    ) -> main_models.RecognizeIntentionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.recognize_intention_with_options(workspace_id, request, headers, runtime)

    async def recognize_intention_async(
        self,
        workspace_id: str,
        request: main_models.RecognizeIntentionRequest,
    ) -> main_models.RecognizeIntentionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.recognize_intention_with_options_async(workspace_id, request, headers, runtime)

    def run_agent_with_sse(
        self,
        workspace_id: str,
        request: main_models.RunAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunAgentResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bot_id):
            body['botId'] = request.bot_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.thread_id):
            body['threadId'] = request.thread_id
        if not DaraCore.is_null(request.use_draft):
            body['useDraft'] = request.use_draft
        if not DaraCore.is_null(request.user_content):
            body['userContent'] = request.user_content
        if not DaraCore.is_null(request.user_inputs):
            body['userInputs'] = request.user_inputs
        if not DaraCore.is_null(request.version_id):
            body['versionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunAgent',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/bot/thread/run',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunAgentResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_agent_with_sse_async(
        self,
        workspace_id: str,
        request: main_models.RunAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunAgentResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bot_id):
            body['botId'] = request.bot_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.thread_id):
            body['threadId'] = request.thread_id
        if not DaraCore.is_null(request.use_draft):
            body['useDraft'] = request.use_draft
        if not DaraCore.is_null(request.user_content):
            body['userContent'] = request.user_content
        if not DaraCore.is_null(request.user_inputs):
            body['userInputs'] = request.user_inputs
        if not DaraCore.is_null(request.version_id):
            body['versionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunAgent',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/bot/thread/run',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunAgentResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_agent_with_options(
        self,
        workspace_id: str,
        request: main_models.RunAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bot_id):
            body['botId'] = request.bot_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.thread_id):
            body['threadId'] = request.thread_id
        if not DaraCore.is_null(request.use_draft):
            body['useDraft'] = request.use_draft
        if not DaraCore.is_null(request.user_content):
            body['userContent'] = request.user_content
        if not DaraCore.is_null(request.user_inputs):
            body['userInputs'] = request.user_inputs
        if not DaraCore.is_null(request.version_id):
            body['versionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunAgent',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/bot/thread/run',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_agent_with_options_async(
        self,
        workspace_id: str,
        request: main_models.RunAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bot_id):
            body['botId'] = request.bot_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.thread_id):
            body['threadId'] = request.thread_id
        if not DaraCore.is_null(request.use_draft):
            body['useDraft'] = request.use_draft
        if not DaraCore.is_null(request.user_content):
            body['userContent'] = request.user_content
        if not DaraCore.is_null(request.user_inputs):
            body['userInputs'] = request.user_inputs
        if not DaraCore.is_null(request.version_id):
            body['versionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunAgent',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/bot/thread/run',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_agent(
        self,
        workspace_id: str,
        request: main_models.RunAgentRequest,
    ) -> main_models.RunAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_agent_with_options(workspace_id, request, headers, runtime)

    async def run_agent_async(
        self,
        workspace_id: str,
        request: main_models.RunAgentRequest,
    ) -> main_models.RunAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_agent_with_options_async(workspace_id, request, headers, runtime)

    def run_chat_result_generation_with_sse(
        self,
        workspace_id: str,
        request: main_models.RunChatResultGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunChatResultGenerationResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.inference_parameters):
            body['inferenceParameters'] = request.inference_parameters
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.tools):
            body['tools'] = request.tools
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunChatResultGeneration',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/run/chat/generation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunChatResultGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_chat_result_generation_with_sse_async(
        self,
        workspace_id: str,
        request: main_models.RunChatResultGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunChatResultGenerationResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.inference_parameters):
            body['inferenceParameters'] = request.inference_parameters
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.tools):
            body['tools'] = request.tools
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunChatResultGeneration',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/run/chat/generation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunChatResultGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_chat_result_generation_with_options(
        self,
        workspace_id: str,
        request: main_models.RunChatResultGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunChatResultGenerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.inference_parameters):
            body['inferenceParameters'] = request.inference_parameters
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.tools):
            body['tools'] = request.tools
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunChatResultGeneration',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/run/chat/generation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunChatResultGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_chat_result_generation_with_options_async(
        self,
        workspace_id: str,
        request: main_models.RunChatResultGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunChatResultGenerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.inference_parameters):
            body['inferenceParameters'] = request.inference_parameters
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.tools):
            body['tools'] = request.tools
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunChatResultGeneration',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/run/chat/generation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunChatResultGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_chat_result_generation(
        self,
        workspace_id: str,
        request: main_models.RunChatResultGenerationRequest,
    ) -> main_models.RunChatResultGenerationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_chat_result_generation_with_options(workspace_id, request, headers, runtime)

    async def run_chat_result_generation_async(
        self,
        workspace_id: str,
        request: main_models.RunChatResultGenerationRequest,
    ) -> main_models.RunChatResultGenerationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_chat_result_generation_with_options_async(workspace_id, request, headers, runtime)

    def run_dialog_analysis_with_sse(
        self,
        workspace_id: str,
        request: main_models.RunDialogAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunDialogAnalysisResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDialogAnalysis',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/dialog/stream/analysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDialogAnalysisResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_dialog_analysis_with_sse_async(
        self,
        workspace_id: str,
        request: main_models.RunDialogAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunDialogAnalysisResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDialogAnalysis',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/dialog/stream/analysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDialogAnalysisResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_dialog_analysis_with_options(
        self,
        workspace_id: str,
        request: main_models.RunDialogAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunDialogAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDialogAnalysis',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/dialog/stream/analysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDialogAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_dialog_analysis_with_options_async(
        self,
        workspace_id: str,
        request: main_models.RunDialogAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunDialogAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDialogAnalysis',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/dialog/stream/analysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDialogAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_dialog_analysis(
        self,
        workspace_id: str,
        request: main_models.RunDialogAnalysisRequest,
    ) -> main_models.RunDialogAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_dialog_analysis_with_options(workspace_id, request, headers, runtime)

    async def run_dialog_analysis_async(
        self,
        workspace_id: str,
        request: main_models.RunDialogAnalysisRequest,
    ) -> main_models.RunDialogAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_dialog_analysis_with_options_async(workspace_id, request, headers, runtime)

    def run_library_chat_generation_with_sse(
        self,
        workspace_id: str,
        request: main_models.RunLibraryChatGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunLibraryChatGenerationResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id_list):
            body['docIdList'] = request.doc_id_list
        if not DaraCore.is_null(request.enable_follow_up):
            body['enableFollowUp'] = request.enable_follow_up
        if not DaraCore.is_null(request.enable_multi_query):
            body['enableMultiQuery'] = request.enable_multi_query
        if not DaraCore.is_null(request.enable_open_qa):
            body['enableOpenQa'] = request.enable_open_qa
        if not DaraCore.is_null(request.follow_up_llm):
            body['followUpLlm'] = request.follow_up_llm
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.llm_type):
            body['llmType'] = request.llm_type
        if not DaraCore.is_null(request.multi_query_llm):
            body['multiQueryLlm'] = request.multi_query_llm
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.query_criteria):
            body['queryCriteria'] = request.query_criteria
        if not DaraCore.is_null(request.rerank_type):
            body['rerankType'] = request.rerank_type
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.sub_query_list):
            body['subQueryList'] = request.sub_query_list
        if not DaraCore.is_null(request.text_search_parameter):
            body['textSearchParameter'] = request.text_search_parameter
        if not DaraCore.is_null(request.top_k):
            body['topK'] = request.top_k
        if not DaraCore.is_null(request.vector_search_parameter):
            body['vectorSearchParameter'] = request.vector_search_parameter
        if not DaraCore.is_null(request.with_document_reference):
            body['withDocumentReference'] = request.with_document_reference
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunLibraryChatGeneration',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/run/library/chat/generation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunLibraryChatGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_library_chat_generation_with_sse_async(
        self,
        workspace_id: str,
        request: main_models.RunLibraryChatGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunLibraryChatGenerationResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id_list):
            body['docIdList'] = request.doc_id_list
        if not DaraCore.is_null(request.enable_follow_up):
            body['enableFollowUp'] = request.enable_follow_up
        if not DaraCore.is_null(request.enable_multi_query):
            body['enableMultiQuery'] = request.enable_multi_query
        if not DaraCore.is_null(request.enable_open_qa):
            body['enableOpenQa'] = request.enable_open_qa
        if not DaraCore.is_null(request.follow_up_llm):
            body['followUpLlm'] = request.follow_up_llm
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.llm_type):
            body['llmType'] = request.llm_type
        if not DaraCore.is_null(request.multi_query_llm):
            body['multiQueryLlm'] = request.multi_query_llm
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.query_criteria):
            body['queryCriteria'] = request.query_criteria
        if not DaraCore.is_null(request.rerank_type):
            body['rerankType'] = request.rerank_type
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.sub_query_list):
            body['subQueryList'] = request.sub_query_list
        if not DaraCore.is_null(request.text_search_parameter):
            body['textSearchParameter'] = request.text_search_parameter
        if not DaraCore.is_null(request.top_k):
            body['topK'] = request.top_k
        if not DaraCore.is_null(request.vector_search_parameter):
            body['vectorSearchParameter'] = request.vector_search_parameter
        if not DaraCore.is_null(request.with_document_reference):
            body['withDocumentReference'] = request.with_document_reference
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunLibraryChatGeneration',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/run/library/chat/generation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunLibraryChatGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_library_chat_generation_with_options(
        self,
        workspace_id: str,
        request: main_models.RunLibraryChatGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunLibraryChatGenerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id_list):
            body['docIdList'] = request.doc_id_list
        if not DaraCore.is_null(request.enable_follow_up):
            body['enableFollowUp'] = request.enable_follow_up
        if not DaraCore.is_null(request.enable_multi_query):
            body['enableMultiQuery'] = request.enable_multi_query
        if not DaraCore.is_null(request.enable_open_qa):
            body['enableOpenQa'] = request.enable_open_qa
        if not DaraCore.is_null(request.follow_up_llm):
            body['followUpLlm'] = request.follow_up_llm
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.llm_type):
            body['llmType'] = request.llm_type
        if not DaraCore.is_null(request.multi_query_llm):
            body['multiQueryLlm'] = request.multi_query_llm
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.query_criteria):
            body['queryCriteria'] = request.query_criteria
        if not DaraCore.is_null(request.rerank_type):
            body['rerankType'] = request.rerank_type
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.sub_query_list):
            body['subQueryList'] = request.sub_query_list
        if not DaraCore.is_null(request.text_search_parameter):
            body['textSearchParameter'] = request.text_search_parameter
        if not DaraCore.is_null(request.top_k):
            body['topK'] = request.top_k
        if not DaraCore.is_null(request.vector_search_parameter):
            body['vectorSearchParameter'] = request.vector_search_parameter
        if not DaraCore.is_null(request.with_document_reference):
            body['withDocumentReference'] = request.with_document_reference
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunLibraryChatGeneration',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/run/library/chat/generation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunLibraryChatGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_library_chat_generation_with_options_async(
        self,
        workspace_id: str,
        request: main_models.RunLibraryChatGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunLibraryChatGenerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id_list):
            body['docIdList'] = request.doc_id_list
        if not DaraCore.is_null(request.enable_follow_up):
            body['enableFollowUp'] = request.enable_follow_up
        if not DaraCore.is_null(request.enable_multi_query):
            body['enableMultiQuery'] = request.enable_multi_query
        if not DaraCore.is_null(request.enable_open_qa):
            body['enableOpenQa'] = request.enable_open_qa
        if not DaraCore.is_null(request.follow_up_llm):
            body['followUpLlm'] = request.follow_up_llm
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.llm_type):
            body['llmType'] = request.llm_type
        if not DaraCore.is_null(request.multi_query_llm):
            body['multiQueryLlm'] = request.multi_query_llm
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.query_criteria):
            body['queryCriteria'] = request.query_criteria
        if not DaraCore.is_null(request.rerank_type):
            body['rerankType'] = request.rerank_type
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.sub_query_list):
            body['subQueryList'] = request.sub_query_list
        if not DaraCore.is_null(request.text_search_parameter):
            body['textSearchParameter'] = request.text_search_parameter
        if not DaraCore.is_null(request.top_k):
            body['topK'] = request.top_k
        if not DaraCore.is_null(request.vector_search_parameter):
            body['vectorSearchParameter'] = request.vector_search_parameter
        if not DaraCore.is_null(request.with_document_reference):
            body['withDocumentReference'] = request.with_document_reference
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunLibraryChatGeneration',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/run/library/chat/generation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunLibraryChatGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_library_chat_generation(
        self,
        workspace_id: str,
        request: main_models.RunLibraryChatGenerationRequest,
    ) -> main_models.RunLibraryChatGenerationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_library_chat_generation_with_options(workspace_id, request, headers, runtime)

    async def run_library_chat_generation_async(
        self,
        workspace_id: str,
        request: main_models.RunLibraryChatGenerationRequest,
    ) -> main_models.RunLibraryChatGenerationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_library_chat_generation_with_options_async(workspace_id, request, headers, runtime)

    def submit_chat_question_with_options(
        self,
        workspace_id: str,
        request: main_models.SubmitChatQuestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitChatQuestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gmt_service):
            body['gmtService'] = request.gmt_service
        if not DaraCore.is_null(request.live_script_content):
            body['liveScriptContent'] = request.live_script_content
        if not DaraCore.is_null(request.open_small_talk):
            body['openSmallTalk'] = request.open_small_talk
        if not DaraCore.is_null(request.question_list):
            body['questionList'] = request.question_list
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitChatQuestion',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/chat/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitChatQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_chat_question_with_options_async(
        self,
        workspace_id: str,
        request: main_models.SubmitChatQuestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitChatQuestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gmt_service):
            body['gmtService'] = request.gmt_service
        if not DaraCore.is_null(request.live_script_content):
            body['liveScriptContent'] = request.live_script_content
        if not DaraCore.is_null(request.open_small_talk):
            body['openSmallTalk'] = request.open_small_talk
        if not DaraCore.is_null(request.question_list):
            body['questionList'] = request.question_list
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitChatQuestion',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/chat/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitChatQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_chat_question(
        self,
        workspace_id: str,
        request: main_models.SubmitChatQuestionRequest,
    ) -> main_models.SubmitChatQuestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_chat_question_with_options(workspace_id, request, headers, runtime)

    async def submit_chat_question_async(
        self,
        workspace_id: str,
        request: main_models.SubmitChatQuestionRequest,
    ) -> main_models.SubmitChatQuestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_chat_question_with_options_async(workspace_id, request, headers, runtime)

    def update_document_with_options(
        self,
        workspace_id: str,
        request: main_models.UpdateDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['docId'] = request.doc_id
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.meta):
            body['meta'] = request.meta
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDocument',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/document/updateDocument',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_document_with_options_async(
        self,
        workspace_id: str,
        request: main_models.UpdateDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['docId'] = request.doc_id
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.meta):
            body['meta'] = request.meta
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDocument',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/document/updateDocument',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_document(
        self,
        workspace_id: str,
        request: main_models.UpdateDocumentRequest,
    ) -> main_models.UpdateDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_document_with_options(workspace_id, request, headers, runtime)

    async def update_document_async(
        self,
        workspace_id: str,
        request: main_models.UpdateDocumentRequest,
    ) -> main_models.UpdateDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_document_with_options_async(workspace_id, request, headers, runtime)

    def update_document_chunk_with_options(
        self,
        workspace_id: str,
        request: main_models.UpdateDocumentChunkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDocumentChunkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chunks):
            body['chunks'] = request.chunks
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDocumentChunk',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/updateDocumentChunk',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDocumentChunkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_document_chunk_with_options_async(
        self,
        workspace_id: str,
        request: main_models.UpdateDocumentChunkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDocumentChunkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chunks):
            body['chunks'] = request.chunks
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDocumentChunk',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/updateDocumentChunk',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDocumentChunkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_document_chunk(
        self,
        workspace_id: str,
        request: main_models.UpdateDocumentChunkRequest,
    ) -> main_models.UpdateDocumentChunkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_document_chunk_with_options(workspace_id, request, headers, runtime)

    async def update_document_chunk_async(
        self,
        workspace_id: str,
        request: main_models.UpdateDocumentChunkRequest,
    ) -> main_models.UpdateDocumentChunkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_document_chunk_with_options_async(workspace_id, request, headers, runtime)

    def update_library_with_options(
        self,
        workspace_id: str,
        request: main_models.UpdateLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLibraryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.index_setting):
            body['indexSetting'] = request.index_setting
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.library_name):
            body['libraryName'] = request.library_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLibrary',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/update',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_library_with_options_async(
        self,
        workspace_id: str,
        request: main_models.UpdateLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLibraryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.index_setting):
            body['indexSetting'] = request.index_setting
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.library_name):
            body['libraryName'] = request.library_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLibrary',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/update',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_library(
        self,
        workspace_id: str,
        request: main_models.UpdateLibraryRequest,
    ) -> main_models.UpdateLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_library_with_options(workspace_id, request, headers, runtime)

    async def update_library_async(
        self,
        workspace_id: str,
        request: main_models.UpdateLibraryRequest,
    ) -> main_models.UpdateLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_library_with_options_async(workspace_id, request, headers, runtime)

    def update_qa_library_with_options(
        self,
        workspace_id: str,
        request: main_models.UpdateQaLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQaLibraryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.parse_qa_results):
            body['parseQaResults'] = request.parse_qa_results
        if not DaraCore.is_null(request.qa_library_id):
            body['qaLibraryId'] = request.qa_library_id
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQaLibrary',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/qa/upload',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQaLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_qa_library_with_options_async(
        self,
        workspace_id: str,
        request: main_models.UpdateQaLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQaLibraryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.parse_qa_results):
            body['parseQaResults'] = request.parse_qa_results
        if not DaraCore.is_null(request.qa_library_id):
            body['qaLibraryId'] = request.qa_library_id
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQaLibrary',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/virtualHuman/qa/upload',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQaLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_qa_library(
        self,
        workspace_id: str,
        request: main_models.UpdateQaLibraryRequest,
    ) -> main_models.UpdateQaLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_qa_library_with_options(workspace_id, request, headers, runtime)

    async def update_qa_library_async(
        self,
        workspace_id: str,
        request: main_models.UpdateQaLibraryRequest,
    ) -> main_models.UpdateQaLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_qa_library_with_options_async(workspace_id, request, headers, runtime)

    def upload_document_with_options(
        self,
        workspace_id: str,
        request: main_models.UploadDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['data'] = request.data
        if not DaraCore.is_null(request.file_name):
            body['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            body['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadDocument',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/document/upload',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_document_with_options_async(
        self,
        workspace_id: str,
        request: main_models.UploadDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['data'] = request.data
        if not DaraCore.is_null(request.file_name):
            body['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            body['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadDocument',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/api/library/document/upload',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_document(
        self,
        workspace_id: str,
        request: main_models.UploadDocumentRequest,
    ) -> main_models.UploadDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upload_document_with_options(workspace_id, request, headers, runtime)

    async def upload_document_async(
        self,
        workspace_id: str,
        request: main_models.UploadDocumentRequest,
    ) -> main_models.UploadDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upload_document_with_options_async(workspace_id, request, headers, runtime)

    def upload_document_advance(
        self,
        workspace_id: str,
        request: main_models.UploadDocumentAdvanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadDocumentResponse:
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
            'Product': 'DianJin',
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
        upload_document_req = main_models.UploadDocumentRequest()
        Utils.convert(request, upload_document_req)
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
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            upload_document_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        upload_document_resp = self.upload_document_with_options(workspace_id, upload_document_req, headers, runtime)
        return upload_document_resp

    async def upload_document_advance_async(
        self,
        workspace_id: str,
        request: main_models.UploadDocumentAdvanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadDocumentResponse:
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
            'Product': 'DianJin',
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
        upload_document_req = main_models.UploadDocumentRequest()
        Utils.convert(request, upload_document_req)
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
                'host': f"{auth_response_body.get('Bucket')}.{Utils.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            upload_document_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        upload_document_resp = await self.upload_document_with_options_async(workspace_id, upload_document_req, headers, runtime)
        return upload_document_resp
