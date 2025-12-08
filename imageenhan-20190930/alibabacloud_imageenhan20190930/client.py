# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import time

from Tea.request import TeaRequest
from Tea.exceptions import TeaException, UnretryableException
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_fileform.client import Client as FileFormClient
from alibabacloud_tea_xml.client import Client as XMLClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imageenhan20190930 import models as imageenhan_20190930_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_tea_fileform import models as file_form_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('imageenhan', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def _post_ossobject(
        self,
        bucket_name: str,
        data: dict,
        runtime: util_models.RuntimeOptions,
    ) -> dict:
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'key': UtilClient.default_string(runtime.key, self._key),
            'cert': UtilClient.default_string(runtime.cert, self._cert),
            'ca': UtilClient.default_string(runtime.ca, self._ca),
            'readTimeout': UtilClient.default_number(runtime.read_timeout, self._read_timeout),
            'connectTimeout': UtilClient.default_number(runtime.connect_timeout, self._connect_timeout),
            'httpProxy': UtilClient.default_string(runtime.http_proxy, self._http_proxy),
            'httpsProxy': UtilClient.default_string(runtime.https_proxy, self._https_proxy),
            'noProxy': UtilClient.default_string(runtime.no_proxy, self._no_proxy),
            'socks5Proxy': UtilClient.default_string(runtime.socks_5proxy, self._socks_5proxy),
            'socks5NetWork': UtilClient.default_string(runtime.socks_5net_work, self._socks_5net_work),
            'maxIdleConns': UtilClient.default_number(runtime.max_idle_conns, self._max_idle_conns),
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': OpenApiClient.default_any(runtime.ignore_ssl, False),
            'tlsMinVersion': self._tls_min_version
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                form = UtilClient.assert_as_map(data)
                boundary = FileFormClient.get_boundary()
                host = UtilClient.assert_as_string(form.get('host'))
                _request.protocol = 'HTTPS'
                _request.method = 'POST'
                _request.pathname = f'/'
                _request.headers = {
                    'host': host,
                    'date': UtilClient.get_date_utcstring(),
                    'user-agent': UtilClient.get_user_agent('')
                }
                _request.headers['content-type'] = f'multipart/form-data; boundary={boundary}'
                _request.body = FileFormClient.to_file_form(form, boundary)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                resp_map = None
                body_str = UtilClient.read_as_string(_response.body)
                if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
                    resp_map = XMLClient.parse_xml(body_str, None)
                    err = UtilClient.assert_as_map(resp_map.get('Error'))
                    raise TeaException({
                        'code': err.get('Code'),
                        'message': err.get('Message'),
                        'data': {
                            'httpCode': _response.status_code,
                            'requestId': err.get('RequestId'),
                            'hostId': err.get('HostId')
                        }
                    })
                resp_map = XMLClient.parse_xml(body_str, None)
                return TeaCore.merge(resp_map)
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def _post_ossobject_async(
        self,
        bucket_name: str,
        data: dict,
        runtime: util_models.RuntimeOptions,
    ) -> dict:
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'key': UtilClient.default_string(runtime.key, self._key),
            'cert': UtilClient.default_string(runtime.cert, self._cert),
            'ca': UtilClient.default_string(runtime.ca, self._ca),
            'readTimeout': UtilClient.default_number(runtime.read_timeout, self._read_timeout),
            'connectTimeout': UtilClient.default_number(runtime.connect_timeout, self._connect_timeout),
            'httpProxy': UtilClient.default_string(runtime.http_proxy, self._http_proxy),
            'httpsProxy': UtilClient.default_string(runtime.https_proxy, self._https_proxy),
            'noProxy': UtilClient.default_string(runtime.no_proxy, self._no_proxy),
            'socks5Proxy': UtilClient.default_string(runtime.socks_5proxy, self._socks_5proxy),
            'socks5NetWork': UtilClient.default_string(runtime.socks_5net_work, self._socks_5net_work),
            'maxIdleConns': UtilClient.default_number(runtime.max_idle_conns, self._max_idle_conns),
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': OpenApiClient.default_any(runtime.ignore_ssl, False),
            'tlsMinVersion': self._tls_min_version
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                form = UtilClient.assert_as_map(data)
                boundary = FileFormClient.get_boundary()
                host = UtilClient.assert_as_string(form.get('host'))
                _request.protocol = 'HTTPS'
                _request.method = 'POST'
                _request.pathname = f'/'
                _request.headers = {
                    'host': host,
                    'date': UtilClient.get_date_utcstring(),
                    'user-agent': UtilClient.get_user_agent('')
                }
                _request.headers['content-type'] = f'multipart/form-data; boundary={boundary}'
                _request.body = FileFormClient.to_file_form(form, boundary)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                resp_map = None
                body_str = await UtilClient.read_as_string_async(_response.body)
                if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
                    resp_map = XMLClient.parse_xml(body_str, None)
                    err = UtilClient.assert_as_map(resp_map.get('Error'))
                    raise TeaException({
                        'code': err.get('Code'),
                        'message': err.get('Message'),
                        'data': {
                            'httpCode': _response.status_code,
                            'requestId': err.get('RequestId'),
                            'hostId': err.get('HostId')
                        }
                    })
                resp_map = XMLClient.parse_xml(body_str, None)
                return TeaCore.merge(resp_map)
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def assess_composition_with_options(
        self,
        request: imageenhan_20190930_models.AssessCompositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.AssessCompositionResponse:
        """
        @param request: AssessCompositionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssessCompositionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssessComposition',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.AssessCompositionResponse(),
            self.call_api(params, req, runtime)
        )

    async def assess_composition_with_options_async(
        self,
        request: imageenhan_20190930_models.AssessCompositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.AssessCompositionResponse:
        """
        @param request: AssessCompositionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssessCompositionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssessComposition',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.AssessCompositionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assess_composition(
        self,
        request: imageenhan_20190930_models.AssessCompositionRequest,
    ) -> imageenhan_20190930_models.AssessCompositionResponse:
        """
        @param request: AssessCompositionRequest
        @return: AssessCompositionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.assess_composition_with_options(request, runtime)

    async def assess_composition_async(
        self,
        request: imageenhan_20190930_models.AssessCompositionRequest,
    ) -> imageenhan_20190930_models.AssessCompositionResponse:
        """
        @param request: AssessCompositionRequest
        @return: AssessCompositionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.assess_composition_with_options_async(request, runtime)

    def assess_composition_advance(
        self,
        request: imageenhan_20190930_models.AssessCompositionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.AssessCompositionResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        assess_composition_req = imageenhan_20190930_models.AssessCompositionRequest()
        OpenApiUtilClient.convert(request, assess_composition_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            assess_composition_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        assess_composition_resp = self.assess_composition_with_options(assess_composition_req, runtime)
        return assess_composition_resp

    async def assess_composition_advance_async(
        self,
        request: imageenhan_20190930_models.AssessCompositionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.AssessCompositionResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        assess_composition_req = imageenhan_20190930_models.AssessCompositionRequest()
        OpenApiUtilClient.convert(request, assess_composition_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            assess_composition_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        assess_composition_resp = await self.assess_composition_with_options_async(assess_composition_req, runtime)
        return assess_composition_resp

    def assess_exposure_with_options(
        self,
        request: imageenhan_20190930_models.AssessExposureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.AssessExposureResponse:
        """
        @param request: AssessExposureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssessExposureResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssessExposure',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.AssessExposureResponse(),
            self.call_api(params, req, runtime)
        )

    async def assess_exposure_with_options_async(
        self,
        request: imageenhan_20190930_models.AssessExposureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.AssessExposureResponse:
        """
        @param request: AssessExposureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssessExposureResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssessExposure',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.AssessExposureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assess_exposure(
        self,
        request: imageenhan_20190930_models.AssessExposureRequest,
    ) -> imageenhan_20190930_models.AssessExposureResponse:
        """
        @param request: AssessExposureRequest
        @return: AssessExposureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.assess_exposure_with_options(request, runtime)

    async def assess_exposure_async(
        self,
        request: imageenhan_20190930_models.AssessExposureRequest,
    ) -> imageenhan_20190930_models.AssessExposureResponse:
        """
        @param request: AssessExposureRequest
        @return: AssessExposureResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.assess_exposure_with_options_async(request, runtime)

    def assess_exposure_advance(
        self,
        request: imageenhan_20190930_models.AssessExposureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.AssessExposureResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        assess_exposure_req = imageenhan_20190930_models.AssessExposureRequest()
        OpenApiUtilClient.convert(request, assess_exposure_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            assess_exposure_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        assess_exposure_resp = self.assess_exposure_with_options(assess_exposure_req, runtime)
        return assess_exposure_resp

    async def assess_exposure_advance_async(
        self,
        request: imageenhan_20190930_models.AssessExposureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.AssessExposureResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        assess_exposure_req = imageenhan_20190930_models.AssessExposureRequest()
        OpenApiUtilClient.convert(request, assess_exposure_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            assess_exposure_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        assess_exposure_resp = await self.assess_exposure_with_options_async(assess_exposure_req, runtime)
        return assess_exposure_resp

    def assess_sharpness_with_options(
        self,
        request: imageenhan_20190930_models.AssessSharpnessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.AssessSharpnessResponse:
        """
        @param request: AssessSharpnessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssessSharpnessResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssessSharpness',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.AssessSharpnessResponse(),
            self.call_api(params, req, runtime)
        )

    async def assess_sharpness_with_options_async(
        self,
        request: imageenhan_20190930_models.AssessSharpnessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.AssessSharpnessResponse:
        """
        @param request: AssessSharpnessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssessSharpnessResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssessSharpness',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.AssessSharpnessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assess_sharpness(
        self,
        request: imageenhan_20190930_models.AssessSharpnessRequest,
    ) -> imageenhan_20190930_models.AssessSharpnessResponse:
        """
        @param request: AssessSharpnessRequest
        @return: AssessSharpnessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.assess_sharpness_with_options(request, runtime)

    async def assess_sharpness_async(
        self,
        request: imageenhan_20190930_models.AssessSharpnessRequest,
    ) -> imageenhan_20190930_models.AssessSharpnessResponse:
        """
        @param request: AssessSharpnessRequest
        @return: AssessSharpnessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.assess_sharpness_with_options_async(request, runtime)

    def assess_sharpness_advance(
        self,
        request: imageenhan_20190930_models.AssessSharpnessAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.AssessSharpnessResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        assess_sharpness_req = imageenhan_20190930_models.AssessSharpnessRequest()
        OpenApiUtilClient.convert(request, assess_sharpness_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            assess_sharpness_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        assess_sharpness_resp = self.assess_sharpness_with_options(assess_sharpness_req, runtime)
        return assess_sharpness_resp

    async def assess_sharpness_advance_async(
        self,
        request: imageenhan_20190930_models.AssessSharpnessAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.AssessSharpnessResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        assess_sharpness_req = imageenhan_20190930_models.AssessSharpnessRequest()
        OpenApiUtilClient.convert(request, assess_sharpness_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            assess_sharpness_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        assess_sharpness_resp = await self.assess_sharpness_with_options_async(assess_sharpness_req, runtime)
        return assess_sharpness_resp

    def change_image_size_with_options(
        self,
        request: imageenhan_20190930_models.ChangeImageSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ChangeImageSizeResponse:
        """
        @param request: ChangeImageSizeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeImageSizeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        if not UtilClient.is_unset(request.width):
            body['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeImageSize',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.ChangeImageSizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_image_size_with_options_async(
        self,
        request: imageenhan_20190930_models.ChangeImageSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ChangeImageSizeResponse:
        """
        @param request: ChangeImageSizeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeImageSizeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        if not UtilClient.is_unset(request.width):
            body['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeImageSize',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.ChangeImageSizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_image_size(
        self,
        request: imageenhan_20190930_models.ChangeImageSizeRequest,
    ) -> imageenhan_20190930_models.ChangeImageSizeResponse:
        """
        @param request: ChangeImageSizeRequest
        @return: ChangeImageSizeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_image_size_with_options(request, runtime)

    async def change_image_size_async(
        self,
        request: imageenhan_20190930_models.ChangeImageSizeRequest,
    ) -> imageenhan_20190930_models.ChangeImageSizeResponse:
        """
        @param request: ChangeImageSizeRequest
        @return: ChangeImageSizeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_image_size_with_options_async(request, runtime)

    def change_image_size_advance(
        self,
        request: imageenhan_20190930_models.ChangeImageSizeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ChangeImageSizeResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        change_image_size_req = imageenhan_20190930_models.ChangeImageSizeRequest()
        OpenApiUtilClient.convert(request, change_image_size_req)
        if not UtilClient.is_unset(request.url_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            change_image_size_req.url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        change_image_size_resp = self.change_image_size_with_options(change_image_size_req, runtime)
        return change_image_size_resp

    async def change_image_size_advance_async(
        self,
        request: imageenhan_20190930_models.ChangeImageSizeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ChangeImageSizeResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        change_image_size_req = imageenhan_20190930_models.ChangeImageSizeRequest()
        OpenApiUtilClient.convert(request, change_image_size_req)
        if not UtilClient.is_unset(request.url_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            change_image_size_req.url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        change_image_size_resp = await self.change_image_size_with_options_async(change_image_size_req, runtime)
        return change_image_size_resp

    def colorize_image_with_options(
        self,
        request: imageenhan_20190930_models.ColorizeImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ColorizeImageResponse:
        """
        @param request: ColorizeImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ColorizeImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ColorizeImage',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.ColorizeImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def colorize_image_with_options_async(
        self,
        request: imageenhan_20190930_models.ColorizeImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ColorizeImageResponse:
        """
        @param request: ColorizeImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ColorizeImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ColorizeImage',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.ColorizeImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def colorize_image(
        self,
        request: imageenhan_20190930_models.ColorizeImageRequest,
    ) -> imageenhan_20190930_models.ColorizeImageResponse:
        """
        @param request: ColorizeImageRequest
        @return: ColorizeImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.colorize_image_with_options(request, runtime)

    async def colorize_image_async(
        self,
        request: imageenhan_20190930_models.ColorizeImageRequest,
    ) -> imageenhan_20190930_models.ColorizeImageResponse:
        """
        @param request: ColorizeImageRequest
        @return: ColorizeImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.colorize_image_with_options_async(request, runtime)

    def colorize_image_advance(
        self,
        request: imageenhan_20190930_models.ColorizeImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ColorizeImageResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        colorize_image_req = imageenhan_20190930_models.ColorizeImageRequest()
        OpenApiUtilClient.convert(request, colorize_image_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            colorize_image_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        colorize_image_resp = self.colorize_image_with_options(colorize_image_req, runtime)
        return colorize_image_resp

    async def colorize_image_advance_async(
        self,
        request: imageenhan_20190930_models.ColorizeImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ColorizeImageResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        colorize_image_req = imageenhan_20190930_models.ColorizeImageRequest()
        OpenApiUtilClient.convert(request, colorize_image_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            colorize_image_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        colorize_image_resp = await self.colorize_image_with_options_async(colorize_image_req, runtime)
        return colorize_image_resp

    def enhance_image_color_with_options(
        self,
        request: imageenhan_20190930_models.EnhanceImageColorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.EnhanceImageColorResponse:
        """
        @param request: EnhanceImageColorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnhanceImageColorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.output_format):
            body['OutputFormat'] = request.output_format
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnhanceImageColor',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.EnhanceImageColorResponse(),
            self.call_api(params, req, runtime)
        )

    async def enhance_image_color_with_options_async(
        self,
        request: imageenhan_20190930_models.EnhanceImageColorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.EnhanceImageColorResponse:
        """
        @param request: EnhanceImageColorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnhanceImageColorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.output_format):
            body['OutputFormat'] = request.output_format
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnhanceImageColor',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.EnhanceImageColorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enhance_image_color(
        self,
        request: imageenhan_20190930_models.EnhanceImageColorRequest,
    ) -> imageenhan_20190930_models.EnhanceImageColorResponse:
        """
        @param request: EnhanceImageColorRequest
        @return: EnhanceImageColorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enhance_image_color_with_options(request, runtime)

    async def enhance_image_color_async(
        self,
        request: imageenhan_20190930_models.EnhanceImageColorRequest,
    ) -> imageenhan_20190930_models.EnhanceImageColorResponse:
        """
        @param request: EnhanceImageColorRequest
        @return: EnhanceImageColorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enhance_image_color_with_options_async(request, runtime)

    def enhance_image_color_advance(
        self,
        request: imageenhan_20190930_models.EnhanceImageColorAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.EnhanceImageColorResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        enhance_image_color_req = imageenhan_20190930_models.EnhanceImageColorRequest()
        OpenApiUtilClient.convert(request, enhance_image_color_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            enhance_image_color_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        enhance_image_color_resp = self.enhance_image_color_with_options(enhance_image_color_req, runtime)
        return enhance_image_color_resp

    async def enhance_image_color_advance_async(
        self,
        request: imageenhan_20190930_models.EnhanceImageColorAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.EnhanceImageColorResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        enhance_image_color_req = imageenhan_20190930_models.EnhanceImageColorRequest()
        OpenApiUtilClient.convert(request, enhance_image_color_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            enhance_image_color_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        enhance_image_color_resp = await self.enhance_image_color_with_options_async(enhance_image_color_req, runtime)
        return enhance_image_color_resp

    def erase_person_with_options(
        self,
        request: imageenhan_20190930_models.ErasePersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ErasePersonResponse:
        """
        @param request: ErasePersonRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ErasePersonResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.user_mask):
            body['UserMask'] = request.user_mask
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ErasePerson',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.ErasePersonResponse(),
            self.call_api(params, req, runtime)
        )

    async def erase_person_with_options_async(
        self,
        request: imageenhan_20190930_models.ErasePersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ErasePersonResponse:
        """
        @param request: ErasePersonRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ErasePersonResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.user_mask):
            body['UserMask'] = request.user_mask
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ErasePerson',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.ErasePersonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def erase_person(
        self,
        request: imageenhan_20190930_models.ErasePersonRequest,
    ) -> imageenhan_20190930_models.ErasePersonResponse:
        """
        @param request: ErasePersonRequest
        @return: ErasePersonResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.erase_person_with_options(request, runtime)

    async def erase_person_async(
        self,
        request: imageenhan_20190930_models.ErasePersonRequest,
    ) -> imageenhan_20190930_models.ErasePersonResponse:
        """
        @param request: ErasePersonRequest
        @return: ErasePersonResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.erase_person_with_options_async(request, runtime)

    def erase_person_advance(
        self,
        request: imageenhan_20190930_models.ErasePersonAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ErasePersonResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        erase_person_req = imageenhan_20190930_models.ErasePersonRequest()
        OpenApiUtilClient.convert(request, erase_person_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            erase_person_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.user_mask_object):
            tmp_resp_1 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.user_mask_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            erase_person_req.user_mask = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        erase_person_resp = self.erase_person_with_options(erase_person_req, runtime)
        return erase_person_resp

    async def erase_person_advance_async(
        self,
        request: imageenhan_20190930_models.ErasePersonAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ErasePersonResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        erase_person_req = imageenhan_20190930_models.ErasePersonRequest()
        OpenApiUtilClient.convert(request, erase_person_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            erase_person_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.user_mask_object):
            tmp_resp_1 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.user_mask_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            erase_person_req.user_mask = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        erase_person_resp = await self.erase_person_with_options_async(erase_person_req, runtime)
        return erase_person_resp

    def extend_image_style_with_options(
        self,
        request: imageenhan_20190930_models.ExtendImageStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ExtendImageStyleResponse:
        """
        @param request: ExtendImageStyleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExtendImageStyleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.major_url):
            body['MajorUrl'] = request.major_url
        if not UtilClient.is_unset(request.style_url):
            body['StyleUrl'] = request.style_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtendImageStyle',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.ExtendImageStyleResponse(),
            self.call_api(params, req, runtime)
        )

    async def extend_image_style_with_options_async(
        self,
        request: imageenhan_20190930_models.ExtendImageStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ExtendImageStyleResponse:
        """
        @param request: ExtendImageStyleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExtendImageStyleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.major_url):
            body['MajorUrl'] = request.major_url
        if not UtilClient.is_unset(request.style_url):
            body['StyleUrl'] = request.style_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtendImageStyle',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.ExtendImageStyleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def extend_image_style(
        self,
        request: imageenhan_20190930_models.ExtendImageStyleRequest,
    ) -> imageenhan_20190930_models.ExtendImageStyleResponse:
        """
        @param request: ExtendImageStyleRequest
        @return: ExtendImageStyleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.extend_image_style_with_options(request, runtime)

    async def extend_image_style_async(
        self,
        request: imageenhan_20190930_models.ExtendImageStyleRequest,
    ) -> imageenhan_20190930_models.ExtendImageStyleResponse:
        """
        @param request: ExtendImageStyleRequest
        @return: ExtendImageStyleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.extend_image_style_with_options_async(request, runtime)

    def extend_image_style_advance(
        self,
        request: imageenhan_20190930_models.ExtendImageStyleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ExtendImageStyleResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        extend_image_style_req = imageenhan_20190930_models.ExtendImageStyleRequest()
        OpenApiUtilClient.convert(request, extend_image_style_req)
        if not UtilClient.is_unset(request.major_url_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.major_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            extend_image_style_req.major_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.style_url_object):
            tmp_resp_1 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.style_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            extend_image_style_req.style_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        extend_image_style_resp = self.extend_image_style_with_options(extend_image_style_req, runtime)
        return extend_image_style_resp

    async def extend_image_style_advance_async(
        self,
        request: imageenhan_20190930_models.ExtendImageStyleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ExtendImageStyleResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        extend_image_style_req = imageenhan_20190930_models.ExtendImageStyleRequest()
        OpenApiUtilClient.convert(request, extend_image_style_req)
        if not UtilClient.is_unset(request.major_url_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.major_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            extend_image_style_req.major_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.style_url_object):
            tmp_resp_1 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.style_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            extend_image_style_req.style_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        extend_image_style_resp = await self.extend_image_style_with_options_async(extend_image_style_req, runtime)
        return extend_image_style_resp

    def generate_cartoonized_image_with_options(
        self,
        request: imageenhan_20190930_models.GenerateCartoonizedImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.GenerateCartoonizedImageResponse:
        """
        @summary 生成式图像卡通化
        
        @param request: GenerateCartoonizedImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCartoonizedImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_type):
            body['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.index):
            body['Index'] = request.index
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateCartoonizedImage',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.GenerateCartoonizedImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_cartoonized_image_with_options_async(
        self,
        request: imageenhan_20190930_models.GenerateCartoonizedImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.GenerateCartoonizedImageResponse:
        """
        @summary 生成式图像卡通化
        
        @param request: GenerateCartoonizedImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCartoonizedImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_type):
            body['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.index):
            body['Index'] = request.index
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateCartoonizedImage',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.GenerateCartoonizedImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_cartoonized_image(
        self,
        request: imageenhan_20190930_models.GenerateCartoonizedImageRequest,
    ) -> imageenhan_20190930_models.GenerateCartoonizedImageResponse:
        """
        @summary 生成式图像卡通化
        
        @param request: GenerateCartoonizedImageRequest
        @return: GenerateCartoonizedImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_cartoonized_image_with_options(request, runtime)

    async def generate_cartoonized_image_async(
        self,
        request: imageenhan_20190930_models.GenerateCartoonizedImageRequest,
    ) -> imageenhan_20190930_models.GenerateCartoonizedImageResponse:
        """
        @summary 生成式图像卡通化
        
        @param request: GenerateCartoonizedImageRequest
        @return: GenerateCartoonizedImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_cartoonized_image_with_options_async(request, runtime)

    def generate_cartoonized_image_advance(
        self,
        request: imageenhan_20190930_models.GenerateCartoonizedImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.GenerateCartoonizedImageResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        generate_cartoonized_image_req = imageenhan_20190930_models.GenerateCartoonizedImageRequest()
        OpenApiUtilClient.convert(request, generate_cartoonized_image_req)
        if not UtilClient.is_unset(request.image_url_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            generate_cartoonized_image_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        generate_cartoonized_image_resp = self.generate_cartoonized_image_with_options(generate_cartoonized_image_req, runtime)
        return generate_cartoonized_image_resp

    async def generate_cartoonized_image_advance_async(
        self,
        request: imageenhan_20190930_models.GenerateCartoonizedImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.GenerateCartoonizedImageResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        generate_cartoonized_image_req = imageenhan_20190930_models.GenerateCartoonizedImageRequest()
        OpenApiUtilClient.convert(request, generate_cartoonized_image_req)
        if not UtilClient.is_unset(request.image_url_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            generate_cartoonized_image_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        generate_cartoonized_image_resp = await self.generate_cartoonized_image_with_options_async(generate_cartoonized_image_req, runtime)
        return generate_cartoonized_image_resp

    def generate_super_resolution_image_with_options(
        self,
        request: imageenhan_20190930_models.GenerateSuperResolutionImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.GenerateSuperResolutionImageResponse:
        """
        @summary 生成式图像超分
        
        @param request: GenerateSuperResolutionImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateSuperResolutionImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.output_format):
            body['OutputFormat'] = request.output_format
        if not UtilClient.is_unset(request.output_quality):
            body['OutputQuality'] = request.output_quality
        if not UtilClient.is_unset(request.scale):
            body['Scale'] = request.scale
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateSuperResolutionImage',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.GenerateSuperResolutionImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_super_resolution_image_with_options_async(
        self,
        request: imageenhan_20190930_models.GenerateSuperResolutionImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.GenerateSuperResolutionImageResponse:
        """
        @summary 生成式图像超分
        
        @param request: GenerateSuperResolutionImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateSuperResolutionImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.output_format):
            body['OutputFormat'] = request.output_format
        if not UtilClient.is_unset(request.output_quality):
            body['OutputQuality'] = request.output_quality
        if not UtilClient.is_unset(request.scale):
            body['Scale'] = request.scale
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateSuperResolutionImage',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.GenerateSuperResolutionImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_super_resolution_image(
        self,
        request: imageenhan_20190930_models.GenerateSuperResolutionImageRequest,
    ) -> imageenhan_20190930_models.GenerateSuperResolutionImageResponse:
        """
        @summary 生成式图像超分
        
        @param request: GenerateSuperResolutionImageRequest
        @return: GenerateSuperResolutionImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_super_resolution_image_with_options(request, runtime)

    async def generate_super_resolution_image_async(
        self,
        request: imageenhan_20190930_models.GenerateSuperResolutionImageRequest,
    ) -> imageenhan_20190930_models.GenerateSuperResolutionImageResponse:
        """
        @summary 生成式图像超分
        
        @param request: GenerateSuperResolutionImageRequest
        @return: GenerateSuperResolutionImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_super_resolution_image_with_options_async(request, runtime)

    def generate_super_resolution_image_advance(
        self,
        request: imageenhan_20190930_models.GenerateSuperResolutionImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.GenerateSuperResolutionImageResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        generate_super_resolution_image_req = imageenhan_20190930_models.GenerateSuperResolutionImageRequest()
        OpenApiUtilClient.convert(request, generate_super_resolution_image_req)
        if not UtilClient.is_unset(request.image_url_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            generate_super_resolution_image_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        generate_super_resolution_image_resp = self.generate_super_resolution_image_with_options(generate_super_resolution_image_req, runtime)
        return generate_super_resolution_image_resp

    async def generate_super_resolution_image_advance_async(
        self,
        request: imageenhan_20190930_models.GenerateSuperResolutionImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.GenerateSuperResolutionImageResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        generate_super_resolution_image_req = imageenhan_20190930_models.GenerateSuperResolutionImageRequest()
        OpenApiUtilClient.convert(request, generate_super_resolution_image_req)
        if not UtilClient.is_unset(request.image_url_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            generate_super_resolution_image_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        generate_super_resolution_image_resp = await self.generate_super_resolution_image_with_options_async(generate_super_resolution_image_req, runtime)
        return generate_super_resolution_image_resp

    def get_async_job_result_with_options(
        self,
        request: imageenhan_20190930_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.GetAsyncJobResultResponse:
        """
        @param request: GetAsyncJobResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncJobResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAsyncJobResult',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.GetAsyncJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_job_result_with_options_async(
        self,
        request: imageenhan_20190930_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.GetAsyncJobResultResponse:
        """
        @param request: GetAsyncJobResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncJobResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAsyncJobResult',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.GetAsyncJobResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_job_result(
        self,
        request: imageenhan_20190930_models.GetAsyncJobResultRequest,
    ) -> imageenhan_20190930_models.GetAsyncJobResultResponse:
        """
        @param request: GetAsyncJobResultRequest
        @return: GetAsyncJobResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result_with_options(request, runtime)

    async def get_async_job_result_async(
        self,
        request: imageenhan_20190930_models.GetAsyncJobResultRequest,
    ) -> imageenhan_20190930_models.GetAsyncJobResultResponse:
        """
        @param request: GetAsyncJobResultRequest
        @return: GetAsyncJobResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_async_job_result_with_options_async(request, runtime)

    def image_blind_character_watermark_with_options(
        self,
        request: imageenhan_20190930_models.ImageBlindCharacterWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ImageBlindCharacterWatermarkResponse:
        """
        @param request: ImageBlindCharacterWatermarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageBlindCharacterWatermarkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.function_type):
            body['FunctionType'] = request.function_type
        if not UtilClient.is_unset(request.origin_image_url):
            body['OriginImageURL'] = request.origin_image_url
        if not UtilClient.is_unset(request.output_file_type):
            body['OutputFileType'] = request.output_file_type
        if not UtilClient.is_unset(request.quality_factor):
            body['QualityFactor'] = request.quality_factor
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.watermark_image_url):
            body['WatermarkImageURL'] = request.watermark_image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImageBlindCharacterWatermark',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.ImageBlindCharacterWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_blind_character_watermark_with_options_async(
        self,
        request: imageenhan_20190930_models.ImageBlindCharacterWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ImageBlindCharacterWatermarkResponse:
        """
        @param request: ImageBlindCharacterWatermarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageBlindCharacterWatermarkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.function_type):
            body['FunctionType'] = request.function_type
        if not UtilClient.is_unset(request.origin_image_url):
            body['OriginImageURL'] = request.origin_image_url
        if not UtilClient.is_unset(request.output_file_type):
            body['OutputFileType'] = request.output_file_type
        if not UtilClient.is_unset(request.quality_factor):
            body['QualityFactor'] = request.quality_factor
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.watermark_image_url):
            body['WatermarkImageURL'] = request.watermark_image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImageBlindCharacterWatermark',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.ImageBlindCharacterWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_blind_character_watermark(
        self,
        request: imageenhan_20190930_models.ImageBlindCharacterWatermarkRequest,
    ) -> imageenhan_20190930_models.ImageBlindCharacterWatermarkResponse:
        """
        @param request: ImageBlindCharacterWatermarkRequest
        @return: ImageBlindCharacterWatermarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.image_blind_character_watermark_with_options(request, runtime)

    async def image_blind_character_watermark_async(
        self,
        request: imageenhan_20190930_models.ImageBlindCharacterWatermarkRequest,
    ) -> imageenhan_20190930_models.ImageBlindCharacterWatermarkResponse:
        """
        @param request: ImageBlindCharacterWatermarkRequest
        @return: ImageBlindCharacterWatermarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.image_blind_character_watermark_with_options_async(request, runtime)

    def image_blind_character_watermark_advance(
        self,
        request: imageenhan_20190930_models.ImageBlindCharacterWatermarkAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ImageBlindCharacterWatermarkResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        image_blind_character_watermark_req = imageenhan_20190930_models.ImageBlindCharacterWatermarkRequest()
        OpenApiUtilClient.convert(request, image_blind_character_watermark_req)
        if not UtilClient.is_unset(request.origin_image_urlobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.origin_image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            image_blind_character_watermark_req.origin_image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.watermark_image_urlobject):
            tmp_resp_1 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.watermark_image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            image_blind_character_watermark_req.watermark_image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        image_blind_character_watermark_resp = self.image_blind_character_watermark_with_options(image_blind_character_watermark_req, runtime)
        return image_blind_character_watermark_resp

    async def image_blind_character_watermark_advance_async(
        self,
        request: imageenhan_20190930_models.ImageBlindCharacterWatermarkAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ImageBlindCharacterWatermarkResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        image_blind_character_watermark_req = imageenhan_20190930_models.ImageBlindCharacterWatermarkRequest()
        OpenApiUtilClient.convert(request, image_blind_character_watermark_req)
        if not UtilClient.is_unset(request.origin_image_urlobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.origin_image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            image_blind_character_watermark_req.origin_image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.watermark_image_urlobject):
            tmp_resp_1 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.watermark_image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            image_blind_character_watermark_req.watermark_image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        image_blind_character_watermark_resp = await self.image_blind_character_watermark_with_options_async(image_blind_character_watermark_req, runtime)
        return image_blind_character_watermark_resp

    def image_blind_pic_watermark_with_options(
        self,
        request: imageenhan_20190930_models.ImageBlindPicWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ImageBlindPicWatermarkResponse:
        """
        @param request: ImageBlindPicWatermarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageBlindPicWatermarkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.function_type):
            body['FunctionType'] = request.function_type
        if not UtilClient.is_unset(request.logo_url):
            body['LogoURL'] = request.logo_url
        if not UtilClient.is_unset(request.origin_image_url):
            body['OriginImageURL'] = request.origin_image_url
        if not UtilClient.is_unset(request.output_file_type):
            body['OutputFileType'] = request.output_file_type
        if not UtilClient.is_unset(request.quality_factor):
            body['QualityFactor'] = request.quality_factor
        if not UtilClient.is_unset(request.watermark_image_url):
            body['WatermarkImageURL'] = request.watermark_image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImageBlindPicWatermark',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.ImageBlindPicWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_blind_pic_watermark_with_options_async(
        self,
        request: imageenhan_20190930_models.ImageBlindPicWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ImageBlindPicWatermarkResponse:
        """
        @param request: ImageBlindPicWatermarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageBlindPicWatermarkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.function_type):
            body['FunctionType'] = request.function_type
        if not UtilClient.is_unset(request.logo_url):
            body['LogoURL'] = request.logo_url
        if not UtilClient.is_unset(request.origin_image_url):
            body['OriginImageURL'] = request.origin_image_url
        if not UtilClient.is_unset(request.output_file_type):
            body['OutputFileType'] = request.output_file_type
        if not UtilClient.is_unset(request.quality_factor):
            body['QualityFactor'] = request.quality_factor
        if not UtilClient.is_unset(request.watermark_image_url):
            body['WatermarkImageURL'] = request.watermark_image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImageBlindPicWatermark',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.ImageBlindPicWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_blind_pic_watermark(
        self,
        request: imageenhan_20190930_models.ImageBlindPicWatermarkRequest,
    ) -> imageenhan_20190930_models.ImageBlindPicWatermarkResponse:
        """
        @param request: ImageBlindPicWatermarkRequest
        @return: ImageBlindPicWatermarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.image_blind_pic_watermark_with_options(request, runtime)

    async def image_blind_pic_watermark_async(
        self,
        request: imageenhan_20190930_models.ImageBlindPicWatermarkRequest,
    ) -> imageenhan_20190930_models.ImageBlindPicWatermarkResponse:
        """
        @param request: ImageBlindPicWatermarkRequest
        @return: ImageBlindPicWatermarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.image_blind_pic_watermark_with_options_async(request, runtime)

    def image_blind_pic_watermark_advance(
        self,
        request: imageenhan_20190930_models.ImageBlindPicWatermarkAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ImageBlindPicWatermarkResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        image_blind_pic_watermark_req = imageenhan_20190930_models.ImageBlindPicWatermarkRequest()
        OpenApiUtilClient.convert(request, image_blind_pic_watermark_req)
        if not UtilClient.is_unset(request.logo_urlobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.logo_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            image_blind_pic_watermark_req.logo_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.origin_image_urlobject):
            tmp_resp_1 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.origin_image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            image_blind_pic_watermark_req.origin_image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.watermark_image_urlobject):
            tmp_resp_2 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_2)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.watermark_image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            image_blind_pic_watermark_req.watermark_image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        image_blind_pic_watermark_resp = self.image_blind_pic_watermark_with_options(image_blind_pic_watermark_req, runtime)
        return image_blind_pic_watermark_resp

    async def image_blind_pic_watermark_advance_async(
        self,
        request: imageenhan_20190930_models.ImageBlindPicWatermarkAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ImageBlindPicWatermarkResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        image_blind_pic_watermark_req = imageenhan_20190930_models.ImageBlindPicWatermarkRequest()
        OpenApiUtilClient.convert(request, image_blind_pic_watermark_req)
        if not UtilClient.is_unset(request.logo_urlobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.logo_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            image_blind_pic_watermark_req.logo_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.origin_image_urlobject):
            tmp_resp_1 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.origin_image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            image_blind_pic_watermark_req.origin_image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.watermark_image_urlobject):
            tmp_resp_2 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_2)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.watermark_image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            image_blind_pic_watermark_req.watermark_image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        image_blind_pic_watermark_resp = await self.image_blind_pic_watermark_with_options_async(image_blind_pic_watermark_req, runtime)
        return image_blind_pic_watermark_resp

    def imitate_photo_style_with_options(
        self,
        request: imageenhan_20190930_models.ImitatePhotoStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ImitatePhotoStyleResponse:
        """
        @param request: ImitatePhotoStyleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImitatePhotoStyleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.style_url):
            body['StyleUrl'] = request.style_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImitatePhotoStyle',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.ImitatePhotoStyleResponse(),
            self.call_api(params, req, runtime)
        )

    async def imitate_photo_style_with_options_async(
        self,
        request: imageenhan_20190930_models.ImitatePhotoStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ImitatePhotoStyleResponse:
        """
        @param request: ImitatePhotoStyleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImitatePhotoStyleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.style_url):
            body['StyleUrl'] = request.style_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImitatePhotoStyle',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.ImitatePhotoStyleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def imitate_photo_style(
        self,
        request: imageenhan_20190930_models.ImitatePhotoStyleRequest,
    ) -> imageenhan_20190930_models.ImitatePhotoStyleResponse:
        """
        @param request: ImitatePhotoStyleRequest
        @return: ImitatePhotoStyleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.imitate_photo_style_with_options(request, runtime)

    async def imitate_photo_style_async(
        self,
        request: imageenhan_20190930_models.ImitatePhotoStyleRequest,
    ) -> imageenhan_20190930_models.ImitatePhotoStyleResponse:
        """
        @param request: ImitatePhotoStyleRequest
        @return: ImitatePhotoStyleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.imitate_photo_style_with_options_async(request, runtime)

    def imitate_photo_style_advance(
        self,
        request: imageenhan_20190930_models.ImitatePhotoStyleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ImitatePhotoStyleResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        imitate_photo_style_req = imageenhan_20190930_models.ImitatePhotoStyleRequest()
        OpenApiUtilClient.convert(request, imitate_photo_style_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            imitate_photo_style_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.style_url_object):
            tmp_resp_1 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.style_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            imitate_photo_style_req.style_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        imitate_photo_style_resp = self.imitate_photo_style_with_options(imitate_photo_style_req, runtime)
        return imitate_photo_style_resp

    async def imitate_photo_style_advance_async(
        self,
        request: imageenhan_20190930_models.ImitatePhotoStyleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.ImitatePhotoStyleResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        imitate_photo_style_req = imageenhan_20190930_models.ImitatePhotoStyleRequest()
        OpenApiUtilClient.convert(request, imitate_photo_style_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            imitate_photo_style_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.style_url_object):
            tmp_resp_1 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.style_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            imitate_photo_style_req.style_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        imitate_photo_style_resp = await self.imitate_photo_style_with_options_async(imitate_photo_style_req, runtime)
        return imitate_photo_style_resp

    def intelligent_composition_with_options(
        self,
        request: imageenhan_20190930_models.IntelligentCompositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.IntelligentCompositionResponse:
        """
        @param request: IntelligentCompositionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IntelligentCompositionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.num_boxes):
            body['NumBoxes'] = request.num_boxes
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IntelligentComposition',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.IntelligentCompositionResponse(),
            self.call_api(params, req, runtime)
        )

    async def intelligent_composition_with_options_async(
        self,
        request: imageenhan_20190930_models.IntelligentCompositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.IntelligentCompositionResponse:
        """
        @param request: IntelligentCompositionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IntelligentCompositionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.num_boxes):
            body['NumBoxes'] = request.num_boxes
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IntelligentComposition',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.IntelligentCompositionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def intelligent_composition(
        self,
        request: imageenhan_20190930_models.IntelligentCompositionRequest,
    ) -> imageenhan_20190930_models.IntelligentCompositionResponse:
        """
        @param request: IntelligentCompositionRequest
        @return: IntelligentCompositionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.intelligent_composition_with_options(request, runtime)

    async def intelligent_composition_async(
        self,
        request: imageenhan_20190930_models.IntelligentCompositionRequest,
    ) -> imageenhan_20190930_models.IntelligentCompositionResponse:
        """
        @param request: IntelligentCompositionRequest
        @return: IntelligentCompositionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.intelligent_composition_with_options_async(request, runtime)

    def intelligent_composition_advance(
        self,
        request: imageenhan_20190930_models.IntelligentCompositionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.IntelligentCompositionResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        intelligent_composition_req = imageenhan_20190930_models.IntelligentCompositionRequest()
        OpenApiUtilClient.convert(request, intelligent_composition_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            intelligent_composition_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        intelligent_composition_resp = self.intelligent_composition_with_options(intelligent_composition_req, runtime)
        return intelligent_composition_resp

    async def intelligent_composition_advance_async(
        self,
        request: imageenhan_20190930_models.IntelligentCompositionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.IntelligentCompositionResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        intelligent_composition_req = imageenhan_20190930_models.IntelligentCompositionRequest()
        OpenApiUtilClient.convert(request, intelligent_composition_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            intelligent_composition_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        intelligent_composition_resp = await self.intelligent_composition_with_options_async(intelligent_composition_req, runtime)
        return intelligent_composition_resp

    def make_super_resolution_image_with_options(
        self,
        request: imageenhan_20190930_models.MakeSuperResolutionImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.MakeSuperResolutionImageResponse:
        """
        @param request: MakeSuperResolutionImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MakeSuperResolutionImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.output_format):
            body['OutputFormat'] = request.output_format
        if not UtilClient.is_unset(request.output_quality):
            body['OutputQuality'] = request.output_quality
        if not UtilClient.is_unset(request.upscale_factor):
            body['UpscaleFactor'] = request.upscale_factor
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MakeSuperResolutionImage',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.MakeSuperResolutionImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def make_super_resolution_image_with_options_async(
        self,
        request: imageenhan_20190930_models.MakeSuperResolutionImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.MakeSuperResolutionImageResponse:
        """
        @param request: MakeSuperResolutionImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MakeSuperResolutionImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.output_format):
            body['OutputFormat'] = request.output_format
        if not UtilClient.is_unset(request.output_quality):
            body['OutputQuality'] = request.output_quality
        if not UtilClient.is_unset(request.upscale_factor):
            body['UpscaleFactor'] = request.upscale_factor
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MakeSuperResolutionImage',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.MakeSuperResolutionImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def make_super_resolution_image(
        self,
        request: imageenhan_20190930_models.MakeSuperResolutionImageRequest,
    ) -> imageenhan_20190930_models.MakeSuperResolutionImageResponse:
        """
        @param request: MakeSuperResolutionImageRequest
        @return: MakeSuperResolutionImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.make_super_resolution_image_with_options(request, runtime)

    async def make_super_resolution_image_async(
        self,
        request: imageenhan_20190930_models.MakeSuperResolutionImageRequest,
    ) -> imageenhan_20190930_models.MakeSuperResolutionImageResponse:
        """
        @param request: MakeSuperResolutionImageRequest
        @return: MakeSuperResolutionImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.make_super_resolution_image_with_options_async(request, runtime)

    def make_super_resolution_image_advance(
        self,
        request: imageenhan_20190930_models.MakeSuperResolutionImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.MakeSuperResolutionImageResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        make_super_resolution_image_req = imageenhan_20190930_models.MakeSuperResolutionImageRequest()
        OpenApiUtilClient.convert(request, make_super_resolution_image_req)
        if not UtilClient.is_unset(request.url_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            make_super_resolution_image_req.url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        make_super_resolution_image_resp = self.make_super_resolution_image_with_options(make_super_resolution_image_req, runtime)
        return make_super_resolution_image_resp

    async def make_super_resolution_image_advance_async(
        self,
        request: imageenhan_20190930_models.MakeSuperResolutionImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.MakeSuperResolutionImageResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        make_super_resolution_image_req = imageenhan_20190930_models.MakeSuperResolutionImageRequest()
        OpenApiUtilClient.convert(request, make_super_resolution_image_req)
        if not UtilClient.is_unset(request.url_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            make_super_resolution_image_req.url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        make_super_resolution_image_resp = await self.make_super_resolution_image_with_options_async(make_super_resolution_image_req, runtime)
        return make_super_resolution_image_resp

    def recolor_hdimage_with_options(
        self,
        request: imageenhan_20190930_models.RecolorHDImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.RecolorHDImageResponse:
        """
        @param request: RecolorHDImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecolorHDImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.color_count):
            body['ColorCount'] = request.color_count
        if not UtilClient.is_unset(request.color_template):
            body['ColorTemplate'] = request.color_template
        if not UtilClient.is_unset(request.degree):
            body['Degree'] = request.degree
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.ref_url):
            body['RefUrl'] = request.ref_url
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecolorHDImage',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.RecolorHDImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def recolor_hdimage_with_options_async(
        self,
        request: imageenhan_20190930_models.RecolorHDImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.RecolorHDImageResponse:
        """
        @param request: RecolorHDImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecolorHDImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.color_count):
            body['ColorCount'] = request.color_count
        if not UtilClient.is_unset(request.color_template):
            body['ColorTemplate'] = request.color_template
        if not UtilClient.is_unset(request.degree):
            body['Degree'] = request.degree
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.ref_url):
            body['RefUrl'] = request.ref_url
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecolorHDImage',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.RecolorHDImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recolor_hdimage(
        self,
        request: imageenhan_20190930_models.RecolorHDImageRequest,
    ) -> imageenhan_20190930_models.RecolorHDImageResponse:
        """
        @param request: RecolorHDImageRequest
        @return: RecolorHDImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recolor_hdimage_with_options(request, runtime)

    async def recolor_hdimage_async(
        self,
        request: imageenhan_20190930_models.RecolorHDImageRequest,
    ) -> imageenhan_20190930_models.RecolorHDImageResponse:
        """
        @param request: RecolorHDImageRequest
        @return: RecolorHDImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recolor_hdimage_with_options_async(request, runtime)

    def recolor_hdimage_advance(
        self,
        request: imageenhan_20190930_models.RecolorHDImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.RecolorHDImageResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        recolor_hdimage_req = imageenhan_20190930_models.RecolorHDImageRequest()
        OpenApiUtilClient.convert(request, recolor_hdimage_req)
        if not UtilClient.is_unset(request.ref_url_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.ref_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            recolor_hdimage_req.ref_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.url_object):
            tmp_resp_1 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            recolor_hdimage_req.url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recolor_hdimage_resp = self.recolor_hdimage_with_options(recolor_hdimage_req, runtime)
        return recolor_hdimage_resp

    async def recolor_hdimage_advance_async(
        self,
        request: imageenhan_20190930_models.RecolorHDImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.RecolorHDImageResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        recolor_hdimage_req = imageenhan_20190930_models.RecolorHDImageRequest()
        OpenApiUtilClient.convert(request, recolor_hdimage_req)
        if not UtilClient.is_unset(request.ref_url_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.ref_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            recolor_hdimage_req.ref_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.url_object):
            tmp_resp_1 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            recolor_hdimage_req.url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recolor_hdimage_resp = await self.recolor_hdimage_with_options_async(recolor_hdimage_req, runtime)
        return recolor_hdimage_resp

    def recolor_image_with_options(
        self,
        request: imageenhan_20190930_models.RecolorImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.RecolorImageResponse:
        """
        @param request: RecolorImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecolorImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.color_count):
            body['ColorCount'] = request.color_count
        if not UtilClient.is_unset(request.color_template):
            body['ColorTemplate'] = request.color_template
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.ref_url):
            body['RefUrl'] = request.ref_url
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecolorImage',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.RecolorImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def recolor_image_with_options_async(
        self,
        request: imageenhan_20190930_models.RecolorImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.RecolorImageResponse:
        """
        @param request: RecolorImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecolorImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.color_count):
            body['ColorCount'] = request.color_count
        if not UtilClient.is_unset(request.color_template):
            body['ColorTemplate'] = request.color_template
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.ref_url):
            body['RefUrl'] = request.ref_url
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecolorImage',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.RecolorImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recolor_image(
        self,
        request: imageenhan_20190930_models.RecolorImageRequest,
    ) -> imageenhan_20190930_models.RecolorImageResponse:
        """
        @param request: RecolorImageRequest
        @return: RecolorImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recolor_image_with_options(request, runtime)

    async def recolor_image_async(
        self,
        request: imageenhan_20190930_models.RecolorImageRequest,
    ) -> imageenhan_20190930_models.RecolorImageResponse:
        """
        @param request: RecolorImageRequest
        @return: RecolorImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recolor_image_with_options_async(request, runtime)

    def recolor_image_advance(
        self,
        request: imageenhan_20190930_models.RecolorImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.RecolorImageResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        recolor_image_req = imageenhan_20190930_models.RecolorImageRequest()
        OpenApiUtilClient.convert(request, recolor_image_req)
        if not UtilClient.is_unset(request.ref_url_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.ref_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            recolor_image_req.ref_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.url_object):
            tmp_resp_1 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            recolor_image_req.url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recolor_image_resp = self.recolor_image_with_options(recolor_image_req, runtime)
        return recolor_image_resp

    async def recolor_image_advance_async(
        self,
        request: imageenhan_20190930_models.RecolorImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.RecolorImageResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        recolor_image_req = imageenhan_20190930_models.RecolorImageRequest()
        OpenApiUtilClient.convert(request, recolor_image_req)
        if not UtilClient.is_unset(request.ref_url_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.ref_url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            recolor_image_req.ref_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.url_object):
            tmp_resp_1 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.url_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            recolor_image_req.url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recolor_image_resp = await self.recolor_image_with_options_async(recolor_image_req, runtime)
        return recolor_image_resp

    def remove_image_subtitles_with_options(
        self,
        request: imageenhan_20190930_models.RemoveImageSubtitlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.RemoveImageSubtitlesResponse:
        """
        @param request: RemoveImageSubtitlesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveImageSubtitlesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bh):
            body['BH'] = request.bh
        if not UtilClient.is_unset(request.bw):
            body['BW'] = request.bw
        if not UtilClient.is_unset(request.bx):
            body['BX'] = request.bx
        if not UtilClient.is_unset(request.by):
            body['BY'] = request.by
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveImageSubtitles',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.RemoveImageSubtitlesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_image_subtitles_with_options_async(
        self,
        request: imageenhan_20190930_models.RemoveImageSubtitlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.RemoveImageSubtitlesResponse:
        """
        @param request: RemoveImageSubtitlesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveImageSubtitlesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bh):
            body['BH'] = request.bh
        if not UtilClient.is_unset(request.bw):
            body['BW'] = request.bw
        if not UtilClient.is_unset(request.bx):
            body['BX'] = request.bx
        if not UtilClient.is_unset(request.by):
            body['BY'] = request.by
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveImageSubtitles',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.RemoveImageSubtitlesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_image_subtitles(
        self,
        request: imageenhan_20190930_models.RemoveImageSubtitlesRequest,
    ) -> imageenhan_20190930_models.RemoveImageSubtitlesResponse:
        """
        @param request: RemoveImageSubtitlesRequest
        @return: RemoveImageSubtitlesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_image_subtitles_with_options(request, runtime)

    async def remove_image_subtitles_async(
        self,
        request: imageenhan_20190930_models.RemoveImageSubtitlesRequest,
    ) -> imageenhan_20190930_models.RemoveImageSubtitlesResponse:
        """
        @param request: RemoveImageSubtitlesRequest
        @return: RemoveImageSubtitlesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_image_subtitles_with_options_async(request, runtime)

    def remove_image_subtitles_advance(
        self,
        request: imageenhan_20190930_models.RemoveImageSubtitlesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.RemoveImageSubtitlesResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        remove_image_subtitles_req = imageenhan_20190930_models.RemoveImageSubtitlesRequest()
        OpenApiUtilClient.convert(request, remove_image_subtitles_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            remove_image_subtitles_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        remove_image_subtitles_resp = self.remove_image_subtitles_with_options(remove_image_subtitles_req, runtime)
        return remove_image_subtitles_resp

    async def remove_image_subtitles_advance_async(
        self,
        request: imageenhan_20190930_models.RemoveImageSubtitlesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.RemoveImageSubtitlesResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        remove_image_subtitles_req = imageenhan_20190930_models.RemoveImageSubtitlesRequest()
        OpenApiUtilClient.convert(request, remove_image_subtitles_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            remove_image_subtitles_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        remove_image_subtitles_resp = await self.remove_image_subtitles_with_options_async(remove_image_subtitles_req, runtime)
        return remove_image_subtitles_resp

    def remove_image_watermark_with_options(
        self,
        request: imageenhan_20190930_models.RemoveImageWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.RemoveImageWatermarkResponse:
        """
        @param request: RemoveImageWatermarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveImageWatermarkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveImageWatermark',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.RemoveImageWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_image_watermark_with_options_async(
        self,
        request: imageenhan_20190930_models.RemoveImageWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.RemoveImageWatermarkResponse:
        """
        @param request: RemoveImageWatermarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveImageWatermarkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveImageWatermark',
            version='2019-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageenhan_20190930_models.RemoveImageWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_image_watermark(
        self,
        request: imageenhan_20190930_models.RemoveImageWatermarkRequest,
    ) -> imageenhan_20190930_models.RemoveImageWatermarkResponse:
        """
        @param request: RemoveImageWatermarkRequest
        @return: RemoveImageWatermarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_image_watermark_with_options(request, runtime)

    async def remove_image_watermark_async(
        self,
        request: imageenhan_20190930_models.RemoveImageWatermarkRequest,
    ) -> imageenhan_20190930_models.RemoveImageWatermarkResponse:
        """
        @param request: RemoveImageWatermarkRequest
        @return: RemoveImageWatermarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_image_watermark_with_options_async(request, runtime)

    def remove_image_watermark_advance(
        self,
        request: imageenhan_20190930_models.RemoveImageWatermarkAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.RemoveImageWatermarkResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        remove_image_watermark_req = imageenhan_20190930_models.RemoveImageWatermarkRequest()
        OpenApiUtilClient.convert(request, remove_image_watermark_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header, runtime)
            remove_image_watermark_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        remove_image_watermark_resp = self.remove_image_watermark_with_options(remove_image_watermark_req, runtime)
        return remove_image_watermark_resp

    async def remove_image_watermark_advance_async(
        self,
        request: imageenhan_20190930_models.RemoveImageWatermarkAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageenhan_20190930_models.RemoveImageWatermarkResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'imageenhan',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        remove_image_watermark_req = imageenhan_20190930_models.RemoveImageWatermarkRequest()
        OpenApiUtilClient.convert(request, remove_image_watermark_req)
        if not UtilClient.is_unset(request.image_urlobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header, runtime)
            remove_image_watermark_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        remove_image_watermark_resp = await self.remove_image_watermark_with_options_async(remove_image_watermark_req, runtime)
        return remove_image_watermark_resp
