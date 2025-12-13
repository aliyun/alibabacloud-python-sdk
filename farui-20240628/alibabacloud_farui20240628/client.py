# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_farui20240628 import models as main_models
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
        self._endpoint = self.get_endpoint('farui', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_text_file_with_options(
        self,
        workspace_id: str,
        request: main_models.CreateTextFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTextFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.contract_id):
            body['ContractId'] = request.contract_id
        if not DaraCore.is_null(request.create_time):
            body['CreateTime'] = request.create_time
        if not DaraCore.is_null(request.text_file_name):
            body['TextFileName'] = request.text_file_name
        if not DaraCore.is_null(request.text_file_url):
            body['TextFileUrl'] = request.text_file_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTextFile',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/data/textFile',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTextFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_text_file_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreateTextFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTextFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.contract_id):
            body['ContractId'] = request.contract_id
        if not DaraCore.is_null(request.create_time):
            body['CreateTime'] = request.create_time
        if not DaraCore.is_null(request.text_file_name):
            body['TextFileName'] = request.text_file_name
        if not DaraCore.is_null(request.text_file_url):
            body['TextFileUrl'] = request.text_file_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTextFile',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/data/textFile',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTextFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_text_file(
        self,
        workspace_id: str,
        request: main_models.CreateTextFileRequest,
    ) -> main_models.CreateTextFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_text_file_with_options(workspace_id, request, headers, runtime)

    async def create_text_file_async(
        self,
        workspace_id: str,
        request: main_models.CreateTextFileRequest,
    ) -> main_models.CreateTextFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_text_file_with_options_async(workspace_id, request, headers, runtime)

    def create_text_file_advance(
        self,
        workspace_id: str,
        request: main_models.CreateTextFileAdvanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTextFileResponse:
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
            'Product': 'FaRui',
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
        create_text_file_req = main_models.CreateTextFileRequest()
        Utils.convert(request, create_text_file_req)
        if not DaraCore.is_null(request.text_file_url_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.text_file_url_object,
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
            create_text_file_req.text_file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        create_text_file_resp = self.create_text_file_with_options(workspace_id, create_text_file_req, headers, runtime)
        return create_text_file_resp

    async def create_text_file_advance_async(
        self,
        workspace_id: str,
        request: main_models.CreateTextFileAdvanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTextFileResponse:
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
            'Product': 'FaRui',
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
        create_text_file_req = main_models.CreateTextFileRequest()
        Utils.convert(request, create_text_file_req)
        if not DaraCore.is_null(request.text_file_url_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.text_file_url_object,
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
            create_text_file_req.text_file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        create_text_file_resp = await self.create_text_file_with_options_async(workspace_id, create_text_file_req, headers, runtime)
        return create_text_file_resp

    def run_contract_extract_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.RunContractExtractRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunContractExtractResponse:
        tmp_req.validate()
        request = main_models.RunContractExtractShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.fields_to_extract):
            request.fields_to_extract_shrink = Utils.array_to_string_with_specified_style(tmp_req.fields_to_extract, 'fieldsToExtract', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.fields_to_extract_shrink):
            body['fieldsToExtract'] = request.fields_to_extract_shrink
        if not DaraCore.is_null(request.file_oss_url):
            body['fileOssUrl'] = request.file_oss_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunContractExtract',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/pop/contract/extraction',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunContractExtractResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_contract_extract_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunContractExtractRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunContractExtractResponse:
        tmp_req.validate()
        request = main_models.RunContractExtractShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.fields_to_extract):
            request.fields_to_extract_shrink = Utils.array_to_string_with_specified_style(tmp_req.fields_to_extract, 'fieldsToExtract', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.fields_to_extract_shrink):
            body['fieldsToExtract'] = request.fields_to_extract_shrink
        if not DaraCore.is_null(request.file_oss_url):
            body['fileOssUrl'] = request.file_oss_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunContractExtract',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/pop/contract/extraction',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunContractExtractResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_contract_extract(
        self,
        workspace_id: str,
        request: main_models.RunContractExtractRequest,
    ) -> main_models.RunContractExtractResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_contract_extract_with_options(workspace_id, request, headers, runtime)

    async def run_contract_extract_async(
        self,
        workspace_id: str,
        request: main_models.RunContractExtractRequest,
    ) -> main_models.RunContractExtractResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_contract_extract_with_options_async(workspace_id, request, headers, runtime)

    def run_contract_result_generation_with_sse(
        self,
        workspace_id: str,
        tmp_req: main_models.RunContractResultGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunContractResultGenerationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunContractResultGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assistant):
            request.assistant_shrink = Utils.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunContractResultGeneration',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/farui/contract/result/genarate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunContractResultGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_contract_result_generation_with_sse_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunContractResultGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunContractResultGenerationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunContractResultGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assistant):
            request.assistant_shrink = Utils.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunContractResultGeneration',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/farui/contract/result/genarate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunContractResultGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_contract_result_generation_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.RunContractResultGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunContractResultGenerationResponse:
        tmp_req.validate()
        request = main_models.RunContractResultGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assistant):
            request.assistant_shrink = Utils.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunContractResultGeneration',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/farui/contract/result/genarate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunContractResultGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_contract_result_generation_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunContractResultGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunContractResultGenerationResponse:
        tmp_req.validate()
        request = main_models.RunContractResultGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assistant):
            request.assistant_shrink = Utils.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunContractResultGeneration',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/farui/contract/result/genarate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunContractResultGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_contract_result_generation(
        self,
        workspace_id: str,
        request: main_models.RunContractResultGenerationRequest,
    ) -> main_models.RunContractResultGenerationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_contract_result_generation_with_options(workspace_id, request, headers, runtime)

    async def run_contract_result_generation_async(
        self,
        workspace_id: str,
        request: main_models.RunContractResultGenerationRequest,
    ) -> main_models.RunContractResultGenerationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_contract_result_generation_with_options_async(workspace_id, request, headers, runtime)

    def run_contract_rule_generation_with_sse(
        self,
        workspace_id: str,
        tmp_req: main_models.RunContractRuleGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunContractRuleGenerationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunContractRuleGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assistant):
            request.assistant_shrink = Utils.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunContractRuleGeneration',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/farui/contract/rule/genarate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunContractRuleGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_contract_rule_generation_with_sse_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunContractRuleGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunContractRuleGenerationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunContractRuleGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assistant):
            request.assistant_shrink = Utils.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunContractRuleGeneration',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/farui/contract/rule/genarate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunContractRuleGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_contract_rule_generation_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.RunContractRuleGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunContractRuleGenerationResponse:
        tmp_req.validate()
        request = main_models.RunContractRuleGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assistant):
            request.assistant_shrink = Utils.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunContractRuleGeneration',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/farui/contract/rule/genarate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunContractRuleGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_contract_rule_generation_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunContractRuleGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunContractRuleGenerationResponse:
        tmp_req.validate()
        request = main_models.RunContractRuleGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assistant):
            request.assistant_shrink = Utils.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunContractRuleGeneration',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/farui/contract/rule/genarate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunContractRuleGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_contract_rule_generation(
        self,
        workspace_id: str,
        request: main_models.RunContractRuleGenerationRequest,
    ) -> main_models.RunContractRuleGenerationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_contract_rule_generation_with_options(workspace_id, request, headers, runtime)

    async def run_contract_rule_generation_async(
        self,
        workspace_id: str,
        request: main_models.RunContractRuleGenerationRequest,
    ) -> main_models.RunContractRuleGenerationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_contract_rule_generation_with_options_async(workspace_id, request, headers, runtime)

    def run_legal_advice_consultation_with_sse(
        self,
        workspace_id: str,
        tmp_req: main_models.RunLegalAdviceConsultationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunLegalAdviceConsultationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunLegalAdviceConsultationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assistant):
            request.assistant_shrink = Utils.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        if not DaraCore.is_null(tmp_req.extra):
            request.extra_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra, 'extra', 'json')
        if not DaraCore.is_null(tmp_req.thread):
            request.thread_shrink = Utils.array_to_string_with_specified_style(tmp_req.thread, 'thread', 'json')
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not DaraCore.is_null(request.extra_shrink):
            body['extra'] = request.extra_shrink
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.thread_shrink):
            body['thread'] = request.thread_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunLegalAdviceConsultation',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/farui/legalAdvice/consult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunLegalAdviceConsultationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_legal_advice_consultation_with_sse_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunLegalAdviceConsultationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunLegalAdviceConsultationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunLegalAdviceConsultationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assistant):
            request.assistant_shrink = Utils.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        if not DaraCore.is_null(tmp_req.extra):
            request.extra_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra, 'extra', 'json')
        if not DaraCore.is_null(tmp_req.thread):
            request.thread_shrink = Utils.array_to_string_with_specified_style(tmp_req.thread, 'thread', 'json')
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not DaraCore.is_null(request.extra_shrink):
            body['extra'] = request.extra_shrink
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.thread_shrink):
            body['thread'] = request.thread_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunLegalAdviceConsultation',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/farui/legalAdvice/consult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunLegalAdviceConsultationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_legal_advice_consultation_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.RunLegalAdviceConsultationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunLegalAdviceConsultationResponse:
        tmp_req.validate()
        request = main_models.RunLegalAdviceConsultationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assistant):
            request.assistant_shrink = Utils.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        if not DaraCore.is_null(tmp_req.extra):
            request.extra_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra, 'extra', 'json')
        if not DaraCore.is_null(tmp_req.thread):
            request.thread_shrink = Utils.array_to_string_with_specified_style(tmp_req.thread, 'thread', 'json')
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not DaraCore.is_null(request.extra_shrink):
            body['extra'] = request.extra_shrink
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.thread_shrink):
            body['thread'] = request.thread_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunLegalAdviceConsultation',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/farui/legalAdvice/consult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunLegalAdviceConsultationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_legal_advice_consultation_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunLegalAdviceConsultationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunLegalAdviceConsultationResponse:
        tmp_req.validate()
        request = main_models.RunLegalAdviceConsultationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assistant):
            request.assistant_shrink = Utils.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        if not DaraCore.is_null(tmp_req.extra):
            request.extra_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra, 'extra', 'json')
        if not DaraCore.is_null(tmp_req.thread):
            request.thread_shrink = Utils.array_to_string_with_specified_style(tmp_req.thread, 'thread', 'json')
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not DaraCore.is_null(request.extra_shrink):
            body['extra'] = request.extra_shrink
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.thread_shrink):
            body['thread'] = request.thread_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunLegalAdviceConsultation',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/farui/legalAdvice/consult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunLegalAdviceConsultationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_legal_advice_consultation(
        self,
        workspace_id: str,
        request: main_models.RunLegalAdviceConsultationRequest,
    ) -> main_models.RunLegalAdviceConsultationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_legal_advice_consultation_with_options(workspace_id, request, headers, runtime)

    async def run_legal_advice_consultation_async(
        self,
        workspace_id: str,
        request: main_models.RunLegalAdviceConsultationRequest,
    ) -> main_models.RunLegalAdviceConsultationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_legal_advice_consultation_with_options_async(workspace_id, request, headers, runtime)

    def run_search_case_full_text_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.RunSearchCaseFullTextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunSearchCaseFullTextResponse:
        tmp_req.validate()
        request = main_models.RunSearchCaseFullTextShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_condition):
            request.filter_condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_condition, 'filterCondition', 'json')
        if not DaraCore.is_null(tmp_req.page_param):
            request.page_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.page_param, 'pageParam', 'json')
        if not DaraCore.is_null(tmp_req.query_keywords):
            request.query_keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_keywords, 'queryKeywords', 'json')
        if not DaraCore.is_null(tmp_req.sort_key_and_direction):
            request.sort_key_and_direction_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort_key_and_direction, 'sortKeyAndDirection', 'json')
        if not DaraCore.is_null(tmp_req.thread):
            request.thread_shrink = Utils.array_to_string_with_specified_style(tmp_req.thread, 'thread', 'json')
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.filter_condition_shrink):
            body['filterCondition'] = request.filter_condition_shrink
        if not DaraCore.is_null(request.page_param_shrink):
            body['pageParam'] = request.page_param_shrink
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.query_keywords_shrink):
            body['queryKeywords'] = request.query_keywords_shrink
        if not DaraCore.is_null(request.refer_level):
            body['referLevel'] = request.refer_level
        if not DaraCore.is_null(request.sort_key_and_direction_shrink):
            body['sortKeyAndDirection'] = request.sort_key_and_direction_shrink
        if not DaraCore.is_null(request.thread_shrink):
            body['thread'] = request.thread_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSearchCaseFullText',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/farui/search/case/fulltext',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunSearchCaseFullTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_search_case_full_text_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunSearchCaseFullTextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunSearchCaseFullTextResponse:
        tmp_req.validate()
        request = main_models.RunSearchCaseFullTextShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_condition):
            request.filter_condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_condition, 'filterCondition', 'json')
        if not DaraCore.is_null(tmp_req.page_param):
            request.page_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.page_param, 'pageParam', 'json')
        if not DaraCore.is_null(tmp_req.query_keywords):
            request.query_keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_keywords, 'queryKeywords', 'json')
        if not DaraCore.is_null(tmp_req.sort_key_and_direction):
            request.sort_key_and_direction_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort_key_and_direction, 'sortKeyAndDirection', 'json')
        if not DaraCore.is_null(tmp_req.thread):
            request.thread_shrink = Utils.array_to_string_with_specified_style(tmp_req.thread, 'thread', 'json')
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.filter_condition_shrink):
            body['filterCondition'] = request.filter_condition_shrink
        if not DaraCore.is_null(request.page_param_shrink):
            body['pageParam'] = request.page_param_shrink
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.query_keywords_shrink):
            body['queryKeywords'] = request.query_keywords_shrink
        if not DaraCore.is_null(request.refer_level):
            body['referLevel'] = request.refer_level
        if not DaraCore.is_null(request.sort_key_and_direction_shrink):
            body['sortKeyAndDirection'] = request.sort_key_and_direction_shrink
        if not DaraCore.is_null(request.thread_shrink):
            body['thread'] = request.thread_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSearchCaseFullText',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/farui/search/case/fulltext',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunSearchCaseFullTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_search_case_full_text(
        self,
        workspace_id: str,
        request: main_models.RunSearchCaseFullTextRequest,
    ) -> main_models.RunSearchCaseFullTextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_search_case_full_text_with_options(workspace_id, request, headers, runtime)

    async def run_search_case_full_text_async(
        self,
        workspace_id: str,
        request: main_models.RunSearchCaseFullTextRequest,
    ) -> main_models.RunSearchCaseFullTextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_search_case_full_text_with_options_async(workspace_id, request, headers, runtime)

    def run_search_law_query_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.RunSearchLawQueryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunSearchLawQueryResponse:
        tmp_req.validate()
        request = main_models.RunSearchLawQueryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_condition):
            request.filter_condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_condition, 'filterCondition', 'json')
        if not DaraCore.is_null(tmp_req.page_param):
            request.page_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.page_param, 'pageParam', 'json')
        if not DaraCore.is_null(tmp_req.query_keywords):
            request.query_keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_keywords, 'queryKeywords', 'json')
        if not DaraCore.is_null(tmp_req.thread):
            request.thread_shrink = Utils.array_to_string_with_specified_style(tmp_req.thread, 'thread', 'json')
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.filter_condition_shrink):
            body['filterCondition'] = request.filter_condition_shrink
        if not DaraCore.is_null(request.page_param_shrink):
            body['pageParam'] = request.page_param_shrink
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.query_keywords_shrink):
            body['queryKeywords'] = request.query_keywords_shrink
        if not DaraCore.is_null(request.thread_shrink):
            body['thread'] = request.thread_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSearchLawQuery',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/farui/search/law/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunSearchLawQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_search_law_query_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunSearchLawQueryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunSearchLawQueryResponse:
        tmp_req.validate()
        request = main_models.RunSearchLawQueryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_condition):
            request.filter_condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_condition, 'filterCondition', 'json')
        if not DaraCore.is_null(tmp_req.page_param):
            request.page_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.page_param, 'pageParam', 'json')
        if not DaraCore.is_null(tmp_req.query_keywords):
            request.query_keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_keywords, 'queryKeywords', 'json')
        if not DaraCore.is_null(tmp_req.thread):
            request.thread_shrink = Utils.array_to_string_with_specified_style(tmp_req.thread, 'thread', 'json')
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.filter_condition_shrink):
            body['filterCondition'] = request.filter_condition_shrink
        if not DaraCore.is_null(request.page_param_shrink):
            body['pageParam'] = request.page_param_shrink
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.query_keywords_shrink):
            body['queryKeywords'] = request.query_keywords_shrink
        if not DaraCore.is_null(request.thread_shrink):
            body['thread'] = request.thread_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSearchLawQuery',
            version = '2024-06-28',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/farui/search/law/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunSearchLawQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_search_law_query(
        self,
        workspace_id: str,
        request: main_models.RunSearchLawQueryRequest,
    ) -> main_models.RunSearchLawQueryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_search_law_query_with_options(workspace_id, request, headers, runtime)

    async def run_search_law_query_async(
        self,
        workspace_id: str,
        request: main_models.RunSearchLawQueryRequest,
    ) -> main_models.RunSearchLawQueryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_search_law_query_with_options_async(workspace_id, request, headers, runtime)
