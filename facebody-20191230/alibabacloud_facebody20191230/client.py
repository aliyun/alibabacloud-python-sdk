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
from alibabacloud_facebody20191230 import models as facebody_20191230_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_darabonba_number.client import Client as NumberClient


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
        self._endpoint = self.get_endpoint('facebody', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_face_with_options(
        self,
        request: facebody_20191230_models.AddFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceResponse:
        """
        @param request: AddFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.extra_data):
            body['ExtraData'] = request.extra_data
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        if not UtilClient.is_unset(request.similarity_score_threshold_between_entity):
            body['SimilarityScoreThresholdBetweenEntity'] = request.similarity_score_threshold_between_entity
        if not UtilClient.is_unset(request.similarity_score_threshold_in_entity):
            body['SimilarityScoreThresholdInEntity'] = request.similarity_score_threshold_in_entity
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.AddFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_with_options_async(
        self,
        request: facebody_20191230_models.AddFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceResponse:
        """
        @param request: AddFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.extra_data):
            body['ExtraData'] = request.extra_data
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        if not UtilClient.is_unset(request.similarity_score_threshold_between_entity):
            body['SimilarityScoreThresholdBetweenEntity'] = request.similarity_score_threshold_between_entity
        if not UtilClient.is_unset(request.similarity_score_threshold_in_entity):
            body['SimilarityScoreThresholdInEntity'] = request.similarity_score_threshold_in_entity
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.AddFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_face(
        self,
        request: facebody_20191230_models.AddFaceRequest,
    ) -> facebody_20191230_models.AddFaceResponse:
        """
        @param request: AddFaceRequest
        @return: AddFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_face_with_options(request, runtime)

    async def add_face_async(
        self,
        request: facebody_20191230_models.AddFaceRequest,
    ) -> facebody_20191230_models.AddFaceResponse:
        """
        @param request: AddFaceRequest
        @return: AddFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_face_with_options_async(request, runtime)

    def add_face_advance(
        self,
        request: facebody_20191230_models.AddFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceResponse:
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
            'Product': 'facebody',
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
        add_face_req = facebody_20191230_models.AddFaceRequest()
        OpenApiUtilClient.convert(request, add_face_req)
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
            add_face_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        add_face_resp = self.add_face_with_options(add_face_req, runtime)
        return add_face_resp

    async def add_face_advance_async(
        self,
        request: facebody_20191230_models.AddFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceResponse:
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
            'Product': 'facebody',
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
        add_face_req = facebody_20191230_models.AddFaceRequest()
        OpenApiUtilClient.convert(request, add_face_req)
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
            add_face_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        add_face_resp = await self.add_face_with_options_async(add_face_req, runtime)
        return add_face_resp

    def add_face_entity_with_options(
        self,
        request: facebody_20191230_models.AddFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceEntityResponse:
        """
        @param request: AddFaceEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFaceEntityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFaceEntity',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.AddFaceEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_entity_with_options_async(
        self,
        request: facebody_20191230_models.AddFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceEntityResponse:
        """
        @param request: AddFaceEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFaceEntityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFaceEntity',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.AddFaceEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_face_entity(
        self,
        request: facebody_20191230_models.AddFaceEntityRequest,
    ) -> facebody_20191230_models.AddFaceEntityResponse:
        """
        @param request: AddFaceEntityRequest
        @return: AddFaceEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_face_entity_with_options(request, runtime)

    async def add_face_entity_async(
        self,
        request: facebody_20191230_models.AddFaceEntityRequest,
    ) -> facebody_20191230_models.AddFaceEntityResponse:
        """
        @param request: AddFaceEntityRequest
        @return: AddFaceEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_face_entity_with_options_async(request, runtime)

    def add_face_image_template_with_options(
        self,
        request: facebody_20191230_models.AddFaceImageTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceImageTemplateResponse:
        """
        @summary 图像人脸融合模板增加
        
        @param request: AddFaceImageTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFaceImageTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFaceImageTemplate',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.AddFaceImageTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_image_template_with_options_async(
        self,
        request: facebody_20191230_models.AddFaceImageTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceImageTemplateResponse:
        """
        @summary 图像人脸融合模板增加
        
        @param request: AddFaceImageTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFaceImageTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFaceImageTemplate',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.AddFaceImageTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_face_image_template(
        self,
        request: facebody_20191230_models.AddFaceImageTemplateRequest,
    ) -> facebody_20191230_models.AddFaceImageTemplateResponse:
        """
        @summary 图像人脸融合模板增加
        
        @param request: AddFaceImageTemplateRequest
        @return: AddFaceImageTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_face_image_template_with_options(request, runtime)

    async def add_face_image_template_async(
        self,
        request: facebody_20191230_models.AddFaceImageTemplateRequest,
    ) -> facebody_20191230_models.AddFaceImageTemplateResponse:
        """
        @summary 图像人脸融合模板增加
        
        @param request: AddFaceImageTemplateRequest
        @return: AddFaceImageTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_face_image_template_with_options_async(request, runtime)

    def add_face_image_template_advance(
        self,
        request: facebody_20191230_models.AddFaceImageTemplateAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceImageTemplateResponse:
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
            'Product': 'facebody',
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
        add_face_image_template_req = facebody_20191230_models.AddFaceImageTemplateRequest()
        OpenApiUtilClient.convert(request, add_face_image_template_req)
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
            add_face_image_template_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        add_face_image_template_resp = self.add_face_image_template_with_options(add_face_image_template_req, runtime)
        return add_face_image_template_resp

    async def add_face_image_template_advance_async(
        self,
        request: facebody_20191230_models.AddFaceImageTemplateAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceImageTemplateResponse:
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
            'Product': 'facebody',
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
        add_face_image_template_req = facebody_20191230_models.AddFaceImageTemplateRequest()
        OpenApiUtilClient.convert(request, add_face_image_template_req)
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
            add_face_image_template_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        add_face_image_template_resp = await self.add_face_image_template_with_options_async(add_face_image_template_req, runtime)
        return add_face_image_template_resp

    def batch_add_faces_with_options(
        self,
        tmp_req: facebody_20191230_models.BatchAddFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BatchAddFacesResponse:
        """
        @summary 批量添加人脸数据
        
        @param tmp_req: BatchAddFacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchAddFacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = facebody_20191230_models.BatchAddFacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.faces):
            request.faces_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.faces, 'Faces', 'json')
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.faces_shrink):
            body['Faces'] = request.faces_shrink
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        if not UtilClient.is_unset(request.similarity_score_threshold_between_entity):
            body['SimilarityScoreThresholdBetweenEntity'] = request.similarity_score_threshold_between_entity
        if not UtilClient.is_unset(request.similarity_score_threshold_in_entity):
            body['SimilarityScoreThresholdInEntity'] = request.similarity_score_threshold_in_entity
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddFaces',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.BatchAddFacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_faces_with_options_async(
        self,
        tmp_req: facebody_20191230_models.BatchAddFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BatchAddFacesResponse:
        """
        @summary 批量添加人脸数据
        
        @param tmp_req: BatchAddFacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchAddFacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = facebody_20191230_models.BatchAddFacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.faces):
            request.faces_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.faces, 'Faces', 'json')
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.faces_shrink):
            body['Faces'] = request.faces_shrink
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        if not UtilClient.is_unset(request.similarity_score_threshold_between_entity):
            body['SimilarityScoreThresholdBetweenEntity'] = request.similarity_score_threshold_between_entity
        if not UtilClient.is_unset(request.similarity_score_threshold_in_entity):
            body['SimilarityScoreThresholdInEntity'] = request.similarity_score_threshold_in_entity
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddFaces',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.BatchAddFacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_faces(
        self,
        request: facebody_20191230_models.BatchAddFacesRequest,
    ) -> facebody_20191230_models.BatchAddFacesResponse:
        """
        @summary 批量添加人脸数据
        
        @param request: BatchAddFacesRequest
        @return: BatchAddFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_add_faces_with_options(request, runtime)

    async def batch_add_faces_async(
        self,
        request: facebody_20191230_models.BatchAddFacesRequest,
    ) -> facebody_20191230_models.BatchAddFacesResponse:
        """
        @summary 批量添加人脸数据
        
        @param request: BatchAddFacesRequest
        @return: BatchAddFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_add_faces_with_options_async(request, runtime)

    def batch_add_faces_advance(
        self,
        request: facebody_20191230_models.BatchAddFacesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BatchAddFacesResponse:
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
            'Product': 'facebody',
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
        batch_add_faces_req = facebody_20191230_models.BatchAddFacesRequest()
        OpenApiUtilClient.convert(request, batch_add_faces_req)
        if not UtilClient.is_unset(request.faces):
            i_0 = 0
            for item_0 in request.faces:
                if not UtilClient.is_unset(item_0.image_urlobject):
                    tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
                    auth_response = UtilClient.assert_as_map(tmp_resp_0)
                    tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
                    use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
                    auth_response_body = UtilClient.stringify_map_value(tmp_body)
                    file_obj = file_form_models.FileField(
                        filename=auth_response_body.get('ObjectKey'),
                        content=item_0.image_urlobject,
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
                    tmp = batch_add_faces_req.faces[i_0]
                    tmp.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        batch_add_faces_resp = self.batch_add_faces_with_options(batch_add_faces_req, runtime)
        return batch_add_faces_resp

    async def batch_add_faces_advance_async(
        self,
        request: facebody_20191230_models.BatchAddFacesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BatchAddFacesResponse:
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
            'Product': 'facebody',
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
        batch_add_faces_req = facebody_20191230_models.BatchAddFacesRequest()
        OpenApiUtilClient.convert(request, batch_add_faces_req)
        if not UtilClient.is_unset(request.faces):
            i_0 = 0
            for item_0 in request.faces:
                if not UtilClient.is_unset(item_0.image_urlobject):
                    tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
                    auth_response = UtilClient.assert_as_map(tmp_resp_0)
                    tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
                    use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
                    auth_response_body = UtilClient.stringify_map_value(tmp_body)
                    file_obj = file_form_models.FileField(
                        filename=auth_response_body.get('ObjectKey'),
                        content=item_0.image_urlobject,
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
                    tmp = batch_add_faces_req.faces[i_0]
                    tmp.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        batch_add_faces_resp = await self.batch_add_faces_with_options_async(batch_add_faces_req, runtime)
        return batch_add_faces_resp

    def blur_face_with_options(
        self,
        request: facebody_20191230_models.BlurFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BlurFaceResponse:
        """
        @param request: BlurFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BlurFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BlurFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.BlurFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def blur_face_with_options_async(
        self,
        request: facebody_20191230_models.BlurFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BlurFaceResponse:
        """
        @param request: BlurFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BlurFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BlurFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.BlurFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def blur_face(
        self,
        request: facebody_20191230_models.BlurFaceRequest,
    ) -> facebody_20191230_models.BlurFaceResponse:
        """
        @param request: BlurFaceRequest
        @return: BlurFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.blur_face_with_options(request, runtime)

    async def blur_face_async(
        self,
        request: facebody_20191230_models.BlurFaceRequest,
    ) -> facebody_20191230_models.BlurFaceResponse:
        """
        @param request: BlurFaceRequest
        @return: BlurFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.blur_face_with_options_async(request, runtime)

    def blur_face_advance(
        self,
        request: facebody_20191230_models.BlurFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BlurFaceResponse:
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
            'Product': 'facebody',
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
        blur_face_req = facebody_20191230_models.BlurFaceRequest()
        OpenApiUtilClient.convert(request, blur_face_req)
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
            blur_face_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        blur_face_resp = self.blur_face_with_options(blur_face_req, runtime)
        return blur_face_resp

    async def blur_face_advance_async(
        self,
        request: facebody_20191230_models.BlurFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BlurFaceResponse:
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
            'Product': 'facebody',
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
        blur_face_req = facebody_20191230_models.BlurFaceRequest()
        OpenApiUtilClient.convert(request, blur_face_req)
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
            blur_face_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        blur_face_resp = await self.blur_face_with_options_async(blur_face_req, runtime)
        return blur_face_resp

    def body_posture_with_options(
        self,
        request: facebody_20191230_models.BodyPostureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BodyPostureResponse:
        """
        @param request: BodyPostureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BodyPostureResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BodyPosture',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.BodyPostureResponse(),
            self.call_api(params, req, runtime)
        )

    async def body_posture_with_options_async(
        self,
        request: facebody_20191230_models.BodyPostureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BodyPostureResponse:
        """
        @param request: BodyPostureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BodyPostureResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BodyPosture',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.BodyPostureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def body_posture(
        self,
        request: facebody_20191230_models.BodyPostureRequest,
    ) -> facebody_20191230_models.BodyPostureResponse:
        """
        @param request: BodyPostureRequest
        @return: BodyPostureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.body_posture_with_options(request, runtime)

    async def body_posture_async(
        self,
        request: facebody_20191230_models.BodyPostureRequest,
    ) -> facebody_20191230_models.BodyPostureResponse:
        """
        @param request: BodyPostureRequest
        @return: BodyPostureResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.body_posture_with_options_async(request, runtime)

    def body_posture_advance(
        self,
        request: facebody_20191230_models.BodyPostureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BodyPostureResponse:
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
            'Product': 'facebody',
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
        body_posture_req = facebody_20191230_models.BodyPostureRequest()
        OpenApiUtilClient.convert(request, body_posture_req)
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
            body_posture_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        body_posture_resp = self.body_posture_with_options(body_posture_req, runtime)
        return body_posture_resp

    async def body_posture_advance_async(
        self,
        request: facebody_20191230_models.BodyPostureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BodyPostureResponse:
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
            'Product': 'facebody',
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
        body_posture_req = facebody_20191230_models.BodyPostureRequest()
        OpenApiUtilClient.convert(request, body_posture_req)
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
            body_posture_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        body_posture_resp = await self.body_posture_with_options_async(body_posture_req, runtime)
        return body_posture_resp

    def compare_face_with_options(
        self,
        request: facebody_20191230_models.CompareFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CompareFaceResponse:
        """
        @summary 人脸比对(1:1)
        
        @param request: CompareFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompareFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_data_a):
            body['ImageDataA'] = request.image_data_a
        if not UtilClient.is_unset(request.image_data_b):
            body['ImageDataB'] = request.image_data_b
        if not UtilClient.is_unset(request.image_urla):
            body['ImageURLA'] = request.image_urla
        if not UtilClient.is_unset(request.image_urlb):
            body['ImageURLB'] = request.image_urlb
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompareFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.CompareFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_face_with_options_async(
        self,
        request: facebody_20191230_models.CompareFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CompareFaceResponse:
        """
        @summary 人脸比对(1:1)
        
        @param request: CompareFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompareFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_data_a):
            body['ImageDataA'] = request.image_data_a
        if not UtilClient.is_unset(request.image_data_b):
            body['ImageDataB'] = request.image_data_b
        if not UtilClient.is_unset(request.image_urla):
            body['ImageURLA'] = request.image_urla
        if not UtilClient.is_unset(request.image_urlb):
            body['ImageURLB'] = request.image_urlb
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompareFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.CompareFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_face(
        self,
        request: facebody_20191230_models.CompareFaceRequest,
    ) -> facebody_20191230_models.CompareFaceResponse:
        """
        @summary 人脸比对(1:1)
        
        @param request: CompareFaceRequest
        @return: CompareFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.compare_face_with_options(request, runtime)

    async def compare_face_async(
        self,
        request: facebody_20191230_models.CompareFaceRequest,
    ) -> facebody_20191230_models.CompareFaceResponse:
        """
        @summary 人脸比对(1:1)
        
        @param request: CompareFaceRequest
        @return: CompareFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.compare_face_with_options_async(request, runtime)

    def compare_face_advance(
        self,
        request: facebody_20191230_models.CompareFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CompareFaceResponse:
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
            'Product': 'facebody',
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
        compare_face_req = facebody_20191230_models.CompareFaceRequest()
        OpenApiUtilClient.convert(request, compare_face_req)
        if not UtilClient.is_unset(request.image_urlaobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlaobject,
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
            compare_face_req.image_urla = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.image_urlbobject):
            tmp_resp_1 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlbobject,
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
            compare_face_req.image_urlb = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        compare_face_resp = self.compare_face_with_options(compare_face_req, runtime)
        return compare_face_resp

    async def compare_face_advance_async(
        self,
        request: facebody_20191230_models.CompareFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CompareFaceResponse:
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
            'Product': 'facebody',
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
        compare_face_req = facebody_20191230_models.CompareFaceRequest()
        OpenApiUtilClient.convert(request, compare_face_req)
        if not UtilClient.is_unset(request.image_urlaobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlaobject,
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
            compare_face_req.image_urla = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.image_urlbobject):
            tmp_resp_1 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlbobject,
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
            compare_face_req.image_urlb = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        compare_face_resp = await self.compare_face_with_options_async(compare_face_req, runtime)
        return compare_face_resp

    def compare_face_with_mask_with_options(
        self,
        request: facebody_20191230_models.CompareFaceWithMaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CompareFaceWithMaskResponse:
        """
        @summary 口罩人脸比对1:1
        
        @param request: CompareFaceWithMaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompareFaceWithMaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_urla):
            body['ImageURLA'] = request.image_urla
        if not UtilClient.is_unset(request.image_urlb):
            body['ImageURLB'] = request.image_urlb
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompareFaceWithMask',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.CompareFaceWithMaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_face_with_mask_with_options_async(
        self,
        request: facebody_20191230_models.CompareFaceWithMaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CompareFaceWithMaskResponse:
        """
        @summary 口罩人脸比对1:1
        
        @param request: CompareFaceWithMaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompareFaceWithMaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_urla):
            body['ImageURLA'] = request.image_urla
        if not UtilClient.is_unset(request.image_urlb):
            body['ImageURLB'] = request.image_urlb
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompareFaceWithMask',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.CompareFaceWithMaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_face_with_mask(
        self,
        request: facebody_20191230_models.CompareFaceWithMaskRequest,
    ) -> facebody_20191230_models.CompareFaceWithMaskResponse:
        """
        @summary 口罩人脸比对1:1
        
        @param request: CompareFaceWithMaskRequest
        @return: CompareFaceWithMaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.compare_face_with_mask_with_options(request, runtime)

    async def compare_face_with_mask_async(
        self,
        request: facebody_20191230_models.CompareFaceWithMaskRequest,
    ) -> facebody_20191230_models.CompareFaceWithMaskResponse:
        """
        @summary 口罩人脸比对1:1
        
        @param request: CompareFaceWithMaskRequest
        @return: CompareFaceWithMaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.compare_face_with_mask_with_options_async(request, runtime)

    def compare_face_with_mask_advance(
        self,
        request: facebody_20191230_models.CompareFaceWithMaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CompareFaceWithMaskResponse:
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
            'Product': 'facebody',
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
        compare_face_with_mask_req = facebody_20191230_models.CompareFaceWithMaskRequest()
        OpenApiUtilClient.convert(request, compare_face_with_mask_req)
        if not UtilClient.is_unset(request.image_urlaobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlaobject,
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
            compare_face_with_mask_req.image_urla = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.image_urlbobject):
            tmp_resp_1 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlbobject,
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
            compare_face_with_mask_req.image_urlb = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        compare_face_with_mask_resp = self.compare_face_with_mask_with_options(compare_face_with_mask_req, runtime)
        return compare_face_with_mask_resp

    async def compare_face_with_mask_advance_async(
        self,
        request: facebody_20191230_models.CompareFaceWithMaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CompareFaceWithMaskResponse:
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
            'Product': 'facebody',
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
        compare_face_with_mask_req = facebody_20191230_models.CompareFaceWithMaskRequest()
        OpenApiUtilClient.convert(request, compare_face_with_mask_req)
        if not UtilClient.is_unset(request.image_urlaobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlaobject,
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
            compare_face_with_mask_req.image_urla = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.image_urlbobject):
            tmp_resp_1 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_urlbobject,
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
            compare_face_with_mask_req.image_urlb = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        compare_face_with_mask_resp = await self.compare_face_with_mask_with_options_async(compare_face_with_mask_req, runtime)
        return compare_face_with_mask_resp

    def create_face_db_with_options(
        self,
        request: facebody_20191230_models.CreateFaceDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CreateFaceDbResponse:
        """
        @param request: CreateFaceDbRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFaceDbResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFaceDb',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.CreateFaceDbResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_face_db_with_options_async(
        self,
        request: facebody_20191230_models.CreateFaceDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CreateFaceDbResponse:
        """
        @param request: CreateFaceDbRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFaceDbResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFaceDb',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.CreateFaceDbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_face_db(
        self,
        request: facebody_20191230_models.CreateFaceDbRequest,
    ) -> facebody_20191230_models.CreateFaceDbResponse:
        """
        @param request: CreateFaceDbRequest
        @return: CreateFaceDbResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_face_db_with_options(request, runtime)

    async def create_face_db_async(
        self,
        request: facebody_20191230_models.CreateFaceDbRequest,
    ) -> facebody_20191230_models.CreateFaceDbResponse:
        """
        @param request: CreateFaceDbRequest
        @return: CreateFaceDbResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_face_db_with_options_async(request, runtime)

    def deepfake_face_with_options(
        self,
        request: facebody_20191230_models.DeepfakeFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeepfakeFaceResponse:
        """
        @summary 换脸鉴别
        
        @param request: DeepfakeFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeepfakeFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tasks):
            body['Tasks'] = request.tasks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeepfakeFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DeepfakeFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def deepfake_face_with_options_async(
        self,
        request: facebody_20191230_models.DeepfakeFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeepfakeFaceResponse:
        """
        @summary 换脸鉴别
        
        @param request: DeepfakeFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeepfakeFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tasks):
            body['Tasks'] = request.tasks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeepfakeFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DeepfakeFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deepfake_face(
        self,
        request: facebody_20191230_models.DeepfakeFaceRequest,
    ) -> facebody_20191230_models.DeepfakeFaceResponse:
        """
        @summary 换脸鉴别
        
        @param request: DeepfakeFaceRequest
        @return: DeepfakeFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deepfake_face_with_options(request, runtime)

    async def deepfake_face_async(
        self,
        request: facebody_20191230_models.DeepfakeFaceRequest,
    ) -> facebody_20191230_models.DeepfakeFaceResponse:
        """
        @summary 换脸鉴别
        
        @param request: DeepfakeFaceRequest
        @return: DeepfakeFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deepfake_face_with_options_async(request, runtime)

    def deepfake_face_advance(
        self,
        request: facebody_20191230_models.DeepfakeFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeepfakeFaceResponse:
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
            'Product': 'facebody',
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
        deepfake_face_req = facebody_20191230_models.DeepfakeFaceRequest()
        OpenApiUtilClient.convert(request, deepfake_face_req)
        if not UtilClient.is_unset(request.tasks):
            i_0 = 0
            for item_0 in request.tasks:
                if not UtilClient.is_unset(item_0.image_urlobject):
                    tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
                    auth_response = UtilClient.assert_as_map(tmp_resp_0)
                    tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
                    use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
                    auth_response_body = UtilClient.stringify_map_value(tmp_body)
                    file_obj = file_form_models.FileField(
                        filename=auth_response_body.get('ObjectKey'),
                        content=item_0.image_urlobject,
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
                    tmp = deepfake_face_req.tasks[i_0]
                    tmp.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        deepfake_face_resp = self.deepfake_face_with_options(deepfake_face_req, runtime)
        return deepfake_face_resp

    async def deepfake_face_advance_async(
        self,
        request: facebody_20191230_models.DeepfakeFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeepfakeFaceResponse:
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
            'Product': 'facebody',
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
        deepfake_face_req = facebody_20191230_models.DeepfakeFaceRequest()
        OpenApiUtilClient.convert(request, deepfake_face_req)
        if not UtilClient.is_unset(request.tasks):
            i_0 = 0
            for item_0 in request.tasks:
                if not UtilClient.is_unset(item_0.image_urlobject):
                    tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
                    auth_response = UtilClient.assert_as_map(tmp_resp_0)
                    tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
                    use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
                    auth_response_body = UtilClient.stringify_map_value(tmp_body)
                    file_obj = file_form_models.FileField(
                        filename=auth_response_body.get('ObjectKey'),
                        content=item_0.image_urlobject,
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
                    tmp = deepfake_face_req.tasks[i_0]
                    tmp.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        deepfake_face_resp = await self.deepfake_face_with_options_async(deepfake_face_req, runtime)
        return deepfake_face_resp

    def delete_face_with_options(
        self,
        request: facebody_20191230_models.DeleteFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceResponse:
        """
        @param request: DeleteFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.face_id):
            body['FaceId'] = request.face_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DeleteFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_with_options_async(
        self,
        request: facebody_20191230_models.DeleteFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceResponse:
        """
        @param request: DeleteFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.face_id):
            body['FaceId'] = request.face_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DeleteFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face(
        self,
        request: facebody_20191230_models.DeleteFaceRequest,
    ) -> facebody_20191230_models.DeleteFaceResponse:
        """
        @param request: DeleteFaceRequest
        @return: DeleteFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_face_with_options(request, runtime)

    async def delete_face_async(
        self,
        request: facebody_20191230_models.DeleteFaceRequest,
    ) -> facebody_20191230_models.DeleteFaceResponse:
        """
        @param request: DeleteFaceRequest
        @return: DeleteFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_with_options_async(request, runtime)

    def delete_face_db_with_options(
        self,
        request: facebody_20191230_models.DeleteFaceDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceDbResponse:
        """
        @param request: DeleteFaceDbRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFaceDbResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFaceDb',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DeleteFaceDbResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_db_with_options_async(
        self,
        request: facebody_20191230_models.DeleteFaceDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceDbResponse:
        """
        @param request: DeleteFaceDbRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFaceDbResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFaceDb',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DeleteFaceDbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face_db(
        self,
        request: facebody_20191230_models.DeleteFaceDbRequest,
    ) -> facebody_20191230_models.DeleteFaceDbResponse:
        """
        @param request: DeleteFaceDbRequest
        @return: DeleteFaceDbResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_face_db_with_options(request, runtime)

    async def delete_face_db_async(
        self,
        request: facebody_20191230_models.DeleteFaceDbRequest,
    ) -> facebody_20191230_models.DeleteFaceDbResponse:
        """
        @param request: DeleteFaceDbRequest
        @return: DeleteFaceDbResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_db_with_options_async(request, runtime)

    def delete_face_entity_with_options(
        self,
        request: facebody_20191230_models.DeleteFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceEntityResponse:
        """
        @param request: DeleteFaceEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFaceEntityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFaceEntity',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DeleteFaceEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_entity_with_options_async(
        self,
        request: facebody_20191230_models.DeleteFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceEntityResponse:
        """
        @param request: DeleteFaceEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFaceEntityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFaceEntity',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DeleteFaceEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face_entity(
        self,
        request: facebody_20191230_models.DeleteFaceEntityRequest,
    ) -> facebody_20191230_models.DeleteFaceEntityResponse:
        """
        @param request: DeleteFaceEntityRequest
        @return: DeleteFaceEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_face_entity_with_options(request, runtime)

    async def delete_face_entity_async(
        self,
        request: facebody_20191230_models.DeleteFaceEntityRequest,
    ) -> facebody_20191230_models.DeleteFaceEntityResponse:
        """
        @param request: DeleteFaceEntityRequest
        @return: DeleteFaceEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_entity_with_options_async(request, runtime)

    def delete_face_image_template_with_options(
        self,
        request: facebody_20191230_models.DeleteFaceImageTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceImageTemplateResponse:
        """
        @summary 图像人脸融合模板删除
        
        @param request: DeleteFaceImageTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFaceImageTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFaceImageTemplate',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DeleteFaceImageTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_image_template_with_options_async(
        self,
        request: facebody_20191230_models.DeleteFaceImageTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceImageTemplateResponse:
        """
        @summary 图像人脸融合模板删除
        
        @param request: DeleteFaceImageTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFaceImageTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFaceImageTemplate',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DeleteFaceImageTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face_image_template(
        self,
        request: facebody_20191230_models.DeleteFaceImageTemplateRequest,
    ) -> facebody_20191230_models.DeleteFaceImageTemplateResponse:
        """
        @summary 图像人脸融合模板删除
        
        @param request: DeleteFaceImageTemplateRequest
        @return: DeleteFaceImageTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_face_image_template_with_options(request, runtime)

    async def delete_face_image_template_async(
        self,
        request: facebody_20191230_models.DeleteFaceImageTemplateRequest,
    ) -> facebody_20191230_models.DeleteFaceImageTemplateResponse:
        """
        @summary 图像人脸融合模板删除
        
        @param request: DeleteFaceImageTemplateRequest
        @return: DeleteFaceImageTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_image_template_with_options_async(request, runtime)

    def detect_body_count_with_options(
        self,
        request: facebody_20191230_models.DetectBodyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
        """
        @param request: DetectBodyCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectBodyCountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectBodyCount',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DetectBodyCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_body_count_with_options_async(
        self,
        request: facebody_20191230_models.DetectBodyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
        """
        @param request: DetectBodyCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectBodyCountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectBodyCount',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DetectBodyCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_body_count(
        self,
        request: facebody_20191230_models.DetectBodyCountRequest,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
        """
        @param request: DetectBodyCountRequest
        @return: DetectBodyCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_body_count_with_options(request, runtime)

    async def detect_body_count_async(
        self,
        request: facebody_20191230_models.DetectBodyCountRequest,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
        """
        @param request: DetectBodyCountRequest
        @return: DetectBodyCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_body_count_with_options_async(request, runtime)

    def detect_body_count_advance(
        self,
        request: facebody_20191230_models.DetectBodyCountAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
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
            'Product': 'facebody',
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
        detect_body_count_req = facebody_20191230_models.DetectBodyCountRequest()
        OpenApiUtilClient.convert(request, detect_body_count_req)
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
            detect_body_count_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_body_count_resp = self.detect_body_count_with_options(detect_body_count_req, runtime)
        return detect_body_count_resp

    async def detect_body_count_advance_async(
        self,
        request: facebody_20191230_models.DetectBodyCountAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
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
            'Product': 'facebody',
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
        detect_body_count_req = facebody_20191230_models.DetectBodyCountRequest()
        OpenApiUtilClient.convert(request, detect_body_count_req)
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
            detect_body_count_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_body_count_resp = await self.detect_body_count_with_options_async(detect_body_count_req, runtime)
        return detect_body_count_resp

    def detect_celebrity_with_options(
        self,
        request: facebody_20191230_models.DetectCelebrityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
        """
        @param request: DetectCelebrityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectCelebrityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectCelebrity',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DetectCelebrityResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_celebrity_with_options_async(
        self,
        request: facebody_20191230_models.DetectCelebrityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
        """
        @param request: DetectCelebrityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectCelebrityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectCelebrity',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DetectCelebrityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_celebrity(
        self,
        request: facebody_20191230_models.DetectCelebrityRequest,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
        """
        @param request: DetectCelebrityRequest
        @return: DetectCelebrityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_celebrity_with_options(request, runtime)

    async def detect_celebrity_async(
        self,
        request: facebody_20191230_models.DetectCelebrityRequest,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
        """
        @param request: DetectCelebrityRequest
        @return: DetectCelebrityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_celebrity_with_options_async(request, runtime)

    def detect_celebrity_advance(
        self,
        request: facebody_20191230_models.DetectCelebrityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
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
            'Product': 'facebody',
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
        detect_celebrity_req = facebody_20191230_models.DetectCelebrityRequest()
        OpenApiUtilClient.convert(request, detect_celebrity_req)
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
            detect_celebrity_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_celebrity_resp = self.detect_celebrity_with_options(detect_celebrity_req, runtime)
        return detect_celebrity_resp

    async def detect_celebrity_advance_async(
        self,
        request: facebody_20191230_models.DetectCelebrityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
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
            'Product': 'facebody',
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
        detect_celebrity_req = facebody_20191230_models.DetectCelebrityRequest()
        OpenApiUtilClient.convert(request, detect_celebrity_req)
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
            detect_celebrity_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_celebrity_resp = await self.detect_celebrity_with_options_async(detect_celebrity_req, runtime)
        return detect_celebrity_resp

    def detect_face_with_options(
        self,
        request: facebody_20191230_models.DetectFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectFaceResponse:
        """
        @param request: DetectFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.landmark):
            body['Landmark'] = request.landmark
        if not UtilClient.is_unset(request.max_face_number):
            body['MaxFaceNumber'] = request.max_face_number
        if not UtilClient.is_unset(request.pose):
            body['Pose'] = request.pose
        if not UtilClient.is_unset(request.quality):
            body['Quality'] = request.quality
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DetectFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_face_with_options_async(
        self,
        request: facebody_20191230_models.DetectFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectFaceResponse:
        """
        @param request: DetectFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.landmark):
            body['Landmark'] = request.landmark
        if not UtilClient.is_unset(request.max_face_number):
            body['MaxFaceNumber'] = request.max_face_number
        if not UtilClient.is_unset(request.pose):
            body['Pose'] = request.pose
        if not UtilClient.is_unset(request.quality):
            body['Quality'] = request.quality
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DetectFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_face(
        self,
        request: facebody_20191230_models.DetectFaceRequest,
    ) -> facebody_20191230_models.DetectFaceResponse:
        """
        @param request: DetectFaceRequest
        @return: DetectFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_face_with_options(request, runtime)

    async def detect_face_async(
        self,
        request: facebody_20191230_models.DetectFaceRequest,
    ) -> facebody_20191230_models.DetectFaceResponse:
        """
        @param request: DetectFaceRequest
        @return: DetectFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_face_with_options_async(request, runtime)

    def detect_face_advance(
        self,
        request: facebody_20191230_models.DetectFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectFaceResponse:
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
            'Product': 'facebody',
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
        detect_face_req = facebody_20191230_models.DetectFaceRequest()
        OpenApiUtilClient.convert(request, detect_face_req)
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
            detect_face_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_face_resp = self.detect_face_with_options(detect_face_req, runtime)
        return detect_face_resp

    async def detect_face_advance_async(
        self,
        request: facebody_20191230_models.DetectFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectFaceResponse:
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
            'Product': 'facebody',
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
        detect_face_req = facebody_20191230_models.DetectFaceRequest()
        OpenApiUtilClient.convert(request, detect_face_req)
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
            detect_face_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_face_resp = await self.detect_face_with_options_async(detect_face_req, runtime)
        return detect_face_resp

    def detect_infrared_living_face_with_options(
        self,
        request: facebody_20191230_models.DetectInfraredLivingFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectInfraredLivingFaceResponse:
        """
        @summary 红外人脸活体检测
        
        @param request: DetectInfraredLivingFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectInfraredLivingFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tasks):
            body['Tasks'] = request.tasks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectInfraredLivingFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DetectInfraredLivingFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_infrared_living_face_with_options_async(
        self,
        request: facebody_20191230_models.DetectInfraredLivingFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectInfraredLivingFaceResponse:
        """
        @summary 红外人脸活体检测
        
        @param request: DetectInfraredLivingFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectInfraredLivingFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tasks):
            body['Tasks'] = request.tasks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectInfraredLivingFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DetectInfraredLivingFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_infrared_living_face(
        self,
        request: facebody_20191230_models.DetectInfraredLivingFaceRequest,
    ) -> facebody_20191230_models.DetectInfraredLivingFaceResponse:
        """
        @summary 红外人脸活体检测
        
        @param request: DetectInfraredLivingFaceRequest
        @return: DetectInfraredLivingFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_infrared_living_face_with_options(request, runtime)

    async def detect_infrared_living_face_async(
        self,
        request: facebody_20191230_models.DetectInfraredLivingFaceRequest,
    ) -> facebody_20191230_models.DetectInfraredLivingFaceResponse:
        """
        @summary 红外人脸活体检测
        
        @param request: DetectInfraredLivingFaceRequest
        @return: DetectInfraredLivingFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_infrared_living_face_with_options_async(request, runtime)

    def detect_infrared_living_face_advance(
        self,
        request: facebody_20191230_models.DetectInfraredLivingFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectInfraredLivingFaceResponse:
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
            'Product': 'facebody',
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
        detect_infrared_living_face_req = facebody_20191230_models.DetectInfraredLivingFaceRequest()
        OpenApiUtilClient.convert(request, detect_infrared_living_face_req)
        if not UtilClient.is_unset(request.tasks):
            i_0 = 0
            for item_0 in request.tasks:
                if not UtilClient.is_unset(item_0.image_urlobject):
                    tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
                    auth_response = UtilClient.assert_as_map(tmp_resp_0)
                    tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
                    use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
                    auth_response_body = UtilClient.stringify_map_value(tmp_body)
                    file_obj = file_form_models.FileField(
                        filename=auth_response_body.get('ObjectKey'),
                        content=item_0.image_urlobject,
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
                    tmp = detect_infrared_living_face_req.tasks[i_0]
                    tmp.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_infrared_living_face_resp = self.detect_infrared_living_face_with_options(detect_infrared_living_face_req, runtime)
        return detect_infrared_living_face_resp

    async def detect_infrared_living_face_advance_async(
        self,
        request: facebody_20191230_models.DetectInfraredLivingFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectInfraredLivingFaceResponse:
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
            'Product': 'facebody',
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
        detect_infrared_living_face_req = facebody_20191230_models.DetectInfraredLivingFaceRequest()
        OpenApiUtilClient.convert(request, detect_infrared_living_face_req)
        if not UtilClient.is_unset(request.tasks):
            i_0 = 0
            for item_0 in request.tasks:
                if not UtilClient.is_unset(item_0.image_urlobject):
                    tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
                    auth_response = UtilClient.assert_as_map(tmp_resp_0)
                    tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
                    use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
                    auth_response_body = UtilClient.stringify_map_value(tmp_body)
                    file_obj = file_form_models.FileField(
                        filename=auth_response_body.get('ObjectKey'),
                        content=item_0.image_urlobject,
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
                    tmp = detect_infrared_living_face_req.tasks[i_0]
                    tmp.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_infrared_living_face_resp = await self.detect_infrared_living_face_with_options_async(detect_infrared_living_face_req, runtime)
        return detect_infrared_living_face_resp

    def detect_living_face_with_options(
        self,
        request: facebody_20191230_models.DetectLivingFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectLivingFaceResponse:
        """
        @summary 人脸活体检测(DetectLivingFace)
        
        @param request: DetectLivingFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectLivingFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tasks):
            body['Tasks'] = request.tasks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectLivingFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DetectLivingFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_living_face_with_options_async(
        self,
        request: facebody_20191230_models.DetectLivingFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectLivingFaceResponse:
        """
        @summary 人脸活体检测(DetectLivingFace)
        
        @param request: DetectLivingFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectLivingFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tasks):
            body['Tasks'] = request.tasks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectLivingFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DetectLivingFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_living_face(
        self,
        request: facebody_20191230_models.DetectLivingFaceRequest,
    ) -> facebody_20191230_models.DetectLivingFaceResponse:
        """
        @summary 人脸活体检测(DetectLivingFace)
        
        @param request: DetectLivingFaceRequest
        @return: DetectLivingFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_living_face_with_options(request, runtime)

    async def detect_living_face_async(
        self,
        request: facebody_20191230_models.DetectLivingFaceRequest,
    ) -> facebody_20191230_models.DetectLivingFaceResponse:
        """
        @summary 人脸活体检测(DetectLivingFace)
        
        @param request: DetectLivingFaceRequest
        @return: DetectLivingFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_living_face_with_options_async(request, runtime)

    def detect_living_face_advance(
        self,
        request: facebody_20191230_models.DetectLivingFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectLivingFaceResponse:
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
            'Product': 'facebody',
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
        detect_living_face_req = facebody_20191230_models.DetectLivingFaceRequest()
        OpenApiUtilClient.convert(request, detect_living_face_req)
        if not UtilClient.is_unset(request.tasks):
            i_0 = 0
            for item_0 in request.tasks:
                if not UtilClient.is_unset(item_0.image_urlobject):
                    tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
                    auth_response = UtilClient.assert_as_map(tmp_resp_0)
                    tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
                    use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
                    auth_response_body = UtilClient.stringify_map_value(tmp_body)
                    file_obj = file_form_models.FileField(
                        filename=auth_response_body.get('ObjectKey'),
                        content=item_0.image_urlobject,
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
                    tmp = detect_living_face_req.tasks[i_0]
                    tmp.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_living_face_resp = self.detect_living_face_with_options(detect_living_face_req, runtime)
        return detect_living_face_resp

    async def detect_living_face_advance_async(
        self,
        request: facebody_20191230_models.DetectLivingFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectLivingFaceResponse:
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
            'Product': 'facebody',
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
        detect_living_face_req = facebody_20191230_models.DetectLivingFaceRequest()
        OpenApiUtilClient.convert(request, detect_living_face_req)
        if not UtilClient.is_unset(request.tasks):
            i_0 = 0
            for item_0 in request.tasks:
                if not UtilClient.is_unset(item_0.image_urlobject):
                    tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
                    auth_response = UtilClient.assert_as_map(tmp_resp_0)
                    tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
                    use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
                    auth_response_body = UtilClient.stringify_map_value(tmp_body)
                    file_obj = file_form_models.FileField(
                        filename=auth_response_body.get('ObjectKey'),
                        content=item_0.image_urlobject,
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
                    tmp = detect_living_face_req.tasks[i_0]
                    tmp.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_living_face_resp = await self.detect_living_face_with_options_async(detect_living_face_req, runtime)
        return detect_living_face_resp

    def detect_pedestrian_with_options(
        self,
        request: facebody_20191230_models.DetectPedestrianRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
        """
        @param request: DetectPedestrianRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectPedestrianResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectPedestrian',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DetectPedestrianResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_pedestrian_with_options_async(
        self,
        request: facebody_20191230_models.DetectPedestrianRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
        """
        @param request: DetectPedestrianRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectPedestrianResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectPedestrian',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DetectPedestrianResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_pedestrian(
        self,
        request: facebody_20191230_models.DetectPedestrianRequest,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
        """
        @param request: DetectPedestrianRequest
        @return: DetectPedestrianResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_pedestrian_with_options(request, runtime)

    async def detect_pedestrian_async(
        self,
        request: facebody_20191230_models.DetectPedestrianRequest,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
        """
        @param request: DetectPedestrianRequest
        @return: DetectPedestrianResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_pedestrian_with_options_async(request, runtime)

    def detect_pedestrian_advance(
        self,
        request: facebody_20191230_models.DetectPedestrianAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
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
            'Product': 'facebody',
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
        detect_pedestrian_req = facebody_20191230_models.DetectPedestrianRequest()
        OpenApiUtilClient.convert(request, detect_pedestrian_req)
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
            detect_pedestrian_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_pedestrian_resp = self.detect_pedestrian_with_options(detect_pedestrian_req, runtime)
        return detect_pedestrian_resp

    async def detect_pedestrian_advance_async(
        self,
        request: facebody_20191230_models.DetectPedestrianAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
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
            'Product': 'facebody',
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
        detect_pedestrian_req = facebody_20191230_models.DetectPedestrianRequest()
        OpenApiUtilClient.convert(request, detect_pedestrian_req)
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
            detect_pedestrian_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_pedestrian_resp = await self.detect_pedestrian_with_options_async(detect_pedestrian_req, runtime)
        return detect_pedestrian_resp

    def detect_video_living_face_with_options(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
        """
        @param request: DetectVideoLivingFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectVideoLivingFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectVideoLivingFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DetectVideoLivingFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_video_living_face_with_options_async(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
        """
        @param request: DetectVideoLivingFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectVideoLivingFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectVideoLivingFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.DetectVideoLivingFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_video_living_face(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceRequest,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
        """
        @param request: DetectVideoLivingFaceRequest
        @return: DetectVideoLivingFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_video_living_face_with_options(request, runtime)

    async def detect_video_living_face_async(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceRequest,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
        """
        @param request: DetectVideoLivingFaceRequest
        @return: DetectVideoLivingFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_video_living_face_with_options_async(request, runtime)

    def detect_video_living_face_advance(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
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
            'Product': 'facebody',
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
        detect_video_living_face_req = facebody_20191230_models.DetectVideoLivingFaceRequest()
        OpenApiUtilClient.convert(request, detect_video_living_face_req)
        if not UtilClient.is_unset(request.video_url_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.video_url_object,
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
            detect_video_living_face_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_video_living_face_resp = self.detect_video_living_face_with_options(detect_video_living_face_req, runtime)
        return detect_video_living_face_resp

    async def detect_video_living_face_advance_async(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
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
            'Product': 'facebody',
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
        detect_video_living_face_req = facebody_20191230_models.DetectVideoLivingFaceRequest()
        OpenApiUtilClient.convert(request, detect_video_living_face_req)
        if not UtilClient.is_unset(request.video_url_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.video_url_object,
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
            detect_video_living_face_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_video_living_face_resp = await self.detect_video_living_face_with_options_async(detect_video_living_face_req, runtime)
        return detect_video_living_face_resp

    def enhance_face_with_options(
        self,
        request: facebody_20191230_models.EnhanceFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
        """
        @param request: EnhanceFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnhanceFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnhanceFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.EnhanceFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def enhance_face_with_options_async(
        self,
        request: facebody_20191230_models.EnhanceFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
        """
        @param request: EnhanceFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnhanceFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnhanceFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.EnhanceFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enhance_face(
        self,
        request: facebody_20191230_models.EnhanceFaceRequest,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
        """
        @param request: EnhanceFaceRequest
        @return: EnhanceFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enhance_face_with_options(request, runtime)

    async def enhance_face_async(
        self,
        request: facebody_20191230_models.EnhanceFaceRequest,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
        """
        @param request: EnhanceFaceRequest
        @return: EnhanceFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enhance_face_with_options_async(request, runtime)

    def enhance_face_advance(
        self,
        request: facebody_20191230_models.EnhanceFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
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
            'Product': 'facebody',
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
        enhance_face_req = facebody_20191230_models.EnhanceFaceRequest()
        OpenApiUtilClient.convert(request, enhance_face_req)
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
            enhance_face_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        enhance_face_resp = self.enhance_face_with_options(enhance_face_req, runtime)
        return enhance_face_resp

    async def enhance_face_advance_async(
        self,
        request: facebody_20191230_models.EnhanceFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
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
            'Product': 'facebody',
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
        enhance_face_req = facebody_20191230_models.EnhanceFaceRequest()
        OpenApiUtilClient.convert(request, enhance_face_req)
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
            enhance_face_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        enhance_face_resp = await self.enhance_face_with_options_async(enhance_face_req, runtime)
        return enhance_face_resp

    def extract_finger_print_with_options(
        self,
        request: facebody_20191230_models.ExtractFingerPrintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractFingerPrintResponse:
        """
        @summary 指纹提取
        
        @param request: ExtractFingerPrintRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExtractFingerPrintResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_data):
            body['ImageData'] = request.image_data
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtractFingerPrint',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.ExtractFingerPrintResponse(),
            self.call_api(params, req, runtime)
        )

    async def extract_finger_print_with_options_async(
        self,
        request: facebody_20191230_models.ExtractFingerPrintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractFingerPrintResponse:
        """
        @summary 指纹提取
        
        @param request: ExtractFingerPrintRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExtractFingerPrintResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_data):
            body['ImageData'] = request.image_data
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtractFingerPrint',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.ExtractFingerPrintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def extract_finger_print(
        self,
        request: facebody_20191230_models.ExtractFingerPrintRequest,
    ) -> facebody_20191230_models.ExtractFingerPrintResponse:
        """
        @summary 指纹提取
        
        @param request: ExtractFingerPrintRequest
        @return: ExtractFingerPrintResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.extract_finger_print_with_options(request, runtime)

    async def extract_finger_print_async(
        self,
        request: facebody_20191230_models.ExtractFingerPrintRequest,
    ) -> facebody_20191230_models.ExtractFingerPrintResponse:
        """
        @summary 指纹提取
        
        @param request: ExtractFingerPrintRequest
        @return: ExtractFingerPrintResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.extract_finger_print_with_options_async(request, runtime)

    def extract_finger_print_advance(
        self,
        request: facebody_20191230_models.ExtractFingerPrintAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractFingerPrintResponse:
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
            'Product': 'facebody',
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
        extract_finger_print_req = facebody_20191230_models.ExtractFingerPrintRequest()
        OpenApiUtilClient.convert(request, extract_finger_print_req)
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
            extract_finger_print_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        extract_finger_print_resp = self.extract_finger_print_with_options(extract_finger_print_req, runtime)
        return extract_finger_print_resp

    async def extract_finger_print_advance_async(
        self,
        request: facebody_20191230_models.ExtractFingerPrintAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractFingerPrintResponse:
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
            'Product': 'facebody',
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
        extract_finger_print_req = facebody_20191230_models.ExtractFingerPrintRequest()
        OpenApiUtilClient.convert(request, extract_finger_print_req)
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
            extract_finger_print_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        extract_finger_print_resp = await self.extract_finger_print_with_options_async(extract_finger_print_req, runtime)
        return extract_finger_print_resp

    def face_beauty_with_options(
        self,
        request: facebody_20191230_models.FaceBeautyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceBeautyResponse:
        """
        @param request: FaceBeautyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FaceBeautyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.sharp):
            body['Sharp'] = request.sharp
        if not UtilClient.is_unset(request.smooth):
            body['Smooth'] = request.smooth
        if not UtilClient.is_unset(request.white):
            body['White'] = request.white
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceBeauty',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.FaceBeautyResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_beauty_with_options_async(
        self,
        request: facebody_20191230_models.FaceBeautyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceBeautyResponse:
        """
        @param request: FaceBeautyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FaceBeautyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.sharp):
            body['Sharp'] = request.sharp
        if not UtilClient.is_unset(request.smooth):
            body['Smooth'] = request.smooth
        if not UtilClient.is_unset(request.white):
            body['White'] = request.white
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceBeauty',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.FaceBeautyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_beauty(
        self,
        request: facebody_20191230_models.FaceBeautyRequest,
    ) -> facebody_20191230_models.FaceBeautyResponse:
        """
        @param request: FaceBeautyRequest
        @return: FaceBeautyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.face_beauty_with_options(request, runtime)

    async def face_beauty_async(
        self,
        request: facebody_20191230_models.FaceBeautyRequest,
    ) -> facebody_20191230_models.FaceBeautyResponse:
        """
        @param request: FaceBeautyRequest
        @return: FaceBeautyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.face_beauty_with_options_async(request, runtime)

    def face_beauty_advance(
        self,
        request: facebody_20191230_models.FaceBeautyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceBeautyResponse:
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
            'Product': 'facebody',
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
        face_beauty_req = facebody_20191230_models.FaceBeautyRequest()
        OpenApiUtilClient.convert(request, face_beauty_req)
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
            face_beauty_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        face_beauty_resp = self.face_beauty_with_options(face_beauty_req, runtime)
        return face_beauty_resp

    async def face_beauty_advance_async(
        self,
        request: facebody_20191230_models.FaceBeautyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceBeautyResponse:
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
            'Product': 'facebody',
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
        face_beauty_req = facebody_20191230_models.FaceBeautyRequest()
        OpenApiUtilClient.convert(request, face_beauty_req)
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
            face_beauty_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        face_beauty_resp = await self.face_beauty_with_options_async(face_beauty_req, runtime)
        return face_beauty_resp

    def gen_real_person_verification_token_with_options(
        self,
        request: facebody_20191230_models.GenRealPersonVerificationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenRealPersonVerificationTokenResponse:
        """
        @param request: GenRealPersonVerificationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenRealPersonVerificationTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.certificate_name):
            body['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.certificate_number):
            body['CertificateNumber'] = request.certificate_number
        if not UtilClient.is_unset(request.meta_info):
            body['MetaInfo'] = request.meta_info
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenRealPersonVerificationToken',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.GenRealPersonVerificationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def gen_real_person_verification_token_with_options_async(
        self,
        request: facebody_20191230_models.GenRealPersonVerificationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenRealPersonVerificationTokenResponse:
        """
        @param request: GenRealPersonVerificationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenRealPersonVerificationTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.certificate_name):
            body['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.certificate_number):
            body['CertificateNumber'] = request.certificate_number
        if not UtilClient.is_unset(request.meta_info):
            body['MetaInfo'] = request.meta_info
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenRealPersonVerificationToken',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.GenRealPersonVerificationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def gen_real_person_verification_token(
        self,
        request: facebody_20191230_models.GenRealPersonVerificationTokenRequest,
    ) -> facebody_20191230_models.GenRealPersonVerificationTokenResponse:
        """
        @param request: GenRealPersonVerificationTokenRequest
        @return: GenRealPersonVerificationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.gen_real_person_verification_token_with_options(request, runtime)

    async def gen_real_person_verification_token_async(
        self,
        request: facebody_20191230_models.GenRealPersonVerificationTokenRequest,
    ) -> facebody_20191230_models.GenRealPersonVerificationTokenResponse:
        """
        @param request: GenRealPersonVerificationTokenRequest
        @return: GenRealPersonVerificationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.gen_real_person_verification_token_with_options_async(request, runtime)

    def generate_human_anime_style_with_options(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
        """
        @param request: GenerateHumanAnimeStyleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateHumanAnimeStyleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algo_type):
            query['AlgoType'] = request.algo_type
        if not UtilClient.is_unset(request.image_url):
            query['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateHumanAnimeStyle',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.GenerateHumanAnimeStyleResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_human_anime_style_with_options_async(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
        """
        @param request: GenerateHumanAnimeStyleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateHumanAnimeStyleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algo_type):
            query['AlgoType'] = request.algo_type
        if not UtilClient.is_unset(request.image_url):
            query['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateHumanAnimeStyle',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.GenerateHumanAnimeStyleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_human_anime_style(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleRequest,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
        """
        @param request: GenerateHumanAnimeStyleRequest
        @return: GenerateHumanAnimeStyleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_human_anime_style_with_options(request, runtime)

    async def generate_human_anime_style_async(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleRequest,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
        """
        @param request: GenerateHumanAnimeStyleRequest
        @return: GenerateHumanAnimeStyleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_human_anime_style_with_options_async(request, runtime)

    def generate_human_anime_style_advance(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
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
            'Product': 'facebody',
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
        generate_human_anime_style_req = facebody_20191230_models.GenerateHumanAnimeStyleRequest()
        OpenApiUtilClient.convert(request, generate_human_anime_style_req)
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
            generate_human_anime_style_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        generate_human_anime_style_resp = self.generate_human_anime_style_with_options(generate_human_anime_style_req, runtime)
        return generate_human_anime_style_resp

    async def generate_human_anime_style_advance_async(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
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
            'Product': 'facebody',
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
        generate_human_anime_style_req = facebody_20191230_models.GenerateHumanAnimeStyleRequest()
        OpenApiUtilClient.convert(request, generate_human_anime_style_req)
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
            generate_human_anime_style_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        generate_human_anime_style_resp = await self.generate_human_anime_style_with_options_async(generate_human_anime_style_req, runtime)
        return generate_human_anime_style_resp

    def generate_human_sketch_style_with_options(
        self,
        request: facebody_20191230_models.GenerateHumanSketchStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanSketchStyleResponse:
        """
        @summary 人像素描风格化
        
        @param request: GenerateHumanSketchStyleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateHumanSketchStyleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.return_type):
            body['ReturnType'] = request.return_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateHumanSketchStyle',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.GenerateHumanSketchStyleResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_human_sketch_style_with_options_async(
        self,
        request: facebody_20191230_models.GenerateHumanSketchStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanSketchStyleResponse:
        """
        @summary 人像素描风格化
        
        @param request: GenerateHumanSketchStyleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateHumanSketchStyleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.return_type):
            body['ReturnType'] = request.return_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateHumanSketchStyle',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.GenerateHumanSketchStyleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_human_sketch_style(
        self,
        request: facebody_20191230_models.GenerateHumanSketchStyleRequest,
    ) -> facebody_20191230_models.GenerateHumanSketchStyleResponse:
        """
        @summary 人像素描风格化
        
        @param request: GenerateHumanSketchStyleRequest
        @return: GenerateHumanSketchStyleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_human_sketch_style_with_options(request, runtime)

    async def generate_human_sketch_style_async(
        self,
        request: facebody_20191230_models.GenerateHumanSketchStyleRequest,
    ) -> facebody_20191230_models.GenerateHumanSketchStyleResponse:
        """
        @summary 人像素描风格化
        
        @param request: GenerateHumanSketchStyleRequest
        @return: GenerateHumanSketchStyleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_human_sketch_style_with_options_async(request, runtime)

    def generate_human_sketch_style_advance(
        self,
        request: facebody_20191230_models.GenerateHumanSketchStyleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanSketchStyleResponse:
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
            'Product': 'facebody',
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
        generate_human_sketch_style_req = facebody_20191230_models.GenerateHumanSketchStyleRequest()
        OpenApiUtilClient.convert(request, generate_human_sketch_style_req)
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
            generate_human_sketch_style_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        generate_human_sketch_style_resp = self.generate_human_sketch_style_with_options(generate_human_sketch_style_req, runtime)
        return generate_human_sketch_style_resp

    async def generate_human_sketch_style_advance_async(
        self,
        request: facebody_20191230_models.GenerateHumanSketchStyleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanSketchStyleResponse:
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
            'Product': 'facebody',
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
        generate_human_sketch_style_req = facebody_20191230_models.GenerateHumanSketchStyleRequest()
        OpenApiUtilClient.convert(request, generate_human_sketch_style_req)
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
            generate_human_sketch_style_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        generate_human_sketch_style_resp = await self.generate_human_sketch_style_with_options_async(generate_human_sketch_style_req, runtime)
        return generate_human_sketch_style_resp

    def get_face_entity_with_options(
        self,
        request: facebody_20191230_models.GetFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GetFaceEntityResponse:
        """
        @param request: GetFaceEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFaceEntityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFaceEntity',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.GetFaceEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_face_entity_with_options_async(
        self,
        request: facebody_20191230_models.GetFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GetFaceEntityResponse:
        """
        @param request: GetFaceEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFaceEntityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFaceEntity',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.GetFaceEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_face_entity(
        self,
        request: facebody_20191230_models.GetFaceEntityRequest,
    ) -> facebody_20191230_models.GetFaceEntityResponse:
        """
        @param request: GetFaceEntityRequest
        @return: GetFaceEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_face_entity_with_options(request, runtime)

    async def get_face_entity_async(
        self,
        request: facebody_20191230_models.GetFaceEntityRequest,
    ) -> facebody_20191230_models.GetFaceEntityResponse:
        """
        @param request: GetFaceEntityRequest
        @return: GetFaceEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_face_entity_with_options_async(request, runtime)

    def get_real_person_verification_result_with_options(
        self,
        request: facebody_20191230_models.GetRealPersonVerificationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GetRealPersonVerificationResultResponse:
        """
        @param request: GetRealPersonVerificationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRealPersonVerificationResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.verification_token):
            body['VerificationToken'] = request.verification_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRealPersonVerificationResult',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.GetRealPersonVerificationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_real_person_verification_result_with_options_async(
        self,
        request: facebody_20191230_models.GetRealPersonVerificationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GetRealPersonVerificationResultResponse:
        """
        @param request: GetRealPersonVerificationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRealPersonVerificationResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.verification_token):
            body['VerificationToken'] = request.verification_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRealPersonVerificationResult',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.GetRealPersonVerificationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_real_person_verification_result(
        self,
        request: facebody_20191230_models.GetRealPersonVerificationResultRequest,
    ) -> facebody_20191230_models.GetRealPersonVerificationResultResponse:
        """
        @param request: GetRealPersonVerificationResultRequest
        @return: GetRealPersonVerificationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_real_person_verification_result_with_options(request, runtime)

    async def get_real_person_verification_result_async(
        self,
        request: facebody_20191230_models.GetRealPersonVerificationResultRequest,
    ) -> facebody_20191230_models.GetRealPersonVerificationResultResponse:
        """
        @param request: GetRealPersonVerificationResultRequest
        @return: GetRealPersonVerificationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_real_person_verification_result_with_options_async(request, runtime)

    def liquify_face_with_options(
        self,
        request: facebody_20191230_models.LiquifyFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.LiquifyFaceResponse:
        """
        @summary 智能瘦脸
        
        @param request: LiquifyFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LiquifyFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.slim_degree):
            body['SlimDegree'] = request.slim_degree
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LiquifyFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.LiquifyFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def liquify_face_with_options_async(
        self,
        request: facebody_20191230_models.LiquifyFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.LiquifyFaceResponse:
        """
        @summary 智能瘦脸
        
        @param request: LiquifyFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LiquifyFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.slim_degree):
            body['SlimDegree'] = request.slim_degree
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LiquifyFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.LiquifyFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def liquify_face(
        self,
        request: facebody_20191230_models.LiquifyFaceRequest,
    ) -> facebody_20191230_models.LiquifyFaceResponse:
        """
        @summary 智能瘦脸
        
        @param request: LiquifyFaceRequest
        @return: LiquifyFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.liquify_face_with_options(request, runtime)

    async def liquify_face_async(
        self,
        request: facebody_20191230_models.LiquifyFaceRequest,
    ) -> facebody_20191230_models.LiquifyFaceResponse:
        """
        @summary 智能瘦脸
        
        @param request: LiquifyFaceRequest
        @return: LiquifyFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.liquify_face_with_options_async(request, runtime)

    def liquify_face_advance(
        self,
        request: facebody_20191230_models.LiquifyFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.LiquifyFaceResponse:
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
            'Product': 'facebody',
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
        liquify_face_req = facebody_20191230_models.LiquifyFaceRequest()
        OpenApiUtilClient.convert(request, liquify_face_req)
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
            liquify_face_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        liquify_face_resp = self.liquify_face_with_options(liquify_face_req, runtime)
        return liquify_face_resp

    async def liquify_face_advance_async(
        self,
        request: facebody_20191230_models.LiquifyFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.LiquifyFaceResponse:
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
            'Product': 'facebody',
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
        liquify_face_req = facebody_20191230_models.LiquifyFaceRequest()
        OpenApiUtilClient.convert(request, liquify_face_req)
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
            liquify_face_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        liquify_face_resp = await self.liquify_face_with_options_async(liquify_face_req, runtime)
        return liquify_face_resp

    def list_face_dbs_with_options(
        self,
        request: facebody_20191230_models.ListFaceDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ListFaceDbsResponse:
        """
        @param request: ListFaceDbsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFaceDbsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFaceDbs',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.ListFaceDbsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_face_dbs_with_options_async(
        self,
        request: facebody_20191230_models.ListFaceDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ListFaceDbsResponse:
        """
        @param request: ListFaceDbsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFaceDbsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFaceDbs',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.ListFaceDbsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_face_dbs(
        self,
        request: facebody_20191230_models.ListFaceDbsRequest,
    ) -> facebody_20191230_models.ListFaceDbsResponse:
        """
        @param request: ListFaceDbsRequest
        @return: ListFaceDbsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_face_dbs_with_options(request, runtime)

    async def list_face_dbs_async(
        self,
        request: facebody_20191230_models.ListFaceDbsRequest,
    ) -> facebody_20191230_models.ListFaceDbsResponse:
        """
        @param request: ListFaceDbsRequest
        @return: ListFaceDbsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_face_dbs_with_options_async(request, runtime)

    def list_face_entities_with_options(
        self,
        request: facebody_20191230_models.ListFaceEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ListFaceEntitiesResponse:
        """
        @param request: ListFaceEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFaceEntitiesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id_prefix):
            body['EntityIdPrefix'] = request.entity_id_prefix
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFaceEntities',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.ListFaceEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_face_entities_with_options_async(
        self,
        request: facebody_20191230_models.ListFaceEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ListFaceEntitiesResponse:
        """
        @param request: ListFaceEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFaceEntitiesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id_prefix):
            body['EntityIdPrefix'] = request.entity_id_prefix
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFaceEntities',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.ListFaceEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_face_entities(
        self,
        request: facebody_20191230_models.ListFaceEntitiesRequest,
    ) -> facebody_20191230_models.ListFaceEntitiesResponse:
        """
        @param request: ListFaceEntitiesRequest
        @return: ListFaceEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_face_entities_with_options(request, runtime)

    async def list_face_entities_async(
        self,
        request: facebody_20191230_models.ListFaceEntitiesRequest,
    ) -> facebody_20191230_models.ListFaceEntitiesResponse:
        """
        @param request: ListFaceEntitiesRequest
        @return: ListFaceEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_face_entities_with_options_async(request, runtime)

    def merge_image_face_with_options(
        self,
        request: facebody_20191230_models.MergeImageFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.MergeImageFaceResponse:
        """
        @summary 图像人脸融合
        
        @param request: MergeImageFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MergeImageFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.add_watermark):
            body['AddWatermark'] = request.add_watermark
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.merge_infos):
            body['MergeInfos'] = request.merge_infos
        if not UtilClient.is_unset(request.model_version):
            body['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.watermark_type):
            body['WatermarkType'] = request.watermark_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MergeImageFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.MergeImageFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def merge_image_face_with_options_async(
        self,
        request: facebody_20191230_models.MergeImageFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.MergeImageFaceResponse:
        """
        @summary 图像人脸融合
        
        @param request: MergeImageFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MergeImageFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.add_watermark):
            body['AddWatermark'] = request.add_watermark
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.merge_infos):
            body['MergeInfos'] = request.merge_infos
        if not UtilClient.is_unset(request.model_version):
            body['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.watermark_type):
            body['WatermarkType'] = request.watermark_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MergeImageFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.MergeImageFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def merge_image_face(
        self,
        request: facebody_20191230_models.MergeImageFaceRequest,
    ) -> facebody_20191230_models.MergeImageFaceResponse:
        """
        @summary 图像人脸融合
        
        @param request: MergeImageFaceRequest
        @return: MergeImageFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.merge_image_face_with_options(request, runtime)

    async def merge_image_face_async(
        self,
        request: facebody_20191230_models.MergeImageFaceRequest,
    ) -> facebody_20191230_models.MergeImageFaceResponse:
        """
        @summary 图像人脸融合
        
        @param request: MergeImageFaceRequest
        @return: MergeImageFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.merge_image_face_with_options_async(request, runtime)

    def merge_image_face_advance(
        self,
        request: facebody_20191230_models.MergeImageFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.MergeImageFaceResponse:
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
            'Product': 'facebody',
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
        merge_image_face_req = facebody_20191230_models.MergeImageFaceRequest()
        OpenApiUtilClient.convert(request, merge_image_face_req)
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
            merge_image_face_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        merge_image_face_resp = self.merge_image_face_with_options(merge_image_face_req, runtime)
        return merge_image_face_resp

    async def merge_image_face_advance_async(
        self,
        request: facebody_20191230_models.MergeImageFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.MergeImageFaceResponse:
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
            'Product': 'facebody',
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
        merge_image_face_req = facebody_20191230_models.MergeImageFaceRequest()
        OpenApiUtilClient.convert(request, merge_image_face_req)
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
            merge_image_face_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        merge_image_face_resp = await self.merge_image_face_with_options_async(merge_image_face_req, runtime)
        return merge_image_face_resp

    def monitor_examination_with_options(
        self,
        request: facebody_20191230_models.MonitorExaminationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.MonitorExaminationResponse:
        """
        @summary 线上监考
        
        @param request: MonitorExaminationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MonitorExaminationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MonitorExamination',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.MonitorExaminationResponse(),
            self.call_api(params, req, runtime)
        )

    async def monitor_examination_with_options_async(
        self,
        request: facebody_20191230_models.MonitorExaminationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.MonitorExaminationResponse:
        """
        @summary 线上监考
        
        @param request: MonitorExaminationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MonitorExaminationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MonitorExamination',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.MonitorExaminationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def monitor_examination(
        self,
        request: facebody_20191230_models.MonitorExaminationRequest,
    ) -> facebody_20191230_models.MonitorExaminationResponse:
        """
        @summary 线上监考
        
        @param request: MonitorExaminationRequest
        @return: MonitorExaminationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.monitor_examination_with_options(request, runtime)

    async def monitor_examination_async(
        self,
        request: facebody_20191230_models.MonitorExaminationRequest,
    ) -> facebody_20191230_models.MonitorExaminationResponse:
        """
        @summary 线上监考
        
        @param request: MonitorExaminationRequest
        @return: MonitorExaminationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.monitor_examination_with_options_async(request, runtime)

    def monitor_examination_advance(
        self,
        request: facebody_20191230_models.MonitorExaminationAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.MonitorExaminationResponse:
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
            'Product': 'facebody',
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
        monitor_examination_req = facebody_20191230_models.MonitorExaminationRequest()
        OpenApiUtilClient.convert(request, monitor_examination_req)
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
            monitor_examination_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        monitor_examination_resp = self.monitor_examination_with_options(monitor_examination_req, runtime)
        return monitor_examination_resp

    async def monitor_examination_advance_async(
        self,
        request: facebody_20191230_models.MonitorExaminationAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.MonitorExaminationResponse:
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
            'Product': 'facebody',
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
        monitor_examination_req = facebody_20191230_models.MonitorExaminationRequest()
        OpenApiUtilClient.convert(request, monitor_examination_req)
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
            monitor_examination_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        monitor_examination_resp = await self.monitor_examination_with_options_async(monitor_examination_req, runtime)
        return monitor_examination_resp

    def pedestrian_detect_attribute_with_options(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
        """
        @param request: PedestrianDetectAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PedestrianDetectAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PedestrianDetectAttribute',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.PedestrianDetectAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def pedestrian_detect_attribute_with_options_async(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
        """
        @param request: PedestrianDetectAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PedestrianDetectAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PedestrianDetectAttribute',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.PedestrianDetectAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pedestrian_detect_attribute(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeRequest,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
        """
        @param request: PedestrianDetectAttributeRequest
        @return: PedestrianDetectAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.pedestrian_detect_attribute_with_options(request, runtime)

    async def pedestrian_detect_attribute_async(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeRequest,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
        """
        @param request: PedestrianDetectAttributeRequest
        @return: PedestrianDetectAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.pedestrian_detect_attribute_with_options_async(request, runtime)

    def pedestrian_detect_attribute_advance(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
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
            'Product': 'facebody',
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
        pedestrian_detect_attribute_req = facebody_20191230_models.PedestrianDetectAttributeRequest()
        OpenApiUtilClient.convert(request, pedestrian_detect_attribute_req)
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
            pedestrian_detect_attribute_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        pedestrian_detect_attribute_resp = self.pedestrian_detect_attribute_with_options(pedestrian_detect_attribute_req, runtime)
        return pedestrian_detect_attribute_resp

    async def pedestrian_detect_attribute_advance_async(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
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
            'Product': 'facebody',
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
        pedestrian_detect_attribute_req = facebody_20191230_models.PedestrianDetectAttributeRequest()
        OpenApiUtilClient.convert(request, pedestrian_detect_attribute_req)
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
            pedestrian_detect_attribute_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        pedestrian_detect_attribute_resp = await self.pedestrian_detect_attribute_with_options_async(pedestrian_detect_attribute_req, runtime)
        return pedestrian_detect_attribute_resp

    def query_face_image_template_with_options(
        self,
        request: facebody_20191230_models.QueryFaceImageTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.QueryFaceImageTemplateResponse:
        """
        @summary 图像人脸融合模板查询
        
        @param request: QueryFaceImageTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFaceImageTemplateResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceImageTemplate',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.QueryFaceImageTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_image_template_with_options_async(
        self,
        request: facebody_20191230_models.QueryFaceImageTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.QueryFaceImageTemplateResponse:
        """
        @summary 图像人脸融合模板查询
        
        @param request: QueryFaceImageTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFaceImageTemplateResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceImageTemplate',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.QueryFaceImageTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_image_template(
        self,
        request: facebody_20191230_models.QueryFaceImageTemplateRequest,
    ) -> facebody_20191230_models.QueryFaceImageTemplateResponse:
        """
        @summary 图像人脸融合模板查询
        
        @param request: QueryFaceImageTemplateRequest
        @return: QueryFaceImageTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_face_image_template_with_options(request, runtime)

    async def query_face_image_template_async(
        self,
        request: facebody_20191230_models.QueryFaceImageTemplateRequest,
    ) -> facebody_20191230_models.QueryFaceImageTemplateResponse:
        """
        @summary 图像人脸融合模板查询
        
        @param request: QueryFaceImageTemplateRequest
        @return: QueryFaceImageTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_face_image_template_with_options_async(request, runtime)

    def recognize_action_with_options(
        self,
        request: facebody_20191230_models.RecognizeActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeActionResponse:
        """
        @summary 动作行为识别(RecognizeAction)
        
        @param request: RecognizeActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeActionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        if not UtilClient.is_unset(request.video_data):
            body['VideoData'] = request.video_data
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeAction',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.RecognizeActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_action_with_options_async(
        self,
        request: facebody_20191230_models.RecognizeActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeActionResponse:
        """
        @summary 动作行为识别(RecognizeAction)
        
        @param request: RecognizeActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeActionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        if not UtilClient.is_unset(request.video_data):
            body['VideoData'] = request.video_data
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeAction',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.RecognizeActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_action(
        self,
        request: facebody_20191230_models.RecognizeActionRequest,
    ) -> facebody_20191230_models.RecognizeActionResponse:
        """
        @summary 动作行为识别(RecognizeAction)
        
        @param request: RecognizeActionRequest
        @return: RecognizeActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_action_with_options(request, runtime)

    async def recognize_action_async(
        self,
        request: facebody_20191230_models.RecognizeActionRequest,
    ) -> facebody_20191230_models.RecognizeActionResponse:
        """
        @summary 动作行为识别(RecognizeAction)
        
        @param request: RecognizeActionRequest
        @return: RecognizeActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_action_with_options_async(request, runtime)

    def recognize_action_advance(
        self,
        request: facebody_20191230_models.RecognizeActionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeActionResponse:
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
            'Product': 'facebody',
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
        recognize_action_req = facebody_20191230_models.RecognizeActionRequest()
        OpenApiUtilClient.convert(request, recognize_action_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
                    auth_response = UtilClient.assert_as_map(tmp_resp_0)
                    tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
                    use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
                    auth_response_body = UtilClient.stringify_map_value(tmp_body)
                    file_obj = file_form_models.FileField(
                        filename=auth_response_body.get('ObjectKey'),
                        content=item_0.urlobject,
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
                    tmp = recognize_action_req.urllist[i_0]
                    tmp.url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        if not UtilClient.is_unset(request.video_url_object):
            tmp_resp_1 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.video_url_object,
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
            recognize_action_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_action_resp = self.recognize_action_with_options(recognize_action_req, runtime)
        return recognize_action_resp

    async def recognize_action_advance_async(
        self,
        request: facebody_20191230_models.RecognizeActionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeActionResponse:
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
            'Product': 'facebody',
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
        recognize_action_req = facebody_20191230_models.RecognizeActionRequest()
        OpenApiUtilClient.convert(request, recognize_action_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
                    auth_response = UtilClient.assert_as_map(tmp_resp_0)
                    tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
                    use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
                    auth_response_body = UtilClient.stringify_map_value(tmp_body)
                    file_obj = file_form_models.FileField(
                        filename=auth_response_body.get('ObjectKey'),
                        content=item_0.urlobject,
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
                    tmp = recognize_action_req.urllist[i_0]
                    tmp.url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        if not UtilClient.is_unset(request.video_url_object):
            tmp_resp_1 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.video_url_object,
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
            recognize_action_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_action_resp = await self.recognize_action_with_options_async(recognize_action_req, runtime)
        return recognize_action_resp

    def recognize_expression_with_options(
        self,
        request: facebody_20191230_models.RecognizeExpressionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
        """
        @param request: RecognizeExpressionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeExpressionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeExpression',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.RecognizeExpressionResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_expression_with_options_async(
        self,
        request: facebody_20191230_models.RecognizeExpressionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
        """
        @param request: RecognizeExpressionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeExpressionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeExpression',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.RecognizeExpressionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_expression(
        self,
        request: facebody_20191230_models.RecognizeExpressionRequest,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
        """
        @param request: RecognizeExpressionRequest
        @return: RecognizeExpressionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_expression_with_options(request, runtime)

    async def recognize_expression_async(
        self,
        request: facebody_20191230_models.RecognizeExpressionRequest,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
        """
        @param request: RecognizeExpressionRequest
        @return: RecognizeExpressionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_expression_with_options_async(request, runtime)

    def recognize_expression_advance(
        self,
        request: facebody_20191230_models.RecognizeExpressionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
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
            'Product': 'facebody',
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
        recognize_expression_req = facebody_20191230_models.RecognizeExpressionRequest()
        OpenApiUtilClient.convert(request, recognize_expression_req)
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
            recognize_expression_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_expression_resp = self.recognize_expression_with_options(recognize_expression_req, runtime)
        return recognize_expression_resp

    async def recognize_expression_advance_async(
        self,
        request: facebody_20191230_models.RecognizeExpressionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
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
            'Product': 'facebody',
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
        recognize_expression_req = facebody_20191230_models.RecognizeExpressionRequest()
        OpenApiUtilClient.convert(request, recognize_expression_req)
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
            recognize_expression_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_expression_resp = await self.recognize_expression_with_options_async(recognize_expression_req, runtime)
        return recognize_expression_resp

    def recognize_face_with_options(
        self,
        request: facebody_20191230_models.RecognizeFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
        """
        @param request: RecognizeFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.age):
            body['Age'] = request.age
        if not UtilClient.is_unset(request.beauty):
            body['Beauty'] = request.beauty
        if not UtilClient.is_unset(request.expression):
            body['Expression'] = request.expression
        if not UtilClient.is_unset(request.gender):
            body['Gender'] = request.gender
        if not UtilClient.is_unset(request.glass):
            body['Glass'] = request.glass
        if not UtilClient.is_unset(request.hat):
            body['Hat'] = request.hat
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.mask):
            body['Mask'] = request.mask
        if not UtilClient.is_unset(request.max_face_number):
            body['MaxFaceNumber'] = request.max_face_number
        if not UtilClient.is_unset(request.quality):
            body['Quality'] = request.quality
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.RecognizeFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_face_with_options_async(
        self,
        request: facebody_20191230_models.RecognizeFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
        """
        @param request: RecognizeFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.age):
            body['Age'] = request.age
        if not UtilClient.is_unset(request.beauty):
            body['Beauty'] = request.beauty
        if not UtilClient.is_unset(request.expression):
            body['Expression'] = request.expression
        if not UtilClient.is_unset(request.gender):
            body['Gender'] = request.gender
        if not UtilClient.is_unset(request.glass):
            body['Glass'] = request.glass
        if not UtilClient.is_unset(request.hat):
            body['Hat'] = request.hat
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.mask):
            body['Mask'] = request.mask
        if not UtilClient.is_unset(request.max_face_number):
            body['MaxFaceNumber'] = request.max_face_number
        if not UtilClient.is_unset(request.quality):
            body['Quality'] = request.quality
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.RecognizeFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_face(
        self,
        request: facebody_20191230_models.RecognizeFaceRequest,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
        """
        @param request: RecognizeFaceRequest
        @return: RecognizeFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_face_with_options(request, runtime)

    async def recognize_face_async(
        self,
        request: facebody_20191230_models.RecognizeFaceRequest,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
        """
        @param request: RecognizeFaceRequest
        @return: RecognizeFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_face_with_options_async(request, runtime)

    def recognize_face_advance(
        self,
        request: facebody_20191230_models.RecognizeFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
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
            'Product': 'facebody',
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
        recognize_face_req = facebody_20191230_models.RecognizeFaceRequest()
        OpenApiUtilClient.convert(request, recognize_face_req)
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
            recognize_face_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_face_resp = self.recognize_face_with_options(recognize_face_req, runtime)
        return recognize_face_resp

    async def recognize_face_advance_async(
        self,
        request: facebody_20191230_models.RecognizeFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
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
            'Product': 'facebody',
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
        recognize_face_req = facebody_20191230_models.RecognizeFaceRequest()
        OpenApiUtilClient.convert(request, recognize_face_req)
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
            recognize_face_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_face_resp = await self.recognize_face_with_options_async(recognize_face_req, runtime)
        return recognize_face_resp

    def recognize_public_face_with_options(
        self,
        request: facebody_20191230_models.RecognizePublicFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizePublicFaceResponse:
        """
        @summary 公众人脸识别(RecognizePublicFace)
        
        @param request: RecognizePublicFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizePublicFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizePublicFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.RecognizePublicFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_public_face_with_options_async(
        self,
        request: facebody_20191230_models.RecognizePublicFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizePublicFaceResponse:
        """
        @summary 公众人脸识别(RecognizePublicFace)
        
        @param request: RecognizePublicFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizePublicFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizePublicFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.RecognizePublicFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_public_face(
        self,
        request: facebody_20191230_models.RecognizePublicFaceRequest,
    ) -> facebody_20191230_models.RecognizePublicFaceResponse:
        """
        @summary 公众人脸识别(RecognizePublicFace)
        
        @param request: RecognizePublicFaceRequest
        @return: RecognizePublicFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_public_face_with_options(request, runtime)

    async def recognize_public_face_async(
        self,
        request: facebody_20191230_models.RecognizePublicFaceRequest,
    ) -> facebody_20191230_models.RecognizePublicFaceResponse:
        """
        @summary 公众人脸识别(RecognizePublicFace)
        
        @param request: RecognizePublicFaceRequest
        @return: RecognizePublicFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_public_face_with_options_async(request, runtime)

    def recognize_public_face_advance(
        self,
        request: facebody_20191230_models.RecognizePublicFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizePublicFaceResponse:
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
            'Product': 'facebody',
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
        recognize_public_face_req = facebody_20191230_models.RecognizePublicFaceRequest()
        OpenApiUtilClient.convert(request, recognize_public_face_req)
        if not UtilClient.is_unset(request.task):
            i_0 = 0
            for item_0 in request.task:
                if not UtilClient.is_unset(item_0.image_urlobject):
                    tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
                    auth_response = UtilClient.assert_as_map(tmp_resp_0)
                    tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
                    use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
                    auth_response_body = UtilClient.stringify_map_value(tmp_body)
                    file_obj = file_form_models.FileField(
                        filename=auth_response_body.get('ObjectKey'),
                        content=item_0.image_urlobject,
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
                    tmp = recognize_public_face_req.task[i_0]
                    tmp.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        recognize_public_face_resp = self.recognize_public_face_with_options(recognize_public_face_req, runtime)
        return recognize_public_face_resp

    async def recognize_public_face_advance_async(
        self,
        request: facebody_20191230_models.RecognizePublicFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizePublicFaceResponse:
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
            'Product': 'facebody',
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
        recognize_public_face_req = facebody_20191230_models.RecognizePublicFaceRequest()
        OpenApiUtilClient.convert(request, recognize_public_face_req)
        if not UtilClient.is_unset(request.task):
            i_0 = 0
            for item_0 in request.task:
                if not UtilClient.is_unset(item_0.image_urlobject):
                    tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
                    auth_response = UtilClient.assert_as_map(tmp_resp_0)
                    tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
                    use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
                    auth_response_body = UtilClient.stringify_map_value(tmp_body)
                    file_obj = file_form_models.FileField(
                        filename=auth_response_body.get('ObjectKey'),
                        content=item_0.image_urlobject,
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
                    tmp = recognize_public_face_req.task[i_0]
                    tmp.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        recognize_public_face_resp = await self.recognize_public_face_with_options_async(recognize_public_face_req, runtime)
        return recognize_public_face_resp

    def retouch_skin_with_options(
        self,
        request: facebody_20191230_models.RetouchSkinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RetouchSkinResponse:
        """
        @summary 美肤
        
        @param request: RetouchSkinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetouchSkinResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.retouch_degree):
            body['RetouchDegree'] = request.retouch_degree
        if not UtilClient.is_unset(request.whitening_degree):
            body['WhiteningDegree'] = request.whitening_degree
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetouchSkin',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.RetouchSkinResponse(),
            self.call_api(params, req, runtime)
        )

    async def retouch_skin_with_options_async(
        self,
        request: facebody_20191230_models.RetouchSkinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RetouchSkinResponse:
        """
        @summary 美肤
        
        @param request: RetouchSkinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetouchSkinResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.retouch_degree):
            body['RetouchDegree'] = request.retouch_degree
        if not UtilClient.is_unset(request.whitening_degree):
            body['WhiteningDegree'] = request.whitening_degree
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetouchSkin',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.RetouchSkinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retouch_skin(
        self,
        request: facebody_20191230_models.RetouchSkinRequest,
    ) -> facebody_20191230_models.RetouchSkinResponse:
        """
        @summary 美肤
        
        @param request: RetouchSkinRequest
        @return: RetouchSkinResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.retouch_skin_with_options(request, runtime)

    async def retouch_skin_async(
        self,
        request: facebody_20191230_models.RetouchSkinRequest,
    ) -> facebody_20191230_models.RetouchSkinResponse:
        """
        @summary 美肤
        
        @param request: RetouchSkinRequest
        @return: RetouchSkinResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.retouch_skin_with_options_async(request, runtime)

    def retouch_skin_advance(
        self,
        request: facebody_20191230_models.RetouchSkinAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RetouchSkinResponse:
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
            'Product': 'facebody',
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
        retouch_skin_req = facebody_20191230_models.RetouchSkinRequest()
        OpenApiUtilClient.convert(request, retouch_skin_req)
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
            retouch_skin_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        retouch_skin_resp = self.retouch_skin_with_options(retouch_skin_req, runtime)
        return retouch_skin_resp

    async def retouch_skin_advance_async(
        self,
        request: facebody_20191230_models.RetouchSkinAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RetouchSkinResponse:
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
            'Product': 'facebody',
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
        retouch_skin_req = facebody_20191230_models.RetouchSkinRequest()
        OpenApiUtilClient.convert(request, retouch_skin_req)
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
            retouch_skin_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        retouch_skin_resp = await self.retouch_skin_with_options_async(retouch_skin_req, runtime)
        return retouch_skin_resp

    def search_face_with_options(
        self,
        request: facebody_20191230_models.SearchFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SearchFaceResponse:
        """
        @summary summary
        
        @param request: SearchFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.db_names):
            body['DbNames'] = request.db_names
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.max_face_num):
            body['MaxFaceNum'] = request.max_face_num
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.SearchFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_face_with_options_async(
        self,
        request: facebody_20191230_models.SearchFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SearchFaceResponse:
        """
        @summary summary
        
        @param request: SearchFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.db_names):
            body['DbNames'] = request.db_names
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.max_face_num):
            body['MaxFaceNum'] = request.max_face_num
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFace',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.SearchFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_face(
        self,
        request: facebody_20191230_models.SearchFaceRequest,
    ) -> facebody_20191230_models.SearchFaceResponse:
        """
        @summary summary
        
        @param request: SearchFaceRequest
        @return: SearchFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_face_with_options(request, runtime)

    async def search_face_async(
        self,
        request: facebody_20191230_models.SearchFaceRequest,
    ) -> facebody_20191230_models.SearchFaceResponse:
        """
        @summary summary
        
        @param request: SearchFaceRequest
        @return: SearchFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_face_with_options_async(request, runtime)

    def search_face_advance(
        self,
        request: facebody_20191230_models.SearchFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SearchFaceResponse:
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
            'Product': 'facebody',
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
        search_face_req = facebody_20191230_models.SearchFaceRequest()
        OpenApiUtilClient.convert(request, search_face_req)
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
            search_face_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        search_face_resp = self.search_face_with_options(search_face_req, runtime)
        return search_face_resp

    async def search_face_advance_async(
        self,
        request: facebody_20191230_models.SearchFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SearchFaceResponse:
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
            'Product': 'facebody',
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
        search_face_req = facebody_20191230_models.SearchFaceRequest()
        OpenApiUtilClient.convert(request, search_face_req)
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
            search_face_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        search_face_resp = await self.search_face_with_options_async(search_face_req, runtime)
        return search_face_resp

    def update_face_entity_with_options(
        self,
        request: facebody_20191230_models.UpdateFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.UpdateFaceEntityResponse:
        """
        @param request: UpdateFaceEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFaceEntityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFaceEntity',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.UpdateFaceEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_face_entity_with_options_async(
        self,
        request: facebody_20191230_models.UpdateFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.UpdateFaceEntityResponse:
        """
        @param request: UpdateFaceEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFaceEntityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFaceEntity',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.UpdateFaceEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_face_entity(
        self,
        request: facebody_20191230_models.UpdateFaceEntityRequest,
    ) -> facebody_20191230_models.UpdateFaceEntityResponse:
        """
        @param request: UpdateFaceEntityRequest
        @return: UpdateFaceEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_face_entity_with_options(request, runtime)

    async def update_face_entity_async(
        self,
        request: facebody_20191230_models.UpdateFaceEntityRequest,
    ) -> facebody_20191230_models.UpdateFaceEntityResponse:
        """
        @param request: UpdateFaceEntityRequest
        @return: UpdateFaceEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_face_entity_with_options_async(request, runtime)
