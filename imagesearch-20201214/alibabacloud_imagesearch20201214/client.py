# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_imagesearch20201214 import models as main_models
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
        self._endpoint = self.get_endpoint('imagesearch', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_image_with_options(
        self,
        request: main_models.AddImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.crop):
            body['Crop'] = request.crop
        if not DaraCore.is_null(request.custom_content):
            body['CustomContent'] = request.custom_content
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.int_attr):
            body['IntAttr'] = request.int_attr
        if not DaraCore.is_null(request.int_attr_2):
            body['IntAttr2'] = request.int_attr_2
        if not DaraCore.is_null(request.int_attr_3):
            body['IntAttr3'] = request.int_attr_3
        if not DaraCore.is_null(request.int_attr_4):
            body['IntAttr4'] = request.int_attr_4
        if not DaraCore.is_null(request.pic_content):
            body['PicContent'] = request.pic_content
        if not DaraCore.is_null(request.pic_name):
            body['PicName'] = request.pic_name
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region):
            body['Region'] = request.region
        if not DaraCore.is_null(request.str_attr):
            body['StrAttr'] = request.str_attr
        if not DaraCore.is_null(request.str_attr_2):
            body['StrAttr2'] = request.str_attr_2
        if not DaraCore.is_null(request.str_attr_3):
            body['StrAttr3'] = request.str_attr_3
        if not DaraCore.is_null(request.str_attr_4):
            body['StrAttr4'] = request.str_attr_4
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddImage',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_image_with_options_async(
        self,
        request: main_models.AddImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.crop):
            body['Crop'] = request.crop
        if not DaraCore.is_null(request.custom_content):
            body['CustomContent'] = request.custom_content
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.int_attr):
            body['IntAttr'] = request.int_attr
        if not DaraCore.is_null(request.int_attr_2):
            body['IntAttr2'] = request.int_attr_2
        if not DaraCore.is_null(request.int_attr_3):
            body['IntAttr3'] = request.int_attr_3
        if not DaraCore.is_null(request.int_attr_4):
            body['IntAttr4'] = request.int_attr_4
        if not DaraCore.is_null(request.pic_content):
            body['PicContent'] = request.pic_content
        if not DaraCore.is_null(request.pic_name):
            body['PicName'] = request.pic_name
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region):
            body['Region'] = request.region
        if not DaraCore.is_null(request.str_attr):
            body['StrAttr'] = request.str_attr
        if not DaraCore.is_null(request.str_attr_2):
            body['StrAttr2'] = request.str_attr_2
        if not DaraCore.is_null(request.str_attr_3):
            body['StrAttr3'] = request.str_attr_3
        if not DaraCore.is_null(request.str_attr_4):
            body['StrAttr4'] = request.str_attr_4
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddImage',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_image(
        self,
        request: main_models.AddImageRequest,
    ) -> main_models.AddImageResponse:
        runtime = RuntimeOptions()
        return self.add_image_with_options(request, runtime)

    async def add_image_async(
        self,
        request: main_models.AddImageRequest,
    ) -> main_models.AddImageResponse:
        runtime = RuntimeOptions()
        return await self.add_image_with_options_async(request, runtime)

    def add_image_advance(
        self,
        request: main_models.AddImageAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddImageResponse:
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
            'Product': 'ImageSearch',
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
        add_image_req = main_models.AddImageRequest()
        Utils.convert(request, add_image_req)
        if not DaraCore.is_null(request.pic_content_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.pic_content_object,
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
            add_image_req.pic_content = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        add_image_resp = self.add_image_with_options(add_image_req, runtime)
        return add_image_resp

    async def add_image_advance_async(
        self,
        request: main_models.AddImageAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddImageResponse:
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
            'Product': 'ImageSearch',
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
        add_image_req = main_models.AddImageRequest()
        Utils.convert(request, add_image_req)
        if not DaraCore.is_null(request.pic_content_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.pic_content_object,
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
            add_image_req.pic_content = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        add_image_resp = await self.add_image_with_options_async(add_image_req, runtime)
        return add_image_resp

    def compare_similar_by_image_with_options(
        self,
        request: main_models.CompareSimilarByImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompareSimilarByImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.primary_pic_content):
            body['PrimaryPicContent'] = request.primary_pic_content
        if not DaraCore.is_null(request.secondary_pic_content):
            body['SecondaryPicContent'] = request.secondary_pic_content
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CompareSimilarByImage',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompareSimilarByImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_similar_by_image_with_options_async(
        self,
        request: main_models.CompareSimilarByImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompareSimilarByImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.primary_pic_content):
            body['PrimaryPicContent'] = request.primary_pic_content
        if not DaraCore.is_null(request.secondary_pic_content):
            body['SecondaryPicContent'] = request.secondary_pic_content
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CompareSimilarByImage',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompareSimilarByImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_similar_by_image(
        self,
        request: main_models.CompareSimilarByImageRequest,
    ) -> main_models.CompareSimilarByImageResponse:
        runtime = RuntimeOptions()
        return self.compare_similar_by_image_with_options(request, runtime)

    async def compare_similar_by_image_async(
        self,
        request: main_models.CompareSimilarByImageRequest,
    ) -> main_models.CompareSimilarByImageResponse:
        runtime = RuntimeOptions()
        return await self.compare_similar_by_image_with_options_async(request, runtime)

    def compare_similar_by_image_advance(
        self,
        request: main_models.CompareSimilarByImageAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompareSimilarByImageResponse:
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
            'Product': 'ImageSearch',
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
        compare_similar_by_image_req = main_models.CompareSimilarByImageRequest()
        Utils.convert(request, compare_similar_by_image_req)
        if not DaraCore.is_null(request.primary_pic_content_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.primary_pic_content_object,
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
            compare_similar_by_image_req.primary_pic_content = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not DaraCore.is_null(request.secondary_pic_content_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.secondary_pic_content_object,
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
            compare_similar_by_image_req.secondary_pic_content = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        compare_similar_by_image_resp = self.compare_similar_by_image_with_options(compare_similar_by_image_req, runtime)
        return compare_similar_by_image_resp

    async def compare_similar_by_image_advance_async(
        self,
        request: main_models.CompareSimilarByImageAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompareSimilarByImageResponse:
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
            'Product': 'ImageSearch',
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
        compare_similar_by_image_req = main_models.CompareSimilarByImageRequest()
        Utils.convert(request, compare_similar_by_image_req)
        if not DaraCore.is_null(request.primary_pic_content_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.primary_pic_content_object,
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
            compare_similar_by_image_req.primary_pic_content = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not DaraCore.is_null(request.secondary_pic_content_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.secondary_pic_content_object,
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
            compare_similar_by_image_req.secondary_pic_content = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        compare_similar_by_image_resp = await self.compare_similar_by_image_with_options_async(compare_similar_by_image_req, runtime)
        return compare_similar_by_image_resp

    def delete_image_with_options(
        self,
        request: main_models.DeleteImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.is_delete_by_filter):
            body['IsDeleteByFilter'] = request.is_delete_by_filter
        if not DaraCore.is_null(request.pic_name):
            body['PicName'] = request.pic_name
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteImage',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_with_options_async(
        self,
        request: main_models.DeleteImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.is_delete_by_filter):
            body['IsDeleteByFilter'] = request.is_delete_by_filter
        if not DaraCore.is_null(request.pic_name):
            body['PicName'] = request.pic_name
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteImage',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_image(
        self,
        request: main_models.DeleteImageRequest,
    ) -> main_models.DeleteImageResponse:
        runtime = RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    async def delete_image_async(
        self,
        request: main_models.DeleteImageRequest,
    ) -> main_models.DeleteImageResponse:
        runtime = RuntimeOptions()
        return await self.delete_image_with_options_async(request, runtime)

    def detail_with_options(
        self,
        request: main_models.DetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Detail',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def detail_with_options_async(
        self,
        request: main_models.DetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Detail',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detail(
        self,
        request: main_models.DetailRequest,
    ) -> main_models.DetailResponse:
        runtime = RuntimeOptions()
        return self.detail_with_options(request, runtime)

    async def detail_async(
        self,
        request: main_models.DetailRequest,
    ) -> main_models.DetailResponse:
        runtime = RuntimeOptions()
        return await self.detail_with_options_async(request, runtime)

    def dump_meta_with_options(
        self,
        request: main_models.DumpMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DumpMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DumpMeta',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DumpMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def dump_meta_with_options_async(
        self,
        request: main_models.DumpMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DumpMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DumpMeta',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DumpMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dump_meta(
        self,
        request: main_models.DumpMetaRequest,
    ) -> main_models.DumpMetaResponse:
        runtime = RuntimeOptions()
        return self.dump_meta_with_options(request, runtime)

    async def dump_meta_async(
        self,
        request: main_models.DumpMetaRequest,
    ) -> main_models.DumpMetaResponse:
        runtime = RuntimeOptions()
        return await self.dump_meta_with_options_async(request, runtime)

    def dump_meta_list_with_options(
        self,
        request: main_models.DumpMetaListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DumpMetaListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DumpMetaList',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DumpMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    async def dump_meta_list_with_options_async(
        self,
        request: main_models.DumpMetaListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DumpMetaListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DumpMetaList',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DumpMetaListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dump_meta_list(
        self,
        request: main_models.DumpMetaListRequest,
    ) -> main_models.DumpMetaListResponse:
        runtime = RuntimeOptions()
        return self.dump_meta_list_with_options(request, runtime)

    async def dump_meta_list_async(
        self,
        request: main_models.DumpMetaListRequest,
    ) -> main_models.DumpMetaListResponse:
        runtime = RuntimeOptions()
        return await self.dump_meta_list_with_options_async(request, runtime)

    def increase_instance_with_options(
        self,
        request: main_models.IncreaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IncreaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.callback_address):
            query['CallbackAddress'] = request.callback_address
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IncreaseInstance',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IncreaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def increase_instance_with_options_async(
        self,
        request: main_models.IncreaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IncreaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.callback_address):
            query['CallbackAddress'] = request.callback_address
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IncreaseInstance',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IncreaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def increase_instance(
        self,
        request: main_models.IncreaseInstanceRequest,
    ) -> main_models.IncreaseInstanceResponse:
        runtime = RuntimeOptions()
        return self.increase_instance_with_options(request, runtime)

    async def increase_instance_async(
        self,
        request: main_models.IncreaseInstanceRequest,
    ) -> main_models.IncreaseInstanceResponse:
        runtime = RuntimeOptions()
        return await self.increase_instance_with_options_async(request, runtime)

    def increase_list_with_options(
        self,
        request: main_models.IncreaseListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IncreaseListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IncreaseList',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IncreaseListResponse(),
            self.call_api(params, req, runtime)
        )

    async def increase_list_with_options_async(
        self,
        request: main_models.IncreaseListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IncreaseListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IncreaseList',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IncreaseListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def increase_list(
        self,
        request: main_models.IncreaseListRequest,
    ) -> main_models.IncreaseListResponse:
        runtime = RuntimeOptions()
        return self.increase_list_with_options(request, runtime)

    async def increase_list_async(
        self,
        request: main_models.IncreaseListRequest,
    ) -> main_models.IncreaseListResponse:
        runtime = RuntimeOptions()
        return await self.increase_list_with_options_async(request, runtime)

    def search_image_by_name_with_options(
        self,
        request: main_models.SearchImageByNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchImageByNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.score_threshold):
            query['ScoreThreshold'] = request.score_threshold
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.distinct_product_id):
            body['DistinctProductId'] = request.distinct_product_id
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.num):
            body['Num'] = request.num
        if not DaraCore.is_null(request.pic_name):
            body['PicName'] = request.pic_name
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.start):
            body['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchImageByName',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchImageByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_image_by_name_with_options_async(
        self,
        request: main_models.SearchImageByNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchImageByNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.score_threshold):
            query['ScoreThreshold'] = request.score_threshold
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.distinct_product_id):
            body['DistinctProductId'] = request.distinct_product_id
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.num):
            body['Num'] = request.num
        if not DaraCore.is_null(request.pic_name):
            body['PicName'] = request.pic_name
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.start):
            body['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchImageByName',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchImageByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_image_by_name(
        self,
        request: main_models.SearchImageByNameRequest,
    ) -> main_models.SearchImageByNameResponse:
        runtime = RuntimeOptions()
        return self.search_image_by_name_with_options(request, runtime)

    async def search_image_by_name_async(
        self,
        request: main_models.SearchImageByNameRequest,
    ) -> main_models.SearchImageByNameResponse:
        runtime = RuntimeOptions()
        return await self.search_image_by_name_with_options_async(request, runtime)

    def search_image_by_pic_with_options(
        self,
        request: main_models.SearchImageByPicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchImageByPicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.score_threshold):
            query['ScoreThreshold'] = request.score_threshold
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.crop):
            body['Crop'] = request.crop
        if not DaraCore.is_null(request.distinct_product_id):
            body['DistinctProductId'] = request.distinct_product_id
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.num):
            body['Num'] = request.num
        if not DaraCore.is_null(request.pic_content):
            body['PicContent'] = request.pic_content
        if not DaraCore.is_null(request.region):
            body['Region'] = request.region
        if not DaraCore.is_null(request.start):
            body['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchImageByPic',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchImageByPicResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_image_by_pic_with_options_async(
        self,
        request: main_models.SearchImageByPicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchImageByPicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.score_threshold):
            query['ScoreThreshold'] = request.score_threshold
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.crop):
            body['Crop'] = request.crop
        if not DaraCore.is_null(request.distinct_product_id):
            body['DistinctProductId'] = request.distinct_product_id
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.num):
            body['Num'] = request.num
        if not DaraCore.is_null(request.pic_content):
            body['PicContent'] = request.pic_content
        if not DaraCore.is_null(request.region):
            body['Region'] = request.region
        if not DaraCore.is_null(request.start):
            body['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchImageByPic',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchImageByPicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_image_by_pic(
        self,
        request: main_models.SearchImageByPicRequest,
    ) -> main_models.SearchImageByPicResponse:
        runtime = RuntimeOptions()
        return self.search_image_by_pic_with_options(request, runtime)

    async def search_image_by_pic_async(
        self,
        request: main_models.SearchImageByPicRequest,
    ) -> main_models.SearchImageByPicResponse:
        runtime = RuntimeOptions()
        return await self.search_image_by_pic_with_options_async(request, runtime)

    def search_image_by_pic_advance(
        self,
        request: main_models.SearchImageByPicAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchImageByPicResponse:
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
            'Product': 'ImageSearch',
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
        search_image_by_pic_req = main_models.SearchImageByPicRequest()
        Utils.convert(request, search_image_by_pic_req)
        if not DaraCore.is_null(request.pic_content_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.pic_content_object,
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
            search_image_by_pic_req.pic_content = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        search_image_by_pic_resp = self.search_image_by_pic_with_options(search_image_by_pic_req, runtime)
        return search_image_by_pic_resp

    async def search_image_by_pic_advance_async(
        self,
        request: main_models.SearchImageByPicAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchImageByPicResponse:
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
            'Product': 'ImageSearch',
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
        search_image_by_pic_req = main_models.SearchImageByPicRequest()
        Utils.convert(request, search_image_by_pic_req)
        if not DaraCore.is_null(request.pic_content_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.pic_content_object,
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
            search_image_by_pic_req.pic_content = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        search_image_by_pic_resp = await self.search_image_by_pic_with_options_async(search_image_by_pic_req, runtime)
        return search_image_by_pic_resp

    def search_image_by_text_with_options(
        self,
        request: main_models.SearchImageByTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchImageByTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.score_threshold):
            query['ScoreThreshold'] = request.score_threshold
        body = {}
        if not DaraCore.is_null(request.distinct_product_id):
            body['DistinctProductId'] = request.distinct_product_id
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.num):
            body['Num'] = request.num
        if not DaraCore.is_null(request.start):
            body['Start'] = request.start
        if not DaraCore.is_null(request.text):
            body['Text'] = request.text
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchImageByText',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchImageByTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_image_by_text_with_options_async(
        self,
        request: main_models.SearchImageByTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchImageByTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.score_threshold):
            query['ScoreThreshold'] = request.score_threshold
        body = {}
        if not DaraCore.is_null(request.distinct_product_id):
            body['DistinctProductId'] = request.distinct_product_id
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.num):
            body['Num'] = request.num
        if not DaraCore.is_null(request.start):
            body['Start'] = request.start
        if not DaraCore.is_null(request.text):
            body['Text'] = request.text
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchImageByText',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchImageByTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_image_by_text(
        self,
        request: main_models.SearchImageByTextRequest,
    ) -> main_models.SearchImageByTextResponse:
        runtime = RuntimeOptions()
        return self.search_image_by_text_with_options(request, runtime)

    async def search_image_by_text_async(
        self,
        request: main_models.SearchImageByTextRequest,
    ) -> main_models.SearchImageByTextResponse:
        runtime = RuntimeOptions()
        return await self.search_image_by_text_with_options_async(request, runtime)

    def update_image_with_options(
        self,
        request: main_models.UpdateImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.int_attr_3):
            query['IntAttr3'] = request.int_attr_3
        if not DaraCore.is_null(request.int_attr_4):
            query['IntAttr4'] = request.int_attr_4
        if not DaraCore.is_null(request.str_attr_3):
            query['StrAttr3'] = request.str_attr_3
        if not DaraCore.is_null(request.str_attr_4):
            query['StrAttr4'] = request.str_attr_4
        body = {}
        if not DaraCore.is_null(request.custom_content):
            body['CustomContent'] = request.custom_content
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.int_attr):
            body['IntAttr'] = request.int_attr
        if not DaraCore.is_null(request.int_attr_2):
            body['IntAttr2'] = request.int_attr_2
        if not DaraCore.is_null(request.pic_name):
            body['PicName'] = request.pic_name
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.str_attr):
            body['StrAttr'] = request.str_attr
        if not DaraCore.is_null(request.str_attr_2):
            body['StrAttr2'] = request.str_attr_2
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateImage',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_image_with_options_async(
        self,
        request: main_models.UpdateImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.int_attr_3):
            query['IntAttr3'] = request.int_attr_3
        if not DaraCore.is_null(request.int_attr_4):
            query['IntAttr4'] = request.int_attr_4
        if not DaraCore.is_null(request.str_attr_3):
            query['StrAttr3'] = request.str_attr_3
        if not DaraCore.is_null(request.str_attr_4):
            query['StrAttr4'] = request.str_attr_4
        body = {}
        if not DaraCore.is_null(request.custom_content):
            body['CustomContent'] = request.custom_content
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.int_attr):
            body['IntAttr'] = request.int_attr
        if not DaraCore.is_null(request.int_attr_2):
            body['IntAttr2'] = request.int_attr_2
        if not DaraCore.is_null(request.pic_name):
            body['PicName'] = request.pic_name
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.str_attr):
            body['StrAttr'] = request.str_attr
        if not DaraCore.is_null(request.str_attr_2):
            body['StrAttr2'] = request.str_attr_2
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateImage',
            version = '2020-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_image(
        self,
        request: main_models.UpdateImageRequest,
    ) -> main_models.UpdateImageResponse:
        runtime = RuntimeOptions()
        return self.update_image_with_options(request, runtime)

    async def update_image_async(
        self,
        request: main_models.UpdateImageRequest,
    ) -> main_models.UpdateImageResponse:
        runtime = RuntimeOptions()
        return await self.update_image_with_options_async(request, runtime)
