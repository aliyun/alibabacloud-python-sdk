# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cloudauth_intl20220809 import models as main_models
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
        self._endpoint = self.get_endpoint('cloudauth-intl', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_face_record_with_options(
        self,
        request: main_models.AddFaceRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceRecordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.face_group_code):
            body['FaceGroupCode'] = request.face_group_code
        if not DaraCore.is_null(request.face_picture):
            body['FacePicture'] = request.face_picture
        if not DaraCore.is_null(request.face_picture_file):
            body['FacePictureFile'] = request.face_picture_file
        if not DaraCore.is_null(request.face_picture_url):
            body['FacePictureUrl'] = request.face_picture_url
        if not DaraCore.is_null(request.face_quality_check):
            body['FaceQualityCheck'] = request.face_quality_check
        if not DaraCore.is_null(request.merchant_user_id):
            body['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddFaceRecord',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFaceRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_record_with_options_async(
        self,
        request: main_models.AddFaceRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceRecordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.face_group_code):
            body['FaceGroupCode'] = request.face_group_code
        if not DaraCore.is_null(request.face_picture):
            body['FacePicture'] = request.face_picture
        if not DaraCore.is_null(request.face_picture_file):
            body['FacePictureFile'] = request.face_picture_file
        if not DaraCore.is_null(request.face_picture_url):
            body['FacePictureUrl'] = request.face_picture_url
        if not DaraCore.is_null(request.face_quality_check):
            body['FaceQualityCheck'] = request.face_quality_check
        if not DaraCore.is_null(request.merchant_user_id):
            body['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddFaceRecord',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFaceRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_face_record(
        self,
        request: main_models.AddFaceRecordRequest,
    ) -> main_models.AddFaceRecordResponse:
        runtime = RuntimeOptions()
        return self.add_face_record_with_options(request, runtime)

    async def add_face_record_async(
        self,
        request: main_models.AddFaceRecordRequest,
    ) -> main_models.AddFaceRecordResponse:
        runtime = RuntimeOptions()
        return await self.add_face_record_with_options_async(request, runtime)

    def add_face_record_advance(
        self,
        request: main_models.AddFaceRecordAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceRecordResponse:
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
            'Product': 'Cloudauth-intl',
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
        add_face_record_req = main_models.AddFaceRecordRequest()
        Utils.convert(request, add_face_record_req)
        if not DaraCore.is_null(request.face_picture_file_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.face_picture_file_object,
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
            add_face_record_req.face_picture_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        add_face_record_resp = self.add_face_record_with_options(add_face_record_req, runtime)
        return add_face_record_resp

    async def add_face_record_advance_async(
        self,
        request: main_models.AddFaceRecordAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceRecordResponse:
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
            'Product': 'Cloudauth-intl',
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
        add_face_record_req = main_models.AddFaceRecordRequest()
        Utils.convert(request, add_face_record_req)
        if not DaraCore.is_null(request.face_picture_file_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.face_picture_file_object,
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
            add_face_record_req.face_picture_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        add_face_record_resp = await self.add_face_record_with_options_async(add_face_record_req, runtime)
        return add_face_record_resp

    def address_compare_intl_with_options(
        self,
        request: main_models.AddressCompareIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddressCompareIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_country):
            query['DefaultCountry'] = request.default_country
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.text_1):
            query['Text1'] = request.text_1
        if not DaraCore.is_null(request.text_2):
            query['Text2'] = request.text_2
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddressCompareIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddressCompareIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def address_compare_intl_with_options_async(
        self,
        request: main_models.AddressCompareIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddressCompareIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_country):
            query['DefaultCountry'] = request.default_country
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.text_1):
            query['Text1'] = request.text_1
        if not DaraCore.is_null(request.text_2):
            query['Text2'] = request.text_2
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddressCompareIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddressCompareIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def address_compare_intl(
        self,
        request: main_models.AddressCompareIntlRequest,
    ) -> main_models.AddressCompareIntlResponse:
        runtime = RuntimeOptions()
        return self.address_compare_intl_with_options(request, runtime)

    async def address_compare_intl_async(
        self,
        request: main_models.AddressCompareIntlRequest,
    ) -> main_models.AddressCompareIntlResponse:
        runtime = RuntimeOptions()
        return await self.address_compare_intl_with_options_async(request, runtime)

    def address_verify_intl_with_options(
        self,
        request: main_models.AddressVerifyIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddressVerifyIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.default_city):
            query['DefaultCity'] = request.default_city
        if not DaraCore.is_null(request.default_country):
            query['DefaultCountry'] = request.default_country
        if not DaraCore.is_null(request.default_district):
            query['DefaultDistrict'] = request.default_district
        if not DaraCore.is_null(request.default_province):
            query['DefaultProvince'] = request.default_province
        if not DaraCore.is_null(request.latitude):
            query['Latitude'] = request.latitude
        if not DaraCore.is_null(request.longitude):
            query['Longitude'] = request.longitude
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.text):
            query['Text'] = request.text
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddressVerifyIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddressVerifyIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def address_verify_intl_with_options_async(
        self,
        request: main_models.AddressVerifyIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddressVerifyIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.default_city):
            query['DefaultCity'] = request.default_city
        if not DaraCore.is_null(request.default_country):
            query['DefaultCountry'] = request.default_country
        if not DaraCore.is_null(request.default_district):
            query['DefaultDistrict'] = request.default_district
        if not DaraCore.is_null(request.default_province):
            query['DefaultProvince'] = request.default_province
        if not DaraCore.is_null(request.latitude):
            query['Latitude'] = request.latitude
        if not DaraCore.is_null(request.longitude):
            query['Longitude'] = request.longitude
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.text):
            query['Text'] = request.text
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddressVerifyIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddressVerifyIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def address_verify_intl(
        self,
        request: main_models.AddressVerifyIntlRequest,
    ) -> main_models.AddressVerifyIntlResponse:
        runtime = RuntimeOptions()
        return self.address_verify_intl_with_options(request, runtime)

    async def address_verify_intl_async(
        self,
        request: main_models.AddressVerifyIntlRequest,
    ) -> main_models.AddressVerifyIntlResponse:
        runtime = RuntimeOptions()
        return await self.address_verify_intl_with_options_async(request, runtime)

    def address_verify_v2intl_with_options(
        self,
        request: main_models.AddressVerifyV2IntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddressVerifyV2IntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_token):
            query['DeviceToken'] = request.device_token
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.reg_country):
            query['RegCountry'] = request.reg_country
        if not DaraCore.is_null(request.text):
            query['Text'] = request.text
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddressVerifyV2Intl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddressVerifyV2IntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def address_verify_v2intl_with_options_async(
        self,
        request: main_models.AddressVerifyV2IntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddressVerifyV2IntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_token):
            query['DeviceToken'] = request.device_token
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.reg_country):
            query['RegCountry'] = request.reg_country
        if not DaraCore.is_null(request.text):
            query['Text'] = request.text
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddressVerifyV2Intl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddressVerifyV2IntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def address_verify_v2intl(
        self,
        request: main_models.AddressVerifyV2IntlRequest,
    ) -> main_models.AddressVerifyV2IntlResponse:
        runtime = RuntimeOptions()
        return self.address_verify_v2intl_with_options(request, runtime)

    async def address_verify_v2intl_async(
        self,
        request: main_models.AddressVerifyV2IntlRequest,
    ) -> main_models.AddressVerifyV2IntlResponse:
        runtime = RuntimeOptions()
        return await self.address_verify_v2intl_with_options_async(request, runtime)

    def bank_meta_verify_intl_with_options(
        self,
        request: main_models.BankMetaVerifyIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BankMetaVerifyIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bank_card):
            query['BankCard'] = request.bank_card
        if not DaraCore.is_null(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.verify_mode):
            query['VerifyMode'] = request.verify_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BankMetaVerifyIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BankMetaVerifyIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def bank_meta_verify_intl_with_options_async(
        self,
        request: main_models.BankMetaVerifyIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BankMetaVerifyIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bank_card):
            query['BankCard'] = request.bank_card
        if not DaraCore.is_null(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.verify_mode):
            query['VerifyMode'] = request.verify_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BankMetaVerifyIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BankMetaVerifyIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bank_meta_verify_intl(
        self,
        request: main_models.BankMetaVerifyIntlRequest,
    ) -> main_models.BankMetaVerifyIntlResponse:
        runtime = RuntimeOptions()
        return self.bank_meta_verify_intl_with_options(request, runtime)

    async def bank_meta_verify_intl_async(
        self,
        request: main_models.BankMetaVerifyIntlRequest,
    ) -> main_models.BankMetaVerifyIntlResponse:
        runtime = RuntimeOptions()
        return await self.bank_meta_verify_intl_with_options_async(request, runtime)

    def card_ocr_with_options(
        self,
        request: main_models.CardOcrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CardOcrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.doc_type):
            query['DocType'] = request.doc_type
        if not DaraCore.is_null(request.id_face_quality):
            query['IdFaceQuality'] = request.id_face_quality
        if not DaraCore.is_null(request.id_ocr_picture_url):
            query['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.ocr):
            query['Ocr'] = request.ocr
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.spoof):
            query['Spoof'] = request.spoof
        body = {}
        if not DaraCore.is_null(request.id_ocr_picture_base_64):
            body['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CardOcr',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CardOcrResponse(),
            self.call_api(params, req, runtime)
        )

    async def card_ocr_with_options_async(
        self,
        request: main_models.CardOcrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CardOcrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.doc_type):
            query['DocType'] = request.doc_type
        if not DaraCore.is_null(request.id_face_quality):
            query['IdFaceQuality'] = request.id_face_quality
        if not DaraCore.is_null(request.id_ocr_picture_url):
            query['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.ocr):
            query['Ocr'] = request.ocr
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.spoof):
            query['Spoof'] = request.spoof
        body = {}
        if not DaraCore.is_null(request.id_ocr_picture_base_64):
            body['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CardOcr',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CardOcrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def card_ocr(
        self,
        request: main_models.CardOcrRequest,
    ) -> main_models.CardOcrResponse:
        runtime = RuntimeOptions()
        return self.card_ocr_with_options(request, runtime)

    async def card_ocr_async(
        self,
        request: main_models.CardOcrRequest,
    ) -> main_models.CardOcrResponse:
        runtime = RuntimeOptions()
        return await self.card_ocr_with_options_async(request, runtime)

    def check_result_with_options(
        self,
        request: main_models.CheckResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extra_image_control_list):
            query['ExtraImageControlList'] = request.extra_image_control_list
        if not DaraCore.is_null(request.is_return_image):
            query['IsReturnImage'] = request.is_return_image
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.return_five_category_spoof_result):
            query['ReturnFiveCategorySpoofResult'] = request.return_five_category_spoof_result
        if not DaraCore.is_null(request.transaction_id):
            query['TransactionId'] = request.transaction_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckResult',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_result_with_options_async(
        self,
        request: main_models.CheckResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extra_image_control_list):
            query['ExtraImageControlList'] = request.extra_image_control_list
        if not DaraCore.is_null(request.is_return_image):
            query['IsReturnImage'] = request.is_return_image
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.return_five_category_spoof_result):
            query['ReturnFiveCategorySpoofResult'] = request.return_five_category_spoof_result
        if not DaraCore.is_null(request.transaction_id):
            query['TransactionId'] = request.transaction_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckResult',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_result(
        self,
        request: main_models.CheckResultRequest,
    ) -> main_models.CheckResultResponse:
        runtime = RuntimeOptions()
        return self.check_result_with_options(request, runtime)

    async def check_result_async(
        self,
        request: main_models.CheckResultRequest,
    ) -> main_models.CheckResultResponse:
        runtime = RuntimeOptions()
        return await self.check_result_with_options_async(request, runtime)

    def check_verify_log_with_options(
        self,
        request: main_models.CheckVerifyLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckVerifyLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.merchant_biz_id):
            body['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckVerifyLog',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckVerifyLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_verify_log_with_options_async(
        self,
        request: main_models.CheckVerifyLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckVerifyLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.merchant_biz_id):
            body['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckVerifyLog',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckVerifyLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_verify_log(
        self,
        request: main_models.CheckVerifyLogRequest,
    ) -> main_models.CheckVerifyLogResponse:
        runtime = RuntimeOptions()
        return self.check_verify_log_with_options(request, runtime)

    async def check_verify_log_async(
        self,
        request: main_models.CheckVerifyLogRequest,
    ) -> main_models.CheckVerifyLogResponse:
        runtime = RuntimeOptions()
        return await self.check_verify_log_with_options_async(request, runtime)

    def credential_get_result_intl_with_options(
        self,
        request: main_models.CredentialGetResultIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialGetResultIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.transaction_id):
            query['TransactionId'] = request.transaction_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CredentialGetResultIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CredentialGetResultIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def credential_get_result_intl_with_options_async(
        self,
        request: main_models.CredentialGetResultIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialGetResultIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.transaction_id):
            query['TransactionId'] = request.transaction_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CredentialGetResultIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CredentialGetResultIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def credential_get_result_intl(
        self,
        request: main_models.CredentialGetResultIntlRequest,
    ) -> main_models.CredentialGetResultIntlResponse:
        runtime = RuntimeOptions()
        return self.credential_get_result_intl_with_options(request, runtime)

    async def credential_get_result_intl_async(
        self,
        request: main_models.CredentialGetResultIntlRequest,
    ) -> main_models.CredentialGetResultIntlResponse:
        runtime = RuntimeOptions()
        return await self.credential_get_result_intl_with_options_async(request, runtime)

    def credential_recognition_intl_with_options(
        self,
        request: main_models.CredentialRecognitionIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialRecognitionIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.doc_type):
            query['DocType'] = request.doc_type
        if not DaraCore.is_null(request.fraud_check):
            query['FraudCheck'] = request.fraud_check
        if not DaraCore.is_null(request.ocr_area):
            query['OcrArea'] = request.ocr_area
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        body = {}
        if not DaraCore.is_null(request.credential_ocr_picture_base_64):
            body['CredentialOcrPictureBase64'] = request.credential_ocr_picture_base_64
        if not DaraCore.is_null(request.credential_ocr_picture_url):
            body['CredentialOcrPictureUrl'] = request.credential_ocr_picture_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CredentialRecognitionIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CredentialRecognitionIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def credential_recognition_intl_with_options_async(
        self,
        request: main_models.CredentialRecognitionIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialRecognitionIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.doc_type):
            query['DocType'] = request.doc_type
        if not DaraCore.is_null(request.fraud_check):
            query['FraudCheck'] = request.fraud_check
        if not DaraCore.is_null(request.ocr_area):
            query['OcrArea'] = request.ocr_area
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        body = {}
        if not DaraCore.is_null(request.credential_ocr_picture_base_64):
            body['CredentialOcrPictureBase64'] = request.credential_ocr_picture_base_64
        if not DaraCore.is_null(request.credential_ocr_picture_url):
            body['CredentialOcrPictureUrl'] = request.credential_ocr_picture_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CredentialRecognitionIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CredentialRecognitionIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def credential_recognition_intl(
        self,
        request: main_models.CredentialRecognitionIntlRequest,
    ) -> main_models.CredentialRecognitionIntlResponse:
        runtime = RuntimeOptions()
        return self.credential_recognition_intl_with_options(request, runtime)

    async def credential_recognition_intl_async(
        self,
        request: main_models.CredentialRecognitionIntlRequest,
    ) -> main_models.CredentialRecognitionIntlResponse:
        runtime = RuntimeOptions()
        return await self.credential_recognition_intl_with_options_async(request, runtime)

    def credential_submit_intl_with_options(
        self,
        request: main_models.CredentialSubmitIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialSubmitIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.doc_type):
            query['DocType'] = request.doc_type
        if not DaraCore.is_null(request.fraud_check):
            query['FraudCheck'] = request.fraud_check
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.ocr_area):
            query['OcrArea'] = request.ocr_area
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        body = {}
        if not DaraCore.is_null(request.credential_ocr_picture_base_64):
            body['CredentialOcrPictureBase64'] = request.credential_ocr_picture_base_64
        if not DaraCore.is_null(request.credential_ocr_picture_url):
            body['CredentialOcrPictureUrl'] = request.credential_ocr_picture_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CredentialSubmitIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CredentialSubmitIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def credential_submit_intl_with_options_async(
        self,
        request: main_models.CredentialSubmitIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialSubmitIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.doc_type):
            query['DocType'] = request.doc_type
        if not DaraCore.is_null(request.fraud_check):
            query['FraudCheck'] = request.fraud_check
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.ocr_area):
            query['OcrArea'] = request.ocr_area
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        body = {}
        if not DaraCore.is_null(request.credential_ocr_picture_base_64):
            body['CredentialOcrPictureBase64'] = request.credential_ocr_picture_base_64
        if not DaraCore.is_null(request.credential_ocr_picture_url):
            body['CredentialOcrPictureUrl'] = request.credential_ocr_picture_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CredentialSubmitIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CredentialSubmitIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def credential_submit_intl(
        self,
        request: main_models.CredentialSubmitIntlRequest,
    ) -> main_models.CredentialSubmitIntlResponse:
        runtime = RuntimeOptions()
        return self.credential_submit_intl_with_options(request, runtime)

    async def credential_submit_intl_async(
        self,
        request: main_models.CredentialSubmitIntlRequest,
    ) -> main_models.CredentialSubmitIntlResponse:
        runtime = RuntimeOptions()
        return await self.credential_submit_intl_with_options_async(request, runtime)

    def credential_verify_intl_with_options(
        self,
        request: main_models.CredentialVerifyIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialVerifyIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cred_name):
            query['CredName'] = request.cred_name
        if not DaraCore.is_null(request.cred_type):
            query['CredType'] = request.cred_type
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        body = {}
        if not DaraCore.is_null(request.image_file):
            body['ImageFile'] = request.image_file
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CredentialVerifyIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CredentialVerifyIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def credential_verify_intl_with_options_async(
        self,
        request: main_models.CredentialVerifyIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialVerifyIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cred_name):
            query['CredName'] = request.cred_name
        if not DaraCore.is_null(request.cred_type):
            query['CredType'] = request.cred_type
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        body = {}
        if not DaraCore.is_null(request.image_file):
            body['ImageFile'] = request.image_file
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CredentialVerifyIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CredentialVerifyIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def credential_verify_intl(
        self,
        request: main_models.CredentialVerifyIntlRequest,
    ) -> main_models.CredentialVerifyIntlResponse:
        runtime = RuntimeOptions()
        return self.credential_verify_intl_with_options(request, runtime)

    async def credential_verify_intl_async(
        self,
        request: main_models.CredentialVerifyIntlRequest,
    ) -> main_models.CredentialVerifyIntlResponse:
        runtime = RuntimeOptions()
        return await self.credential_verify_intl_with_options_async(request, runtime)

    def credential_verify_intl_advance(
        self,
        request: main_models.CredentialVerifyIntlAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialVerifyIntlResponse:
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
            'Product': 'Cloudauth-intl',
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
        credential_verify_intl_req = main_models.CredentialVerifyIntlRequest()
        Utils.convert(request, credential_verify_intl_req)
        if not DaraCore.is_null(request.image_file_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.image_file_object,
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
            credential_verify_intl_req.image_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        credential_verify_intl_resp = self.credential_verify_intl_with_options(credential_verify_intl_req, runtime)
        return credential_verify_intl_resp

    async def credential_verify_intl_advance_async(
        self,
        request: main_models.CredentialVerifyIntlAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialVerifyIntlResponse:
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
            'Product': 'Cloudauth-intl',
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
        credential_verify_intl_req = main_models.CredentialVerifyIntlRequest()
        Utils.convert(request, credential_verify_intl_req)
        if not DaraCore.is_null(request.image_file_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.image_file_object,
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
            credential_verify_intl_req.image_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        credential_verify_intl_resp = await self.credential_verify_intl_with_options_async(credential_verify_intl_req, runtime)
        return credential_verify_intl_resp

    def deepfake_detect_intl_with_options(
        self,
        request: main_models.DeepfakeDetectIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeepfakeDetectIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.face_input_type):
            query['FaceInputType'] = request.face_input_type
        if not DaraCore.is_null(request.face_url):
            query['FaceUrl'] = request.face_url
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        body = {}
        if not DaraCore.is_null(request.face_base_64):
            body['FaceBase64'] = request.face_base_64
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeepfakeDetectIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeepfakeDetectIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def deepfake_detect_intl_with_options_async(
        self,
        request: main_models.DeepfakeDetectIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeepfakeDetectIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.face_input_type):
            query['FaceInputType'] = request.face_input_type
        if not DaraCore.is_null(request.face_url):
            query['FaceUrl'] = request.face_url
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        body = {}
        if not DaraCore.is_null(request.face_base_64):
            body['FaceBase64'] = request.face_base_64
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeepfakeDetectIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeepfakeDetectIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deepfake_detect_intl(
        self,
        request: main_models.DeepfakeDetectIntlRequest,
    ) -> main_models.DeepfakeDetectIntlResponse:
        runtime = RuntimeOptions()
        return self.deepfake_detect_intl_with_options(request, runtime)

    async def deepfake_detect_intl_async(
        self,
        request: main_models.DeepfakeDetectIntlRequest,
    ) -> main_models.DeepfakeDetectIntlResponse:
        runtime = RuntimeOptions()
        return await self.deepfake_detect_intl_with_options_async(request, runtime)

    def deepfake_detect_intl_stream_with_options(
        self,
        request: main_models.DeepfakeDetectIntlStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeepfakeDetectIntlStreamResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.face_base_64):
            body['FaceBase64'] = request.face_base_64
        if not DaraCore.is_null(request.face_file):
            body['FaceFile'] = request.face_file
        if not DaraCore.is_null(request.face_input_type):
            body['FaceInputType'] = request.face_input_type
        if not DaraCore.is_null(request.face_url):
            body['FaceUrl'] = request.face_url
        if not DaraCore.is_null(request.merchant_biz_id):
            body['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_code):
            body['SceneCode'] = request.scene_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeepfakeDetectIntlStream',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeepfakeDetectIntlStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def deepfake_detect_intl_stream_with_options_async(
        self,
        request: main_models.DeepfakeDetectIntlStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeepfakeDetectIntlStreamResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.face_base_64):
            body['FaceBase64'] = request.face_base_64
        if not DaraCore.is_null(request.face_file):
            body['FaceFile'] = request.face_file
        if not DaraCore.is_null(request.face_input_type):
            body['FaceInputType'] = request.face_input_type
        if not DaraCore.is_null(request.face_url):
            body['FaceUrl'] = request.face_url
        if not DaraCore.is_null(request.merchant_biz_id):
            body['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_code):
            body['SceneCode'] = request.scene_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeepfakeDetectIntlStream',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeepfakeDetectIntlStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deepfake_detect_intl_stream(
        self,
        request: main_models.DeepfakeDetectIntlStreamRequest,
    ) -> main_models.DeepfakeDetectIntlStreamResponse:
        runtime = RuntimeOptions()
        return self.deepfake_detect_intl_stream_with_options(request, runtime)

    async def deepfake_detect_intl_stream_async(
        self,
        request: main_models.DeepfakeDetectIntlStreamRequest,
    ) -> main_models.DeepfakeDetectIntlStreamResponse:
        runtime = RuntimeOptions()
        return await self.deepfake_detect_intl_stream_with_options_async(request, runtime)

    def deepfake_detect_intl_stream_advance(
        self,
        request: main_models.DeepfakeDetectIntlStreamAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeepfakeDetectIntlStreamResponse:
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
            'Product': 'Cloudauth-intl',
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
        deepfake_detect_intl_stream_req = main_models.DeepfakeDetectIntlStreamRequest()
        Utils.convert(request, deepfake_detect_intl_stream_req)
        if not DaraCore.is_null(request.face_file_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.face_file_object,
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
            deepfake_detect_intl_stream_req.face_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        deepfake_detect_intl_stream_resp = self.deepfake_detect_intl_stream_with_options(deepfake_detect_intl_stream_req, runtime)
        return deepfake_detect_intl_stream_resp

    async def deepfake_detect_intl_stream_advance_async(
        self,
        request: main_models.DeepfakeDetectIntlStreamAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeepfakeDetectIntlStreamResponse:
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
            'Product': 'Cloudauth-intl',
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
        deepfake_detect_intl_stream_req = main_models.DeepfakeDetectIntlStreamRequest()
        Utils.convert(request, deepfake_detect_intl_stream_req)
        if not DaraCore.is_null(request.face_file_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.face_file_object,
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
            deepfake_detect_intl_stream_req.face_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        deepfake_detect_intl_stream_resp = await self.deepfake_detect_intl_stream_with_options_async(deepfake_detect_intl_stream_req, runtime)
        return deepfake_detect_intl_stream_resp

    def delete_face_group_with_options(
        self,
        request: main_models.DeleteFaceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaceGroup',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_group_with_options_async(
        self,
        request: main_models.DeleteFaceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaceGroup',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face_group(
        self,
        request: main_models.DeleteFaceGroupRequest,
    ) -> main_models.DeleteFaceGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_face_group_with_options(request, runtime)

    async def delete_face_group_async(
        self,
        request: main_models.DeleteFaceGroupRequest,
    ) -> main_models.DeleteFaceGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_face_group_with_options_async(request, runtime)

    def delete_face_record_with_options(
        self,
        request: main_models.DeleteFaceRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaceRecordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaceRecord',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaceRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_record_with_options_async(
        self,
        request: main_models.DeleteFaceRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaceRecordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaceRecord',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaceRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face_record(
        self,
        request: main_models.DeleteFaceRecordRequest,
    ) -> main_models.DeleteFaceRecordResponse:
        runtime = RuntimeOptions()
        return self.delete_face_record_with_options(request, runtime)

    async def delete_face_record_async(
        self,
        request: main_models.DeleteFaceRecordRequest,
    ) -> main_models.DeleteFaceRecordResponse:
        runtime = RuntimeOptions()
        return await self.delete_face_record_with_options_async(request, runtime)

    def delete_verify_result_with_options(
        self,
        request: main_models.DeleteVerifyResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVerifyResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_after_query):
            query['DeleteAfterQuery'] = request.delete_after_query
        if not DaraCore.is_null(request.delete_type):
            query['DeleteType'] = request.delete_type
        if not DaraCore.is_null(request.transaction_id):
            query['TransactionId'] = request.transaction_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVerifyResult',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVerifyResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_verify_result_with_options_async(
        self,
        request: main_models.DeleteVerifyResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVerifyResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_after_query):
            query['DeleteAfterQuery'] = request.delete_after_query
        if not DaraCore.is_null(request.delete_type):
            query['DeleteType'] = request.delete_type
        if not DaraCore.is_null(request.transaction_id):
            query['TransactionId'] = request.transaction_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVerifyResult',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVerifyResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_verify_result(
        self,
        request: main_models.DeleteVerifyResultRequest,
    ) -> main_models.DeleteVerifyResultResponse:
        runtime = RuntimeOptions()
        return self.delete_verify_result_with_options(request, runtime)

    async def delete_verify_result_async(
        self,
        request: main_models.DeleteVerifyResultRequest,
    ) -> main_models.DeleteVerifyResultResponse:
        runtime = RuntimeOptions()
        return await self.delete_verify_result_with_options_async(request, runtime)

    def doc_ocr_with_options(
        self,
        request: main_models.DocOcrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DocOcrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.card_side):
            query['CardSide'] = request.card_side
        if not DaraCore.is_null(request.doc_type):
            query['DocType'] = request.doc_type
        if not DaraCore.is_null(request.id_face_quality):
            query['IdFaceQuality'] = request.id_face_quality
        if not DaraCore.is_null(request.id_ocr_picture_url):
            query['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not DaraCore.is_null(request.id_threshold):
            query['IdThreshold'] = request.id_threshold
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.ocr):
            query['Ocr'] = request.ocr
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.spoof):
            query['Spoof'] = request.spoof
        body = {}
        if not DaraCore.is_null(request.id_ocr_picture_base_64):
            body['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DocOcr',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DocOcrResponse(),
            self.call_api(params, req, runtime)
        )

    async def doc_ocr_with_options_async(
        self,
        request: main_models.DocOcrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DocOcrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.card_side):
            query['CardSide'] = request.card_side
        if not DaraCore.is_null(request.doc_type):
            query['DocType'] = request.doc_type
        if not DaraCore.is_null(request.id_face_quality):
            query['IdFaceQuality'] = request.id_face_quality
        if not DaraCore.is_null(request.id_ocr_picture_url):
            query['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not DaraCore.is_null(request.id_threshold):
            query['IdThreshold'] = request.id_threshold
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.ocr):
            query['Ocr'] = request.ocr
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.spoof):
            query['Spoof'] = request.spoof
        body = {}
        if not DaraCore.is_null(request.id_ocr_picture_base_64):
            body['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DocOcr',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DocOcrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def doc_ocr(
        self,
        request: main_models.DocOcrRequest,
    ) -> main_models.DocOcrResponse:
        runtime = RuntimeOptions()
        return self.doc_ocr_with_options(request, runtime)

    async def doc_ocr_async(
        self,
        request: main_models.DocOcrRequest,
    ) -> main_models.DocOcrResponse:
        runtime = RuntimeOptions()
        return await self.doc_ocr_with_options_async(request, runtime)

    def doc_ocr_max_with_options(
        self,
        request: main_models.DocOcrMaxRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DocOcrMaxResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ocr_value_standard):
            query['OcrValueStandard'] = request.ocr_value_standard
        body = {}
        if not DaraCore.is_null(request.authorize):
            body['Authorize'] = request.authorize
        if not DaraCore.is_null(request.doc_page):
            body['DocPage'] = request.doc_page
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.id_ocr_picture_base_64):
            body['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        if not DaraCore.is_null(request.id_ocr_picture_url):
            body['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not DaraCore.is_null(request.id_spoof):
            body['IdSpoof'] = request.id_spoof
        if not DaraCore.is_null(request.id_threshold):
            body['IdThreshold'] = request.id_threshold
        if not DaraCore.is_null(request.merchant_biz_id):
            body['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            body['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.ocr_model):
            body['OcrModel'] = request.ocr_model
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.scene_code):
            body['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.spoof):
            body['Spoof'] = request.spoof
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DocOcrMax',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DocOcrMaxResponse(),
            self.call_api(params, req, runtime)
        )

    async def doc_ocr_max_with_options_async(
        self,
        request: main_models.DocOcrMaxRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DocOcrMaxResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ocr_value_standard):
            query['OcrValueStandard'] = request.ocr_value_standard
        body = {}
        if not DaraCore.is_null(request.authorize):
            body['Authorize'] = request.authorize
        if not DaraCore.is_null(request.doc_page):
            body['DocPage'] = request.doc_page
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.id_ocr_picture_base_64):
            body['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        if not DaraCore.is_null(request.id_ocr_picture_url):
            body['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not DaraCore.is_null(request.id_spoof):
            body['IdSpoof'] = request.id_spoof
        if not DaraCore.is_null(request.id_threshold):
            body['IdThreshold'] = request.id_threshold
        if not DaraCore.is_null(request.merchant_biz_id):
            body['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            body['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.ocr_model):
            body['OcrModel'] = request.ocr_model
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.scene_code):
            body['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.spoof):
            body['Spoof'] = request.spoof
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DocOcrMax',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DocOcrMaxResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def doc_ocr_max(
        self,
        request: main_models.DocOcrMaxRequest,
    ) -> main_models.DocOcrMaxResponse:
        runtime = RuntimeOptions()
        return self.doc_ocr_max_with_options(request, runtime)

    async def doc_ocr_max_async(
        self,
        request: main_models.DocOcrMaxRequest,
    ) -> main_models.DocOcrMaxResponse:
        runtime = RuntimeOptions()
        return await self.doc_ocr_max_with_options_async(request, runtime)

    def download_verify_record_intl_with_options(
        self,
        request: main_models.DownloadVerifyRecordIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadVerifyRecordIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.download_mode):
            query['DownloadMode'] = request.download_mode
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadVerifyRecordIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadVerifyRecordIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_verify_record_intl_with_options_async(
        self,
        request: main_models.DownloadVerifyRecordIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadVerifyRecordIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.download_mode):
            query['DownloadMode'] = request.download_mode
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadVerifyRecordIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadVerifyRecordIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_verify_record_intl(
        self,
        request: main_models.DownloadVerifyRecordIntlRequest,
    ) -> main_models.DownloadVerifyRecordIntlResponse:
        runtime = RuntimeOptions()
        return self.download_verify_record_intl_with_options(request, runtime)

    async def download_verify_record_intl_async(
        self,
        request: main_models.DownloadVerifyRecordIntlRequest,
    ) -> main_models.DownloadVerifyRecordIntlResponse:
        runtime = RuntimeOptions()
        return await self.download_verify_record_intl_with_options_async(request, runtime)

    def ekyc_verify_with_options(
        self,
        request: main_models.EkycVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EkycVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authorize):
            query['Authorize'] = request.authorize
        if not DaraCore.is_null(request.crop):
            query['Crop'] = request.crop
        if not DaraCore.is_null(request.doc_name):
            query['DocName'] = request.doc_name
        if not DaraCore.is_null(request.doc_no):
            query['DocNo'] = request.doc_no
        if not DaraCore.is_null(request.doc_type):
            query['DocType'] = request.doc_type
        if not DaraCore.is_null(request.face_picture_url):
            query['FacePictureUrl'] = request.face_picture_url
        if not DaraCore.is_null(request.id_ocr_picture_url):
            query['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not DaraCore.is_null(request.id_threshold):
            query['IdThreshold'] = request.id_threshold
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        body = {}
        if not DaraCore.is_null(request.face_picture_base_64):
            body['FacePictureBase64'] = request.face_picture_base_64
        if not DaraCore.is_null(request.id_ocr_picture_base_64):
            body['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EkycVerify',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EkycVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def ekyc_verify_with_options_async(
        self,
        request: main_models.EkycVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EkycVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authorize):
            query['Authorize'] = request.authorize
        if not DaraCore.is_null(request.crop):
            query['Crop'] = request.crop
        if not DaraCore.is_null(request.doc_name):
            query['DocName'] = request.doc_name
        if not DaraCore.is_null(request.doc_no):
            query['DocNo'] = request.doc_no
        if not DaraCore.is_null(request.doc_type):
            query['DocType'] = request.doc_type
        if not DaraCore.is_null(request.face_picture_url):
            query['FacePictureUrl'] = request.face_picture_url
        if not DaraCore.is_null(request.id_ocr_picture_url):
            query['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not DaraCore.is_null(request.id_threshold):
            query['IdThreshold'] = request.id_threshold
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        body = {}
        if not DaraCore.is_null(request.face_picture_base_64):
            body['FacePictureBase64'] = request.face_picture_base_64
        if not DaraCore.is_null(request.id_ocr_picture_base_64):
            body['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EkycVerify',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EkycVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ekyc_verify(
        self,
        request: main_models.EkycVerifyRequest,
    ) -> main_models.EkycVerifyResponse:
        runtime = RuntimeOptions()
        return self.ekyc_verify_with_options(request, runtime)

    async def ekyc_verify_async(
        self,
        request: main_models.EkycVerifyRequest,
    ) -> main_models.EkycVerifyResponse:
        runtime = RuntimeOptions()
        return await self.ekyc_verify_with_options_async(request, runtime)

    def face_compare_with_options(
        self,
        request: main_models.FaceCompareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FaceCompareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.face_picture_quality_check):
            query['FacePictureQualityCheck'] = request.face_picture_quality_check
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.source_face_picture_url):
            query['SourceFacePictureUrl'] = request.source_face_picture_url
        if not DaraCore.is_null(request.target_face_picture_url):
            query['TargetFacePictureUrl'] = request.target_face_picture_url
        body = {}
        if not DaraCore.is_null(request.source_face_picture):
            body['SourceFacePicture'] = request.source_face_picture
        if not DaraCore.is_null(request.target_face_picture):
            body['TargetFacePicture'] = request.target_face_picture
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FaceCompare',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FaceCompareResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_compare_with_options_async(
        self,
        request: main_models.FaceCompareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FaceCompareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.face_picture_quality_check):
            query['FacePictureQualityCheck'] = request.face_picture_quality_check
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.source_face_picture_url):
            query['SourceFacePictureUrl'] = request.source_face_picture_url
        if not DaraCore.is_null(request.target_face_picture_url):
            query['TargetFacePictureUrl'] = request.target_face_picture_url
        body = {}
        if not DaraCore.is_null(request.source_face_picture):
            body['SourceFacePicture'] = request.source_face_picture
        if not DaraCore.is_null(request.target_face_picture):
            body['TargetFacePicture'] = request.target_face_picture
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FaceCompare',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FaceCompareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_compare(
        self,
        request: main_models.FaceCompareRequest,
    ) -> main_models.FaceCompareResponse:
        runtime = RuntimeOptions()
        return self.face_compare_with_options(request, runtime)

    async def face_compare_async(
        self,
        request: main_models.FaceCompareRequest,
    ) -> main_models.FaceCompareResponse:
        runtime = RuntimeOptions()
        return await self.face_compare_with_options_async(request, runtime)

    def face_cross_compare_intl_with_options(
        self,
        request: main_models.FaceCrossCompareIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FaceCrossCompareIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compare_model):
            query['CompareModel'] = request.compare_model
        if not DaraCore.is_null(request.face_verify_threshold):
            query['FaceVerifyThreshold'] = request.face_verify_threshold
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.source_aface_picture_url):
            query['SourceAFacePictureUrl'] = request.source_aface_picture_url
        if not DaraCore.is_null(request.source_bface_picture_url):
            query['SourceBFacePictureUrl'] = request.source_bface_picture_url
        if not DaraCore.is_null(request.source_cface_picture_url):
            query['SourceCFacePictureUrl'] = request.source_cface_picture_url
        body = {}
        if not DaraCore.is_null(request.source_aface_picture):
            body['SourceAFacePicture'] = request.source_aface_picture
        if not DaraCore.is_null(request.source_bface_picture):
            body['SourceBFacePicture'] = request.source_bface_picture
        if not DaraCore.is_null(request.source_cface_picture):
            body['SourceCFacePicture'] = request.source_cface_picture
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FaceCrossCompareIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FaceCrossCompareIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_cross_compare_intl_with_options_async(
        self,
        request: main_models.FaceCrossCompareIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FaceCrossCompareIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compare_model):
            query['CompareModel'] = request.compare_model
        if not DaraCore.is_null(request.face_verify_threshold):
            query['FaceVerifyThreshold'] = request.face_verify_threshold
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.source_aface_picture_url):
            query['SourceAFacePictureUrl'] = request.source_aface_picture_url
        if not DaraCore.is_null(request.source_bface_picture_url):
            query['SourceBFacePictureUrl'] = request.source_bface_picture_url
        if not DaraCore.is_null(request.source_cface_picture_url):
            query['SourceCFacePictureUrl'] = request.source_cface_picture_url
        body = {}
        if not DaraCore.is_null(request.source_aface_picture):
            body['SourceAFacePicture'] = request.source_aface_picture
        if not DaraCore.is_null(request.source_bface_picture):
            body['SourceBFacePicture'] = request.source_bface_picture
        if not DaraCore.is_null(request.source_cface_picture):
            body['SourceCFacePicture'] = request.source_cface_picture
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FaceCrossCompareIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FaceCrossCompareIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_cross_compare_intl(
        self,
        request: main_models.FaceCrossCompareIntlRequest,
    ) -> main_models.FaceCrossCompareIntlResponse:
        runtime = RuntimeOptions()
        return self.face_cross_compare_intl_with_options(request, runtime)

    async def face_cross_compare_intl_async(
        self,
        request: main_models.FaceCrossCompareIntlRequest,
    ) -> main_models.FaceCrossCompareIntlResponse:
        runtime = RuntimeOptions()
        return await self.face_cross_compare_intl_with_options_async(request, runtime)

    def face_duplication_check_intl_with_options(
        self,
        request: main_models.FaceDuplicationCheckIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FaceDuplicationCheckIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        body = {}
        if not DaraCore.is_null(request.auto_registration):
            body['AutoRegistration'] = request.auto_registration
        if not DaraCore.is_null(request.face_group_codes):
            body['FaceGroupCodes'] = request.face_group_codes
        if not DaraCore.is_null(request.face_register_group_code):
            body['FaceRegisterGroupCode'] = request.face_register_group_code
        if not DaraCore.is_null(request.face_verify_threshold):
            body['FaceVerifyThreshold'] = request.face_verify_threshold
        if not DaraCore.is_null(request.liveness):
            body['Liveness'] = request.liveness
        if not DaraCore.is_null(request.merchant_biz_id):
            body['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            body['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.return_faces):
            body['ReturnFaces'] = request.return_faces
        if not DaraCore.is_null(request.save_face_picture):
            body['SaveFacePicture'] = request.save_face_picture
        if not DaraCore.is_null(request.scene_code):
            body['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.source_face_picture):
            body['SourceFacePicture'] = request.source_face_picture
        if not DaraCore.is_null(request.source_face_picture_url):
            body['SourceFacePictureUrl'] = request.source_face_picture_url
        if not DaraCore.is_null(request.target_face_picture):
            body['TargetFacePicture'] = request.target_face_picture
        if not DaraCore.is_null(request.target_face_picture_url):
            body['TargetFacePictureUrl'] = request.target_face_picture_url
        if not DaraCore.is_null(request.verify_model):
            body['VerifyModel'] = request.verify_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FaceDuplicationCheckIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FaceDuplicationCheckIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_duplication_check_intl_with_options_async(
        self,
        request: main_models.FaceDuplicationCheckIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FaceDuplicationCheckIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        body = {}
        if not DaraCore.is_null(request.auto_registration):
            body['AutoRegistration'] = request.auto_registration
        if not DaraCore.is_null(request.face_group_codes):
            body['FaceGroupCodes'] = request.face_group_codes
        if not DaraCore.is_null(request.face_register_group_code):
            body['FaceRegisterGroupCode'] = request.face_register_group_code
        if not DaraCore.is_null(request.face_verify_threshold):
            body['FaceVerifyThreshold'] = request.face_verify_threshold
        if not DaraCore.is_null(request.liveness):
            body['Liveness'] = request.liveness
        if not DaraCore.is_null(request.merchant_biz_id):
            body['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            body['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.return_faces):
            body['ReturnFaces'] = request.return_faces
        if not DaraCore.is_null(request.save_face_picture):
            body['SaveFacePicture'] = request.save_face_picture
        if not DaraCore.is_null(request.scene_code):
            body['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.source_face_picture):
            body['SourceFacePicture'] = request.source_face_picture
        if not DaraCore.is_null(request.source_face_picture_url):
            body['SourceFacePictureUrl'] = request.source_face_picture_url
        if not DaraCore.is_null(request.target_face_picture):
            body['TargetFacePicture'] = request.target_face_picture
        if not DaraCore.is_null(request.target_face_picture_url):
            body['TargetFacePictureUrl'] = request.target_face_picture_url
        if not DaraCore.is_null(request.verify_model):
            body['VerifyModel'] = request.verify_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FaceDuplicationCheckIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FaceDuplicationCheckIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_duplication_check_intl(
        self,
        request: main_models.FaceDuplicationCheckIntlRequest,
    ) -> main_models.FaceDuplicationCheckIntlResponse:
        runtime = RuntimeOptions()
        return self.face_duplication_check_intl_with_options(request, runtime)

    async def face_duplication_check_intl_async(
        self,
        request: main_models.FaceDuplicationCheckIntlRequest,
    ) -> main_models.FaceDuplicationCheckIntlResponse:
        runtime = RuntimeOptions()
        return await self.face_duplication_check_intl_with_options_async(request, runtime)

    def face_guard_risk_with_options(
        self,
        request: main_models.FaceGuardRiskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FaceGuardRiskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.device_token):
            query['DeviceToken'] = request.device_token
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FaceGuardRisk',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FaceGuardRiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_guard_risk_with_options_async(
        self,
        request: main_models.FaceGuardRiskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FaceGuardRiskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.device_token):
            query['DeviceToken'] = request.device_token
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FaceGuardRisk',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FaceGuardRiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_guard_risk(
        self,
        request: main_models.FaceGuardRiskRequest,
    ) -> main_models.FaceGuardRiskResponse:
        runtime = RuntimeOptions()
        return self.face_guard_risk_with_options(request, runtime)

    async def face_guard_risk_async(
        self,
        request: main_models.FaceGuardRiskRequest,
    ) -> main_models.FaceGuardRiskResponse:
        runtime = RuntimeOptions()
        return await self.face_guard_risk_with_options_async(request, runtime)

    def face_liveness_with_options(
        self,
        request: main_models.FaceLivenessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FaceLivenessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.crop):
            query['Crop'] = request.crop
        if not DaraCore.is_null(request.face_picture_url):
            query['FacePictureUrl'] = request.face_picture_url
        if not DaraCore.is_null(request.face_quality):
            query['FaceQuality'] = request.face_quality
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.occlusion):
            query['Occlusion'] = request.occlusion
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        body = {}
        if not DaraCore.is_null(request.face_picture_base_64):
            body['FacePictureBase64'] = request.face_picture_base_64
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FaceLiveness',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FaceLivenessResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_liveness_with_options_async(
        self,
        request: main_models.FaceLivenessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FaceLivenessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.crop):
            query['Crop'] = request.crop
        if not DaraCore.is_null(request.face_picture_url):
            query['FacePictureUrl'] = request.face_picture_url
        if not DaraCore.is_null(request.face_quality):
            query['FaceQuality'] = request.face_quality
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.occlusion):
            query['Occlusion'] = request.occlusion
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        body = {}
        if not DaraCore.is_null(request.face_picture_base_64):
            body['FacePictureBase64'] = request.face_picture_base_64
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FaceLiveness',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FaceLivenessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_liveness(
        self,
        request: main_models.FaceLivenessRequest,
    ) -> main_models.FaceLivenessResponse:
        runtime = RuntimeOptions()
        return self.face_liveness_with_options(request, runtime)

    async def face_liveness_async(
        self,
        request: main_models.FaceLivenessRequest,
    ) -> main_models.FaceLivenessResponse:
        runtime = RuntimeOptions()
        return await self.face_liveness_with_options_async(request, runtime)

    def fraud_result_call_back_with_options(
        self,
        request: main_models.FraudResultCallBackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FraudResultCallBackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.ext_params):
            query['ExtParams'] = request.ext_params
        if not DaraCore.is_null(request.result_code):
            query['ResultCode'] = request.result_code
        if not DaraCore.is_null(request.verify_deploy_env):
            query['VerifyDeployEnv'] = request.verify_deploy_env
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FraudResultCallBack',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FraudResultCallBackResponse(),
            self.call_api(params, req, runtime)
        )

    async def fraud_result_call_back_with_options_async(
        self,
        request: main_models.FraudResultCallBackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FraudResultCallBackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.ext_params):
            query['ExtParams'] = request.ext_params
        if not DaraCore.is_null(request.result_code):
            query['ResultCode'] = request.result_code
        if not DaraCore.is_null(request.verify_deploy_env):
            query['VerifyDeployEnv'] = request.verify_deploy_env
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FraudResultCallBack',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FraudResultCallBackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fraud_result_call_back(
        self,
        request: main_models.FraudResultCallBackRequest,
    ) -> main_models.FraudResultCallBackResponse:
        runtime = RuntimeOptions()
        return self.fraud_result_call_back_with_options(request, runtime)

    async def fraud_result_call_back_async(
        self,
        request: main_models.FraudResultCallBackRequest,
    ) -> main_models.FraudResultCallBackResponse:
        runtime = RuntimeOptions()
        return await self.fraud_result_call_back_with_options_async(request, runtime)

    def id_2meta_period_verify_intl_with_options(
        self,
        request: main_models.Id2MetaPeriodVerifyIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id2MetaPeriodVerifyIntlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_name):
            body['DocName'] = request.doc_name
        if not DaraCore.is_null(request.doc_no):
            body['DocNo'] = request.doc_no
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.merchant_biz_id):
            body['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            body['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_code):
            body['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.validity_end_date):
            body['ValidityEndDate'] = request.validity_end_date
        if not DaraCore.is_null(request.validity_start_date):
            body['ValidityStartDate'] = request.validity_start_date
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Id2MetaPeriodVerifyIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Id2MetaPeriodVerifyIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def id_2meta_period_verify_intl_with_options_async(
        self,
        request: main_models.Id2MetaPeriodVerifyIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id2MetaPeriodVerifyIntlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_name):
            body['DocName'] = request.doc_name
        if not DaraCore.is_null(request.doc_no):
            body['DocNo'] = request.doc_no
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.merchant_biz_id):
            body['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            body['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_code):
            body['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.validity_end_date):
            body['ValidityEndDate'] = request.validity_end_date
        if not DaraCore.is_null(request.validity_start_date):
            body['ValidityStartDate'] = request.validity_start_date
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Id2MetaPeriodVerifyIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Id2MetaPeriodVerifyIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def id_2meta_period_verify_intl(
        self,
        request: main_models.Id2MetaPeriodVerifyIntlRequest,
    ) -> main_models.Id2MetaPeriodVerifyIntlResponse:
        runtime = RuntimeOptions()
        return self.id_2meta_period_verify_intl_with_options(request, runtime)

    async def id_2meta_period_verify_intl_async(
        self,
        request: main_models.Id2MetaPeriodVerifyIntlRequest,
    ) -> main_models.Id2MetaPeriodVerifyIntlResponse:
        runtime = RuntimeOptions()
        return await self.id_2meta_period_verify_intl_with_options_async(request, runtime)

    def id_2meta_verify_intl_with_options(
        self,
        request: main_models.Id2MetaVerifyIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id2MetaVerifyIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Id2MetaVerifyIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Id2MetaVerifyIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def id_2meta_verify_intl_with_options_async(
        self,
        request: main_models.Id2MetaVerifyIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id2MetaVerifyIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Id2MetaVerifyIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Id2MetaVerifyIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def id_2meta_verify_intl(
        self,
        request: main_models.Id2MetaVerifyIntlRequest,
    ) -> main_models.Id2MetaVerifyIntlResponse:
        runtime = RuntimeOptions()
        return self.id_2meta_verify_intl_with_options(request, runtime)

    async def id_2meta_verify_intl_async(
        self,
        request: main_models.Id2MetaVerifyIntlRequest,
    ) -> main_models.Id2MetaVerifyIntlResponse:
        runtime = RuntimeOptions()
        return await self.id_2meta_verify_intl_with_options_async(request, runtime)

    def initialize_with_options(
        self,
        tmp_req: main_models.InitializeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitializeResponse:
        tmp_req.validate()
        request = main_models.InitializeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_page_config):
            request.doc_page_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_page_config, 'DocPageConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.app_quality_check):
            query['AppQualityCheck'] = request.app_quality_check
        if not DaraCore.is_null(request.authorize):
            query['Authorize'] = request.authorize
        if not DaraCore.is_null(request.auto_registration):
            query['AutoRegistration'] = request.auto_registration
        if not DaraCore.is_null(request.callback_token):
            query['CallbackToken'] = request.callback_token
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.chameleon_frame_enable):
            query['ChameleonFrameEnable'] = request.chameleon_frame_enable
        if not DaraCore.is_null(request.crop):
            query['Crop'] = request.crop
        if not DaraCore.is_null(request.date_of_birth):
            query['DateOfBirth'] = request.date_of_birth
        if not DaraCore.is_null(request.date_of_expiry):
            query['DateOfExpiry'] = request.date_of_expiry
        if not DaraCore.is_null(request.doc_name):
            query['DocName'] = request.doc_name
        if not DaraCore.is_null(request.doc_no):
            query['DocNo'] = request.doc_no
        if not DaraCore.is_null(request.doc_page_config_shrink):
            query['DocPageConfig'] = request.doc_page_config_shrink
        if not DaraCore.is_null(request.doc_scan_mode):
            query['DocScanMode'] = request.doc_scan_mode
        if not DaraCore.is_null(request.doc_type):
            query['DocType'] = request.doc_type
        if not DaraCore.is_null(request.doc_video):
            query['DocVideo'] = request.doc_video
        if not DaraCore.is_null(request.document_number):
            query['DocumentNumber'] = request.document_number
        if not DaraCore.is_null(request.edit_ocr_result):
            query['EditOcrResult'] = request.edit_ocr_result
        if not DaraCore.is_null(request.experience_code):
            query['ExperienceCode'] = request.experience_code
        if not DaraCore.is_null(request.face_group_codes):
            query['FaceGroupCodes'] = request.face_group_codes
        if not DaraCore.is_null(request.face_picture_url):
            query['FacePictureUrl'] = request.face_picture_url
        if not DaraCore.is_null(request.face_register_group_code):
            query['FaceRegisterGroupCode'] = request.face_register_group_code
        if not DaraCore.is_null(request.face_verify_threshold):
            query['FaceVerifyThreshold'] = request.face_verify_threshold
        if not DaraCore.is_null(request.id_face_quality):
            query['IdFaceQuality'] = request.id_face_quality
        if not DaraCore.is_null(request.id_spoof):
            query['IdSpoof'] = request.id_spoof
        if not DaraCore.is_null(request.id_threshold):
            query['IdThreshold'] = request.id_threshold
        if not DaraCore.is_null(request.language_config):
            query['LanguageConfig'] = request.language_config
        if not DaraCore.is_null(request.mrtdinput):
            query['MRTDInput'] = request.mrtdinput
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.meta_info):
            query['MetaInfo'] = request.meta_info
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.ocr):
            query['Ocr'] = request.ocr
        if not DaraCore.is_null(request.pages):
            query['Pages'] = request.pages
        if not DaraCore.is_null(request.procedure_priority):
            query['ProcedurePriority'] = request.procedure_priority
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_flow):
            query['ProductFlow'] = request.product_flow
        if not DaraCore.is_null(request.return_faces):
            query['ReturnFaces'] = request.return_faces
        if not DaraCore.is_null(request.return_url):
            query['ReturnUrl'] = request.return_url
        if not DaraCore.is_null(request.save_face_picture):
            query['SaveFacePicture'] = request.save_face_picture
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.security_level):
            query['SecurityLevel'] = request.security_level
        if not DaraCore.is_null(request.show_album_icon):
            query['ShowAlbumIcon'] = request.show_album_icon
        if not DaraCore.is_null(request.show_guide_page):
            query['ShowGuidePage'] = request.show_guide_page
        if not DaraCore.is_null(request.show_ocr_result):
            query['ShowOcrResult'] = request.show_ocr_result
        if not DaraCore.is_null(request.style_config):
            query['StyleConfig'] = request.style_config
        if not DaraCore.is_null(request.target_face_picture):
            query['TargetFacePicture'] = request.target_face_picture
        if not DaraCore.is_null(request.target_face_picture_url):
            query['TargetFacePictureUrl'] = request.target_face_picture_url
        if not DaraCore.is_null(request.use_nfc):
            query['UseNFC'] = request.use_nfc
        if not DaraCore.is_null(request.verify_model):
            query['VerifyModel'] = request.verify_model
        body = {}
        if not DaraCore.is_null(request.face_picture_base_64):
            body['FacePictureBase64'] = request.face_picture_base_64
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Initialize',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitializeResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_with_options_async(
        self,
        tmp_req: main_models.InitializeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitializeResponse:
        tmp_req.validate()
        request = main_models.InitializeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_page_config):
            request.doc_page_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_page_config, 'DocPageConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.app_quality_check):
            query['AppQualityCheck'] = request.app_quality_check
        if not DaraCore.is_null(request.authorize):
            query['Authorize'] = request.authorize
        if not DaraCore.is_null(request.auto_registration):
            query['AutoRegistration'] = request.auto_registration
        if not DaraCore.is_null(request.callback_token):
            query['CallbackToken'] = request.callback_token
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.chameleon_frame_enable):
            query['ChameleonFrameEnable'] = request.chameleon_frame_enable
        if not DaraCore.is_null(request.crop):
            query['Crop'] = request.crop
        if not DaraCore.is_null(request.date_of_birth):
            query['DateOfBirth'] = request.date_of_birth
        if not DaraCore.is_null(request.date_of_expiry):
            query['DateOfExpiry'] = request.date_of_expiry
        if not DaraCore.is_null(request.doc_name):
            query['DocName'] = request.doc_name
        if not DaraCore.is_null(request.doc_no):
            query['DocNo'] = request.doc_no
        if not DaraCore.is_null(request.doc_page_config_shrink):
            query['DocPageConfig'] = request.doc_page_config_shrink
        if not DaraCore.is_null(request.doc_scan_mode):
            query['DocScanMode'] = request.doc_scan_mode
        if not DaraCore.is_null(request.doc_type):
            query['DocType'] = request.doc_type
        if not DaraCore.is_null(request.doc_video):
            query['DocVideo'] = request.doc_video
        if not DaraCore.is_null(request.document_number):
            query['DocumentNumber'] = request.document_number
        if not DaraCore.is_null(request.edit_ocr_result):
            query['EditOcrResult'] = request.edit_ocr_result
        if not DaraCore.is_null(request.experience_code):
            query['ExperienceCode'] = request.experience_code
        if not DaraCore.is_null(request.face_group_codes):
            query['FaceGroupCodes'] = request.face_group_codes
        if not DaraCore.is_null(request.face_picture_url):
            query['FacePictureUrl'] = request.face_picture_url
        if not DaraCore.is_null(request.face_register_group_code):
            query['FaceRegisterGroupCode'] = request.face_register_group_code
        if not DaraCore.is_null(request.face_verify_threshold):
            query['FaceVerifyThreshold'] = request.face_verify_threshold
        if not DaraCore.is_null(request.id_face_quality):
            query['IdFaceQuality'] = request.id_face_quality
        if not DaraCore.is_null(request.id_spoof):
            query['IdSpoof'] = request.id_spoof
        if not DaraCore.is_null(request.id_threshold):
            query['IdThreshold'] = request.id_threshold
        if not DaraCore.is_null(request.language_config):
            query['LanguageConfig'] = request.language_config
        if not DaraCore.is_null(request.mrtdinput):
            query['MRTDInput'] = request.mrtdinput
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.meta_info):
            query['MetaInfo'] = request.meta_info
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.ocr):
            query['Ocr'] = request.ocr
        if not DaraCore.is_null(request.pages):
            query['Pages'] = request.pages
        if not DaraCore.is_null(request.procedure_priority):
            query['ProcedurePriority'] = request.procedure_priority
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_flow):
            query['ProductFlow'] = request.product_flow
        if not DaraCore.is_null(request.return_faces):
            query['ReturnFaces'] = request.return_faces
        if not DaraCore.is_null(request.return_url):
            query['ReturnUrl'] = request.return_url
        if not DaraCore.is_null(request.save_face_picture):
            query['SaveFacePicture'] = request.save_face_picture
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.security_level):
            query['SecurityLevel'] = request.security_level
        if not DaraCore.is_null(request.show_album_icon):
            query['ShowAlbumIcon'] = request.show_album_icon
        if not DaraCore.is_null(request.show_guide_page):
            query['ShowGuidePage'] = request.show_guide_page
        if not DaraCore.is_null(request.show_ocr_result):
            query['ShowOcrResult'] = request.show_ocr_result
        if not DaraCore.is_null(request.style_config):
            query['StyleConfig'] = request.style_config
        if not DaraCore.is_null(request.target_face_picture):
            query['TargetFacePicture'] = request.target_face_picture
        if not DaraCore.is_null(request.target_face_picture_url):
            query['TargetFacePictureUrl'] = request.target_face_picture_url
        if not DaraCore.is_null(request.use_nfc):
            query['UseNFC'] = request.use_nfc
        if not DaraCore.is_null(request.verify_model):
            query['VerifyModel'] = request.verify_model
        body = {}
        if not DaraCore.is_null(request.face_picture_base_64):
            body['FacePictureBase64'] = request.face_picture_base_64
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Initialize',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitializeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize(
        self,
        request: main_models.InitializeRequest,
    ) -> main_models.InitializeResponse:
        runtime = RuntimeOptions()
        return self.initialize_with_options(request, runtime)

    async def initialize_async(
        self,
        request: main_models.InitializeRequest,
    ) -> main_models.InitializeResponse:
        runtime = RuntimeOptions()
        return await self.initialize_with_options_async(request, runtime)

    def keepalive_intl_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.KeepaliveIntlResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'KeepaliveIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KeepaliveIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def keepalive_intl_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.KeepaliveIntlResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'KeepaliveIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KeepaliveIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def keepalive_intl(self) -> main_models.KeepaliveIntlResponse:
        runtime = RuntimeOptions()
        return self.keepalive_intl_with_options(runtime)

    async def keepalive_intl_async(self) -> main_models.KeepaliveIntlResponse:
        runtime = RuntimeOptions()
        return await self.keepalive_intl_with_options_async(runtime)

    def mobile_2meta_verify_intl_with_options(
        self,
        request: main_models.Mobile2MetaVerifyIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Mobile2MetaVerifyIntlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Mobile2MetaVerifyIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Mobile2MetaVerifyIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_2meta_verify_intl_with_options_async(
        self,
        request: main_models.Mobile2MetaVerifyIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Mobile2MetaVerifyIntlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Mobile2MetaVerifyIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Mobile2MetaVerifyIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_2meta_verify_intl(
        self,
        request: main_models.Mobile2MetaVerifyIntlRequest,
    ) -> main_models.Mobile2MetaVerifyIntlResponse:
        runtime = RuntimeOptions()
        return self.mobile_2meta_verify_intl_with_options(request, runtime)

    async def mobile_2meta_verify_intl_async(
        self,
        request: main_models.Mobile2MetaVerifyIntlRequest,
    ) -> main_models.Mobile2MetaVerifyIntlResponse:
        runtime = RuntimeOptions()
        return await self.mobile_2meta_verify_intl_with_options_async(request, runtime)

    def mobile_3meta_verify_intl_with_options(
        self,
        request: main_models.Mobile3MetaVerifyIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Mobile3MetaVerifyIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Mobile3MetaVerifyIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Mobile3MetaVerifyIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_3meta_verify_intl_with_options_async(
        self,
        request: main_models.Mobile3MetaVerifyIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Mobile3MetaVerifyIntlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Mobile3MetaVerifyIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Mobile3MetaVerifyIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_3meta_verify_intl(
        self,
        request: main_models.Mobile3MetaVerifyIntlRequest,
    ) -> main_models.Mobile3MetaVerifyIntlResponse:
        runtime = RuntimeOptions()
        return self.mobile_3meta_verify_intl_with_options(request, runtime)

    async def mobile_3meta_verify_intl_async(
        self,
        request: main_models.Mobile3MetaVerifyIntlRequest,
    ) -> main_models.Mobile3MetaVerifyIntlResponse:
        runtime = RuntimeOptions()
        return await self.mobile_3meta_verify_intl_with_options_async(request, runtime)

    def modify_face_group_with_options(
        self,
        request: main_models.ModifyFaceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFaceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFaceGroup',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFaceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_face_group_with_options_async(
        self,
        request: main_models.ModifyFaceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFaceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFaceGroup',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFaceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_face_group(
        self,
        request: main_models.ModifyFaceGroupRequest,
    ) -> main_models.ModifyFaceGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_face_group_with_options(request, runtime)

    async def modify_face_group_async(
        self,
        request: main_models.ModifyFaceGroupRequest,
    ) -> main_models.ModifyFaceGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_face_group_with_options_async(request, runtime)

    def modify_face_record_with_options(
        self,
        request: main_models.ModifyFaceRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFaceRecordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.face_group_code):
            body['FaceGroupCode'] = request.face_group_code
        if not DaraCore.is_null(request.img_oss_infos):
            body['ImgOssInfos'] = request.img_oss_infos
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFaceRecord',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFaceRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_face_record_with_options_async(
        self,
        request: main_models.ModifyFaceRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFaceRecordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.face_group_code):
            body['FaceGroupCode'] = request.face_group_code
        if not DaraCore.is_null(request.img_oss_infos):
            body['ImgOssInfos'] = request.img_oss_infos
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFaceRecord',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFaceRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_face_record(
        self,
        request: main_models.ModifyFaceRecordRequest,
    ) -> main_models.ModifyFaceRecordResponse:
        runtime = RuntimeOptions()
        return self.modify_face_record_with_options(request, runtime)

    async def modify_face_record_async(
        self,
        request: main_models.ModifyFaceRecordRequest,
    ) -> main_models.ModifyFaceRecordResponse:
        runtime = RuntimeOptions()
        return await self.modify_face_record_with_options_async(request, runtime)

    def query_face_group_with_options(
        self,
        request: main_models.QueryFaceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.group_code):
            query['GroupCode'] = request.group_code
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceGroup',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_group_with_options_async(
        self,
        request: main_models.QueryFaceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.group_code):
            query['GroupCode'] = request.group_code
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceGroup',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_group(
        self,
        request: main_models.QueryFaceGroupRequest,
    ) -> main_models.QueryFaceGroupResponse:
        runtime = RuntimeOptions()
        return self.query_face_group_with_options(request, runtime)

    async def query_face_group_async(
        self,
        request: main_models.QueryFaceGroupRequest,
    ) -> main_models.QueryFaceGroupResponse:
        runtime = RuntimeOptions()
        return await self.query_face_group_with_options_async(request, runtime)

    def query_face_record_with_options(
        self,
        request: main_models.QueryFaceRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.face_group_code):
            query['FaceGroupCode'] = request.face_group_code
        if not DaraCore.is_null(request.face_id):
            query['FaceId'] = request.face_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.registration_type):
            query['RegistrationType'] = request.registration_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceRecord',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_record_with_options_async(
        self,
        request: main_models.QueryFaceRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.face_group_code):
            query['FaceGroupCode'] = request.face_group_code
        if not DaraCore.is_null(request.face_id):
            query['FaceId'] = request.face_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.registration_type):
            query['RegistrationType'] = request.registration_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceRecord',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_record(
        self,
        request: main_models.QueryFaceRecordRequest,
    ) -> main_models.QueryFaceRecordResponse:
        runtime = RuntimeOptions()
        return self.query_face_record_with_options(request, runtime)

    async def query_face_record_async(
        self,
        request: main_models.QueryFaceRecordRequest,
    ) -> main_models.QueryFaceRecordResponse:
        runtime = RuntimeOptions()
        return await self.query_face_record_with_options_async(request, runtime)

    def temp_access_token_intl_with_options(
        self,
        request: main_models.TempAccessTokenIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TempAccessTokenIntlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TempAccessTokenIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TempAccessTokenIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def temp_access_token_intl_with_options_async(
        self,
        request: main_models.TempAccessTokenIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TempAccessTokenIntlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TempAccessTokenIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TempAccessTokenIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def temp_access_token_intl(
        self,
        request: main_models.TempAccessTokenIntlRequest,
    ) -> main_models.TempAccessTokenIntlResponse:
        runtime = RuntimeOptions()
        return self.temp_access_token_intl_with_options(request, runtime)

    async def temp_access_token_intl_async(
        self,
        request: main_models.TempAccessTokenIntlRequest,
    ) -> main_models.TempAccessTokenIntlResponse:
        runtime = RuntimeOptions()
        return await self.temp_access_token_intl_with_options_async(request, runtime)

    def temp_oss_url_intl_with_options(
        self,
        request: main_models.TempOssUrlIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TempOssUrlIntlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.object_name):
            body['ObjectName'] = request.object_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TempOssUrlIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TempOssUrlIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def temp_oss_url_intl_with_options_async(
        self,
        request: main_models.TempOssUrlIntlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TempOssUrlIntlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.object_name):
            body['ObjectName'] = request.object_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TempOssUrlIntl',
            version = '2022-08-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TempOssUrlIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def temp_oss_url_intl(
        self,
        request: main_models.TempOssUrlIntlRequest,
    ) -> main_models.TempOssUrlIntlResponse:
        runtime = RuntimeOptions()
        return self.temp_oss_url_intl_with_options(request, runtime)

    async def temp_oss_url_intl_async(
        self,
        request: main_models.TempOssUrlIntlRequest,
    ) -> main_models.TempOssUrlIntlResponse:
        runtime = RuntimeOptions()
        return await self.temp_oss_url_intl_with_options_async(request, runtime)
