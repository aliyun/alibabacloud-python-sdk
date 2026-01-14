# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_energyexpertexternal20220923 import models as main_models
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
        self._endpoint = self.get_endpoint('energyexpertexternal', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_folder_with_options(
        self,
        request: main_models.AddFolderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddFolderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.folder_name):
            body['folderName'] = request.folder_name
        if not DaraCore.is_null(request.parent_folder_id):
            body['parentFolderId'] = request.parent_folder_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddFolder',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aidoc/folder/add',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_folder_with_options_async(
        self,
        request: main_models.AddFolderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddFolderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.folder_name):
            body['folderName'] = request.folder_name
        if not DaraCore.is_null(request.parent_folder_id):
            body['parentFolderId'] = request.parent_folder_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddFolder',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aidoc/folder/add',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_folder(
        self,
        request: main_models.AddFolderRequest,
    ) -> main_models.AddFolderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_folder_with_options(request, headers, runtime)

    async def add_folder_async(
        self,
        request: main_models.AddFolderRequest,
    ) -> main_models.AddFolderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_folder_with_options_async(request, headers, runtime)

    def analyze_vl_realtime_with_options(
        self,
        request: main_models.AnalyzeVlRealtimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AnalyzeVlRealtimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_url):
            query['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        if not DaraCore.is_null(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeVlRealtime',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aidoc/document/analyzeVlRealtime',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnalyzeVlRealtimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def analyze_vl_realtime_with_options_async(
        self,
        request: main_models.AnalyzeVlRealtimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AnalyzeVlRealtimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_url):
            query['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        if not DaraCore.is_null(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeVlRealtime',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aidoc/document/analyzeVlRealtime',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnalyzeVlRealtimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def analyze_vl_realtime(
        self,
        request: main_models.AnalyzeVlRealtimeRequest,
    ) -> main_models.AnalyzeVlRealtimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.analyze_vl_realtime_with_options(request, headers, runtime)

    async def analyze_vl_realtime_async(
        self,
        request: main_models.AnalyzeVlRealtimeRequest,
    ) -> main_models.AnalyzeVlRealtimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.analyze_vl_realtime_with_options_async(request, headers, runtime)

    def analyze_vl_realtime_advance(
        self,
        request: main_models.AnalyzeVlRealtimeAdvanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AnalyzeVlRealtimeResponse:
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
            'Product': 'energyExpertExternal',
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
        analyze_vl_realtime_req = main_models.AnalyzeVlRealtimeRequest()
        Utils.convert(request, analyze_vl_realtime_req)
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
            analyze_vl_realtime_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        analyze_vl_realtime_resp = self.analyze_vl_realtime_with_options(analyze_vl_realtime_req, headers, runtime)
        return analyze_vl_realtime_resp

    async def analyze_vl_realtime_advance_async(
        self,
        request: main_models.AnalyzeVlRealtimeAdvanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AnalyzeVlRealtimeResponse:
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
            'Product': 'energyExpertExternal',
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
        analyze_vl_realtime_req = main_models.AnalyzeVlRealtimeRequest()
        Utils.convert(request, analyze_vl_realtime_req)
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
            analyze_vl_realtime_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        analyze_vl_realtime_resp = await self.analyze_vl_realtime_with_options_async(analyze_vl_realtime_req, headers, runtime)
        return analyze_vl_realtime_resp

    def batch_save_instruction_status_with_options(
        self,
        request: main_models.BatchSaveInstructionStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchSaveInstructionStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.factory_id):
            body['factoryId'] = request.factory_id
        if not DaraCore.is_null(request.p_key):
            body['pKey'] = request.p_key
        if not DaraCore.is_null(request.status_list):
            body['statusList'] = request.status_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchSaveInstructionStatus',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/hvac/batchSaveInstructionStatus',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSaveInstructionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_save_instruction_status_with_options_async(
        self,
        request: main_models.BatchSaveInstructionStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchSaveInstructionStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.factory_id):
            body['factoryId'] = request.factory_id
        if not DaraCore.is_null(request.p_key):
            body['pKey'] = request.p_key
        if not DaraCore.is_null(request.status_list):
            body['statusList'] = request.status_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchSaveInstructionStatus',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/hvac/batchSaveInstructionStatus',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSaveInstructionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_save_instruction_status(
        self,
        request: main_models.BatchSaveInstructionStatusRequest,
    ) -> main_models.BatchSaveInstructionStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_save_instruction_status_with_options(request, headers, runtime)

    async def batch_save_instruction_status_async(
        self,
        request: main_models.BatchSaveInstructionStatusRequest,
    ) -> main_models.BatchSaveInstructionStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_save_instruction_status_with_options_async(request, headers, runtime)

    def batch_update_system_running_plan_with_options(
        self,
        request: main_models.BatchUpdateSystemRunningPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchUpdateSystemRunningPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.control_type):
            body['controlType'] = request.control_type
        if not DaraCore.is_null(request.date_type):
            body['dateType'] = request.date_type
        if not DaraCore.is_null(request.earliest_startup_time):
            body['earliestStartupTime'] = request.earliest_startup_time
        if not DaraCore.is_null(request.end_time):
            body['endTime'] = request.end_time
        if not DaraCore.is_null(request.factory_id):
            body['factoryId'] = request.factory_id
        if not DaraCore.is_null(request.latest_shutdown_time):
            body['latestShutdownTime'] = request.latest_shutdown_time
        if not DaraCore.is_null(request.max_carbon_dioxide):
            body['maxCarbonDioxide'] = request.max_carbon_dioxide
        if not DaraCore.is_null(request.max_tem):
            body['maxTem'] = request.max_tem
        if not DaraCore.is_null(request.min_tem):
            body['minTem'] = request.min_tem
        if not DaraCore.is_null(request.season_mode):
            body['seasonMode'] = request.season_mode
        if not DaraCore.is_null(request.start_time):
            body['startTime'] = request.start_time
        if not DaraCore.is_null(request.system_id):
            body['systemId'] = request.system_id
        if not DaraCore.is_null(request.working_end_time):
            body['workingEndTime'] = request.working_end_time
        if not DaraCore.is_null(request.working_start_time):
            body['workingStartTime'] = request.working_start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchUpdateSystemRunningPlan',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/hvac/batchUpdateSystemRunningPlan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUpdateSystemRunningPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_update_system_running_plan_with_options_async(
        self,
        request: main_models.BatchUpdateSystemRunningPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchUpdateSystemRunningPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.control_type):
            body['controlType'] = request.control_type
        if not DaraCore.is_null(request.date_type):
            body['dateType'] = request.date_type
        if not DaraCore.is_null(request.earliest_startup_time):
            body['earliestStartupTime'] = request.earliest_startup_time
        if not DaraCore.is_null(request.end_time):
            body['endTime'] = request.end_time
        if not DaraCore.is_null(request.factory_id):
            body['factoryId'] = request.factory_id
        if not DaraCore.is_null(request.latest_shutdown_time):
            body['latestShutdownTime'] = request.latest_shutdown_time
        if not DaraCore.is_null(request.max_carbon_dioxide):
            body['maxCarbonDioxide'] = request.max_carbon_dioxide
        if not DaraCore.is_null(request.max_tem):
            body['maxTem'] = request.max_tem
        if not DaraCore.is_null(request.min_tem):
            body['minTem'] = request.min_tem
        if not DaraCore.is_null(request.season_mode):
            body['seasonMode'] = request.season_mode
        if not DaraCore.is_null(request.start_time):
            body['startTime'] = request.start_time
        if not DaraCore.is_null(request.system_id):
            body['systemId'] = request.system_id
        if not DaraCore.is_null(request.working_end_time):
            body['workingEndTime'] = request.working_end_time
        if not DaraCore.is_null(request.working_start_time):
            body['workingStartTime'] = request.working_start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchUpdateSystemRunningPlan',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/hvac/batchUpdateSystemRunningPlan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUpdateSystemRunningPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_update_system_running_plan(
        self,
        request: main_models.BatchUpdateSystemRunningPlanRequest,
    ) -> main_models.BatchUpdateSystemRunningPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_update_system_running_plan_with_options(request, headers, runtime)

    async def batch_update_system_running_plan_async(
        self,
        request: main_models.BatchUpdateSystemRunningPlanRequest,
    ) -> main_models.BatchUpdateSystemRunningPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_update_system_running_plan_with_options_async(request, headers, runtime)

    def chat_with_options(
        self,
        request: main_models.ChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_ids):
            body['documentIds'] = request.document_ids
        if not DaraCore.is_null(request.question):
            body['question'] = request.question
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Chat',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_with_options_async(
        self,
        request: main_models.ChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_ids):
            body['documentIds'] = request.document_ids
        if not DaraCore.is_null(request.question):
            body['question'] = request.question
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Chat',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat(
        self,
        request: main_models.ChatRequest,
    ) -> main_models.ChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.chat_with_options(request, headers, runtime)

    async def chat_async(
        self,
        request: main_models.ChatRequest,
    ) -> main_models.ChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.chat_with_options_async(request, headers, runtime)

    def chat_stream_with_sse(
        self,
        request: main_models.ChatStreamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.ChatStreamResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_ids):
            body['documentIds'] = request.document_ids
        if not DaraCore.is_null(request.question):
            body['question'] = request.question
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChatStream',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/chat/stream',
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
                main_models.ChatStreamResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def chat_stream_with_sse_async(
        self,
        request: main_models.ChatStreamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.ChatStreamResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_ids):
            body['documentIds'] = request.document_ids
        if not DaraCore.is_null(request.question):
            body['question'] = request.question
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChatStream',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/chat/stream',
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
                main_models.ChatStreamResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def chat_stream_with_options(
        self,
        request: main_models.ChatStreamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChatStreamResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_ids):
            body['documentIds'] = request.document_ids
        if not DaraCore.is_null(request.question):
            body['question'] = request.question
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChatStream',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/chat/stream',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_stream_with_options_async(
        self,
        request: main_models.ChatStreamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChatStreamResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_ids):
            body['documentIds'] = request.document_ids
        if not DaraCore.is_null(request.question):
            body['question'] = request.question
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChatStream',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/chat/stream',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_stream(
        self,
        request: main_models.ChatStreamRequest,
    ) -> main_models.ChatStreamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.chat_stream_with_options(request, headers, runtime)

    async def chat_stream_async(
        self,
        request: main_models.ChatStreamRequest,
    ) -> main_models.ChatStreamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.chat_stream_with_options_async(request, headers, runtime)

    def create_chat_session_with_options(
        self,
        request: main_models.CreateChatSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.folder_id):
            body['folderId'] = request.folder_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatSession',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/chat/session/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chat_session_with_options_async(
        self,
        request: main_models.CreateChatSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.folder_id):
            body['folderId'] = request.folder_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatSession',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/chat/session/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chat_session(
        self,
        request: main_models.CreateChatSessionRequest,
    ) -> main_models.CreateChatSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_chat_session_with_options(request, headers, runtime)

    async def create_chat_session_async(
        self,
        request: main_models.CreateChatSessionRequest,
    ) -> main_models.CreateChatSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_chat_session_with_options_async(request, headers, runtime)

    def delete_document_with_options(
        self,
        request: main_models.DeleteDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocumentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocument',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aidoc/document/delete',
            method = 'DELETE',
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
        request: main_models.DeleteDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocumentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocument',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aidoc/document/delete',
            method = 'DELETE',
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
        request: main_models.DeleteDocumentRequest,
    ) -> main_models.DeleteDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_document_with_options(request, headers, runtime)

    async def delete_document_async(
        self,
        request: main_models.DeleteDocumentRequest,
    ) -> main_models.DeleteDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_document_with_options_async(request, headers, runtime)

    def delete_folder_with_options(
        self,
        request: main_models.DeleteFolderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFolderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.folder_id):
            query['folderId'] = request.folder_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFolder',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aidoc/folder/delete',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_folder_with_options_async(
        self,
        request: main_models.DeleteFolderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFolderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.folder_id):
            query['folderId'] = request.folder_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFolder',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aidoc/folder/delete',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_folder(
        self,
        request: main_models.DeleteFolderRequest,
    ) -> main_models.DeleteFolderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_folder_with_options(request, headers, runtime)

    async def delete_folder_async(
        self,
        request: main_models.DeleteFolderRequest,
    ) -> main_models.DeleteFolderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_folder_with_options_async(request, headers, runtime)

    def detail_document_with_options(
        self,
        request: main_models.DetailDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DetailDocumentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetailDocument',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aidoc/document/detail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetailDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def detail_document_with_options_async(
        self,
        request: main_models.DetailDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DetailDocumentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetailDocument',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aidoc/document/detail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetailDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detail_document(
        self,
        request: main_models.DetailDocumentRequest,
    ) -> main_models.DetailDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.detail_document_with_options(request, headers, runtime)

    async def detail_document_async(
        self,
        request: main_models.DetailDocumentRequest,
    ) -> main_models.DetailDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.detail_document_with_options_async(request, headers, runtime)

    def edit_prohibited_devices_with_options(
        self,
        request: main_models.EditProhibitedDevicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EditProhibitedDevicesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.factory_id):
            body['factoryId'] = request.factory_id
        if not DaraCore.is_null(request.hvac_device_config_volist):
            body['hvacDeviceConfigVOList'] = request.hvac_device_config_volist
        if not DaraCore.is_null(request.system_id):
            body['systemId'] = request.system_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditProhibitedDevices',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/hvac/editProhibitedDevices',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditProhibitedDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_prohibited_devices_with_options_async(
        self,
        request: main_models.EditProhibitedDevicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EditProhibitedDevicesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.factory_id):
            body['factoryId'] = request.factory_id
        if not DaraCore.is_null(request.hvac_device_config_volist):
            body['hvacDeviceConfigVOList'] = request.hvac_device_config_volist
        if not DaraCore.is_null(request.system_id):
            body['systemId'] = request.system_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditProhibitedDevices',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/hvac/editProhibitedDevices',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditProhibitedDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_prohibited_devices(
        self,
        request: main_models.EditProhibitedDevicesRequest,
    ) -> main_models.EditProhibitedDevicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.edit_prohibited_devices_with_options(request, headers, runtime)

    async def edit_prohibited_devices_async(
        self,
        request: main_models.EditProhibitedDevicesRequest,
    ) -> main_models.EditProhibitedDevicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.edit_prohibited_devices_with_options_async(request, headers, runtime)

    def edit_unfavorable_area_devices_with_options(
        self,
        request: main_models.EditUnfavorableAreaDevicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EditUnfavorableAreaDevicesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.factory_id):
            body['factoryId'] = request.factory_id
        if not DaraCore.is_null(request.hvac_device_config_volist):
            body['hvacDeviceConfigVOList'] = request.hvac_device_config_volist
        if not DaraCore.is_null(request.system_id):
            body['systemId'] = request.system_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditUnfavorableAreaDevices',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/hvac/editUnfavorableAreaDevices',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditUnfavorableAreaDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_unfavorable_area_devices_with_options_async(
        self,
        request: main_models.EditUnfavorableAreaDevicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EditUnfavorableAreaDevicesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.factory_id):
            body['factoryId'] = request.factory_id
        if not DaraCore.is_null(request.hvac_device_config_volist):
            body['hvacDeviceConfigVOList'] = request.hvac_device_config_volist
        if not DaraCore.is_null(request.system_id):
            body['systemId'] = request.system_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditUnfavorableAreaDevices',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/hvac/editUnfavorableAreaDevices',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditUnfavorableAreaDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_unfavorable_area_devices(
        self,
        request: main_models.EditUnfavorableAreaDevicesRequest,
    ) -> main_models.EditUnfavorableAreaDevicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.edit_unfavorable_area_devices_with_options(request, headers, runtime)

    async def edit_unfavorable_area_devices_async(
        self,
        request: main_models.EditUnfavorableAreaDevicesRequest,
    ) -> main_models.EditUnfavorableAreaDevicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.edit_unfavorable_area_devices_with_options_async(request, headers, runtime)

    def generate_result_with_options(
        self,
        request: main_models.GenerateResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateResult',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/generate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_result_with_options_async(
        self,
        request: main_models.GenerateResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateResult',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/generate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_result(
        self,
        request: main_models.GenerateResultRequest,
    ) -> main_models.GenerateResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.generate_result_with_options(request, headers, runtime)

    async def generate_result_async(
        self,
        request: main_models.GenerateResultRequest,
    ) -> main_models.GenerateResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.generate_result_with_options_async(request, headers, runtime)

    def get_area_elec_constitute_with_options(
        self,
        request: main_models.GetAreaElecConstituteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAreaElecConstituteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.year):
            body['year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAreaElecConstitute',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/analysis/elec/area',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAreaElecConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_area_elec_constitute_with_options_async(
        self,
        request: main_models.GetAreaElecConstituteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAreaElecConstituteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.year):
            body['year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAreaElecConstitute',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/analysis/elec/area',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAreaElecConstituteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_area_elec_constitute(
        self,
        request: main_models.GetAreaElecConstituteRequest,
    ) -> main_models.GetAreaElecConstituteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_area_elec_constitute_with_options(request, headers, runtime)

    async def get_area_elec_constitute_async(
        self,
        request: main_models.GetAreaElecConstituteRequest,
    ) -> main_models.GetAreaElecConstituteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_area_elec_constitute_with_options_async(request, headers, runtime)

    def get_carbon_emission_trend_with_options(
        self,
        request: main_models.GetCarbonEmissionTrendRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCarbonEmissionTrendResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.module_code):
            body['moduleCode'] = request.module_code
        if not DaraCore.is_null(request.module_type):
            body['moduleType'] = request.module_type
        if not DaraCore.is_null(request.trend_type):
            body['trendType'] = request.trend_type
        if not DaraCore.is_null(request.year_list):
            body['yearList'] = request.year_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCarbonEmissionTrend',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/analysis/trend',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCarbonEmissionTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_carbon_emission_trend_with_options_async(
        self,
        request: main_models.GetCarbonEmissionTrendRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCarbonEmissionTrendResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.module_code):
            body['moduleCode'] = request.module_code
        if not DaraCore.is_null(request.module_type):
            body['moduleType'] = request.module_type
        if not DaraCore.is_null(request.trend_type):
            body['trendType'] = request.trend_type
        if not DaraCore.is_null(request.year_list):
            body['yearList'] = request.year_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCarbonEmissionTrend',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/analysis/trend',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCarbonEmissionTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_carbon_emission_trend(
        self,
        request: main_models.GetCarbonEmissionTrendRequest,
    ) -> main_models.GetCarbonEmissionTrendResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_carbon_emission_trend_with_options(request, headers, runtime)

    async def get_carbon_emission_trend_async(
        self,
        request: main_models.GetCarbonEmissionTrendRequest,
    ) -> main_models.GetCarbonEmissionTrendResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_carbon_emission_trend_with_options_async(request, headers, runtime)

    def get_chat_folder_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetChatFolderListResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetChatFolderList',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/chat/folder/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatFolderListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_folder_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetChatFolderListResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetChatFolderList',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/chat/folder/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatFolderListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat_folder_list(self) -> main_models.GetChatFolderListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_chat_folder_list_with_options(headers, runtime)

    async def get_chat_folder_list_async(self) -> main_models.GetChatFolderListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_chat_folder_list_with_options_async(headers, runtime)

    def get_chat_list_with_options(
        self,
        request: main_models.GetChatListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetChatListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetChatList',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/chat/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_list_with_options_async(
        self,
        request: main_models.GetChatListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetChatListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetChatList',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/chat/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat_list(
        self,
        request: main_models.GetChatListRequest,
    ) -> main_models.GetChatListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_chat_list_with_options(request, headers, runtime)

    async def get_chat_list_async(
        self,
        request: main_models.GetChatListRequest,
    ) -> main_models.GetChatListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_chat_list_with_options_async(request, headers, runtime)

    def get_chat_session_list_with_options(
        self,
        request: main_models.GetChatSessionListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetChatSessionListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['currentPage'] = request.current_page
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetChatSessionList',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/chat/session/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatSessionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_session_list_with_options_async(
        self,
        request: main_models.GetChatSessionListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetChatSessionListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['currentPage'] = request.current_page
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetChatSessionList',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/chat/session/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatSessionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat_session_list(
        self,
        request: main_models.GetChatSessionListRequest,
    ) -> main_models.GetChatSessionListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_chat_session_list_with_options(request, headers, runtime)

    async def get_chat_session_list_async(
        self,
        request: main_models.GetChatSessionListRequest,
    ) -> main_models.GetChatSessionListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_chat_session_list_with_options_async(request, headers, runtime)

    def get_data_item_list_with_options(
        self,
        request: main_models.GetDataItemListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataItemListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDataItemList',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/data/item/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataItemListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_item_list_with_options_async(
        self,
        request: main_models.GetDataItemListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataItemListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDataItemList',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/data/item/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataItemListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_item_list(
        self,
        request: main_models.GetDataItemListRequest,
    ) -> main_models.GetDataItemListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_data_item_list_with_options(request, headers, runtime)

    async def get_data_item_list_async(
        self,
        request: main_models.GetDataItemListRequest,
    ) -> main_models.GetDataItemListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_data_item_list_with_options_async(request, headers, runtime)

    def get_data_quality_analysis_with_options(
        self,
        request: main_models.GetDataQualityAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.data_quality_evaluation_type):
            body['dataQualityEvaluationType'] = request.data_quality_evaluation_type
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityAnalysis',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/data/quality/analysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_quality_analysis_with_options_async(
        self,
        request: main_models.GetDataQualityAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataQualityAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.data_quality_evaluation_type):
            body['dataQualityEvaluationType'] = request.data_quality_evaluation_type
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDataQualityAnalysis',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/data/quality/analysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataQualityAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_quality_analysis(
        self,
        request: main_models.GetDataQualityAnalysisRequest,
    ) -> main_models.GetDataQualityAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_data_quality_analysis_with_options(request, headers, runtime)

    async def get_data_quality_analysis_async(
        self,
        request: main_models.GetDataQualityAnalysisRequest,
    ) -> main_models.GetDataQualityAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_data_quality_analysis_with_options_async(request, headers, runtime)

    def get_device_info_with_options(
        self,
        request: main_models.GetDeviceInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['deviceId'] = request.device_id
        if not DaraCore.is_null(request.ds):
            query['ds'] = request.ds
        if not DaraCore.is_null(request.factory_id):
            query['factoryId'] = request.factory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceInfo',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/external/getDeviceInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_info_with_options_async(
        self,
        request: main_models.GetDeviceInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['deviceId'] = request.device_id
        if not DaraCore.is_null(request.ds):
            query['ds'] = request.ds
        if not DaraCore.is_null(request.factory_id):
            query['factoryId'] = request.factory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceInfo',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/external/getDeviceInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_info(
        self,
        request: main_models.GetDeviceInfoRequest,
    ) -> main_models.GetDeviceInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_device_info_with_options(request, headers, runtime)

    async def get_device_info_async(
        self,
        request: main_models.GetDeviceInfoRequest,
    ) -> main_models.GetDeviceInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_device_info_with_options_async(request, headers, runtime)

    def get_device_list_with_options(
        self,
        request: main_models.GetDeviceListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.factory_id):
            query['factoryId'] = request.factory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceList',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/external/getDeviceList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_list_with_options_async(
        self,
        request: main_models.GetDeviceListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.factory_id):
            query['factoryId'] = request.factory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceList',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/external/getDeviceList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_list(
        self,
        request: main_models.GetDeviceListRequest,
    ) -> main_models.GetDeviceListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_device_list_with_options(request, headers, runtime)

    async def get_device_list_async(
        self,
        request: main_models.GetDeviceListRequest,
    ) -> main_models.GetDeviceListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_device_list_with_options_async(request, headers, runtime)

    def get_doc_extraction_result_with_options(
        self,
        request: main_models.GetDocExtractionResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocExtractionResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocExtractionResult',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/getDocExtractionResult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocExtractionResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doc_extraction_result_with_options_async(
        self,
        request: main_models.GetDocExtractionResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocExtractionResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocExtractionResult',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/getDocExtractionResult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocExtractionResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doc_extraction_result(
        self,
        request: main_models.GetDocExtractionResultRequest,
    ) -> main_models.GetDocExtractionResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_doc_extraction_result_with_options(request, headers, runtime)

    async def get_doc_extraction_result_async(
        self,
        request: main_models.GetDocExtractionResultRequest,
    ) -> main_models.GetDocExtractionResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_doc_extraction_result_with_options_async(request, headers, runtime)

    def get_doc_parsing_result_with_options(
        self,
        request: main_models.GetDocParsingResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocParsingResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.return_format):
            body['returnFormat'] = request.return_format
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocParsingResult',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/getDocParsingResult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocParsingResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doc_parsing_result_with_options_async(
        self,
        request: main_models.GetDocParsingResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocParsingResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.return_format):
            body['returnFormat'] = request.return_format
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocParsingResult',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/getDocParsingResult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocParsingResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doc_parsing_result(
        self,
        request: main_models.GetDocParsingResultRequest,
    ) -> main_models.GetDocParsingResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_doc_parsing_result_with_options(request, headers, runtime)

    async def get_doc_parsing_result_async(
        self,
        request: main_models.GetDocParsingResultRequest,
    ) -> main_models.GetDocParsingResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_doc_parsing_result_with_options_async(request, headers, runtime)

    def get_document_analyze_result_with_options(
        self,
        request: main_models.GetDocumentAnalyzeResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentAnalyzeResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.job_id):
            body['jobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentAnalyzeResult',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aidoc/document/getDocumentAnalyzeResult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentAnalyzeResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_analyze_result_with_options_async(
        self,
        request: main_models.GetDocumentAnalyzeResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentAnalyzeResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.job_id):
            body['jobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentAnalyzeResult',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aidoc/document/getDocumentAnalyzeResult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentAnalyzeResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_analyze_result(
        self,
        request: main_models.GetDocumentAnalyzeResultRequest,
    ) -> main_models.GetDocumentAnalyzeResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_document_analyze_result_with_options(request, headers, runtime)

    async def get_document_analyze_result_async(
        self,
        request: main_models.GetDocumentAnalyzeResultRequest,
    ) -> main_models.GetDocumentAnalyzeResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_document_analyze_result_with_options_async(request, headers, runtime)

    def get_elec_constitute_with_options(
        self,
        request: main_models.GetElecConstituteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetElecConstituteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.year):
            body['year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetElecConstitute',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/analysis/elec/constitute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetElecConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_elec_constitute_with_options_async(
        self,
        request: main_models.GetElecConstituteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetElecConstituteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.year):
            body['year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetElecConstitute',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/analysis/elec/constitute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetElecConstituteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_elec_constitute(
        self,
        request: main_models.GetElecConstituteRequest,
    ) -> main_models.GetElecConstituteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_elec_constitute_with_options(request, headers, runtime)

    async def get_elec_constitute_async(
        self,
        request: main_models.GetElecConstituteRequest,
    ) -> main_models.GetElecConstituteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_elec_constitute_with_options_async(request, headers, runtime)

    def get_elec_trend_with_options(
        self,
        request: main_models.GetElecTrendRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetElecTrendResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.year_list):
            body['yearList'] = request.year_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetElecTrend',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/analysis/elec/trend',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetElecTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_elec_trend_with_options_async(
        self,
        request: main_models.GetElecTrendRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetElecTrendResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.year_list):
            body['yearList'] = request.year_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetElecTrend',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/analysis/elec/trend',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetElecTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_elec_trend(
        self,
        request: main_models.GetElecTrendRequest,
    ) -> main_models.GetElecTrendResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_elec_trend_with_options(request, headers, runtime)

    async def get_elec_trend_async(
        self,
        request: main_models.GetElecTrendRequest,
    ) -> main_models.GetElecTrendResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_elec_trend_with_options_async(request, headers, runtime)

    def get_emission_source_constitute_with_options(
        self,
        request: main_models.GetEmissionSourceConstituteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEmissionSourceConstituteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.module_code):
            body['moduleCode'] = request.module_code
        if not DaraCore.is_null(request.module_type):
            body['moduleType'] = request.module_type
        if not DaraCore.is_null(request.year):
            body['year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEmissionSourceConstitute',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/analysis/constitute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEmissionSourceConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_emission_source_constitute_with_options_async(
        self,
        request: main_models.GetEmissionSourceConstituteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEmissionSourceConstituteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.module_code):
            body['moduleCode'] = request.module_code
        if not DaraCore.is_null(request.module_type):
            body['moduleType'] = request.module_type
        if not DaraCore.is_null(request.year):
            body['year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEmissionSourceConstitute',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/analysis/constitute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEmissionSourceConstituteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_emission_source_constitute(
        self,
        request: main_models.GetEmissionSourceConstituteRequest,
    ) -> main_models.GetEmissionSourceConstituteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_emission_source_constitute_with_options(request, headers, runtime)

    async def get_emission_source_constitute_async(
        self,
        request: main_models.GetEmissionSourceConstituteRequest,
    ) -> main_models.GetEmissionSourceConstituteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_emission_source_constitute_with_options_async(request, headers, runtime)

    def get_emission_summary_with_options(
        self,
        request: main_models.GetEmissionSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEmissionSummaryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.module_code):
            body['moduleCode'] = request.module_code
        if not DaraCore.is_null(request.module_type):
            body['moduleType'] = request.module_type
        if not DaraCore.is_null(request.year):
            body['year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEmissionSummary',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/analysis/summary',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEmissionSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_emission_summary_with_options_async(
        self,
        request: main_models.GetEmissionSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEmissionSummaryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.module_code):
            body['moduleCode'] = request.module_code
        if not DaraCore.is_null(request.module_type):
            body['moduleType'] = request.module_type
        if not DaraCore.is_null(request.year):
            body['year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEmissionSummary',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/analysis/summary',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEmissionSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_emission_summary(
        self,
        request: main_models.GetEmissionSummaryRequest,
    ) -> main_models.GetEmissionSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_emission_summary_with_options(request, headers, runtime)

    async def get_emission_summary_async(
        self,
        request: main_models.GetEmissionSummaryRequest,
    ) -> main_models.GetEmissionSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_emission_summary_with_options_async(request, headers, runtime)

    def get_epd_inventory_constitute_with_options(
        self,
        request: main_models.GetEpdInventoryConstituteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEpdInventoryConstituteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEpdInventoryConstitute',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/epd/inventory/constitute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEpdInventoryConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_epd_inventory_constitute_with_options_async(
        self,
        request: main_models.GetEpdInventoryConstituteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEpdInventoryConstituteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEpdInventoryConstitute',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/epd/inventory/constitute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEpdInventoryConstituteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_epd_inventory_constitute(
        self,
        request: main_models.GetEpdInventoryConstituteRequest,
    ) -> main_models.GetEpdInventoryConstituteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_epd_inventory_constitute_with_options(request, headers, runtime)

    async def get_epd_inventory_constitute_async(
        self,
        request: main_models.GetEpdInventoryConstituteRequest,
    ) -> main_models.GetEpdInventoryConstituteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_epd_inventory_constitute_with_options_async(request, headers, runtime)

    def get_epd_summary_with_options(
        self,
        request: main_models.GetEpdSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEpdSummaryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEpdSummary',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/epd/summary',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEpdSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_epd_summary_with_options_async(
        self,
        request: main_models.GetEpdSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEpdSummaryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEpdSummary',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/epd/summary',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEpdSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_epd_summary(
        self,
        request: main_models.GetEpdSummaryRequest,
    ) -> main_models.GetEpdSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_epd_summary_with_options(request, headers, runtime)

    async def get_epd_summary_async(
        self,
        request: main_models.GetEpdSummaryRequest,
    ) -> main_models.GetEpdSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_epd_summary_with_options_async(request, headers, runtime)

    def get_footprint_list_with_options(
        self,
        request: main_models.GetFootprintListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFootprintListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.current_page):
            body['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFootprintList',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/product/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFootprintListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_footprint_list_with_options_async(
        self,
        request: main_models.GetFootprintListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFootprintListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.current_page):
            body['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFootprintList',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/product/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFootprintListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_footprint_list(
        self,
        request: main_models.GetFootprintListRequest,
    ) -> main_models.GetFootprintListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_footprint_list_with_options(request, headers, runtime)

    async def get_footprint_list_async(
        self,
        request: main_models.GetFootprintListRequest,
    ) -> main_models.GetFootprintListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_footprint_list_with_options_async(request, headers, runtime)

    def get_gas_constitute_with_options(
        self,
        request: main_models.GetGasConstituteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGasConstituteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.module_code):
            body['moduleCode'] = request.module_code
        if not DaraCore.is_null(request.module_type):
            body['moduleType'] = request.module_type
        if not DaraCore.is_null(request.year):
            body['year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGasConstitute',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/analysis/gas/constitute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGasConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gas_constitute_with_options_async(
        self,
        request: main_models.GetGasConstituteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGasConstituteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.module_code):
            body['moduleCode'] = request.module_code
        if not DaraCore.is_null(request.module_type):
            body['moduleType'] = request.module_type
        if not DaraCore.is_null(request.year):
            body['year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGasConstitute',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/analysis/gas/constitute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGasConstituteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gas_constitute(
        self,
        request: main_models.GetGasConstituteRequest,
    ) -> main_models.GetGasConstituteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_gas_constitute_with_options(request, headers, runtime)

    async def get_gas_constitute_async(
        self,
        request: main_models.GetGasConstituteRequest,
    ) -> main_models.GetGasConstituteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_gas_constitute_with_options_async(request, headers, runtime)

    def get_gwp_benchmark_list_with_options(
        self,
        request: main_models.GetGwpBenchmarkListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGwpBenchmarkListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGwpBenchmarkList',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/gwp/benchmark/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGwpBenchmarkListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gwp_benchmark_list_with_options_async(
        self,
        request: main_models.GetGwpBenchmarkListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGwpBenchmarkListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGwpBenchmarkList',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/gwp/benchmark/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGwpBenchmarkListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gwp_benchmark_list(
        self,
        request: main_models.GetGwpBenchmarkListRequest,
    ) -> main_models.GetGwpBenchmarkListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_gwp_benchmark_list_with_options(request, headers, runtime)

    async def get_gwp_benchmark_list_async(
        self,
        request: main_models.GetGwpBenchmarkListRequest,
    ) -> main_models.GetGwpBenchmarkListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_gwp_benchmark_list_with_options_async(request, headers, runtime)

    def get_gwp_benchmark_summary_with_options(
        self,
        request: main_models.GetGwpBenchmarkSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGwpBenchmarkSummaryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGwpBenchmarkSummary',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/gwp/benchmark/summary',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGwpBenchmarkSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gwp_benchmark_summary_with_options_async(
        self,
        request: main_models.GetGwpBenchmarkSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGwpBenchmarkSummaryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGwpBenchmarkSummary',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/gwp/benchmark/summary',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGwpBenchmarkSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gwp_benchmark_summary(
        self,
        request: main_models.GetGwpBenchmarkSummaryRequest,
    ) -> main_models.GetGwpBenchmarkSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_gwp_benchmark_summary_with_options(request, headers, runtime)

    async def get_gwp_benchmark_summary_async(
        self,
        request: main_models.GetGwpBenchmarkSummaryRequest,
    ) -> main_models.GetGwpBenchmarkSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_gwp_benchmark_summary_with_options_async(request, headers, runtime)

    def get_gwp_inventory_constitute_with_options(
        self,
        request: main_models.GetGwpInventoryConstituteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGwpInventoryConstituteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGwpInventoryConstitute',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/gwp/inventory/constitute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGwpInventoryConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gwp_inventory_constitute_with_options_async(
        self,
        request: main_models.GetGwpInventoryConstituteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGwpInventoryConstituteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGwpInventoryConstitute',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/gwp/inventory/constitute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGwpInventoryConstituteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gwp_inventory_constitute(
        self,
        request: main_models.GetGwpInventoryConstituteRequest,
    ) -> main_models.GetGwpInventoryConstituteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_gwp_inventory_constitute_with_options(request, headers, runtime)

    async def get_gwp_inventory_constitute_async(
        self,
        request: main_models.GetGwpInventoryConstituteRequest,
    ) -> main_models.GetGwpInventoryConstituteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_gwp_inventory_constitute_with_options_async(request, headers, runtime)

    def get_gwp_inventory_summary_with_options(
        self,
        request: main_models.GetGwpInventorySummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGwpInventorySummaryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGwpInventorySummary',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/gwp/inventory/summary',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGwpInventorySummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gwp_inventory_summary_with_options_async(
        self,
        request: main_models.GetGwpInventorySummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGwpInventorySummaryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGwpInventorySummary',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/gwp/inventory/summary',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGwpInventorySummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gwp_inventory_summary(
        self,
        request: main_models.GetGwpInventorySummaryRequest,
    ) -> main_models.GetGwpInventorySummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_gwp_inventory_summary_with_options(request, headers, runtime)

    async def get_gwp_inventory_summary_async(
        self,
        request: main_models.GetGwpInventorySummaryRequest,
    ) -> main_models.GetGwpInventorySummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_gwp_inventory_summary_with_options_async(request, headers, runtime)

    def get_inventory_list_with_options(
        self,
        request: main_models.GetInventoryListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInventoryListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.emission_type):
            body['emissionType'] = request.emission_type
        if not DaraCore.is_null(request.group):
            body['group'] = request.group
        if not DaraCore.is_null(request.method_type):
            body['methodType'] = request.method_type
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInventoryList',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/inventory/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInventoryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_inventory_list_with_options_async(
        self,
        request: main_models.GetInventoryListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInventoryListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.emission_type):
            body['emissionType'] = request.emission_type
        if not DaraCore.is_null(request.group):
            body['group'] = request.group
        if not DaraCore.is_null(request.method_type):
            body['methodType'] = request.method_type
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInventoryList',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/inventory/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInventoryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_inventory_list(
        self,
        request: main_models.GetInventoryListRequest,
    ) -> main_models.GetInventoryListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_inventory_list_with_options(request, headers, runtime)

    async def get_inventory_list_async(
        self,
        request: main_models.GetInventoryListRequest,
    ) -> main_models.GetInventoryListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_inventory_list_with_options_async(request, headers, runtime)

    def get_org_and_factory_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOrgAndFactoryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetOrgAndFactory',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/external/getOrgAndFactory',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrgAndFactoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_org_and_factory_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOrgAndFactoryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetOrgAndFactory',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/external/getOrgAndFactory',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrgAndFactoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_org_and_factory(self) -> main_models.GetOrgAndFactoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_org_and_factory_with_options(headers, runtime)

    async def get_org_and_factory_async(self) -> main_models.GetOrgAndFactoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_org_and_factory_with_options_async(headers, runtime)

    def get_org_constitute_with_options(
        self,
        request: main_models.GetOrgConstituteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOrgConstituteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.module_code):
            body['moduleCode'] = request.module_code
        if not DaraCore.is_null(request.module_type):
            body['moduleType'] = request.module_type
        if not DaraCore.is_null(request.year):
            body['year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOrgConstitute',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/analysis/org',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrgConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_org_constitute_with_options_async(
        self,
        request: main_models.GetOrgConstituteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOrgConstituteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.module_code):
            body['moduleCode'] = request.module_code
        if not DaraCore.is_null(request.module_type):
            body['moduleType'] = request.module_type
        if not DaraCore.is_null(request.year):
            body['year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOrgConstitute',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/analysis/org',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrgConstituteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_org_constitute(
        self,
        request: main_models.GetOrgConstituteRequest,
    ) -> main_models.GetOrgConstituteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_org_constitute_with_options(request, headers, runtime)

    async def get_org_constitute_async(
        self,
        request: main_models.GetOrgConstituteRequest,
    ) -> main_models.GetOrgConstituteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_org_constitute_with_options_async(request, headers, runtime)

    def get_pcr_info_with_options(
        self,
        request: main_models.GetPcrInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPcrInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPcrInfo',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/pcr/detail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPcrInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pcr_info_with_options_async(
        self,
        request: main_models.GetPcrInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPcrInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPcrInfo',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/pcr/detail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPcrInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pcr_info(
        self,
        request: main_models.GetPcrInfoRequest,
    ) -> main_models.GetPcrInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pcr_info_with_options(request, headers, runtime)

    async def get_pcr_info_async(
        self,
        request: main_models.GetPcrInfoRequest,
    ) -> main_models.GetPcrInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pcr_info_with_options_async(request, headers, runtime)

    def get_reduction_proposal_with_options(
        self,
        request: main_models.GetReductionProposalRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetReductionProposalResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.data_quality_evaluation_type):
            body['dataQualityEvaluationType'] = request.data_quality_evaluation_type
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetReductionProposal',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/reduction/proposal',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetReductionProposalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_reduction_proposal_with_options_async(
        self,
        request: main_models.GetReductionProposalRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetReductionProposalResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.data_quality_evaluation_type):
            body['dataQualityEvaluationType'] = request.data_quality_evaluation_type
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetReductionProposal',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/reduction/proposal',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetReductionProposalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_reduction_proposal(
        self,
        request: main_models.GetReductionProposalRequest,
    ) -> main_models.GetReductionProposalResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_reduction_proposal_with_options(request, headers, runtime)

    async def get_reduction_proposal_async(
        self,
        request: main_models.GetReductionProposalRequest,
    ) -> main_models.GetReductionProposalResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_reduction_proposal_with_options_async(request, headers, runtime)

    def get_vlextraction_result_with_options(
        self,
        request: main_models.GetVLExtractionResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVLExtractionResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVLExtractionResult',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/getVLExtractionResult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVLExtractionResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vlextraction_result_with_options_async(
        self,
        request: main_models.GetVLExtractionResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVLExtractionResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVLExtractionResult',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/getVLExtractionResult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVLExtractionResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vlextraction_result(
        self,
        request: main_models.GetVLExtractionResultRequest,
    ) -> main_models.GetVLExtractionResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_vlextraction_result_with_options(request, headers, runtime)

    async def get_vlextraction_result_async(
        self,
        request: main_models.GetVLExtractionResultRequest,
    ) -> main_models.GetVLExtractionResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_vlextraction_result_with_options_async(request, headers, runtime)

    def is_completed_with_options(
        self,
        request: main_models.IsCompletedRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.IsCompletedResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'IsCompleted',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/completed',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IsCompletedResponse(),
            self.call_api(params, req, runtime)
        )

    async def is_completed_with_options_async(
        self,
        request: main_models.IsCompletedRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.IsCompletedResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_type):
            body['productType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'IsCompleted',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/footprint/result/completed',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IsCompletedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def is_completed(
        self,
        request: main_models.IsCompletedRequest,
    ) -> main_models.IsCompletedResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.is_completed_with_options(request, headers, runtime)

    async def is_completed_async(
        self,
        request: main_models.IsCompletedRequest,
    ) -> main_models.IsCompletedResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.is_completed_with_options_async(request, headers, runtime)

    def push_device_data_with_options(
        self,
        request: main_models.PushDeviceDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PushDeviceDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.device_type):
            body['deviceType'] = request.device_type
        if not DaraCore.is_null(request.devices):
            body['devices'] = request.devices
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushDeviceData',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/data/increment/push',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushDeviceDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_device_data_with_options_async(
        self,
        request: main_models.PushDeviceDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PushDeviceDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.device_type):
            body['deviceType'] = request.device_type
        if not DaraCore.is_null(request.devices):
            body['devices'] = request.devices
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushDeviceData',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/data/increment/push',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushDeviceDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_device_data(
        self,
        request: main_models.PushDeviceDataRequest,
    ) -> main_models.PushDeviceDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.push_device_data_with_options(request, headers, runtime)

    async def push_device_data_async(
        self,
        request: main_models.PushDeviceDataRequest,
    ) -> main_models.PushDeviceDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.push_device_data_with_options_async(request, headers, runtime)

    def push_item_data_with_options(
        self,
        request: main_models.PushItemDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PushItemDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.items):
            body['items'] = request.items
        if not DaraCore.is_null(request.year):
            body['year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushItemData',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/data/item/push',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushItemDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_item_data_with_options_async(
        self,
        request: main_models.PushItemDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PushItemDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.items):
            body['items'] = request.items
        if not DaraCore.is_null(request.year):
            body['year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushItemData',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/data/item/push',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushItemDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_item_data(
        self,
        request: main_models.PushItemDataRequest,
    ) -> main_models.PushItemDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.push_item_data_with_options(request, headers, runtime)

    async def push_item_data_async(
        self,
        request: main_models.PushItemDataRequest,
    ) -> main_models.PushItemDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.push_item_data_with_options_async(request, headers, runtime)

    def recalculate_carbon_emission_with_options(
        self,
        request: main_models.RecalculateCarbonEmissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RecalculateCarbonEmissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.year):
            body['year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RecalculateCarbonEmission',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/data/item/recalculate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecalculateCarbonEmissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def recalculate_carbon_emission_with_options_async(
        self,
        request: main_models.RecalculateCarbonEmissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RecalculateCarbonEmissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.year):
            body['year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RecalculateCarbonEmission',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/emission/data/item/recalculate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecalculateCarbonEmissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recalculate_carbon_emission(
        self,
        request: main_models.RecalculateCarbonEmissionRequest,
    ) -> main_models.RecalculateCarbonEmissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.recalculate_carbon_emission_with_options(request, headers, runtime)

    async def recalculate_carbon_emission_async(
        self,
        request: main_models.RecalculateCarbonEmissionRequest,
    ) -> main_models.RecalculateCarbonEmissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.recalculate_carbon_emission_with_options_async(request, headers, runtime)

    def retrieve_with_options(
        self,
        request: main_models.RetrieveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RetrieveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_ids):
            body['documentIds'] = request.document_ids
        if not DaraCore.is_null(request.folder_ids):
            body['folderIds'] = request.folder_ids
        if not DaraCore.is_null(request.pre_retrieve_top_k):
            body['preRetrieveTopK'] = request.pre_retrieve_top_k
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.reranker_threshold):
            body['rerankerThreshold'] = request.reranker_threshold
        if not DaraCore.is_null(request.top_k):
            body['topK'] = request.top_k
        if not DaraCore.is_null(request.use_reranker):
            body['useReranker'] = request.use_reranker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Retrieve',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/knowledgebase/retrieve',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetrieveResponse(),
            self.call_api(params, req, runtime)
        )

    async def retrieve_with_options_async(
        self,
        request: main_models.RetrieveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RetrieveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_ids):
            body['documentIds'] = request.document_ids
        if not DaraCore.is_null(request.folder_ids):
            body['folderIds'] = request.folder_ids
        if not DaraCore.is_null(request.pre_retrieve_top_k):
            body['preRetrieveTopK'] = request.pre_retrieve_top_k
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.reranker_threshold):
            body['rerankerThreshold'] = request.reranker_threshold
        if not DaraCore.is_null(request.top_k):
            body['topK'] = request.top_k
        if not DaraCore.is_null(request.use_reranker):
            body['useReranker'] = request.use_reranker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Retrieve',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/knowledgebase/retrieve',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetrieveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retrieve(
        self,
        request: main_models.RetrieveRequest,
    ) -> main_models.RetrieveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.retrieve_with_options(request, headers, runtime)

    async def retrieve_async(
        self,
        request: main_models.RetrieveRequest,
    ) -> main_models.RetrieveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.retrieve_with_options_async(request, headers, runtime)

    def send_document_ask_question_with_options(
        self,
        request: main_models.SendDocumentAskQuestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendDocumentAskQuestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.folder_id):
            body['folderId'] = request.folder_id
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendDocumentAskQuestion',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aidoc/document/sendDocumentAskQuestion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendDocumentAskQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_document_ask_question_with_options_async(
        self,
        request: main_models.SendDocumentAskQuestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendDocumentAskQuestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.folder_id):
            body['folderId'] = request.folder_id
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendDocumentAskQuestion',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aidoc/document/sendDocumentAskQuestion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendDocumentAskQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_document_ask_question(
        self,
        request: main_models.SendDocumentAskQuestionRequest,
    ) -> main_models.SendDocumentAskQuestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.send_document_ask_question_with_options(request, headers, runtime)

    async def send_document_ask_question_async(
        self,
        request: main_models.SendDocumentAskQuestionRequest,
    ) -> main_models.SendDocumentAskQuestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.send_document_ask_question_with_options_async(request, headers, runtime)

    def set_running_plan_with_options(
        self,
        request: main_models.SetRunningPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SetRunningPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.control_type):
            body['controlType'] = request.control_type
        if not DaraCore.is_null(request.date_type):
            body['dateType'] = request.date_type
        if not DaraCore.is_null(request.earliest_startup_time):
            body['earliestStartupTime'] = request.earliest_startup_time
        if not DaraCore.is_null(request.end_time):
            body['endTime'] = request.end_time
        if not DaraCore.is_null(request.factory_id):
            body['factoryId'] = request.factory_id
        if not DaraCore.is_null(request.latest_shutdown_time):
            body['latestShutdownTime'] = request.latest_shutdown_time
        if not DaraCore.is_null(request.max_carbon_dioxide):
            body['maxCarbonDioxide'] = request.max_carbon_dioxide
        if not DaraCore.is_null(request.max_tem):
            body['maxTem'] = request.max_tem
        if not DaraCore.is_null(request.min_tem):
            body['minTem'] = request.min_tem
        if not DaraCore.is_null(request.p_key):
            body['pKey'] = request.p_key
        if not DaraCore.is_null(request.season_mode):
            body['seasonMode'] = request.season_mode
        if not DaraCore.is_null(request.start_time):
            body['startTime'] = request.start_time
        if not DaraCore.is_null(request.statistics_time):
            body['statisticsTime'] = request.statistics_time
        if not DaraCore.is_null(request.system_id):
            body['systemId'] = request.system_id
        if not DaraCore.is_null(request.working_end_time):
            body['workingEndTime'] = request.working_end_time
        if not DaraCore.is_null(request.working_start_time):
            body['workingStartTime'] = request.working_start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetRunningPlan',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/hvac/setRunningPlan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetRunningPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_running_plan_with_options_async(
        self,
        request: main_models.SetRunningPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SetRunningPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.control_type):
            body['controlType'] = request.control_type
        if not DaraCore.is_null(request.date_type):
            body['dateType'] = request.date_type
        if not DaraCore.is_null(request.earliest_startup_time):
            body['earliestStartupTime'] = request.earliest_startup_time
        if not DaraCore.is_null(request.end_time):
            body['endTime'] = request.end_time
        if not DaraCore.is_null(request.factory_id):
            body['factoryId'] = request.factory_id
        if not DaraCore.is_null(request.latest_shutdown_time):
            body['latestShutdownTime'] = request.latest_shutdown_time
        if not DaraCore.is_null(request.max_carbon_dioxide):
            body['maxCarbonDioxide'] = request.max_carbon_dioxide
        if not DaraCore.is_null(request.max_tem):
            body['maxTem'] = request.max_tem
        if not DaraCore.is_null(request.min_tem):
            body['minTem'] = request.min_tem
        if not DaraCore.is_null(request.p_key):
            body['pKey'] = request.p_key
        if not DaraCore.is_null(request.season_mode):
            body['seasonMode'] = request.season_mode
        if not DaraCore.is_null(request.start_time):
            body['startTime'] = request.start_time
        if not DaraCore.is_null(request.statistics_time):
            body['statisticsTime'] = request.statistics_time
        if not DaraCore.is_null(request.system_id):
            body['systemId'] = request.system_id
        if not DaraCore.is_null(request.working_end_time):
            body['workingEndTime'] = request.working_end_time
        if not DaraCore.is_null(request.working_start_time):
            body['workingStartTime'] = request.working_start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetRunningPlan',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/carbon/hvac/setRunningPlan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetRunningPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_running_plan(
        self,
        request: main_models.SetRunningPlanRequest,
    ) -> main_models.SetRunningPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.set_running_plan_with_options(request, headers, runtime)

    async def set_running_plan_async(
        self,
        request: main_models.SetRunningPlanRequest,
    ) -> main_models.SetRunningPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.set_running_plan_with_options_async(request, headers, runtime)

    def submit_doc_extraction_task_with_options(
        self,
        request: main_models.SubmitDocExtractionTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocExtractionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extract_type):
            query['extractType'] = request.extract_type
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.folder_id):
            query['folderId'] = request.folder_id
        if not DaraCore.is_null(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDocExtractionTask',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/submitDocExtractionTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDocExtractionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_doc_extraction_task_with_options_async(
        self,
        request: main_models.SubmitDocExtractionTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocExtractionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extract_type):
            query['extractType'] = request.extract_type
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.folder_id):
            query['folderId'] = request.folder_id
        if not DaraCore.is_null(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDocExtractionTask',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/submitDocExtractionTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDocExtractionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_doc_extraction_task(
        self,
        request: main_models.SubmitDocExtractionTaskRequest,
    ) -> main_models.SubmitDocExtractionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_doc_extraction_task_with_options(request, headers, runtime)

    async def submit_doc_extraction_task_async(
        self,
        request: main_models.SubmitDocExtractionTaskRequest,
    ) -> main_models.SubmitDocExtractionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_doc_extraction_task_with_options_async(request, headers, runtime)

    def submit_doc_extraction_task_advance(
        self,
        request: main_models.SubmitDocExtractionTaskAdvanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocExtractionTaskResponse:
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
            'Product': 'energyExpertExternal',
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
        submit_doc_extraction_task_req = main_models.SubmitDocExtractionTaskRequest()
        Utils.convert(request, submit_doc_extraction_task_req)
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
            submit_doc_extraction_task_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_doc_extraction_task_resp = self.submit_doc_extraction_task_with_options(submit_doc_extraction_task_req, headers, runtime)
        return submit_doc_extraction_task_resp

    async def submit_doc_extraction_task_advance_async(
        self,
        request: main_models.SubmitDocExtractionTaskAdvanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocExtractionTaskResponse:
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
            'Product': 'energyExpertExternal',
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
        submit_doc_extraction_task_req = main_models.SubmitDocExtractionTaskRequest()
        Utils.convert(request, submit_doc_extraction_task_req)
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
            submit_doc_extraction_task_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_doc_extraction_task_resp = await self.submit_doc_extraction_task_with_options_async(submit_doc_extraction_task_req, headers, runtime)
        return submit_doc_extraction_task_resp

    def submit_doc_parsing_task_with_options(
        self,
        request: main_models.SubmitDocParsingTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocParsingTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.folder_id):
            query['folderId'] = request.folder_id
        if not DaraCore.is_null(request.need_analyze_img):
            query['needAnalyzeImg'] = request.need_analyze_img
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDocParsingTask',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/submitDocParsingTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDocParsingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_doc_parsing_task_with_options_async(
        self,
        request: main_models.SubmitDocParsingTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocParsingTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.folder_id):
            query['folderId'] = request.folder_id
        if not DaraCore.is_null(request.need_analyze_img):
            query['needAnalyzeImg'] = request.need_analyze_img
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDocParsingTask',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/submitDocParsingTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDocParsingTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_doc_parsing_task(
        self,
        request: main_models.SubmitDocParsingTaskRequest,
    ) -> main_models.SubmitDocParsingTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_doc_parsing_task_with_options(request, headers, runtime)

    async def submit_doc_parsing_task_async(
        self,
        request: main_models.SubmitDocParsingTaskRequest,
    ) -> main_models.SubmitDocParsingTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_doc_parsing_task_with_options_async(request, headers, runtime)

    def submit_doc_parsing_task_advance(
        self,
        request: main_models.SubmitDocParsingTaskAdvanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocParsingTaskResponse:
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
            'Product': 'energyExpertExternal',
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
        submit_doc_parsing_task_req = main_models.SubmitDocParsingTaskRequest()
        Utils.convert(request, submit_doc_parsing_task_req)
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
            submit_doc_parsing_task_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_doc_parsing_task_resp = self.submit_doc_parsing_task_with_options(submit_doc_parsing_task_req, headers, runtime)
        return submit_doc_parsing_task_resp

    async def submit_doc_parsing_task_advance_async(
        self,
        request: main_models.SubmitDocParsingTaskAdvanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocParsingTaskResponse:
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
            'Product': 'energyExpertExternal',
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
        submit_doc_parsing_task_req = main_models.SubmitDocParsingTaskRequest()
        Utils.convert(request, submit_doc_parsing_task_req)
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
            submit_doc_parsing_task_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_doc_parsing_task_resp = await self.submit_doc_parsing_task_with_options_async(submit_doc_parsing_task_req, headers, runtime)
        return submit_doc_parsing_task_resp

    def submit_document_analyze_job_with_options(
        self,
        request: main_models.SubmitDocumentAnalyzeJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocumentAnalyzeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analysis_type):
            query['analysisType'] = request.analysis_type
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.folder_id):
            query['folderId'] = request.folder_id
        if not DaraCore.is_null(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDocumentAnalyzeJob',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aidoc/document/submitDocumentAnalyzeJob',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDocumentAnalyzeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_document_analyze_job_with_options_async(
        self,
        request: main_models.SubmitDocumentAnalyzeJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocumentAnalyzeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analysis_type):
            query['analysisType'] = request.analysis_type
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.folder_id):
            query['folderId'] = request.folder_id
        if not DaraCore.is_null(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDocumentAnalyzeJob',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aidoc/document/submitDocumentAnalyzeJob',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDocumentAnalyzeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_document_analyze_job(
        self,
        request: main_models.SubmitDocumentAnalyzeJobRequest,
    ) -> main_models.SubmitDocumentAnalyzeJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_document_analyze_job_with_options(request, headers, runtime)

    async def submit_document_analyze_job_async(
        self,
        request: main_models.SubmitDocumentAnalyzeJobRequest,
    ) -> main_models.SubmitDocumentAnalyzeJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_document_analyze_job_with_options_async(request, headers, runtime)

    def submit_document_analyze_job_advance(
        self,
        request: main_models.SubmitDocumentAnalyzeJobAdvanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocumentAnalyzeJobResponse:
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
            'Product': 'energyExpertExternal',
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
        submit_document_analyze_job_req = main_models.SubmitDocumentAnalyzeJobRequest()
        Utils.convert(request, submit_document_analyze_job_req)
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
            submit_document_analyze_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_document_analyze_job_resp = self.submit_document_analyze_job_with_options(submit_document_analyze_job_req, headers, runtime)
        return submit_document_analyze_job_resp

    async def submit_document_analyze_job_advance_async(
        self,
        request: main_models.SubmitDocumentAnalyzeJobAdvanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocumentAnalyzeJobResponse:
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
            'Product': 'energyExpertExternal',
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
        submit_document_analyze_job_req = main_models.SubmitDocumentAnalyzeJobRequest()
        Utils.convert(request, submit_document_analyze_job_req)
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
            submit_document_analyze_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_document_analyze_job_resp = await self.submit_document_analyze_job_with_options_async(submit_document_analyze_job_req, headers, runtime)
        return submit_document_analyze_job_resp

    def submit_vlextraction_task_with_options(
        self,
        request: main_models.SubmitVLExtractionTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitVLExtractionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.folder_id):
            query['folderId'] = request.folder_id
        if not DaraCore.is_null(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitVLExtractionTask',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/submitVLExtractionTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitVLExtractionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_vlextraction_task_with_options_async(
        self,
        request: main_models.SubmitVLExtractionTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitVLExtractionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['fileUrl'] = request.file_url
        if not DaraCore.is_null(request.folder_id):
            query['folderId'] = request.folder_id
        if not DaraCore.is_null(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitVLExtractionTask',
            version = '2022-09-23',
            protocol = 'HTTPS',
            pathname = f'/api/v2/aidoc/document/submitVLExtractionTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitVLExtractionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_vlextraction_task(
        self,
        request: main_models.SubmitVLExtractionTaskRequest,
    ) -> main_models.SubmitVLExtractionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_vlextraction_task_with_options(request, headers, runtime)

    async def submit_vlextraction_task_async(
        self,
        request: main_models.SubmitVLExtractionTaskRequest,
    ) -> main_models.SubmitVLExtractionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_vlextraction_task_with_options_async(request, headers, runtime)

    def submit_vlextraction_task_advance(
        self,
        request: main_models.SubmitVLExtractionTaskAdvanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitVLExtractionTaskResponse:
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
            'Product': 'energyExpertExternal',
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
        submit_vlextraction_task_req = main_models.SubmitVLExtractionTaskRequest()
        Utils.convert(request, submit_vlextraction_task_req)
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
            submit_vlextraction_task_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_vlextraction_task_resp = self.submit_vlextraction_task_with_options(submit_vlextraction_task_req, headers, runtime)
        return submit_vlextraction_task_resp

    async def submit_vlextraction_task_advance_async(
        self,
        request: main_models.SubmitVLExtractionTaskAdvanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitVLExtractionTaskResponse:
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
            'Product': 'energyExpertExternal',
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
        submit_vlextraction_task_req = main_models.SubmitVLExtractionTaskRequest()
        Utils.convert(request, submit_vlextraction_task_req)
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
            submit_vlextraction_task_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_vlextraction_task_resp = await self.submit_vlextraction_task_with_options_async(submit_vlextraction_task_req, headers, runtime)
        return submit_vlextraction_task_resp
