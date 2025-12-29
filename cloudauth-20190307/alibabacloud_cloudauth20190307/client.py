# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cloudauth20190307 import models as main_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudauth', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def a_igcface_verify_with_options(
        self,
        request: main_models.AIGCFaceVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AIGCFaceVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.face_contrast_picture_url):
            query['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_object_name):
            query['OssObjectName'] = request.oss_object_name
        if not DaraCore.is_null(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        body = {}
        if not DaraCore.is_null(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AIGCFaceVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AIGCFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def a_igcface_verify_with_options_async(
        self,
        request: main_models.AIGCFaceVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AIGCFaceVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.face_contrast_picture_url):
            query['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_object_name):
            query['OssObjectName'] = request.oss_object_name
        if not DaraCore.is_null(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        body = {}
        if not DaraCore.is_null(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AIGCFaceVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AIGCFaceVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def a_igcface_verify(
        self,
        request: main_models.AIGCFaceVerifyRequest,
    ) -> main_models.AIGCFaceVerifyResponse:
        runtime = RuntimeOptions()
        return self.a_igcface_verify_with_options(request, runtime)

    async def a_igcface_verify_async(
        self,
        request: main_models.AIGCFaceVerifyRequest,
    ) -> main_models.AIGCFaceVerifyResponse:
        runtime = RuntimeOptions()
        return await self.a_igcface_verify_with_options_async(request, runtime)

    def bank_meta_verify_with_options(
        self,
        request: main_models.BankMetaVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BankMetaVerifyResponse:
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
            action = 'BankMetaVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BankMetaVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def bank_meta_verify_with_options_async(
        self,
        request: main_models.BankMetaVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BankMetaVerifyResponse:
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
            action = 'BankMetaVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BankMetaVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bank_meta_verify(
        self,
        request: main_models.BankMetaVerifyRequest,
    ) -> main_models.BankMetaVerifyResponse:
        runtime = RuntimeOptions()
        return self.bank_meta_verify_with_options(request, runtime)

    async def bank_meta_verify_async(
        self,
        request: main_models.BankMetaVerifyRequest,
    ) -> main_models.BankMetaVerifyResponse:
        runtime = RuntimeOptions()
        return await self.bank_meta_verify_with_options_async(request, runtime)

    def compare_face_verify_with_options(
        self,
        request: main_models.CompareFaceVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompareFaceVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.crop):
            body['Crop'] = request.crop
        if not DaraCore.is_null(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.source_certify_id):
            body['SourceCertifyId'] = request.source_certify_id
        if not DaraCore.is_null(request.source_face_contrast_picture):
            body['SourceFaceContrastPicture'] = request.source_face_contrast_picture
        if not DaraCore.is_null(request.source_face_contrast_picture_url):
            body['SourceFaceContrastPictureUrl'] = request.source_face_contrast_picture_url
        if not DaraCore.is_null(request.source_oss_bucket_name):
            body['SourceOssBucketName'] = request.source_oss_bucket_name
        if not DaraCore.is_null(request.source_oss_object_name):
            body['SourceOssObjectName'] = request.source_oss_object_name
        if not DaraCore.is_null(request.target_certify_id):
            body['TargetCertifyId'] = request.target_certify_id
        if not DaraCore.is_null(request.target_face_contrast_picture):
            body['TargetFaceContrastPicture'] = request.target_face_contrast_picture
        if not DaraCore.is_null(request.target_face_contrast_picture_url):
            body['TargetFaceContrastPictureUrl'] = request.target_face_contrast_picture_url
        if not DaraCore.is_null(request.target_oss_bucket_name):
            body['TargetOssBucketName'] = request.target_oss_bucket_name
        if not DaraCore.is_null(request.target_oss_object_name):
            body['TargetOssObjectName'] = request.target_oss_object_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CompareFaceVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompareFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_face_verify_with_options_async(
        self,
        request: main_models.CompareFaceVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompareFaceVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.crop):
            body['Crop'] = request.crop
        if not DaraCore.is_null(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.source_certify_id):
            body['SourceCertifyId'] = request.source_certify_id
        if not DaraCore.is_null(request.source_face_contrast_picture):
            body['SourceFaceContrastPicture'] = request.source_face_contrast_picture
        if not DaraCore.is_null(request.source_face_contrast_picture_url):
            body['SourceFaceContrastPictureUrl'] = request.source_face_contrast_picture_url
        if not DaraCore.is_null(request.source_oss_bucket_name):
            body['SourceOssBucketName'] = request.source_oss_bucket_name
        if not DaraCore.is_null(request.source_oss_object_name):
            body['SourceOssObjectName'] = request.source_oss_object_name
        if not DaraCore.is_null(request.target_certify_id):
            body['TargetCertifyId'] = request.target_certify_id
        if not DaraCore.is_null(request.target_face_contrast_picture):
            body['TargetFaceContrastPicture'] = request.target_face_contrast_picture
        if not DaraCore.is_null(request.target_face_contrast_picture_url):
            body['TargetFaceContrastPictureUrl'] = request.target_face_contrast_picture_url
        if not DaraCore.is_null(request.target_oss_bucket_name):
            body['TargetOssBucketName'] = request.target_oss_bucket_name
        if not DaraCore.is_null(request.target_oss_object_name):
            body['TargetOssObjectName'] = request.target_oss_object_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CompareFaceVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompareFaceVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_face_verify(
        self,
        request: main_models.CompareFaceVerifyRequest,
    ) -> main_models.CompareFaceVerifyResponse:
        runtime = RuntimeOptions()
        return self.compare_face_verify_with_options(request, runtime)

    async def compare_face_verify_async(
        self,
        request: main_models.CompareFaceVerifyRequest,
    ) -> main_models.CompareFaceVerifyResponse:
        runtime = RuntimeOptions()
        return await self.compare_face_verify_with_options_async(request, runtime)

    def compare_faces_with_options(
        self,
        request: main_models.CompareFacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompareFacesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.source_image_type):
            body['SourceImageType'] = request.source_image_type
        if not DaraCore.is_null(request.source_image_value):
            body['SourceImageValue'] = request.source_image_value
        if not DaraCore.is_null(request.target_image_type):
            body['TargetImageType'] = request.target_image_type
        if not DaraCore.is_null(request.target_image_value):
            body['TargetImageValue'] = request.target_image_value
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CompareFaces',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompareFacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_faces_with_options_async(
        self,
        request: main_models.CompareFacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompareFacesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.source_image_type):
            body['SourceImageType'] = request.source_image_type
        if not DaraCore.is_null(request.source_image_value):
            body['SourceImageValue'] = request.source_image_value
        if not DaraCore.is_null(request.target_image_type):
            body['TargetImageType'] = request.target_image_type
        if not DaraCore.is_null(request.target_image_value):
            body['TargetImageValue'] = request.target_image_value
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CompareFaces',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompareFacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_faces(
        self,
        request: main_models.CompareFacesRequest,
    ) -> main_models.CompareFacesResponse:
        runtime = RuntimeOptions()
        return self.compare_faces_with_options(request, runtime)

    async def compare_faces_async(
        self,
        request: main_models.CompareFacesRequest,
    ) -> main_models.CompareFacesResponse:
        runtime = RuntimeOptions()
        return await self.compare_faces_with_options_async(request, runtime)

    def contrast_face_verify_with_options(
        self,
        request: main_models.ContrastFaceVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContrastFaceVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        body = {}
        if not DaraCore.is_null(request.cert_name):
            body['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_no):
            body['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.cert_type):
            body['CertType'] = request.cert_type
        if not DaraCore.is_null(request.certify_id):
            body['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.crop):
            body['Crop'] = request.crop
        if not DaraCore.is_null(request.device_token):
            body['DeviceToken'] = request.device_token
        if not DaraCore.is_null(request.encrypt_type):
            body['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.face_contrast_file):
            body['FaceContrastFile'] = request.face_contrast_file
        if not DaraCore.is_null(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        if not DaraCore.is_null(request.face_contrast_picture_url):
            body['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not DaraCore.is_null(request.ip):
            body['Ip'] = request.ip
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.oss_bucket_name):
            body['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_object_name):
            body['OssObjectName'] = request.oss_object_name
        if not DaraCore.is_null(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ContrastFaceVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContrastFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def contrast_face_verify_with_options_async(
        self,
        request: main_models.ContrastFaceVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContrastFaceVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        body = {}
        if not DaraCore.is_null(request.cert_name):
            body['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_no):
            body['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.cert_type):
            body['CertType'] = request.cert_type
        if not DaraCore.is_null(request.certify_id):
            body['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.crop):
            body['Crop'] = request.crop
        if not DaraCore.is_null(request.device_token):
            body['DeviceToken'] = request.device_token
        if not DaraCore.is_null(request.encrypt_type):
            body['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.face_contrast_file):
            body['FaceContrastFile'] = request.face_contrast_file
        if not DaraCore.is_null(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        if not DaraCore.is_null(request.face_contrast_picture_url):
            body['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not DaraCore.is_null(request.ip):
            body['Ip'] = request.ip
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.oss_bucket_name):
            body['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_object_name):
            body['OssObjectName'] = request.oss_object_name
        if not DaraCore.is_null(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ContrastFaceVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContrastFaceVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def contrast_face_verify(
        self,
        request: main_models.ContrastFaceVerifyRequest,
    ) -> main_models.ContrastFaceVerifyResponse:
        runtime = RuntimeOptions()
        return self.contrast_face_verify_with_options(request, runtime)

    async def contrast_face_verify_async(
        self,
        request: main_models.ContrastFaceVerifyRequest,
    ) -> main_models.ContrastFaceVerifyResponse:
        runtime = RuntimeOptions()
        return await self.contrast_face_verify_with_options_async(request, runtime)

    def contrast_face_verify_advance(
        self,
        request: main_models.ContrastFaceVerifyAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContrastFaceVerifyResponse:
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
            'Product': 'Cloudauth',
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
        contrast_face_verify_req = main_models.ContrastFaceVerifyRequest()
        Utils.convert(request, contrast_face_verify_req)
        if not DaraCore.is_null(request.face_contrast_file_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.face_contrast_file_object,
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
            contrast_face_verify_req.face_contrast_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        contrast_face_verify_resp = self.contrast_face_verify_with_options(contrast_face_verify_req, runtime)
        return contrast_face_verify_resp

    async def contrast_face_verify_advance_async(
        self,
        request: main_models.ContrastFaceVerifyAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContrastFaceVerifyResponse:
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
            'Product': 'Cloudauth',
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
        contrast_face_verify_req = main_models.ContrastFaceVerifyRequest()
        Utils.convert(request, contrast_face_verify_req)
        if not DaraCore.is_null(request.face_contrast_file_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.face_contrast_file_object,
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
            contrast_face_verify_req.face_contrast_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        contrast_face_verify_resp = await self.contrast_face_verify_with_options_async(contrast_face_verify_req, runtime)
        return contrast_face_verify_resp

    def create_ant_cloud_auth_scene_with_options(
        self,
        request: main_models.CreateAntCloudAuthSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAntCloudAuthSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_mini_program):
            query['BindMiniProgram'] = request.bind_mini_program
        if not DaraCore.is_null(request.check_file_body):
            query['CheckFileBody'] = request.check_file_body
        if not DaraCore.is_null(request.check_file_name):
            query['CheckFileName'] = request.check_file_name
        if not DaraCore.is_null(request.mini_program_name):
            query['MiniProgramName'] = request.mini_program_name
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.return_pic_count):
            query['ReturnPicCount'] = request.return_pic_count
        if not DaraCore.is_null(request.return_video_length):
            query['ReturnVideoLength'] = request.return_video_length
        if not DaraCore.is_null(request.scene_name):
            query['SceneName'] = request.scene_name
        if not DaraCore.is_null(request.store_image):
            query['StoreImage'] = request.store_image
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAntCloudAuthScene',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAntCloudAuthSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ant_cloud_auth_scene_with_options_async(
        self,
        request: main_models.CreateAntCloudAuthSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAntCloudAuthSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_mini_program):
            query['BindMiniProgram'] = request.bind_mini_program
        if not DaraCore.is_null(request.check_file_body):
            query['CheckFileBody'] = request.check_file_body
        if not DaraCore.is_null(request.check_file_name):
            query['CheckFileName'] = request.check_file_name
        if not DaraCore.is_null(request.mini_program_name):
            query['MiniProgramName'] = request.mini_program_name
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.return_pic_count):
            query['ReturnPicCount'] = request.return_pic_count
        if not DaraCore.is_null(request.return_video_length):
            query['ReturnVideoLength'] = request.return_video_length
        if not DaraCore.is_null(request.scene_name):
            query['SceneName'] = request.scene_name
        if not DaraCore.is_null(request.store_image):
            query['StoreImage'] = request.store_image
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAntCloudAuthScene',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAntCloudAuthSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ant_cloud_auth_scene(
        self,
        request: main_models.CreateAntCloudAuthSceneRequest,
    ) -> main_models.CreateAntCloudAuthSceneResponse:
        runtime = RuntimeOptions()
        return self.create_ant_cloud_auth_scene_with_options(request, runtime)

    async def create_ant_cloud_auth_scene_async(
        self,
        request: main_models.CreateAntCloudAuthSceneRequest,
    ) -> main_models.CreateAntCloudAuthSceneResponse:
        runtime = RuntimeOptions()
        return await self.create_ant_cloud_auth_scene_with_options_async(request, runtime)

    def create_auth_key_with_options(
        self,
        request: main_models.CreateAuthKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAuthKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_years):
            query['AuthYears'] = request.auth_years
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.test):
            query['Test'] = request.test
        if not DaraCore.is_null(request.user_device_id):
            query['UserDeviceId'] = request.user_device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAuthKey',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAuthKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_auth_key_with_options_async(
        self,
        request: main_models.CreateAuthKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAuthKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_years):
            query['AuthYears'] = request.auth_years
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.test):
            query['Test'] = request.test
        if not DaraCore.is_null(request.user_device_id):
            query['UserDeviceId'] = request.user_device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAuthKey',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAuthKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_auth_key(
        self,
        request: main_models.CreateAuthKeyRequest,
    ) -> main_models.CreateAuthKeyResponse:
        runtime = RuntimeOptions()
        return self.create_auth_key_with_options(request, runtime)

    async def create_auth_key_async(
        self,
        request: main_models.CreateAuthKeyRequest,
    ) -> main_models.CreateAuthKeyResponse:
        runtime = RuntimeOptions()
        return await self.create_auth_key_with_options_async(request, runtime)

    def create_cloudauthst_scene_with_options(
        self,
        request: main_models.CreateCloudauthstSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudauthstSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_name):
            query['SceneName'] = request.scene_name
        if not DaraCore.is_null(request.store_image):
            query['StoreImage'] = request.store_image
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudauthstScene',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudauthstSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloudauthst_scene_with_options_async(
        self,
        request: main_models.CreateCloudauthstSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudauthstSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_name):
            query['SceneName'] = request.scene_name
        if not DaraCore.is_null(request.store_image):
            query['StoreImage'] = request.store_image
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudauthstScene',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudauthstSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloudauthst_scene(
        self,
        request: main_models.CreateCloudauthstSceneRequest,
    ) -> main_models.CreateCloudauthstSceneResponse:
        runtime = RuntimeOptions()
        return self.create_cloudauthst_scene_with_options(request, runtime)

    async def create_cloudauthst_scene_async(
        self,
        request: main_models.CreateCloudauthstSceneRequest,
    ) -> main_models.CreateCloudauthstSceneResponse:
        runtime = RuntimeOptions()
        return await self.create_cloudauthst_scene_with_options_async(request, runtime)

    def create_scene_config_with_options(
        self,
        request: main_models.CreateSceneConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSceneConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.scene_id):
            body['sceneId'] = request.scene_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSceneConfig',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSceneConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scene_config_with_options_async(
        self,
        request: main_models.CreateSceneConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSceneConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.scene_id):
            body['sceneId'] = request.scene_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSceneConfig',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSceneConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scene_config(
        self,
        request: main_models.CreateSceneConfigRequest,
    ) -> main_models.CreateSceneConfigResponse:
        runtime = RuntimeOptions()
        return self.create_scene_config_with_options(request, runtime)

    async def create_scene_config_async(
        self,
        request: main_models.CreateSceneConfigRequest,
    ) -> main_models.CreateSceneConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_scene_config_with_options_async(request, runtime)

    def create_verify_setting_with_options(
        self,
        request: main_models.CreateVerifySettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVerifySettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_name):
            query['BizName'] = request.biz_name
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.guide_step):
            query['GuideStep'] = request.guide_step
        if not DaraCore.is_null(request.privacy_step):
            query['PrivacyStep'] = request.privacy_step
        if not DaraCore.is_null(request.result_step):
            query['ResultStep'] = request.result_step
        if not DaraCore.is_null(request.solution):
            query['Solution'] = request.solution
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVerifySetting',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVerifySettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_verify_setting_with_options_async(
        self,
        request: main_models.CreateVerifySettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVerifySettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_name):
            query['BizName'] = request.biz_name
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.guide_step):
            query['GuideStep'] = request.guide_step
        if not DaraCore.is_null(request.privacy_step):
            query['PrivacyStep'] = request.privacy_step
        if not DaraCore.is_null(request.result_step):
            query['ResultStep'] = request.result_step
        if not DaraCore.is_null(request.solution):
            query['Solution'] = request.solution
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVerifySetting',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVerifySettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_verify_setting(
        self,
        request: main_models.CreateVerifySettingRequest,
    ) -> main_models.CreateVerifySettingResponse:
        runtime = RuntimeOptions()
        return self.create_verify_setting_with_options(request, runtime)

    async def create_verify_setting_async(
        self,
        request: main_models.CreateVerifySettingRequest,
    ) -> main_models.CreateVerifySettingResponse:
        runtime = RuntimeOptions()
        return await self.create_verify_setting_with_options_async(request, runtime)

    def create_whitelist_setting_with_options(
        self,
        request: main_models.CreateWhitelistSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWhitelistSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_no):
            query['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.valid_day):
            query['ValidDay'] = request.valid_day
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWhitelistSetting',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWhitelistSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_whitelist_setting_with_options_async(
        self,
        request: main_models.CreateWhitelistSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWhitelistSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_no):
            query['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.valid_day):
            query['ValidDay'] = request.valid_day
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWhitelistSetting',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWhitelistSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_whitelist_setting(
        self,
        request: main_models.CreateWhitelistSettingRequest,
    ) -> main_models.CreateWhitelistSettingResponse:
        runtime = RuntimeOptions()
        return self.create_whitelist_setting_with_options(request, runtime)

    async def create_whitelist_setting_async(
        self,
        request: main_models.CreateWhitelistSettingRequest,
    ) -> main_models.CreateWhitelistSettingResponse:
        runtime = RuntimeOptions()
        return await self.create_whitelist_setting_with_options_async(request, runtime)

    def credential_product_verify_v2with_options(
        self,
        request: main_models.CredentialProductVerifyV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialProductVerifyV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cred_name):
            query['CredName'] = request.cred_name
        if not DaraCore.is_null(request.cred_type):
            query['CredType'] = request.cred_type
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.merchant_id):
            query['MerchantId'] = request.merchant_id
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
            action = 'CredentialProductVerifyV2',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CredentialProductVerifyV2Response(),
            self.call_api(params, req, runtime)
        )

    async def credential_product_verify_v2with_options_async(
        self,
        request: main_models.CredentialProductVerifyV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialProductVerifyV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cred_name):
            query['CredName'] = request.cred_name
        if not DaraCore.is_null(request.cred_type):
            query['CredType'] = request.cred_type
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.merchant_id):
            query['MerchantId'] = request.merchant_id
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
            action = 'CredentialProductVerifyV2',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CredentialProductVerifyV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def credential_product_verify_v2(
        self,
        request: main_models.CredentialProductVerifyV2Request,
    ) -> main_models.CredentialProductVerifyV2Response:
        runtime = RuntimeOptions()
        return self.credential_product_verify_v2with_options(request, runtime)

    async def credential_product_verify_v2_async(
        self,
        request: main_models.CredentialProductVerifyV2Request,
    ) -> main_models.CredentialProductVerifyV2Response:
        runtime = RuntimeOptions()
        return await self.credential_product_verify_v2with_options_async(request, runtime)

    def credential_product_verify_v2advance(
        self,
        request: main_models.CredentialProductVerifyV2AdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialProductVerifyV2Response:
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
            'Product': 'Cloudauth',
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
        credential_product_verify_v2req = main_models.CredentialProductVerifyV2Request()
        Utils.convert(request, credential_product_verify_v2req)
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
            credential_product_verify_v2req.image_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        credential_product_verify_v2resp = self.credential_product_verify_v2with_options(credential_product_verify_v2req, runtime)
        return credential_product_verify_v2resp

    async def credential_product_verify_v2advance_async(
        self,
        request: main_models.CredentialProductVerifyV2AdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialProductVerifyV2Response:
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
            'Product': 'Cloudauth',
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
        credential_product_verify_v2req = main_models.CredentialProductVerifyV2Request()
        Utils.convert(request, credential_product_verify_v2req)
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
            credential_product_verify_v2req.image_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        credential_product_verify_v2resp = await self.credential_product_verify_v2with_options_async(credential_product_verify_v2req, runtime)
        return credential_product_verify_v2resp

    def credential_verify_with_options(
        self,
        tmp_req: main_models.CredentialVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialVerifyResponse:
        tmp_req.validate()
        request = main_models.CredentialVerifyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.merchant_detail):
            request.merchant_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.merchant_detail, 'MerchantDetail', 'json')
        query = {}
        if not DaraCore.is_null(request.cert_num):
            query['CertNum'] = request.cert_num
        if not DaraCore.is_null(request.cred_name):
            query['CredName'] = request.cred_name
        if not DaraCore.is_null(request.cred_type):
            query['CredType'] = request.cred_type
        if not DaraCore.is_null(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.is_check):
            query['IsCheck'] = request.is_check
        if not DaraCore.is_null(request.is_ocr):
            query['IsOCR'] = request.is_ocr
        if not DaraCore.is_null(request.merchant_detail_shrink):
            query['MerchantDetail'] = request.merchant_detail_shrink
        if not DaraCore.is_null(request.merchant_id):
            query['MerchantId'] = request.merchant_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_model):
            query['PromptModel'] = request.prompt_model
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        body = {}
        if not DaraCore.is_null(request.image_context):
            body['ImageContext'] = request.image_context
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CredentialVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CredentialVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def credential_verify_with_options_async(
        self,
        tmp_req: main_models.CredentialVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialVerifyResponse:
        tmp_req.validate()
        request = main_models.CredentialVerifyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.merchant_detail):
            request.merchant_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.merchant_detail, 'MerchantDetail', 'json')
        query = {}
        if not DaraCore.is_null(request.cert_num):
            query['CertNum'] = request.cert_num
        if not DaraCore.is_null(request.cred_name):
            query['CredName'] = request.cred_name
        if not DaraCore.is_null(request.cred_type):
            query['CredType'] = request.cred_type
        if not DaraCore.is_null(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.is_check):
            query['IsCheck'] = request.is_check
        if not DaraCore.is_null(request.is_ocr):
            query['IsOCR'] = request.is_ocr
        if not DaraCore.is_null(request.merchant_detail_shrink):
            query['MerchantDetail'] = request.merchant_detail_shrink
        if not DaraCore.is_null(request.merchant_id):
            query['MerchantId'] = request.merchant_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_model):
            query['PromptModel'] = request.prompt_model
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        body = {}
        if not DaraCore.is_null(request.image_context):
            body['ImageContext'] = request.image_context
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CredentialVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CredentialVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def credential_verify(
        self,
        request: main_models.CredentialVerifyRequest,
    ) -> main_models.CredentialVerifyResponse:
        runtime = RuntimeOptions()
        return self.credential_verify_with_options(request, runtime)

    async def credential_verify_async(
        self,
        request: main_models.CredentialVerifyRequest,
    ) -> main_models.CredentialVerifyResponse:
        runtime = RuntimeOptions()
        return await self.credential_verify_with_options_async(request, runtime)

    def credential_verify_v2with_options(
        self,
        tmp_req: main_models.CredentialVerifyV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialVerifyV2Response:
        tmp_req.validate()
        request = main_models.CredentialVerifyV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.merchant_detail):
            request.merchant_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.merchant_detail, 'MerchantDetail', 'json')
        query = {}
        if not DaraCore.is_null(request.cert_num):
            query['CertNum'] = request.cert_num
        if not DaraCore.is_null(request.cred_name):
            query['CredName'] = request.cred_name
        if not DaraCore.is_null(request.cred_type):
            query['CredType'] = request.cred_type
        if not DaraCore.is_null(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.is_check):
            query['IsCheck'] = request.is_check
        if not DaraCore.is_null(request.is_ocr):
            query['IsOcr'] = request.is_ocr
        if not DaraCore.is_null(request.merchant_detail_shrink):
            query['MerchantDetail'] = request.merchant_detail_shrink
        if not DaraCore.is_null(request.merchant_id):
            query['MerchantId'] = request.merchant_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_model):
            query['PromptModel'] = request.prompt_model
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        body = {}
        if not DaraCore.is_null(request.image_context):
            body['ImageContext'] = request.image_context
        if not DaraCore.is_null(request.image_file):
            body['ImageFile'] = request.image_file
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CredentialVerifyV2',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CredentialVerifyV2Response(),
            self.call_api(params, req, runtime)
        )

    async def credential_verify_v2with_options_async(
        self,
        tmp_req: main_models.CredentialVerifyV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialVerifyV2Response:
        tmp_req.validate()
        request = main_models.CredentialVerifyV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.merchant_detail):
            request.merchant_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.merchant_detail, 'MerchantDetail', 'json')
        query = {}
        if not DaraCore.is_null(request.cert_num):
            query['CertNum'] = request.cert_num
        if not DaraCore.is_null(request.cred_name):
            query['CredName'] = request.cred_name
        if not DaraCore.is_null(request.cred_type):
            query['CredType'] = request.cred_type
        if not DaraCore.is_null(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.is_check):
            query['IsCheck'] = request.is_check
        if not DaraCore.is_null(request.is_ocr):
            query['IsOcr'] = request.is_ocr
        if not DaraCore.is_null(request.merchant_detail_shrink):
            query['MerchantDetail'] = request.merchant_detail_shrink
        if not DaraCore.is_null(request.merchant_id):
            query['MerchantId'] = request.merchant_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_model):
            query['PromptModel'] = request.prompt_model
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        body = {}
        if not DaraCore.is_null(request.image_context):
            body['ImageContext'] = request.image_context
        if not DaraCore.is_null(request.image_file):
            body['ImageFile'] = request.image_file
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CredentialVerifyV2',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CredentialVerifyV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def credential_verify_v2(
        self,
        request: main_models.CredentialVerifyV2Request,
    ) -> main_models.CredentialVerifyV2Response:
        runtime = RuntimeOptions()
        return self.credential_verify_v2with_options(request, runtime)

    async def credential_verify_v2_async(
        self,
        request: main_models.CredentialVerifyV2Request,
    ) -> main_models.CredentialVerifyV2Response:
        runtime = RuntimeOptions()
        return await self.credential_verify_v2with_options_async(request, runtime)

    def credential_verify_v2advance(
        self,
        request: main_models.CredentialVerifyV2AdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialVerifyV2Response:
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
            'Product': 'Cloudauth',
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
        credential_verify_v2req = main_models.CredentialVerifyV2Request()
        Utils.convert(request, credential_verify_v2req)
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
            credential_verify_v2req.image_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        credential_verify_v2resp = self.credential_verify_v2with_options(credential_verify_v2req, runtime)
        return credential_verify_v2resp

    async def credential_verify_v2advance_async(
        self,
        request: main_models.CredentialVerifyV2AdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CredentialVerifyV2Response:
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
            'Product': 'Cloudauth',
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
        credential_verify_v2req = main_models.CredentialVerifyV2Request()
        Utils.convert(request, credential_verify_v2req)
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
            credential_verify_v2req.image_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        credential_verify_v2resp = await self.credential_verify_v2with_options_async(credential_verify_v2req, runtime)
        return credential_verify_v2resp

    def deepfake_detect_with_options(
        self,
        request: main_models.DeepfakeDetectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeepfakeDetectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.face_input_type):
            query['FaceInputType'] = request.face_input_type
        if not DaraCore.is_null(request.face_url):
            query['FaceUrl'] = request.face_url
        if not DaraCore.is_null(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        body = {}
        if not DaraCore.is_null(request.face_base_64):
            body['FaceBase64'] = request.face_base_64
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeepfakeDetect',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeepfakeDetectResponse(),
            self.call_api(params, req, runtime)
        )

    async def deepfake_detect_with_options_async(
        self,
        request: main_models.DeepfakeDetectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeepfakeDetectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.face_input_type):
            query['FaceInputType'] = request.face_input_type
        if not DaraCore.is_null(request.face_url):
            query['FaceUrl'] = request.face_url
        if not DaraCore.is_null(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        body = {}
        if not DaraCore.is_null(request.face_base_64):
            body['FaceBase64'] = request.face_base_64
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeepfakeDetect',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeepfakeDetectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deepfake_detect(
        self,
        request: main_models.DeepfakeDetectRequest,
    ) -> main_models.DeepfakeDetectResponse:
        runtime = RuntimeOptions()
        return self.deepfake_detect_with_options(request, runtime)

    async def deepfake_detect_async(
        self,
        request: main_models.DeepfakeDetectRequest,
    ) -> main_models.DeepfakeDetectResponse:
        runtime = RuntimeOptions()
        return await self.deepfake_detect_with_options_async(request, runtime)

    def delete_all_customize_flow_strategy_with_options(
        self,
        request: main_models.DeleteAllCustomizeFlowStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAllCustomizeFlowStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAllCustomizeFlowStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAllCustomizeFlowStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_all_customize_flow_strategy_with_options_async(
        self,
        request: main_models.DeleteAllCustomizeFlowStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAllCustomizeFlowStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAllCustomizeFlowStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAllCustomizeFlowStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_all_customize_flow_strategy(
        self,
        request: main_models.DeleteAllCustomizeFlowStrategyRequest,
    ) -> main_models.DeleteAllCustomizeFlowStrategyResponse:
        runtime = RuntimeOptions()
        return self.delete_all_customize_flow_strategy_with_options(request, runtime)

    async def delete_all_customize_flow_strategy_async(
        self,
        request: main_models.DeleteAllCustomizeFlowStrategyRequest,
    ) -> main_models.DeleteAllCustomizeFlowStrategyResponse:
        runtime = RuntimeOptions()
        return await self.delete_all_customize_flow_strategy_with_options_async(request, runtime)

    def delete_ant_cloud_auth_scene_with_options(
        self,
        request: main_models.DeleteAntCloudAuthSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAntCloudAuthSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAntCloudAuthScene',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAntCloudAuthSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ant_cloud_auth_scene_with_options_async(
        self,
        request: main_models.DeleteAntCloudAuthSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAntCloudAuthSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAntCloudAuthScene',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAntCloudAuthSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ant_cloud_auth_scene(
        self,
        request: main_models.DeleteAntCloudAuthSceneRequest,
    ) -> main_models.DeleteAntCloudAuthSceneResponse:
        runtime = RuntimeOptions()
        return self.delete_ant_cloud_auth_scene_with_options(request, runtime)

    async def delete_ant_cloud_auth_scene_async(
        self,
        request: main_models.DeleteAntCloudAuthSceneRequest,
    ) -> main_models.DeleteAntCloudAuthSceneResponse:
        runtime = RuntimeOptions()
        return await self.delete_ant_cloud_auth_scene_with_options_async(request, runtime)

    def delete_black_list_strategy_with_options(
        self,
        request: main_models.DeleteBlackListStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBlackListStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBlackListStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBlackListStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_black_list_strategy_with_options_async(
        self,
        request: main_models.DeleteBlackListStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBlackListStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBlackListStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBlackListStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_black_list_strategy(
        self,
        request: main_models.DeleteBlackListStrategyRequest,
    ) -> main_models.DeleteBlackListStrategyResponse:
        runtime = RuntimeOptions()
        return self.delete_black_list_strategy_with_options(request, runtime)

    async def delete_black_list_strategy_async(
        self,
        request: main_models.DeleteBlackListStrategyRequest,
    ) -> main_models.DeleteBlackListStrategyResponse:
        runtime = RuntimeOptions()
        return await self.delete_black_list_strategy_with_options_async(request, runtime)

    def delete_cloudauthst_scene_with_options(
        self,
        request: main_models.DeleteCloudauthstSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudauthstSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudauthstScene',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudauthstSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloudauthst_scene_with_options_async(
        self,
        request: main_models.DeleteCloudauthstSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudauthstSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudauthstScene',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudauthstSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloudauthst_scene(
        self,
        request: main_models.DeleteCloudauthstSceneRequest,
    ) -> main_models.DeleteCloudauthstSceneResponse:
        runtime = RuntimeOptions()
        return self.delete_cloudauthst_scene_with_options(request, runtime)

    async def delete_cloudauthst_scene_async(
        self,
        request: main_models.DeleteCloudauthstSceneRequest,
    ) -> main_models.DeleteCloudauthstSceneResponse:
        runtime = RuntimeOptions()
        return await self.delete_cloudauthst_scene_with_options_async(request, runtime)

    def delete_control_strategy_with_options(
        self,
        request: main_models.DeleteControlStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteControlStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteControlStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteControlStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_control_strategy_with_options_async(
        self,
        request: main_models.DeleteControlStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteControlStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteControlStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteControlStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_control_strategy(
        self,
        request: main_models.DeleteControlStrategyRequest,
    ) -> main_models.DeleteControlStrategyResponse:
        runtime = RuntimeOptions()
        return self.delete_control_strategy_with_options(request, runtime)

    async def delete_control_strategy_async(
        self,
        request: main_models.DeleteControlStrategyRequest,
    ) -> main_models.DeleteControlStrategyResponse:
        runtime = RuntimeOptions()
        return await self.delete_control_strategy_with_options_async(request, runtime)

    def delete_customize_flow_strategy_with_options(
        self,
        request: main_models.DeleteCustomizeFlowStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomizeFlowStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomizeFlowStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomizeFlowStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_customize_flow_strategy_with_options_async(
        self,
        request: main_models.DeleteCustomizeFlowStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomizeFlowStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomizeFlowStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomizeFlowStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_customize_flow_strategy(
        self,
        request: main_models.DeleteCustomizeFlowStrategyRequest,
    ) -> main_models.DeleteCustomizeFlowStrategyResponse:
        runtime = RuntimeOptions()
        return self.delete_customize_flow_strategy_with_options(request, runtime)

    async def delete_customize_flow_strategy_async(
        self,
        request: main_models.DeleteCustomizeFlowStrategyRequest,
    ) -> main_models.DeleteCustomizeFlowStrategyResponse:
        runtime = RuntimeOptions()
        return await self.delete_customize_flow_strategy_with_options_async(request, runtime)

    def delete_face_verify_result_with_options(
        self,
        request: main_models.DeleteFaceVerifyResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaceVerifyResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.delete_after_query):
            query['DeleteAfterQuery'] = request.delete_after_query
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaceVerifyResult',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaceVerifyResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_verify_result_with_options_async(
        self,
        request: main_models.DeleteFaceVerifyResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaceVerifyResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.delete_after_query):
            query['DeleteAfterQuery'] = request.delete_after_query
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaceVerifyResult',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaceVerifyResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face_verify_result(
        self,
        request: main_models.DeleteFaceVerifyResultRequest,
    ) -> main_models.DeleteFaceVerifyResultResponse:
        runtime = RuntimeOptions()
        return self.delete_face_verify_result_with_options(request, runtime)

    async def delete_face_verify_result_async(
        self,
        request: main_models.DeleteFaceVerifyResultRequest,
    ) -> main_models.DeleteFaceVerifyResultResponse:
        runtime = RuntimeOptions()
        return await self.delete_face_verify_result_with_options_async(request, runtime)

    def delete_scene_config_with_options(
        self,
        request: main_models.DeleteSceneConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSceneConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.scene_config_id):
            body['sceneConfigId'] = request.scene_config_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSceneConfig',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSceneConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scene_config_with_options_async(
        self,
        request: main_models.DeleteSceneConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSceneConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.scene_config_id):
            body['sceneConfigId'] = request.scene_config_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSceneConfig',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSceneConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scene_config(
        self,
        request: main_models.DeleteSceneConfigRequest,
    ) -> main_models.DeleteSceneConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_scene_config_with_options(request, runtime)

    async def delete_scene_config_async(
        self,
        request: main_models.DeleteSceneConfigRequest,
    ) -> main_models.DeleteSceneConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_scene_config_with_options_async(request, runtime)

    def delete_whitelist_setting_with_options(
        self,
        request: main_models.DeleteWhitelistSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWhitelistSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWhitelistSetting',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWhitelistSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_whitelist_setting_with_options_async(
        self,
        request: main_models.DeleteWhitelistSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWhitelistSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWhitelistSetting',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWhitelistSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_whitelist_setting(
        self,
        request: main_models.DeleteWhitelistSettingRequest,
    ) -> main_models.DeleteWhitelistSettingResponse:
        runtime = RuntimeOptions()
        return self.delete_whitelist_setting_with_options(request, runtime)

    async def delete_whitelist_setting_async(
        self,
        request: main_models.DeleteWhitelistSettingRequest,
    ) -> main_models.DeleteWhitelistSettingResponse:
        runtime = RuntimeOptions()
        return await self.delete_whitelist_setting_with_options_async(request, runtime)

    def describe_ant_and_cloud_auth_user_status_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAntAndCloudAuthUserStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeAntAndCloudAuthUserStatus',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAntAndCloudAuthUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_and_cloud_auth_user_status_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAntAndCloudAuthUserStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeAntAndCloudAuthUserStatus',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAntAndCloudAuthUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_and_cloud_auth_user_status(self) -> main_models.DescribeAntAndCloudAuthUserStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_ant_and_cloud_auth_user_status_with_options(runtime)

    async def describe_ant_and_cloud_auth_user_status_async(self) -> main_models.DescribeAntAndCloudAuthUserStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_ant_and_cloud_auth_user_status_with_options_async(runtime)

    def describe_auth_verify_with_options(
        self,
        request: main_models.DescribeAuthVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.certify_id):
            body['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuthVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auth_verify_with_options_async(
        self,
        request: main_models.DescribeAuthVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.certify_id):
            body['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuthVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auth_verify(
        self,
        request: main_models.DescribeAuthVerifyRequest,
    ) -> main_models.DescribeAuthVerifyResponse:
        runtime = RuntimeOptions()
        return self.describe_auth_verify_with_options(request, runtime)

    async def describe_auth_verify_async(
        self,
        request: main_models.DescribeAuthVerifyRequest,
    ) -> main_models.DescribeAuthVerifyResponse:
        runtime = RuntimeOptions()
        return await self.describe_auth_verify_with_options_async(request, runtime)

    def describe_card_verify_with_options(
        self,
        request: main_models.DescribeCardVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCardVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCardVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCardVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_card_verify_with_options_async(
        self,
        request: main_models.DescribeCardVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCardVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCardVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCardVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_card_verify(
        self,
        request: main_models.DescribeCardVerifyRequest,
    ) -> main_models.DescribeCardVerifyResponse:
        runtime = RuntimeOptions()
        return self.describe_card_verify_with_options(request, runtime)

    async def describe_card_verify_async(
        self,
        request: main_models.DescribeCardVerifyRequest,
    ) -> main_models.DescribeCardVerifyResponse:
        runtime = RuntimeOptions()
        return await self.describe_card_verify_with_options_async(request, runtime)

    def describe_cloudauthst_scene_list_with_options(
        self,
        request: main_models.DescribeCloudauthstSceneListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudauthstSceneListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudauthstSceneList',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudauthstSceneListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloudauthst_scene_list_with_options_async(
        self,
        request: main_models.DescribeCloudauthstSceneListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudauthstSceneListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudauthstSceneList',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudauthstSceneListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloudauthst_scene_list(
        self,
        request: main_models.DescribeCloudauthstSceneListRequest,
    ) -> main_models.DescribeCloudauthstSceneListResponse:
        runtime = RuntimeOptions()
        return self.describe_cloudauthst_scene_list_with_options(request, runtime)

    async def describe_cloudauthst_scene_list_async(
        self,
        request: main_models.DescribeCloudauthstSceneListRequest,
    ) -> main_models.DescribeCloudauthstSceneListResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloudauthst_scene_list_with_options_async(request, runtime)

    def describe_device_info_with_options(
        self,
        request: main_models.DescribeDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.expired_end_day):
            query['ExpiredEndDay'] = request.expired_end_day
        if not DaraCore.is_null(request.expired_start_day):
            query['ExpiredStartDay'] = request.expired_start_day
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_device_id):
            query['UserDeviceId'] = request.user_device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeviceInfo',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_device_info_with_options_async(
        self,
        request: main_models.DescribeDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.expired_end_day):
            query['ExpiredEndDay'] = request.expired_end_day
        if not DaraCore.is_null(request.expired_start_day):
            query['ExpiredStartDay'] = request.expired_start_day
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_device_id):
            query['UserDeviceId'] = request.user_device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeviceInfo',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_device_info(
        self,
        request: main_models.DescribeDeviceInfoRequest,
    ) -> main_models.DescribeDeviceInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_device_info_with_options(request, runtime)

    async def describe_device_info_async(
        self,
        request: main_models.DescribeDeviceInfoRequest,
    ) -> main_models.DescribeDeviceInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_device_info_with_options_async(request, runtime)

    def describe_face_guard_risk_with_options(
        self,
        request: main_models.DescribeFaceGuardRiskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFaceGuardRiskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.device_token):
            query['DeviceToken'] = request.device_token
        if not DaraCore.is_null(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFaceGuardRisk',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFaceGuardRiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_face_guard_risk_with_options_async(
        self,
        request: main_models.DescribeFaceGuardRiskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFaceGuardRiskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.device_token):
            query['DeviceToken'] = request.device_token
        if not DaraCore.is_null(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFaceGuardRisk',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFaceGuardRiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_face_guard_risk(
        self,
        request: main_models.DescribeFaceGuardRiskRequest,
    ) -> main_models.DescribeFaceGuardRiskResponse:
        runtime = RuntimeOptions()
        return self.describe_face_guard_risk_with_options(request, runtime)

    async def describe_face_guard_risk_async(
        self,
        request: main_models.DescribeFaceGuardRiskRequest,
    ) -> main_models.DescribeFaceGuardRiskResponse:
        runtime = RuntimeOptions()
        return await self.describe_face_guard_risk_with_options_async(request, runtime)

    def describe_face_verify_with_options(
        self,
        request: main_models.DescribeFaceVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFaceVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.picture_return_type):
            query['PictureReturnType'] = request.picture_return_type
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFaceVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_face_verify_with_options_async(
        self,
        request: main_models.DescribeFaceVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFaceVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.picture_return_type):
            query['PictureReturnType'] = request.picture_return_type
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFaceVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFaceVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_face_verify(
        self,
        request: main_models.DescribeFaceVerifyRequest,
    ) -> main_models.DescribeFaceVerifyResponse:
        runtime = RuntimeOptions()
        return self.describe_face_verify_with_options(request, runtime)

    async def describe_face_verify_async(
        self,
        request: main_models.DescribeFaceVerifyRequest,
    ) -> main_models.DescribeFaceVerifyResponse:
        runtime = RuntimeOptions()
        return await self.describe_face_verify_with_options_async(request, runtime)

    def describe_info_check_export_record_with_options(
        self,
        request: main_models.DescribeInfoCheckExportRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInfoCheckExportRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInfoCheckExportRecord',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInfoCheckExportRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_info_check_export_record_with_options_async(
        self,
        request: main_models.DescribeInfoCheckExportRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInfoCheckExportRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInfoCheckExportRecord',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInfoCheckExportRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_info_check_export_record(
        self,
        request: main_models.DescribeInfoCheckExportRecordRequest,
    ) -> main_models.DescribeInfoCheckExportRecordResponse:
        runtime = RuntimeOptions()
        return self.describe_info_check_export_record_with_options(request, runtime)

    async def describe_info_check_export_record_async(
        self,
        request: main_models.DescribeInfoCheckExportRecordRequest,
    ) -> main_models.DescribeInfoCheckExportRecordResponse:
        runtime = RuntimeOptions()
        return await self.describe_info_check_export_record_with_options_async(request, runtime)

    def describe_list_ant_cloud_auth_scenes_with_options(
        self,
        request: main_models.DescribeListAntCloudAuthScenesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeListAntCloudAuthScenesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeListAntCloudAuthScenes',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeListAntCloudAuthScenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_list_ant_cloud_auth_scenes_with_options_async(
        self,
        request: main_models.DescribeListAntCloudAuthScenesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeListAntCloudAuthScenesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeListAntCloudAuthScenes',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeListAntCloudAuthScenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_list_ant_cloud_auth_scenes(
        self,
        request: main_models.DescribeListAntCloudAuthScenesRequest,
    ) -> main_models.DescribeListAntCloudAuthScenesResponse:
        runtime = RuntimeOptions()
        return self.describe_list_ant_cloud_auth_scenes_with_options(request, runtime)

    async def describe_list_ant_cloud_auth_scenes_async(
        self,
        request: main_models.DescribeListAntCloudAuthScenesRequest,
    ) -> main_models.DescribeListAntCloudAuthScenesResponse:
        runtime = RuntimeOptions()
        return await self.describe_list_ant_cloud_auth_scenes_with_options_async(request, runtime)

    def describe_list_face_verify_data_with_options(
        self,
        request: main_models.DescribeListFaceVerifyDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeListFaceVerifyDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gmt_end):
            query['GmtEnd'] = request.gmt_end
        if not DaraCore.is_null(request.gmt_start):
            query['GmtStart'] = request.gmt_start
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeListFaceVerifyData',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeListFaceVerifyDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_list_face_verify_data_with_options_async(
        self,
        request: main_models.DescribeListFaceVerifyDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeListFaceVerifyDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gmt_end):
            query['GmtEnd'] = request.gmt_end
        if not DaraCore.is_null(request.gmt_start):
            query['GmtStart'] = request.gmt_start
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeListFaceVerifyData',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeListFaceVerifyDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_list_face_verify_data(
        self,
        request: main_models.DescribeListFaceVerifyDataRequest,
    ) -> main_models.DescribeListFaceVerifyDataResponse:
        runtime = RuntimeOptions()
        return self.describe_list_face_verify_data_with_options(request, runtime)

    async def describe_list_face_verify_data_async(
        self,
        request: main_models.DescribeListFaceVerifyDataRequest,
    ) -> main_models.DescribeListFaceVerifyDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_list_face_verify_data_with_options_async(request, runtime)

    def describe_list_face_verify_infos_with_options(
        self,
        request: main_models.DescribeListFaceVerifyInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeListFaceVerifyInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.gmt_end):
            query['GmtEnd'] = request.gmt_end
        if not DaraCore.is_null(request.gmt_start):
            query['GmtStart'] = request.gmt_start
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeListFaceVerifyInfos',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeListFaceVerifyInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_list_face_verify_infos_with_options_async(
        self,
        request: main_models.DescribeListFaceVerifyInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeListFaceVerifyInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.gmt_end):
            query['GmtEnd'] = request.gmt_end
        if not DaraCore.is_null(request.gmt_start):
            query['GmtStart'] = request.gmt_start
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeListFaceVerifyInfos',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeListFaceVerifyInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_list_face_verify_infos(
        self,
        request: main_models.DescribeListFaceVerifyInfosRequest,
    ) -> main_models.DescribeListFaceVerifyInfosResponse:
        runtime = RuntimeOptions()
        return self.describe_list_face_verify_infos_with_options(request, runtime)

    async def describe_list_face_verify_infos_async(
        self,
        request: main_models.DescribeListFaceVerifyInfosRequest,
    ) -> main_models.DescribeListFaceVerifyInfosResponse:
        runtime = RuntimeOptions()
        return await self.describe_list_face_verify_infos_with_options_async(request, runtime)

    def describe_meta_search_page_list_with_options(
        self,
        request: main_models.DescribeMetaSearchPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetaSearchPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api):
            query['Api'] = request.api
        if not DaraCore.is_null(request.bank_card):
            query['BankCard'] = request.bank_card
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.isp_name):
            query['IspName'] = request.isp_name
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_code):
            query['SubCode'] = request.sub_code
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetaSearchPageList',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetaSearchPageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meta_search_page_list_with_options_async(
        self,
        request: main_models.DescribeMetaSearchPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetaSearchPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api):
            query['Api'] = request.api
        if not DaraCore.is_null(request.bank_card):
            query['BankCard'] = request.bank_card
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.isp_name):
            query['IspName'] = request.isp_name
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_code):
            query['SubCode'] = request.sub_code
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetaSearchPageList',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetaSearchPageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meta_search_page_list(
        self,
        request: main_models.DescribeMetaSearchPageListRequest,
    ) -> main_models.DescribeMetaSearchPageListResponse:
        runtime = RuntimeOptions()
        return self.describe_meta_search_page_list_with_options(request, runtime)

    async def describe_meta_search_page_list_async(
        self,
        request: main_models.DescribeMetaSearchPageListRequest,
    ) -> main_models.DescribeMetaSearchPageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_meta_search_page_list_with_options_async(request, runtime)

    def describe_meta_statistics_list_with_options(
        self,
        request: main_models.DescribeMetaStatisticsListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetaStatisticsListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api):
            query['Api'] = request.api
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetaStatisticsList',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetaStatisticsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meta_statistics_list_with_options_async(
        self,
        request: main_models.DescribeMetaStatisticsListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetaStatisticsListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api):
            query['Api'] = request.api
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetaStatisticsList',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetaStatisticsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meta_statistics_list(
        self,
        request: main_models.DescribeMetaStatisticsListRequest,
    ) -> main_models.DescribeMetaStatisticsListResponse:
        runtime = RuntimeOptions()
        return self.describe_meta_statistics_list_with_options(request, runtime)

    async def describe_meta_statistics_list_async(
        self,
        request: main_models.DescribeMetaStatisticsListRequest,
    ) -> main_models.DescribeMetaStatisticsListResponse:
        runtime = RuntimeOptions()
        return await self.describe_meta_statistics_list_with_options_async(request, runtime)

    def describe_meta_statistics_page_list_with_options(
        self,
        request: main_models.DescribeMetaStatisticsPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetaStatisticsPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api):
            query['Api'] = request.api
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetaStatisticsPageList',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetaStatisticsPageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meta_statistics_page_list_with_options_async(
        self,
        request: main_models.DescribeMetaStatisticsPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetaStatisticsPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api):
            query['Api'] = request.api
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetaStatisticsPageList',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetaStatisticsPageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meta_statistics_page_list(
        self,
        request: main_models.DescribeMetaStatisticsPageListRequest,
    ) -> main_models.DescribeMetaStatisticsPageListResponse:
        runtime = RuntimeOptions()
        return self.describe_meta_statistics_page_list_with_options(request, runtime)

    async def describe_meta_statistics_page_list_async(
        self,
        request: main_models.DescribeMetaStatisticsPageListRequest,
    ) -> main_models.DescribeMetaStatisticsPageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_meta_statistics_page_list_with_options_async(request, runtime)

    def describe_oss_status_with_options(
        self,
        request: main_models.DescribeOssStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOssStatus',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_status_with_options_async(
        self,
        request: main_models.DescribeOssStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOssStatus',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_status(
        self,
        request: main_models.DescribeOssStatusRequest,
    ) -> main_models.DescribeOssStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_oss_status_with_options(request, runtime)

    async def describe_oss_status_async(
        self,
        request: main_models.DescribeOssStatusRequest,
    ) -> main_models.DescribeOssStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_oss_status_with_options_async(request, runtime)

    def describe_oss_status_v2with_options(
        self,
        request: main_models.DescribeOssStatusV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssStatusV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOssStatusV2',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssStatusV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_status_v2with_options_async(
        self,
        request: main_models.DescribeOssStatusV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssStatusV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOssStatusV2',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssStatusV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_status_v2(
        self,
        request: main_models.DescribeOssStatusV2Request,
    ) -> main_models.DescribeOssStatusV2Response:
        runtime = RuntimeOptions()
        return self.describe_oss_status_v2with_options(request, runtime)

    async def describe_oss_status_v2_async(
        self,
        request: main_models.DescribeOssStatusV2Request,
    ) -> main_models.DescribeOssStatusV2Response:
        runtime = RuntimeOptions()
        return await self.describe_oss_status_v2with_options_async(request, runtime)

    def describe_oss_upload_token_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssUploadTokenResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeOssUploadToken',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssUploadTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_upload_token_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssUploadTokenResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeOssUploadToken',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssUploadTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_upload_token(self) -> main_models.DescribeOssUploadTokenResponse:
        runtime = RuntimeOptions()
        return self.describe_oss_upload_token_with_options(runtime)

    async def describe_oss_upload_token_async(self) -> main_models.DescribeOssUploadTokenResponse:
        runtime = RuntimeOptions()
        return await self.describe_oss_upload_token_with_options_async(runtime)

    def describe_page_face_verify_data_with_options(
        self,
        request: main_models.DescribePageFaceVerifyDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePageFaceVerifyDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePageFaceVerifyData',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePageFaceVerifyDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_page_face_verify_data_with_options_async(
        self,
        request: main_models.DescribePageFaceVerifyDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePageFaceVerifyDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePageFaceVerifyData',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePageFaceVerifyDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_page_face_verify_data(
        self,
        request: main_models.DescribePageFaceVerifyDataRequest,
    ) -> main_models.DescribePageFaceVerifyDataResponse:
        runtime = RuntimeOptions()
        return self.describe_page_face_verify_data_with_options(request, runtime)

    async def describe_page_face_verify_data_async(
        self,
        request: main_models.DescribePageFaceVerifyDataRequest,
    ) -> main_models.DescribePageFaceVerifyDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_page_face_verify_data_with_options_async(request, runtime)

    def describe_page_setting_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePageSettingResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribePageSetting',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePageSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_page_setting_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePageSettingResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribePageSetting',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePageSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_page_setting(self) -> main_models.DescribePageSettingResponse:
        runtime = RuntimeOptions()
        return self.describe_page_setting_with_options(runtime)

    async def describe_page_setting_async(self) -> main_models.DescribePageSettingResponse:
        runtime = RuntimeOptions()
        return await self.describe_page_setting_with_options_async(runtime)

    def describe_product_code_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductCodeResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeProductCode',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_product_code_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductCodeResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeProductCode',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_product_code(self) -> main_models.DescribeProductCodeResponse:
        runtime = RuntimeOptions()
        return self.describe_product_code_with_options(runtime)

    async def describe_product_code_async(self) -> main_models.DescribeProductCodeResponse:
        runtime = RuntimeOptions()
        return await self.describe_product_code_with_options_async(runtime)

    def describe_smart_statistics_page_list_with_options(
        self,
        request: main_models.DescribeSmartStatisticsPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSmartStatisticsPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSmartStatisticsPageList',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSmartStatisticsPageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_statistics_page_list_with_options_async(
        self,
        request: main_models.DescribeSmartStatisticsPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSmartStatisticsPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSmartStatisticsPageList',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSmartStatisticsPageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_smart_statistics_page_list(
        self,
        request: main_models.DescribeSmartStatisticsPageListRequest,
    ) -> main_models.DescribeSmartStatisticsPageListResponse:
        runtime = RuntimeOptions()
        return self.describe_smart_statistics_page_list_with_options(request, runtime)

    async def describe_smart_statistics_page_list_async(
        self,
        request: main_models.DescribeSmartStatisticsPageListRequest,
    ) -> main_models.DescribeSmartStatisticsPageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_smart_statistics_page_list_with_options_async(request, runtime)

    def describe_verify_device_risk_statistics_with_options(
        self,
        request: main_models.DescribeVerifyDeviceRiskStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyDeviceRiskStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyDeviceRiskStatistics',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyDeviceRiskStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_device_risk_statistics_with_options_async(
        self,
        request: main_models.DescribeVerifyDeviceRiskStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyDeviceRiskStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyDeviceRiskStatistics',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyDeviceRiskStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_device_risk_statistics(
        self,
        request: main_models.DescribeVerifyDeviceRiskStatisticsRequest,
    ) -> main_models.DescribeVerifyDeviceRiskStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_verify_device_risk_statistics_with_options(request, runtime)

    async def describe_verify_device_risk_statistics_async(
        self,
        request: main_models.DescribeVerifyDeviceRiskStatisticsRequest,
    ) -> main_models.DescribeVerifyDeviceRiskStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_verify_device_risk_statistics_with_options_async(request, runtime)

    def describe_verify_fail_statistics_with_options(
        self,
        request: main_models.DescribeVerifyFailStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyFailStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.age_gt):
            query['AgeGt'] = request.age_gt
        if not DaraCore.is_null(request.api):
            query['Api'] = request.api
        if not DaraCore.is_null(request.device_type):
            query['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyFailStatistics',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyFailStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_fail_statistics_with_options_async(
        self,
        request: main_models.DescribeVerifyFailStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyFailStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.age_gt):
            query['AgeGt'] = request.age_gt
        if not DaraCore.is_null(request.api):
            query['Api'] = request.api
        if not DaraCore.is_null(request.device_type):
            query['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyFailStatistics',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyFailStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_fail_statistics(
        self,
        request: main_models.DescribeVerifyFailStatisticsRequest,
    ) -> main_models.DescribeVerifyFailStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_verify_fail_statistics_with_options(request, runtime)

    async def describe_verify_fail_statistics_async(
        self,
        request: main_models.DescribeVerifyFailStatisticsRequest,
    ) -> main_models.DescribeVerifyFailStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_verify_fail_statistics_with_options_async(request, runtime)

    def describe_verify_personas_device_model_statistics_with_options(
        self,
        request: main_models.DescribeVerifyPersonasDeviceModelStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyPersonasDeviceModelStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyPersonasDeviceModelStatistics',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyPersonasDeviceModelStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_personas_device_model_statistics_with_options_async(
        self,
        request: main_models.DescribeVerifyPersonasDeviceModelStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyPersonasDeviceModelStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyPersonasDeviceModelStatistics',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyPersonasDeviceModelStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_personas_device_model_statistics(
        self,
        request: main_models.DescribeVerifyPersonasDeviceModelStatisticsRequest,
    ) -> main_models.DescribeVerifyPersonasDeviceModelStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_verify_personas_device_model_statistics_with_options(request, runtime)

    async def describe_verify_personas_device_model_statistics_async(
        self,
        request: main_models.DescribeVerifyPersonasDeviceModelStatisticsRequest,
    ) -> main_models.DescribeVerifyPersonasDeviceModelStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_verify_personas_device_model_statistics_with_options_async(request, runtime)

    def describe_verify_personas_os_statistics_with_options(
        self,
        request: main_models.DescribeVerifyPersonasOsStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyPersonasOsStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyPersonasOsStatistics',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyPersonasOsStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_personas_os_statistics_with_options_async(
        self,
        request: main_models.DescribeVerifyPersonasOsStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyPersonasOsStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyPersonasOsStatistics',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyPersonasOsStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_personas_os_statistics(
        self,
        request: main_models.DescribeVerifyPersonasOsStatisticsRequest,
    ) -> main_models.DescribeVerifyPersonasOsStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_verify_personas_os_statistics_with_options(request, runtime)

    async def describe_verify_personas_os_statistics_async(
        self,
        request: main_models.DescribeVerifyPersonasOsStatisticsRequest,
    ) -> main_models.DescribeVerifyPersonasOsStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_verify_personas_os_statistics_with_options_async(request, runtime)

    def describe_verify_personas_province_statistics_with_options(
        self,
        request: main_models.DescribeVerifyPersonasProvinceStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyPersonasProvinceStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyPersonasProvinceStatistics',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyPersonasProvinceStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_personas_province_statistics_with_options_async(
        self,
        request: main_models.DescribeVerifyPersonasProvinceStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyPersonasProvinceStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyPersonasProvinceStatistics',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyPersonasProvinceStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_personas_province_statistics(
        self,
        request: main_models.DescribeVerifyPersonasProvinceStatisticsRequest,
    ) -> main_models.DescribeVerifyPersonasProvinceStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_verify_personas_province_statistics_with_options(request, runtime)

    async def describe_verify_personas_province_statistics_async(
        self,
        request: main_models.DescribeVerifyPersonasProvinceStatisticsRequest,
    ) -> main_models.DescribeVerifyPersonasProvinceStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_verify_personas_province_statistics_with_options_async(request, runtime)

    def describe_verify_personas_sex_statistics_with_options(
        self,
        request: main_models.DescribeVerifyPersonasSexStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyPersonasSexStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyPersonasSexStatistics',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyPersonasSexStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_personas_sex_statistics_with_options_async(
        self,
        request: main_models.DescribeVerifyPersonasSexStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyPersonasSexStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyPersonasSexStatistics',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyPersonasSexStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_personas_sex_statistics(
        self,
        request: main_models.DescribeVerifyPersonasSexStatisticsRequest,
    ) -> main_models.DescribeVerifyPersonasSexStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_verify_personas_sex_statistics_with_options(request, runtime)

    async def describe_verify_personas_sex_statistics_async(
        self,
        request: main_models.DescribeVerifyPersonasSexStatisticsRequest,
    ) -> main_models.DescribeVerifyPersonasSexStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_verify_personas_sex_statistics_with_options_async(request, runtime)

    def describe_verify_result_with_options(
        self,
        request: main_models.DescribeVerifyResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyResult',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_result_with_options_async(
        self,
        request: main_models.DescribeVerifyResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyResult',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_result(
        self,
        request: main_models.DescribeVerifyResultRequest,
    ) -> main_models.DescribeVerifyResultResponse:
        runtime = RuntimeOptions()
        return self.describe_verify_result_with_options(request, runtime)

    async def describe_verify_result_async(
        self,
        request: main_models.DescribeVerifyResultRequest,
    ) -> main_models.DescribeVerifyResultResponse:
        runtime = RuntimeOptions()
        return await self.describe_verify_result_with_options_async(request, runtime)

    def describe_verify_sdkwith_options(
        self,
        request: main_models.DescribeVerifySDKRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifySDKResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifySDK',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifySDKResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_sdkwith_options_async(
        self,
        request: main_models.DescribeVerifySDKRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifySDKResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifySDK',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifySDKResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_sdk(
        self,
        request: main_models.DescribeVerifySDKRequest,
    ) -> main_models.DescribeVerifySDKResponse:
        runtime = RuntimeOptions()
        return self.describe_verify_sdkwith_options(request, runtime)

    async def describe_verify_sdk_async(
        self,
        request: main_models.DescribeVerifySDKRequest,
    ) -> main_models.DescribeVerifySDKResponse:
        runtime = RuntimeOptions()
        return await self.describe_verify_sdkwith_options_async(request, runtime)

    def describe_verify_search_page_list_with_options(
        self,
        request: main_models.DescribeVerifySearchPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifySearchPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_no):
            query['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.has_device_risk):
            query['HasDeviceRisk'] = request.has_device_risk
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.passed):
            query['Passed'] = request.passed
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.root):
            query['Root'] = request.root
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.simulator):
            query['Simulator'] = request.simulator
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_code):
            query['SubCode'] = request.sub_code
        if not DaraCore.is_null(request.sub_codes):
            query['SubCodes'] = request.sub_codes
        if not DaraCore.is_null(request.virtual_video):
            query['VirtualVideo'] = request.virtual_video
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifySearchPageList',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifySearchPageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_search_page_list_with_options_async(
        self,
        request: main_models.DescribeVerifySearchPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifySearchPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_no):
            query['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.has_device_risk):
            query['HasDeviceRisk'] = request.has_device_risk
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.passed):
            query['Passed'] = request.passed
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.root):
            query['Root'] = request.root
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.simulator):
            query['Simulator'] = request.simulator
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_code):
            query['SubCode'] = request.sub_code
        if not DaraCore.is_null(request.sub_codes):
            query['SubCodes'] = request.sub_codes
        if not DaraCore.is_null(request.virtual_video):
            query['VirtualVideo'] = request.virtual_video
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifySearchPageList',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifySearchPageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_search_page_list(
        self,
        request: main_models.DescribeVerifySearchPageListRequest,
    ) -> main_models.DescribeVerifySearchPageListResponse:
        runtime = RuntimeOptions()
        return self.describe_verify_search_page_list_with_options(request, runtime)

    async def describe_verify_search_page_list_async(
        self,
        request: main_models.DescribeVerifySearchPageListRequest,
    ) -> main_models.DescribeVerifySearchPageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_verify_search_page_list_with_options_async(request, runtime)

    def describe_verify_statistics_with_options(
        self,
        request: main_models.DescribeVerifyStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.age_gt):
            query['AgeGt'] = request.age_gt
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyStatistics',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_statistics_with_options_async(
        self,
        request: main_models.DescribeVerifyStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.age_gt):
            query['AgeGt'] = request.age_gt
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyStatistics',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_statistics(
        self,
        request: main_models.DescribeVerifyStatisticsRequest,
    ) -> main_models.DescribeVerifyStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_verify_statistics_with_options(request, runtime)

    async def describe_verify_statistics_async(
        self,
        request: main_models.DescribeVerifyStatisticsRequest,
    ) -> main_models.DescribeVerifyStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_verify_statistics_with_options_async(request, runtime)

    def describe_verify_token_with_options(
        self,
        request: main_models.DescribeVerifyTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.callback_seed):
            query['CallbackSeed'] = request.callback_seed
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.face_retained_image_url):
            query['FaceRetainedImageUrl'] = request.face_retained_image_url
        if not DaraCore.is_null(request.failed_redirect_url):
            query['FailedRedirectUrl'] = request.failed_redirect_url
        if not DaraCore.is_null(request.id_card_back_image_url):
            query['IdCardBackImageUrl'] = request.id_card_back_image_url
        if not DaraCore.is_null(request.id_card_front_image_url):
            query['IdCardFrontImageUrl'] = request.id_card_front_image_url
        if not DaraCore.is_null(request.id_card_number):
            query['IdCardNumber'] = request.id_card_number
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.passed_redirect_url):
            query['PassedRedirectUrl'] = request.passed_redirect_url
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_ip):
            query['UserIp'] = request.user_ip
        if not DaraCore.is_null(request.user_phone_number):
            query['UserPhoneNumber'] = request.user_phone_number
        if not DaraCore.is_null(request.user_regist_time):
            query['UserRegistTime'] = request.user_regist_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyToken',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_token_with_options_async(
        self,
        request: main_models.DescribeVerifyTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.callback_seed):
            query['CallbackSeed'] = request.callback_seed
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.face_retained_image_url):
            query['FaceRetainedImageUrl'] = request.face_retained_image_url
        if not DaraCore.is_null(request.failed_redirect_url):
            query['FailedRedirectUrl'] = request.failed_redirect_url
        if not DaraCore.is_null(request.id_card_back_image_url):
            query['IdCardBackImageUrl'] = request.id_card_back_image_url
        if not DaraCore.is_null(request.id_card_front_image_url):
            query['IdCardFrontImageUrl'] = request.id_card_front_image_url
        if not DaraCore.is_null(request.id_card_number):
            query['IdCardNumber'] = request.id_card_number
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.passed_redirect_url):
            query['PassedRedirectUrl'] = request.passed_redirect_url
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_ip):
            query['UserIp'] = request.user_ip
        if not DaraCore.is_null(request.user_phone_number):
            query['UserPhoneNumber'] = request.user_phone_number
        if not DaraCore.is_null(request.user_regist_time):
            query['UserRegistTime'] = request.user_regist_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyToken',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_token(
        self,
        request: main_models.DescribeVerifyTokenRequest,
    ) -> main_models.DescribeVerifyTokenResponse:
        runtime = RuntimeOptions()
        return self.describe_verify_token_with_options(request, runtime)

    async def describe_verify_token_async(
        self,
        request: main_models.DescribeVerifyTokenRequest,
    ) -> main_models.DescribeVerifyTokenResponse:
        runtime = RuntimeOptions()
        return await self.describe_verify_token_with_options_async(request, runtime)

    def describe_whitelist_setting_with_options(
        self,
        request: main_models.DescribeWhitelistSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWhitelistSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_no):
            query['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.valid_end_date):
            query['ValidEndDate'] = request.valid_end_date
        if not DaraCore.is_null(request.valid_start_date):
            query['ValidStartDate'] = request.valid_start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWhitelistSetting',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWhitelistSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_whitelist_setting_with_options_async(
        self,
        request: main_models.DescribeWhitelistSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWhitelistSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_no):
            query['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.valid_end_date):
            query['ValidEndDate'] = request.valid_end_date
        if not DaraCore.is_null(request.valid_start_date):
            query['ValidStartDate'] = request.valid_start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWhitelistSetting',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWhitelistSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_whitelist_setting(
        self,
        request: main_models.DescribeWhitelistSettingRequest,
    ) -> main_models.DescribeWhitelistSettingResponse:
        runtime = RuntimeOptions()
        return self.describe_whitelist_setting_with_options(request, runtime)

    async def describe_whitelist_setting_async(
        self,
        request: main_models.DescribeWhitelistSettingRequest,
    ) -> main_models.DescribeWhitelistSettingResponse:
        runtime = RuntimeOptions()
        return await self.describe_whitelist_setting_with_options_async(request, runtime)

    def detect_face_attributes_with_options(
        self,
        request: main_models.DetectFaceAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectFaceAttributesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.material_value):
            body['MaterialValue'] = request.material_value
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetectFaceAttributes',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectFaceAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_face_attributes_with_options_async(
        self,
        request: main_models.DetectFaceAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectFaceAttributesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.material_value):
            body['MaterialValue'] = request.material_value
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetectFaceAttributes',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectFaceAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_face_attributes(
        self,
        request: main_models.DetectFaceAttributesRequest,
    ) -> main_models.DetectFaceAttributesResponse:
        runtime = RuntimeOptions()
        return self.detect_face_attributes_with_options(request, runtime)

    async def detect_face_attributes_async(
        self,
        request: main_models.DetectFaceAttributesRequest,
    ) -> main_models.DetectFaceAttributesResponse:
        runtime = RuntimeOptions()
        return await self.detect_face_attributes_with_options_async(request, runtime)

    def download_verify_records_with_options(
        self,
        request: main_models.DownloadVerifyRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadVerifyRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_param):
            query['BizParam'] = request.biz_param
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadVerifyRecords',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadVerifyRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_verify_records_with_options_async(
        self,
        request: main_models.DownloadVerifyRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadVerifyRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_param):
            query['BizParam'] = request.biz_param
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadVerifyRecords',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadVerifyRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_verify_records(
        self,
        request: main_models.DownloadVerifyRecordsRequest,
    ) -> main_models.DownloadVerifyRecordsResponse:
        runtime = RuntimeOptions()
        return self.download_verify_records_with_options(request, runtime)

    async def download_verify_records_async(
        self,
        request: main_models.DownloadVerifyRecordsRequest,
    ) -> main_models.DownloadVerifyRecordsResponse:
        runtime = RuntimeOptions()
        return await self.download_verify_records_with_options_async(request, runtime)

    def id_2meta_period_verify_with_options(
        self,
        request: main_models.Id2MetaPeriodVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id2MetaPeriodVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        if not DaraCore.is_null(request.validity_end_date):
            body['ValidityEndDate'] = request.validity_end_date
        if not DaraCore.is_null(request.validity_start_date):
            body['ValidityStartDate'] = request.validity_start_date
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Id2MetaPeriodVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Id2MetaPeriodVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def id_2meta_period_verify_with_options_async(
        self,
        request: main_models.Id2MetaPeriodVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id2MetaPeriodVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        if not DaraCore.is_null(request.validity_end_date):
            body['ValidityEndDate'] = request.validity_end_date
        if not DaraCore.is_null(request.validity_start_date):
            body['ValidityStartDate'] = request.validity_start_date
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Id2MetaPeriodVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Id2MetaPeriodVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def id_2meta_period_verify(
        self,
        request: main_models.Id2MetaPeriodVerifyRequest,
    ) -> main_models.Id2MetaPeriodVerifyResponse:
        runtime = RuntimeOptions()
        return self.id_2meta_period_verify_with_options(request, runtime)

    async def id_2meta_period_verify_async(
        self,
        request: main_models.Id2MetaPeriodVerifyRequest,
    ) -> main_models.Id2MetaPeriodVerifyResponse:
        runtime = RuntimeOptions()
        return await self.id_2meta_period_verify_with_options_async(request, runtime)

    def id_2meta_standard_verify_with_options(
        self,
        request: main_models.Id2MetaStandardVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id2MetaStandardVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Id2MetaStandardVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Id2MetaStandardVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def id_2meta_standard_verify_with_options_async(
        self,
        request: main_models.Id2MetaStandardVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id2MetaStandardVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Id2MetaStandardVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Id2MetaStandardVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def id_2meta_standard_verify(
        self,
        request: main_models.Id2MetaStandardVerifyRequest,
    ) -> main_models.Id2MetaStandardVerifyResponse:
        runtime = RuntimeOptions()
        return self.id_2meta_standard_verify_with_options(request, runtime)

    async def id_2meta_standard_verify_async(
        self,
        request: main_models.Id2MetaStandardVerifyRequest,
    ) -> main_models.Id2MetaStandardVerifyResponse:
        runtime = RuntimeOptions()
        return await self.id_2meta_standard_verify_with_options_async(request, runtime)

    def id_2meta_verify_with_options(
        self,
        request: main_models.Id2MetaVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id2MetaVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Id2MetaVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Id2MetaVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def id_2meta_verify_with_options_async(
        self,
        request: main_models.Id2MetaVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id2MetaVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Id2MetaVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Id2MetaVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def id_2meta_verify(
        self,
        request: main_models.Id2MetaVerifyRequest,
    ) -> main_models.Id2MetaVerifyResponse:
        runtime = RuntimeOptions()
        return self.id_2meta_verify_with_options(request, runtime)

    async def id_2meta_verify_async(
        self,
        request: main_models.Id2MetaVerifyRequest,
    ) -> main_models.Id2MetaVerifyResponse:
        runtime = RuntimeOptions()
        return await self.id_2meta_verify_with_options_async(request, runtime)

    def id_2meta_verify_with_ocrwith_options(
        self,
        request: main_models.Id2MetaVerifyWithOCRRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id2MetaVerifyWithOCRResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cert_file):
            body['CertFile'] = request.cert_file
        if not DaraCore.is_null(request.cert_national_file):
            body['CertNationalFile'] = request.cert_national_file
        if not DaraCore.is_null(request.cert_national_url):
            body['CertNationalUrl'] = request.cert_national_url
        if not DaraCore.is_null(request.cert_url):
            body['CertUrl'] = request.cert_url
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Id2MetaVerifyWithOCR',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Id2MetaVerifyWithOCRResponse(),
            self.call_api(params, req, runtime)
        )

    async def id_2meta_verify_with_ocrwith_options_async(
        self,
        request: main_models.Id2MetaVerifyWithOCRRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id2MetaVerifyWithOCRResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cert_file):
            body['CertFile'] = request.cert_file
        if not DaraCore.is_null(request.cert_national_file):
            body['CertNationalFile'] = request.cert_national_file
        if not DaraCore.is_null(request.cert_national_url):
            body['CertNationalUrl'] = request.cert_national_url
        if not DaraCore.is_null(request.cert_url):
            body['CertUrl'] = request.cert_url
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Id2MetaVerifyWithOCR',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Id2MetaVerifyWithOCRResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def id_2meta_verify_with_ocr(
        self,
        request: main_models.Id2MetaVerifyWithOCRRequest,
    ) -> main_models.Id2MetaVerifyWithOCRResponse:
        runtime = RuntimeOptions()
        return self.id_2meta_verify_with_ocrwith_options(request, runtime)

    async def id_2meta_verify_with_ocr_async(
        self,
        request: main_models.Id2MetaVerifyWithOCRRequest,
    ) -> main_models.Id2MetaVerifyWithOCRResponse:
        runtime = RuntimeOptions()
        return await self.id_2meta_verify_with_ocrwith_options_async(request, runtime)

    def id_2meta_verify_with_ocradvance(
        self,
        request: main_models.Id2MetaVerifyWithOCRAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id2MetaVerifyWithOCRResponse:
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
            'Product': 'Cloudauth',
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
        id_2meta_verify_with_ocrreq = main_models.Id2MetaVerifyWithOCRRequest()
        Utils.convert(request, id_2meta_verify_with_ocrreq)
        if not DaraCore.is_null(request.cert_file_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.cert_file_object,
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
            id_2meta_verify_with_ocrreq.cert_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not DaraCore.is_null(request.cert_national_file_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.cert_national_file_object,
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
            id_2meta_verify_with_ocrreq.cert_national_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        id_2meta_verify_with_ocrresp = self.id_2meta_verify_with_ocrwith_options(id_2meta_verify_with_ocrreq, runtime)
        return id_2meta_verify_with_ocrresp

    async def id_2meta_verify_with_ocradvance_async(
        self,
        request: main_models.Id2MetaVerifyWithOCRAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id2MetaVerifyWithOCRResponse:
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
            'Product': 'Cloudauth',
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
        id_2meta_verify_with_ocrreq = main_models.Id2MetaVerifyWithOCRRequest()
        Utils.convert(request, id_2meta_verify_with_ocrreq)
        if not DaraCore.is_null(request.cert_file_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.cert_file_object,
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
            id_2meta_verify_with_ocrreq.cert_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not DaraCore.is_null(request.cert_national_file_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.cert_national_file_object,
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
            id_2meta_verify_with_ocrreq.cert_national_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        id_2meta_verify_with_ocrresp = await self.id_2meta_verify_with_ocrwith_options_async(id_2meta_verify_with_ocrreq, runtime)
        return id_2meta_verify_with_ocrresp

    def id_3meta_verify_with_options(
        self,
        request: main_models.Id3MetaVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id3MetaVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.crop):
            body['Crop'] = request.crop
        if not DaraCore.is_null(request.face_file):
            body['FaceFile'] = request.face_file
        if not DaraCore.is_null(request.face_url):
            body['FaceUrl'] = request.face_url
        if not DaraCore.is_null(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Id3MetaVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Id3MetaVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def id_3meta_verify_with_options_async(
        self,
        request: main_models.Id3MetaVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id3MetaVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.crop):
            body['Crop'] = request.crop
        if not DaraCore.is_null(request.face_file):
            body['FaceFile'] = request.face_file
        if not DaraCore.is_null(request.face_url):
            body['FaceUrl'] = request.face_url
        if not DaraCore.is_null(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Id3MetaVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Id3MetaVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def id_3meta_verify(
        self,
        request: main_models.Id3MetaVerifyRequest,
    ) -> main_models.Id3MetaVerifyResponse:
        runtime = RuntimeOptions()
        return self.id_3meta_verify_with_options(request, runtime)

    async def id_3meta_verify_async(
        self,
        request: main_models.Id3MetaVerifyRequest,
    ) -> main_models.Id3MetaVerifyResponse:
        runtime = RuntimeOptions()
        return await self.id_3meta_verify_with_options_async(request, runtime)

    def id_3meta_verify_advance(
        self,
        request: main_models.Id3MetaVerifyAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id3MetaVerifyResponse:
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
            'Product': 'Cloudauth',
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
        id_3meta_verify_req = main_models.Id3MetaVerifyRequest()
        Utils.convert(request, id_3meta_verify_req)
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
            id_3meta_verify_req.face_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        id_3meta_verify_resp = self.id_3meta_verify_with_options(id_3meta_verify_req, runtime)
        return id_3meta_verify_resp

    async def id_3meta_verify_advance_async(
        self,
        request: main_models.Id3MetaVerifyAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id3MetaVerifyResponse:
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
            'Product': 'Cloudauth',
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
        id_3meta_verify_req = main_models.Id3MetaVerifyRequest()
        Utils.convert(request, id_3meta_verify_req)
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
            id_3meta_verify_req.face_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        id_3meta_verify_resp = await self.id_3meta_verify_with_options_async(id_3meta_verify_req, runtime)
        return id_3meta_verify_resp

    def id_3meta_verify_with_ocrwith_options(
        self,
        request: main_models.Id3MetaVerifyWithOCRRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id3MetaVerifyWithOCRResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cert_file):
            body['CertFile'] = request.cert_file
        if not DaraCore.is_null(request.cert_national_file):
            body['CertNationalFile'] = request.cert_national_file
        if not DaraCore.is_null(request.cert_national_url):
            body['CertNationalUrl'] = request.cert_national_url
        if not DaraCore.is_null(request.cert_url):
            body['CertUrl'] = request.cert_url
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Id3MetaVerifyWithOCR',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Id3MetaVerifyWithOCRResponse(),
            self.call_api(params, req, runtime)
        )

    async def id_3meta_verify_with_ocrwith_options_async(
        self,
        request: main_models.Id3MetaVerifyWithOCRRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id3MetaVerifyWithOCRResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cert_file):
            body['CertFile'] = request.cert_file
        if not DaraCore.is_null(request.cert_national_file):
            body['CertNationalFile'] = request.cert_national_file
        if not DaraCore.is_null(request.cert_national_url):
            body['CertNationalUrl'] = request.cert_national_url
        if not DaraCore.is_null(request.cert_url):
            body['CertUrl'] = request.cert_url
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Id3MetaVerifyWithOCR',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Id3MetaVerifyWithOCRResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def id_3meta_verify_with_ocr(
        self,
        request: main_models.Id3MetaVerifyWithOCRRequest,
    ) -> main_models.Id3MetaVerifyWithOCRResponse:
        runtime = RuntimeOptions()
        return self.id_3meta_verify_with_ocrwith_options(request, runtime)

    async def id_3meta_verify_with_ocr_async(
        self,
        request: main_models.Id3MetaVerifyWithOCRRequest,
    ) -> main_models.Id3MetaVerifyWithOCRResponse:
        runtime = RuntimeOptions()
        return await self.id_3meta_verify_with_ocrwith_options_async(request, runtime)

    def id_3meta_verify_with_ocradvance(
        self,
        request: main_models.Id3MetaVerifyWithOCRAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id3MetaVerifyWithOCRResponse:
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
            'Product': 'Cloudauth',
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
        id_3meta_verify_with_ocrreq = main_models.Id3MetaVerifyWithOCRRequest()
        Utils.convert(request, id_3meta_verify_with_ocrreq)
        if not DaraCore.is_null(request.cert_file_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.cert_file_object,
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
            id_3meta_verify_with_ocrreq.cert_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not DaraCore.is_null(request.cert_national_file_object):
            auth_response = auth_client.call_api(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.cert_national_file_object,
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
            id_3meta_verify_with_ocrreq.cert_national_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        id_3meta_verify_with_ocrresp = self.id_3meta_verify_with_ocrwith_options(id_3meta_verify_with_ocrreq, runtime)
        return id_3meta_verify_with_ocrresp

    async def id_3meta_verify_with_ocradvance_async(
        self,
        request: main_models.Id3MetaVerifyWithOCRAdvanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Id3MetaVerifyWithOCRResponse:
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
            'Product': 'Cloudauth',
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
        id_3meta_verify_with_ocrreq = main_models.Id3MetaVerifyWithOCRRequest()
        Utils.convert(request, id_3meta_verify_with_ocrreq)
        if not DaraCore.is_null(request.cert_file_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.cert_file_object,
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
            id_3meta_verify_with_ocrreq.cert_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not DaraCore.is_null(request.cert_national_file_object):
            auth_response = await auth_client.call_api_async(auth_params, auth_req, runtime)
            tmp_body = auth_response.get('body')
            use_accelerate = bool(tmp_body.get('UseAccelerate'))
            auth_response_body = Utils.stringify_map_value(tmp_body)
            file_obj = FileField(
                filename = auth_response_body.get('ObjectKey'),
                content = request.cert_national_file_object,
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
            id_3meta_verify_with_ocrreq.cert_national_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        id_3meta_verify_with_ocrresp = await self.id_3meta_verify_with_ocrwith_options_async(id_3meta_verify_with_ocrreq, runtime)
        return id_3meta_verify_with_ocrresp

    def init_auth_verify_with_options(
        self,
        request: main_models.InitAuthVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitAuthVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.callback_token):
            body['CallbackToken'] = request.callback_token
        if not DaraCore.is_null(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.card_page_number):
            body['CardPageNumber'] = request.card_page_number
        if not DaraCore.is_null(request.card_type):
            body['CardType'] = request.card_type
        if not DaraCore.is_null(request.doc_scan_mode):
            body['DocScanMode'] = request.doc_scan_mode
        if not DaraCore.is_null(request.id_spoof):
            body['IdSpoof'] = request.id_spoof
        if not DaraCore.is_null(request.meta_info):
            body['MetaInfo'] = request.meta_info
        if not DaraCore.is_null(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InitAuthVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitAuthVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_auth_verify_with_options_async(
        self,
        request: main_models.InitAuthVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitAuthVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.callback_token):
            body['CallbackToken'] = request.callback_token
        if not DaraCore.is_null(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.card_page_number):
            body['CardPageNumber'] = request.card_page_number
        if not DaraCore.is_null(request.card_type):
            body['CardType'] = request.card_type
        if not DaraCore.is_null(request.doc_scan_mode):
            body['DocScanMode'] = request.doc_scan_mode
        if not DaraCore.is_null(request.id_spoof):
            body['IdSpoof'] = request.id_spoof
        if not DaraCore.is_null(request.meta_info):
            body['MetaInfo'] = request.meta_info
        if not DaraCore.is_null(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InitAuthVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitAuthVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_auth_verify(
        self,
        request: main_models.InitAuthVerifyRequest,
    ) -> main_models.InitAuthVerifyResponse:
        runtime = RuntimeOptions()
        return self.init_auth_verify_with_options(request, runtime)

    async def init_auth_verify_async(
        self,
        request: main_models.InitAuthVerifyRequest,
    ) -> main_models.InitAuthVerifyResponse:
        runtime = RuntimeOptions()
        return await self.init_auth_verify_with_options_async(request, runtime)

    def init_card_verify_with_options(
        self,
        request: main_models.InitCardVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitCardVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callback_token):
            query['CallbackToken'] = request.callback_token
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.card_page_number):
            query['CardPageNumber'] = request.card_page_number
        if not DaraCore.is_null(request.card_type):
            query['CardType'] = request.card_type
        if not DaraCore.is_null(request.doc_scan_mode):
            query['DocScanMode'] = request.doc_scan_mode
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.meta_info):
            query['MetaInfo'] = request.meta_info
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.picture_save):
            query['PictureSave'] = request.picture_save
        if not DaraCore.is_null(request.verify_meta):
            query['VerifyMeta'] = request.verify_meta
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitCardVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitCardVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_card_verify_with_options_async(
        self,
        request: main_models.InitCardVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitCardVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callback_token):
            query['CallbackToken'] = request.callback_token
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.card_page_number):
            query['CardPageNumber'] = request.card_page_number
        if not DaraCore.is_null(request.card_type):
            query['CardType'] = request.card_type
        if not DaraCore.is_null(request.doc_scan_mode):
            query['DocScanMode'] = request.doc_scan_mode
        if not DaraCore.is_null(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not DaraCore.is_null(request.meta_info):
            query['MetaInfo'] = request.meta_info
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.picture_save):
            query['PictureSave'] = request.picture_save
        if not DaraCore.is_null(request.verify_meta):
            query['VerifyMeta'] = request.verify_meta
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitCardVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitCardVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_card_verify(
        self,
        request: main_models.InitCardVerifyRequest,
    ) -> main_models.InitCardVerifyResponse:
        runtime = RuntimeOptions()
        return self.init_card_verify_with_options(request, runtime)

    async def init_card_verify_async(
        self,
        request: main_models.InitCardVerifyRequest,
    ) -> main_models.InitCardVerifyResponse:
        runtime = RuntimeOptions()
        return await self.init_card_verify_with_options_async(request, runtime)

    def init_face_verify_with_options(
        self,
        request: main_models.InitFaceVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitFaceVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_quality_check):
            query['AppQualityCheck'] = request.app_quality_check
        if not DaraCore.is_null(request.birthday):
            query['Birthday'] = request.birthday
        if not DaraCore.is_null(request.callback_token):
            query['CallbackToken'] = request.callback_token
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.camera_selection):
            query['CameraSelection'] = request.camera_selection
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_no):
            query['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.cert_type):
            query['CertType'] = request.cert_type
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.certify_url_style):
            query['CertifyUrlStyle'] = request.certify_url_style
        if not DaraCore.is_null(request.certify_url_type):
            query['CertifyUrlType'] = request.certify_url_type
        if not DaraCore.is_null(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.face_contrast_picture_url):
            query['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not DaraCore.is_null(request.face_guard_output):
            query['FaceGuardOutput'] = request.face_guard_output
        if not DaraCore.is_null(request.h_5degrade_confirm_btn):
            query['H5DegradeConfirmBtn'] = request.h_5degrade_confirm_btn
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.meta_info):
            query['MetaInfo'] = request.meta_info
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.need_multi_face_check):
            query['NeedMultiFaceCheck'] = request.need_multi_face_check
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_object_name):
            query['OssObjectName'] = request.oss_object_name
        if not DaraCore.is_null(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        if not DaraCore.is_null(request.procedure_priority):
            query['ProcedurePriority'] = request.procedure_priority
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.rarely_characters):
            query['RarelyCharacters'] = request.rarely_characters
        if not DaraCore.is_null(request.read_img):
            query['ReadImg'] = request.read_img
        if not DaraCore.is_null(request.return_url):
            query['ReturnUrl'] = request.return_url
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.suitable_type):
            query['SuitableType'] = request.suitable_type
        if not DaraCore.is_null(request.ui_custom_url):
            query['UiCustomUrl'] = request.ui_custom_url
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.validity_date):
            query['ValidityDate'] = request.validity_date
        if not DaraCore.is_null(request.video_evidence):
            query['VideoEvidence'] = request.video_evidence
        if not DaraCore.is_null(request.voluntary_customized_content):
            query['VoluntaryCustomizedContent'] = request.voluntary_customized_content
        body = {}
        if not DaraCore.is_null(request.auth_id):
            body['AuthId'] = request.auth_id
        if not DaraCore.is_null(request.crop):
            body['Crop'] = request.crop
        if not DaraCore.is_null(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InitFaceVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_face_verify_with_options_async(
        self,
        request: main_models.InitFaceVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitFaceVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_quality_check):
            query['AppQualityCheck'] = request.app_quality_check
        if not DaraCore.is_null(request.birthday):
            query['Birthday'] = request.birthday
        if not DaraCore.is_null(request.callback_token):
            query['CallbackToken'] = request.callback_token
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.camera_selection):
            query['CameraSelection'] = request.camera_selection
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_no):
            query['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.cert_type):
            query['CertType'] = request.cert_type
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.certify_url_style):
            query['CertifyUrlStyle'] = request.certify_url_style
        if not DaraCore.is_null(request.certify_url_type):
            query['CertifyUrlType'] = request.certify_url_type
        if not DaraCore.is_null(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.face_contrast_picture_url):
            query['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not DaraCore.is_null(request.face_guard_output):
            query['FaceGuardOutput'] = request.face_guard_output
        if not DaraCore.is_null(request.h_5degrade_confirm_btn):
            query['H5DegradeConfirmBtn'] = request.h_5degrade_confirm_btn
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.meta_info):
            query['MetaInfo'] = request.meta_info
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.need_multi_face_check):
            query['NeedMultiFaceCheck'] = request.need_multi_face_check
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_object_name):
            query['OssObjectName'] = request.oss_object_name
        if not DaraCore.is_null(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        if not DaraCore.is_null(request.procedure_priority):
            query['ProcedurePriority'] = request.procedure_priority
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.rarely_characters):
            query['RarelyCharacters'] = request.rarely_characters
        if not DaraCore.is_null(request.read_img):
            query['ReadImg'] = request.read_img
        if not DaraCore.is_null(request.return_url):
            query['ReturnUrl'] = request.return_url
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.suitable_type):
            query['SuitableType'] = request.suitable_type
        if not DaraCore.is_null(request.ui_custom_url):
            query['UiCustomUrl'] = request.ui_custom_url
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.validity_date):
            query['ValidityDate'] = request.validity_date
        if not DaraCore.is_null(request.video_evidence):
            query['VideoEvidence'] = request.video_evidence
        if not DaraCore.is_null(request.voluntary_customized_content):
            query['VoluntaryCustomizedContent'] = request.voluntary_customized_content
        body = {}
        if not DaraCore.is_null(request.auth_id):
            body['AuthId'] = request.auth_id
        if not DaraCore.is_null(request.crop):
            body['Crop'] = request.crop
        if not DaraCore.is_null(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InitFaceVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitFaceVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_face_verify(
        self,
        request: main_models.InitFaceVerifyRequest,
    ) -> main_models.InitFaceVerifyResponse:
        runtime = RuntimeOptions()
        return self.init_face_verify_with_options(request, runtime)

    async def init_face_verify_async(
        self,
        request: main_models.InitFaceVerifyRequest,
    ) -> main_models.InitFaceVerifyResponse:
        runtime = RuntimeOptions()
        return await self.init_face_verify_with_options_async(request, runtime)

    def insert_white_list_setting_with_options(
        self,
        request: main_models.InsertWhiteListSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InsertWhiteListSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_no):
            query['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.valid_day):
            query['ValidDay'] = request.valid_day
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertWhiteListSetting',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertWhiteListSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_white_list_setting_with_options_async(
        self,
        request: main_models.InsertWhiteListSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InsertWhiteListSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_no):
            query['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.valid_day):
            query['ValidDay'] = request.valid_day
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertWhiteListSetting',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertWhiteListSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_white_list_setting(
        self,
        request: main_models.InsertWhiteListSettingRequest,
    ) -> main_models.InsertWhiteListSettingResponse:
        runtime = RuntimeOptions()
        return self.insert_white_list_setting_with_options(request, runtime)

    async def insert_white_list_setting_async(
        self,
        request: main_models.InsertWhiteListSettingRequest,
    ) -> main_models.InsertWhiteListSettingResponse:
        runtime = RuntimeOptions()
        return await self.insert_white_list_setting_with_options_async(request, runtime)

    def liveness_face_verify_with_options(
        self,
        request: main_models.LivenessFaceVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LivenessFaceVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        body = {}
        if not DaraCore.is_null(request.certify_id):
            body['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.crop):
            body['Crop'] = request.crop
        if not DaraCore.is_null(request.device_token):
            body['DeviceToken'] = request.device_token
        if not DaraCore.is_null(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        if not DaraCore.is_null(request.face_contrast_picture_url):
            body['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not DaraCore.is_null(request.ip):
            body['Ip'] = request.ip
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.oss_bucket_name):
            body['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_object_name):
            body['OssObjectName'] = request.oss_object_name
        if not DaraCore.is_null(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LivenessFaceVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LivenessFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def liveness_face_verify_with_options_async(
        self,
        request: main_models.LivenessFaceVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LivenessFaceVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        body = {}
        if not DaraCore.is_null(request.certify_id):
            body['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.crop):
            body['Crop'] = request.crop
        if not DaraCore.is_null(request.device_token):
            body['DeviceToken'] = request.device_token
        if not DaraCore.is_null(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        if not DaraCore.is_null(request.face_contrast_picture_url):
            body['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not DaraCore.is_null(request.ip):
            body['Ip'] = request.ip
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.oss_bucket_name):
            body['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_object_name):
            body['OssObjectName'] = request.oss_object_name
        if not DaraCore.is_null(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LivenessFaceVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LivenessFaceVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def liveness_face_verify(
        self,
        request: main_models.LivenessFaceVerifyRequest,
    ) -> main_models.LivenessFaceVerifyResponse:
        runtime = RuntimeOptions()
        return self.liveness_face_verify_with_options(request, runtime)

    async def liveness_face_verify_async(
        self,
        request: main_models.LivenessFaceVerifyRequest,
    ) -> main_models.LivenessFaceVerifyResponse:
        runtime = RuntimeOptions()
        return await self.liveness_face_verify_with_options_async(request, runtime)

    def mobile_2meta_verify_with_options(
        self,
        request: main_models.Mobile2MetaVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Mobile2MetaVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Mobile2MetaVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Mobile2MetaVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_2meta_verify_with_options_async(
        self,
        request: main_models.Mobile2MetaVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Mobile2MetaVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Mobile2MetaVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Mobile2MetaVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_2meta_verify(
        self,
        request: main_models.Mobile2MetaVerifyRequest,
    ) -> main_models.Mobile2MetaVerifyResponse:
        runtime = RuntimeOptions()
        return self.mobile_2meta_verify_with_options(request, runtime)

    async def mobile_2meta_verify_async(
        self,
        request: main_models.Mobile2MetaVerifyRequest,
    ) -> main_models.Mobile2MetaVerifyResponse:
        runtime = RuntimeOptions()
        return await self.mobile_2meta_verify_with_options_async(request, runtime)

    def mobile_3meta_detail_standard_verify_with_options(
        self,
        request: main_models.Mobile3MetaDetailStandardVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Mobile3MetaDetailStandardVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Mobile3MetaDetailStandardVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Mobile3MetaDetailStandardVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_3meta_detail_standard_verify_with_options_async(
        self,
        request: main_models.Mobile3MetaDetailStandardVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Mobile3MetaDetailStandardVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Mobile3MetaDetailStandardVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Mobile3MetaDetailStandardVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_3meta_detail_standard_verify(
        self,
        request: main_models.Mobile3MetaDetailStandardVerifyRequest,
    ) -> main_models.Mobile3MetaDetailStandardVerifyResponse:
        runtime = RuntimeOptions()
        return self.mobile_3meta_detail_standard_verify_with_options(request, runtime)

    async def mobile_3meta_detail_standard_verify_async(
        self,
        request: main_models.Mobile3MetaDetailStandardVerifyRequest,
    ) -> main_models.Mobile3MetaDetailStandardVerifyResponse:
        runtime = RuntimeOptions()
        return await self.mobile_3meta_detail_standard_verify_with_options_async(request, runtime)

    def mobile_3meta_detail_verify_with_options(
        self,
        request: main_models.Mobile3MetaDetailVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Mobile3MetaDetailVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Mobile3MetaDetailVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Mobile3MetaDetailVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_3meta_detail_verify_with_options_async(
        self,
        request: main_models.Mobile3MetaDetailVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Mobile3MetaDetailVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Mobile3MetaDetailVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Mobile3MetaDetailVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_3meta_detail_verify(
        self,
        request: main_models.Mobile3MetaDetailVerifyRequest,
    ) -> main_models.Mobile3MetaDetailVerifyResponse:
        runtime = RuntimeOptions()
        return self.mobile_3meta_detail_verify_with_options(request, runtime)

    async def mobile_3meta_detail_verify_async(
        self,
        request: main_models.Mobile3MetaDetailVerifyRequest,
    ) -> main_models.Mobile3MetaDetailVerifyResponse:
        runtime = RuntimeOptions()
        return await self.mobile_3meta_detail_verify_with_options_async(request, runtime)

    def mobile_3meta_simple_standard_verify_with_options(
        self,
        request: main_models.Mobile3MetaSimpleStandardVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Mobile3MetaSimpleStandardVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Mobile3MetaSimpleStandardVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Mobile3MetaSimpleStandardVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_3meta_simple_standard_verify_with_options_async(
        self,
        request: main_models.Mobile3MetaSimpleStandardVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Mobile3MetaSimpleStandardVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Mobile3MetaSimpleStandardVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Mobile3MetaSimpleStandardVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_3meta_simple_standard_verify(
        self,
        request: main_models.Mobile3MetaSimpleStandardVerifyRequest,
    ) -> main_models.Mobile3MetaSimpleStandardVerifyResponse:
        runtime = RuntimeOptions()
        return self.mobile_3meta_simple_standard_verify_with_options(request, runtime)

    async def mobile_3meta_simple_standard_verify_async(
        self,
        request: main_models.Mobile3MetaSimpleStandardVerifyRequest,
    ) -> main_models.Mobile3MetaSimpleStandardVerifyResponse:
        runtime = RuntimeOptions()
        return await self.mobile_3meta_simple_standard_verify_with_options_async(request, runtime)

    def mobile_3meta_simple_verify_with_options(
        self,
        request: main_models.Mobile3MetaSimpleVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Mobile3MetaSimpleVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Mobile3MetaSimpleVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Mobile3MetaSimpleVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_3meta_simple_verify_with_options_async(
        self,
        request: main_models.Mobile3MetaSimpleVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Mobile3MetaSimpleVerifyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Mobile3MetaSimpleVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Mobile3MetaSimpleVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_3meta_simple_verify(
        self,
        request: main_models.Mobile3MetaSimpleVerifyRequest,
    ) -> main_models.Mobile3MetaSimpleVerifyResponse:
        runtime = RuntimeOptions()
        return self.mobile_3meta_simple_verify_with_options(request, runtime)

    async def mobile_3meta_simple_verify_async(
        self,
        request: main_models.Mobile3MetaSimpleVerifyRequest,
    ) -> main_models.Mobile3MetaSimpleVerifyResponse:
        runtime = RuntimeOptions()
        return await self.mobile_3meta_simple_verify_with_options_async(request, runtime)

    def mobile_detect_with_options(
        self,
        request: main_models.MobileDetectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MobileDetectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.mobiles):
            body['Mobiles'] = request.mobiles
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MobileDetect',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MobileDetectResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_detect_with_options_async(
        self,
        request: main_models.MobileDetectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MobileDetectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.mobiles):
            body['Mobiles'] = request.mobiles
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MobileDetect',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MobileDetectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_detect(
        self,
        request: main_models.MobileDetectRequest,
    ) -> main_models.MobileDetectResponse:
        runtime = RuntimeOptions()
        return self.mobile_detect_with_options(request, runtime)

    async def mobile_detect_async(
        self,
        request: main_models.MobileDetectRequest,
    ) -> main_models.MobileDetectResponse:
        runtime = RuntimeOptions()
        return await self.mobile_detect_with_options_async(request, runtime)

    def mobile_online_status_with_options(
        self,
        request: main_models.MobileOnlineStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MobileOnlineStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MobileOnlineStatus',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MobileOnlineStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_online_status_with_options_async(
        self,
        request: main_models.MobileOnlineStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MobileOnlineStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MobileOnlineStatus',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MobileOnlineStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_online_status(
        self,
        request: main_models.MobileOnlineStatusRequest,
    ) -> main_models.MobileOnlineStatusResponse:
        runtime = RuntimeOptions()
        return self.mobile_online_status_with_options(request, runtime)

    async def mobile_online_status_async(
        self,
        request: main_models.MobileOnlineStatusRequest,
    ) -> main_models.MobileOnlineStatusResponse:
        runtime = RuntimeOptions()
        return await self.mobile_online_status_with_options_async(request, runtime)

    def mobile_online_time_with_options(
        self,
        request: main_models.MobileOnlineTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MobileOnlineTimeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MobileOnlineTime',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MobileOnlineTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_online_time_with_options_async(
        self,
        request: main_models.MobileOnlineTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MobileOnlineTimeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.mobile):
            body['Mobile'] = request.mobile
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MobileOnlineTime',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MobileOnlineTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_online_time(
        self,
        request: main_models.MobileOnlineTimeRequest,
    ) -> main_models.MobileOnlineTimeResponse:
        runtime = RuntimeOptions()
        return self.mobile_online_time_with_options(request, runtime)

    async def mobile_online_time_async(
        self,
        request: main_models.MobileOnlineTimeRequest,
    ) -> main_models.MobileOnlineTimeResponse:
        runtime = RuntimeOptions()
        return await self.mobile_online_time_with_options_async(request, runtime)

    def modify_black_list_strategy_with_options(
        self,
        tmp_req: main_models.ModifyBlackListStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBlackListStrategyResponse:
        tmp_req.validate()
        request = main_models.ModifyBlackListStrategyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.black_list_strategy):
            request.black_list_strategy_shrink = Utils.array_to_string_with_specified_style(tmp_req.black_list_strategy, 'BlackListStrategy', 'json')
        query = {}
        if not DaraCore.is_null(request.black_list_strategy_shrink):
            query['BlackListStrategy'] = request.black_list_strategy_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBlackListStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBlackListStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_black_list_strategy_with_options_async(
        self,
        tmp_req: main_models.ModifyBlackListStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBlackListStrategyResponse:
        tmp_req.validate()
        request = main_models.ModifyBlackListStrategyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.black_list_strategy):
            request.black_list_strategy_shrink = Utils.array_to_string_with_specified_style(tmp_req.black_list_strategy, 'BlackListStrategy', 'json')
        query = {}
        if not DaraCore.is_null(request.black_list_strategy_shrink):
            query['BlackListStrategy'] = request.black_list_strategy_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBlackListStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBlackListStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_black_list_strategy(
        self,
        request: main_models.ModifyBlackListStrategyRequest,
    ) -> main_models.ModifyBlackListStrategyResponse:
        runtime = RuntimeOptions()
        return self.modify_black_list_strategy_with_options(request, runtime)

    async def modify_black_list_strategy_async(
        self,
        request: main_models.ModifyBlackListStrategyRequest,
    ) -> main_models.ModifyBlackListStrategyResponse:
        runtime = RuntimeOptions()
        return await self.modify_black_list_strategy_with_options_async(request, runtime)

    def modify_control_strategy_with_options(
        self,
        tmp_req: main_models.ModifyControlStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyControlStrategyResponse:
        tmp_req.validate()
        request = main_models.ModifyControlStrategyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.control_strategy_list):
            request.control_strategy_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.control_strategy_list, 'ControlStrategyList', 'json')
        query = {}
        if not DaraCore.is_null(request.control_strategy_list_shrink):
            query['ControlStrategyList'] = request.control_strategy_list_shrink
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyControlStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyControlStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_control_strategy_with_options_async(
        self,
        tmp_req: main_models.ModifyControlStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyControlStrategyResponse:
        tmp_req.validate()
        request = main_models.ModifyControlStrategyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.control_strategy_list):
            request.control_strategy_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.control_strategy_list, 'ControlStrategyList', 'json')
        query = {}
        if not DaraCore.is_null(request.control_strategy_list_shrink):
            query['ControlStrategyList'] = request.control_strategy_list_shrink
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyControlStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyControlStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_control_strategy(
        self,
        request: main_models.ModifyControlStrategyRequest,
    ) -> main_models.ModifyControlStrategyResponse:
        runtime = RuntimeOptions()
        return self.modify_control_strategy_with_options(request, runtime)

    async def modify_control_strategy_async(
        self,
        request: main_models.ModifyControlStrategyRequest,
    ) -> main_models.ModifyControlStrategyResponse:
        runtime = RuntimeOptions()
        return await self.modify_control_strategy_with_options_async(request, runtime)

    def modify_customize_flow_strategy_list_with_options(
        self,
        tmp_req: main_models.ModifyCustomizeFlowStrategyListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCustomizeFlowStrategyListResponse:
        tmp_req.validate()
        request = main_models.ModifyCustomizeFlowStrategyListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.strategy_object):
            request.strategy_object_shrink = Utils.array_to_string_with_specified_style(tmp_req.strategy_object, 'StrategyObject', 'json')
        query = {}
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.strategy_object_shrink):
            query['StrategyObject'] = request.strategy_object_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCustomizeFlowStrategyList',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCustomizeFlowStrategyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_customize_flow_strategy_list_with_options_async(
        self,
        tmp_req: main_models.ModifyCustomizeFlowStrategyListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCustomizeFlowStrategyListResponse:
        tmp_req.validate()
        request = main_models.ModifyCustomizeFlowStrategyListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.strategy_object):
            request.strategy_object_shrink = Utils.array_to_string_with_specified_style(tmp_req.strategy_object, 'StrategyObject', 'json')
        query = {}
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.strategy_object_shrink):
            query['StrategyObject'] = request.strategy_object_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCustomizeFlowStrategyList',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCustomizeFlowStrategyListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_customize_flow_strategy_list(
        self,
        request: main_models.ModifyCustomizeFlowStrategyListRequest,
    ) -> main_models.ModifyCustomizeFlowStrategyListResponse:
        runtime = RuntimeOptions()
        return self.modify_customize_flow_strategy_list_with_options(request, runtime)

    async def modify_customize_flow_strategy_list_async(
        self,
        request: main_models.ModifyCustomizeFlowStrategyListRequest,
    ) -> main_models.ModifyCustomizeFlowStrategyListResponse:
        runtime = RuntimeOptions()
        return await self.modify_customize_flow_strategy_list_with_options_async(request, runtime)

    def modify_device_info_with_options(
        self,
        request: main_models.ModifyDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.expired_day):
            query['ExpiredDay'] = request.expired_day
        if not DaraCore.is_null(request.user_device_id):
            query['UserDeviceId'] = request.user_device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDeviceInfo',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_device_info_with_options_async(
        self,
        request: main_models.ModifyDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.expired_day):
            query['ExpiredDay'] = request.expired_day
        if not DaraCore.is_null(request.user_device_id):
            query['UserDeviceId'] = request.user_device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDeviceInfo',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_device_info(
        self,
        request: main_models.ModifyDeviceInfoRequest,
    ) -> main_models.ModifyDeviceInfoResponse:
        runtime = RuntimeOptions()
        return self.modify_device_info_with_options(request, runtime)

    async def modify_device_info_async(
        self,
        request: main_models.ModifyDeviceInfoRequest,
    ) -> main_models.ModifyDeviceInfoResponse:
        runtime = RuntimeOptions()
        return await self.modify_device_info_with_options_async(request, runtime)

    def page_query_white_list_setting_with_options(
        self,
        request: main_models.PageQueryWhiteListSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PageQueryWhiteListSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_no):
            query['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.valid_end_date):
            query['ValidEndDate'] = request.valid_end_date
        if not DaraCore.is_null(request.valid_start_date):
            query['ValidStartDate'] = request.valid_start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PageQueryWhiteListSetting',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PageQueryWhiteListSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def page_query_white_list_setting_with_options_async(
        self,
        request: main_models.PageQueryWhiteListSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PageQueryWhiteListSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_no):
            query['CertNo'] = request.cert_no
        if not DaraCore.is_null(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.valid_end_date):
            query['ValidEndDate'] = request.valid_end_date
        if not DaraCore.is_null(request.valid_start_date):
            query['ValidStartDate'] = request.valid_start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PageQueryWhiteListSetting',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PageQueryWhiteListSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def page_query_white_list_setting(
        self,
        request: main_models.PageQueryWhiteListSettingRequest,
    ) -> main_models.PageQueryWhiteListSettingResponse:
        runtime = RuntimeOptions()
        return self.page_query_white_list_setting_with_options(request, runtime)

    async def page_query_white_list_setting_async(
        self,
        request: main_models.PageQueryWhiteListSettingRequest,
    ) -> main_models.PageQueryWhiteListSettingResponse:
        runtime = RuntimeOptions()
        return await self.page_query_white_list_setting_with_options_async(request, runtime)

    def query_black_list_strategy_with_options(
        self,
        request: main_models.QueryBlackListStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBlackListStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBlackListStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBlackListStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_black_list_strategy_with_options_async(
        self,
        request: main_models.QueryBlackListStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBlackListStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBlackListStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBlackListStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_black_list_strategy(
        self,
        request: main_models.QueryBlackListStrategyRequest,
    ) -> main_models.QueryBlackListStrategyResponse:
        runtime = RuntimeOptions()
        return self.query_black_list_strategy_with_options(request, runtime)

    async def query_black_list_strategy_async(
        self,
        request: main_models.QueryBlackListStrategyRequest,
    ) -> main_models.QueryBlackListStrategyResponse:
        runtime = RuntimeOptions()
        return await self.query_black_list_strategy_with_options_async(request, runtime)

    def query_control_strategy_with_options(
        self,
        request: main_models.QueryControlStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryControlStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryControlStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryControlStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_control_strategy_with_options_async(
        self,
        request: main_models.QueryControlStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryControlStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryControlStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryControlStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_control_strategy(
        self,
        request: main_models.QueryControlStrategyRequest,
    ) -> main_models.QueryControlStrategyResponse:
        runtime = RuntimeOptions()
        return self.query_control_strategy_with_options(request, runtime)

    async def query_control_strategy_async(
        self,
        request: main_models.QueryControlStrategyRequest,
    ) -> main_models.QueryControlStrategyResponse:
        runtime = RuntimeOptions()
        return await self.query_control_strategy_with_options_async(request, runtime)

    def query_customize_flow_strategy_with_options(
        self,
        request: main_models.QueryCustomizeFlowStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCustomizeFlowStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCustomizeFlowStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCustomizeFlowStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_customize_flow_strategy_with_options_async(
        self,
        request: main_models.QueryCustomizeFlowStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCustomizeFlowStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCustomizeFlowStrategy',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCustomizeFlowStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_customize_flow_strategy(
        self,
        request: main_models.QueryCustomizeFlowStrategyRequest,
    ) -> main_models.QueryCustomizeFlowStrategyResponse:
        runtime = RuntimeOptions()
        return self.query_customize_flow_strategy_with_options(request, runtime)

    async def query_customize_flow_strategy_async(
        self,
        request: main_models.QueryCustomizeFlowStrategyRequest,
    ) -> main_models.QueryCustomizeFlowStrategyResponse:
        runtime = RuntimeOptions()
        return await self.query_customize_flow_strategy_with_options_async(request, runtime)

    def query_scene_configs_with_options(
        self,
        request: main_models.QuerySceneConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySceneConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySceneConfigs',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySceneConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_scene_configs_with_options_async(
        self,
        request: main_models.QuerySceneConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySceneConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySceneConfigs',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySceneConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_scene_configs(
        self,
        request: main_models.QuerySceneConfigsRequest,
    ) -> main_models.QuerySceneConfigsResponse:
        runtime = RuntimeOptions()
        return self.query_scene_configs_with_options(request, runtime)

    async def query_scene_configs_async(
        self,
        request: main_models.QuerySceneConfigsRequest,
    ) -> main_models.QuerySceneConfigsResponse:
        runtime = RuntimeOptions()
        return await self.query_scene_configs_with_options_async(request, runtime)

    def query_verify_download_task_with_options(
        self,
        request: main_models.QueryVerifyDownloadTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVerifyDownloadTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVerifyDownloadTask',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVerifyDownloadTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_verify_download_task_with_options_async(
        self,
        request: main_models.QueryVerifyDownloadTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVerifyDownloadTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVerifyDownloadTask',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVerifyDownloadTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_verify_download_task(
        self,
        request: main_models.QueryVerifyDownloadTaskRequest,
    ) -> main_models.QueryVerifyDownloadTaskResponse:
        runtime = RuntimeOptions()
        return self.query_verify_download_task_with_options(request, runtime)

    async def query_verify_download_task_async(
        self,
        request: main_models.QueryVerifyDownloadTaskRequest,
    ) -> main_models.QueryVerifyDownloadTaskResponse:
        runtime = RuntimeOptions()
        return await self.query_verify_download_task_with_options_async(request, runtime)

    def query_verify_flow_package_with_options(
        self,
        request: main_models.QueryVerifyFlowPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVerifyFlowPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVerifyFlowPackage',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVerifyFlowPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_verify_flow_package_with_options_async(
        self,
        request: main_models.QueryVerifyFlowPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVerifyFlowPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVerifyFlowPackage',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVerifyFlowPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_verify_flow_package(
        self,
        request: main_models.QueryVerifyFlowPackageRequest,
    ) -> main_models.QueryVerifyFlowPackageResponse:
        runtime = RuntimeOptions()
        return self.query_verify_flow_package_with_options(request, runtime)

    async def query_verify_flow_package_async(
        self,
        request: main_models.QueryVerifyFlowPackageRequest,
    ) -> main_models.QueryVerifyFlowPackageResponse:
        runtime = RuntimeOptions()
        return await self.query_verify_flow_package_with_options_async(request, runtime)

    def query_verify_invoke_satistic_with_options(
        self,
        request: main_models.QueryVerifyInvokeSatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVerifyInvokeSatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_program_list):
            query['ProductProgramList'] = request.product_program_list
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.scene_id_list):
            query['SceneIdList'] = request.scene_id_list
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.statistics_type):
            query['StatisticsType'] = request.statistics_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVerifyInvokeSatistic',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVerifyInvokeSatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_verify_invoke_satistic_with_options_async(
        self,
        request: main_models.QueryVerifyInvokeSatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVerifyInvokeSatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_program_list):
            query['ProductProgramList'] = request.product_program_list
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.scene_id_list):
            query['SceneIdList'] = request.scene_id_list
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.statistics_type):
            query['StatisticsType'] = request.statistics_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVerifyInvokeSatistic',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVerifyInvokeSatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_verify_invoke_satistic(
        self,
        request: main_models.QueryVerifyInvokeSatisticRequest,
    ) -> main_models.QueryVerifyInvokeSatisticResponse:
        runtime = RuntimeOptions()
        return self.query_verify_invoke_satistic_with_options(request, runtime)

    async def query_verify_invoke_satistic_async(
        self,
        request: main_models.QueryVerifyInvokeSatisticRequest,
    ) -> main_models.QueryVerifyInvokeSatisticResponse:
        runtime = RuntimeOptions()
        return await self.query_verify_invoke_satistic_with_options_async(request, runtime)

    def remove_white_list_setting_with_options(
        self,
        tmp_req: main_models.RemoveWhiteListSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveWhiteListSettingResponse:
        tmp_req.validate()
        request = main_models.RemoveWhiteListSettingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not DaraCore.is_null(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveWhiteListSetting',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveWhiteListSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_white_list_setting_with_options_async(
        self,
        tmp_req: main_models.RemoveWhiteListSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveWhiteListSettingResponse:
        tmp_req.validate()
        request = main_models.RemoveWhiteListSettingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not DaraCore.is_null(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveWhiteListSetting',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveWhiteListSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_white_list_setting(
        self,
        request: main_models.RemoveWhiteListSettingRequest,
    ) -> main_models.RemoveWhiteListSettingResponse:
        runtime = RuntimeOptions()
        return self.remove_white_list_setting_with_options(request, runtime)

    async def remove_white_list_setting_async(
        self,
        request: main_models.RemoveWhiteListSettingRequest,
    ) -> main_models.RemoveWhiteListSettingResponse:
        runtime = RuntimeOptions()
        return await self.remove_white_list_setting_with_options_async(request, runtime)

    def update_ant_cloud_auth_scene_with_options(
        self,
        request: main_models.UpdateAntCloudAuthSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAntCloudAuthSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_mini_program):
            query['BindMiniProgram'] = request.bind_mini_program
        if not DaraCore.is_null(request.check_file_body):
            query['CheckFileBody'] = request.check_file_body
        if not DaraCore.is_null(request.check_file_name):
            query['CheckFileName'] = request.check_file_name
        if not DaraCore.is_null(request.mini_program_name):
            query['MiniProgramName'] = request.mini_program_name
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.return_pic_count):
            query['ReturnPicCount'] = request.return_pic_count
        if not DaraCore.is_null(request.return_video_length):
            query['ReturnVideoLength'] = request.return_video_length
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.scene_name):
            query['SceneName'] = request.scene_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.store_image):
            query['StoreImage'] = request.store_image
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAntCloudAuthScene',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAntCloudAuthSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ant_cloud_auth_scene_with_options_async(
        self,
        request: main_models.UpdateAntCloudAuthSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAntCloudAuthSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_mini_program):
            query['BindMiniProgram'] = request.bind_mini_program
        if not DaraCore.is_null(request.check_file_body):
            query['CheckFileBody'] = request.check_file_body
        if not DaraCore.is_null(request.check_file_name):
            query['CheckFileName'] = request.check_file_name
        if not DaraCore.is_null(request.mini_program_name):
            query['MiniProgramName'] = request.mini_program_name
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.return_pic_count):
            query['ReturnPicCount'] = request.return_pic_count
        if not DaraCore.is_null(request.return_video_length):
            query['ReturnVideoLength'] = request.return_video_length
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.scene_name):
            query['SceneName'] = request.scene_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.store_image):
            query['StoreImage'] = request.store_image
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAntCloudAuthScene',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAntCloudAuthSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ant_cloud_auth_scene(
        self,
        request: main_models.UpdateAntCloudAuthSceneRequest,
    ) -> main_models.UpdateAntCloudAuthSceneResponse:
        runtime = RuntimeOptions()
        return self.update_ant_cloud_auth_scene_with_options(request, runtime)

    async def update_ant_cloud_auth_scene_async(
        self,
        request: main_models.UpdateAntCloudAuthSceneRequest,
    ) -> main_models.UpdateAntCloudAuthSceneResponse:
        runtime = RuntimeOptions()
        return await self.update_ant_cloud_auth_scene_with_options_async(request, runtime)

    def update_scene_config_with_options(
        self,
        request: main_models.UpdateSceneConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSceneConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.scene_id):
            body['sceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSceneConfig',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSceneConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scene_config_with_options_async(
        self,
        request: main_models.UpdateSceneConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSceneConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.scene_id):
            body['sceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSceneConfig',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSceneConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scene_config(
        self,
        request: main_models.UpdateSceneConfigRequest,
    ) -> main_models.UpdateSceneConfigResponse:
        runtime = RuntimeOptions()
        return self.update_scene_config_with_options(request, runtime)

    async def update_scene_config_async(
        self,
        request: main_models.UpdateSceneConfigRequest,
    ) -> main_models.UpdateSceneConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_scene_config_with_options_async(request, runtime)

    def vehicle_5item_query_with_options(
        self,
        request: main_models.Vehicle5ItemQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Vehicle5ItemQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not DaraCore.is_null(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Vehicle5ItemQuery',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Vehicle5ItemQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def vehicle_5item_query_with_options_async(
        self,
        request: main_models.Vehicle5ItemQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.Vehicle5ItemQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not DaraCore.is_null(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Vehicle5ItemQuery',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Vehicle5ItemQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vehicle_5item_query(
        self,
        request: main_models.Vehicle5ItemQueryRequest,
    ) -> main_models.Vehicle5ItemQueryResponse:
        runtime = RuntimeOptions()
        return self.vehicle_5item_query_with_options(request, runtime)

    async def vehicle_5item_query_async(
        self,
        request: main_models.Vehicle5ItemQueryRequest,
    ) -> main_models.Vehicle5ItemQueryResponse:
        runtime = RuntimeOptions()
        return await self.vehicle_5item_query_with_options_async(request, runtime)

    def vehicle_insure_query_with_options(
        self,
        request: main_models.VehicleInsureQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VehicleInsureQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not DaraCore.is_null(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        if not DaraCore.is_null(request.vin):
            query['Vin'] = request.vin
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VehicleInsureQuery',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VehicleInsureQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def vehicle_insure_query_with_options_async(
        self,
        request: main_models.VehicleInsureQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VehicleInsureQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not DaraCore.is_null(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        if not DaraCore.is_null(request.vin):
            query['Vin'] = request.vin
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VehicleInsureQuery',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VehicleInsureQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vehicle_insure_query(
        self,
        request: main_models.VehicleInsureQueryRequest,
    ) -> main_models.VehicleInsureQueryResponse:
        runtime = RuntimeOptions()
        return self.vehicle_insure_query_with_options(request, runtime)

    async def vehicle_insure_query_async(
        self,
        request: main_models.VehicleInsureQueryRequest,
    ) -> main_models.VehicleInsureQueryResponse:
        runtime = RuntimeOptions()
        return await self.vehicle_insure_query_with_options_async(request, runtime)

    def vehicle_meta_verify_with_options(
        self,
        request: main_models.VehicleMetaVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VehicleMetaVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not DaraCore.is_null(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        if not DaraCore.is_null(request.verify_meta_type):
            query['VerifyMetaType'] = request.verify_meta_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VehicleMetaVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VehicleMetaVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def vehicle_meta_verify_with_options_async(
        self,
        request: main_models.VehicleMetaVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VehicleMetaVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not DaraCore.is_null(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        if not DaraCore.is_null(request.verify_meta_type):
            query['VerifyMetaType'] = request.verify_meta_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VehicleMetaVerify',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VehicleMetaVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vehicle_meta_verify(
        self,
        request: main_models.VehicleMetaVerifyRequest,
    ) -> main_models.VehicleMetaVerifyResponse:
        runtime = RuntimeOptions()
        return self.vehicle_meta_verify_with_options(request, runtime)

    async def vehicle_meta_verify_async(
        self,
        request: main_models.VehicleMetaVerifyRequest,
    ) -> main_models.VehicleMetaVerifyResponse:
        runtime = RuntimeOptions()
        return await self.vehicle_meta_verify_with_options_async(request, runtime)

    def vehicle_meta_verify_v2with_options(
        self,
        request: main_models.VehicleMetaVerifyV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.VehicleMetaVerifyV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not DaraCore.is_null(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        if not DaraCore.is_null(request.verify_meta_type):
            query['VerifyMetaType'] = request.verify_meta_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VehicleMetaVerifyV2',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VehicleMetaVerifyV2Response(),
            self.call_api(params, req, runtime)
        )

    async def vehicle_meta_verify_v2with_options_async(
        self,
        request: main_models.VehicleMetaVerifyV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.VehicleMetaVerifyV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not DaraCore.is_null(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        if not DaraCore.is_null(request.verify_meta_type):
            query['VerifyMetaType'] = request.verify_meta_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VehicleMetaVerifyV2',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VehicleMetaVerifyV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def vehicle_meta_verify_v2(
        self,
        request: main_models.VehicleMetaVerifyV2Request,
    ) -> main_models.VehicleMetaVerifyV2Response:
        runtime = RuntimeOptions()
        return self.vehicle_meta_verify_v2with_options(request, runtime)

    async def vehicle_meta_verify_v2_async(
        self,
        request: main_models.VehicleMetaVerifyV2Request,
    ) -> main_models.VehicleMetaVerifyV2Response:
        runtime = RuntimeOptions()
        return await self.vehicle_meta_verify_v2with_options_async(request, runtime)

    def vehicle_query_with_options(
        self,
        request: main_models.VehicleQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VehicleQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not DaraCore.is_null(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VehicleQuery',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VehicleQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def vehicle_query_with_options_async(
        self,
        request: main_models.VehicleQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VehicleQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param_type):
            query['ParamType'] = request.param_type
        if not DaraCore.is_null(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not DaraCore.is_null(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VehicleQuery',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VehicleQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vehicle_query(
        self,
        request: main_models.VehicleQueryRequest,
    ) -> main_models.VehicleQueryResponse:
        runtime = RuntimeOptions()
        return self.vehicle_query_with_options(request, runtime)

    async def vehicle_query_async(
        self,
        request: main_models.VehicleQueryRequest,
    ) -> main_models.VehicleQueryResponse:
        runtime = RuntimeOptions()
        return await self.vehicle_query_with_options_async(request, runtime)

    def verify_material_with_options(
        self,
        request: main_models.VerifyMaterialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyMaterialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.face_image_url):
            query['FaceImageUrl'] = request.face_image_url
        if not DaraCore.is_null(request.id_card_back_image_url):
            query['IdCardBackImageUrl'] = request.id_card_back_image_url
        if not DaraCore.is_null(request.id_card_front_image_url):
            query['IdCardFrontImageUrl'] = request.id_card_front_image_url
        if not DaraCore.is_null(request.id_card_number):
            query['IdCardNumber'] = request.id_card_number
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyMaterial',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_material_with_options_async(
        self,
        request: main_models.VerifyMaterialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyMaterialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.face_image_url):
            query['FaceImageUrl'] = request.face_image_url
        if not DaraCore.is_null(request.id_card_back_image_url):
            query['IdCardBackImageUrl'] = request.id_card_back_image_url
        if not DaraCore.is_null(request.id_card_front_image_url):
            query['IdCardFrontImageUrl'] = request.id_card_front_image_url
        if not DaraCore.is_null(request.id_card_number):
            query['IdCardNumber'] = request.id_card_number
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyMaterial',
            version = '2019-03-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyMaterialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_material(
        self,
        request: main_models.VerifyMaterialRequest,
    ) -> main_models.VerifyMaterialResponse:
        runtime = RuntimeOptions()
        return self.verify_material_with_options(request, runtime)

    async def verify_material_async(
        self,
        request: main_models.VerifyMaterialRequest,
    ) -> main_models.VerifyMaterialResponse:
        runtime = RuntimeOptions()
        return await self.verify_material_with_options_async(request, runtime)
