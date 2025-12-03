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
from alibabacloud_alimt20181012 import models as alimt_20181012_models
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
        self._endpoint_map = {
            'cn-hangzhou': 'mt.cn-hangzhou.aliyuncs.com',
            'ap-northeast-1': 'mt.aliyuncs.com',
            'ap-northeast-2-pop': 'mt.aliyuncs.com',
            'ap-south-1': 'mt.aliyuncs.com',
            'ap-southeast-1': 'mt.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'mt.aliyuncs.com',
            'ap-southeast-3': 'mt.aliyuncs.com',
            'ap-southeast-5': 'mt.aliyuncs.com',
            'cn-beijing': 'mt.aliyuncs.com',
            'cn-beijing-finance-1': 'mt.aliyuncs.com',
            'cn-beijing-finance-pop': 'mt.aliyuncs.com',
            'cn-beijing-gov-1': 'mt.aliyuncs.com',
            'cn-beijing-nu16-b01': 'mt.aliyuncs.com',
            'cn-chengdu': 'mt.aliyuncs.com',
            'cn-edge-1': 'mt.aliyuncs.com',
            'cn-fujian': 'mt.aliyuncs.com',
            'cn-haidian-cm12-c01': 'mt.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'mt.aliyuncs.com',
            'cn-hangzhou-finance': 'mt.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'mt.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'mt.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'mt.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'mt.aliyuncs.com',
            'cn-hangzhou-test-306': 'mt.aliyuncs.com',
            'cn-hongkong': 'mt.aliyuncs.com',
            'cn-hongkong-finance-pop': 'mt.aliyuncs.com',
            'cn-huhehaote': 'mt.aliyuncs.com',
            'cn-north-2-gov-1': 'mt.aliyuncs.com',
            'cn-qingdao': 'mt.aliyuncs.com',
            'cn-qingdao-nebula': 'mt.aliyuncs.com',
            'cn-shanghai': 'mt.aliyuncs.com',
            'cn-shanghai-et15-b01': 'mt.aliyuncs.com',
            'cn-shanghai-et2-b01': 'mt.aliyuncs.com',
            'cn-shanghai-finance-1': 'mt.aliyuncs.com',
            'cn-shanghai-inner': 'mt.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'mt.aliyuncs.com',
            'cn-shenzhen': 'mt.aliyuncs.com',
            'cn-shenzhen-finance-1': 'mt.aliyuncs.com',
            'cn-shenzhen-inner': 'mt.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'mt.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'mt.aliyuncs.com',
            'cn-wuhan': 'mt.aliyuncs.com',
            'cn-yushanfang': 'mt.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'mt.aliyuncs.com',
            'cn-zhangjiakou': 'mt.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'mt.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'mt.aliyuncs.com',
            'eu-central-1': 'mt.aliyuncs.com',
            'eu-west-1': 'mt.aliyuncs.com',
            'eu-west-1-oxs': 'mt.aliyuncs.com',
            'me-east-1': 'mt.aliyuncs.com',
            'rus-west-1-pop': 'mt.aliyuncs.com',
            'us-east-1': 'mt.aliyuncs.com',
            'us-west-1': 'mt.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('alimt', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_async_translate_with_options(
        self,
        request: alimt_20181012_models.CreateAsyncTranslateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.CreateAsyncTranslateResponse:
        """
        @summary 大文本异步翻译，支持5000-50000字翻译
        
        @param request: CreateAsyncTranslateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAsyncTranslateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_type):
            body['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAsyncTranslate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.CreateAsyncTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_async_translate_with_options_async(
        self,
        request: alimt_20181012_models.CreateAsyncTranslateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.CreateAsyncTranslateResponse:
        """
        @summary 大文本异步翻译，支持5000-50000字翻译
        
        @param request: CreateAsyncTranslateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAsyncTranslateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_type):
            body['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAsyncTranslate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.CreateAsyncTranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_async_translate(
        self,
        request: alimt_20181012_models.CreateAsyncTranslateRequest,
    ) -> alimt_20181012_models.CreateAsyncTranslateResponse:
        """
        @summary 大文本异步翻译，支持5000-50000字翻译
        
        @param request: CreateAsyncTranslateRequest
        @return: CreateAsyncTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_async_translate_with_options(request, runtime)

    async def create_async_translate_async(
        self,
        request: alimt_20181012_models.CreateAsyncTranslateRequest,
    ) -> alimt_20181012_models.CreateAsyncTranslateResponse:
        """
        @summary 大文本异步翻译，支持5000-50000字翻译
        
        @param request: CreateAsyncTranslateRequest
        @return: CreateAsyncTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_async_translate_with_options_async(request, runtime)

    def create_doc_translate_task_with_options(
        self,
        request: alimt_20181012_models.CreateDocTranslateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.CreateDocTranslateTaskResponse:
        """
        @param request: CreateDocTranslateTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDocTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDocTranslateTask',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.CreateDocTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_doc_translate_task_with_options_async(
        self,
        request: alimt_20181012_models.CreateDocTranslateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.CreateDocTranslateTaskResponse:
        """
        @param request: CreateDocTranslateTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDocTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDocTranslateTask',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.CreateDocTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_doc_translate_task(
        self,
        request: alimt_20181012_models.CreateDocTranslateTaskRequest,
    ) -> alimt_20181012_models.CreateDocTranslateTaskResponse:
        """
        @param request: CreateDocTranslateTaskRequest
        @return: CreateDocTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_doc_translate_task_with_options(request, runtime)

    async def create_doc_translate_task_async(
        self,
        request: alimt_20181012_models.CreateDocTranslateTaskRequest,
    ) -> alimt_20181012_models.CreateDocTranslateTaskResponse:
        """
        @param request: CreateDocTranslateTaskRequest
        @return: CreateDocTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_doc_translate_task_with_options_async(request, runtime)

    def create_doc_translate_task_advance(
        self,
        request: alimt_20181012_models.CreateDocTranslateTaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.CreateDocTranslateTaskResponse:
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
            'Product': 'alimt',
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
        create_doc_translate_task_req = alimt_20181012_models.CreateDocTranslateTaskRequest()
        OpenApiUtilClient.convert(request, create_doc_translate_task_req)
        if not UtilClient.is_unset(request.file_url_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_url_object,
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
            create_doc_translate_task_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        create_doc_translate_task_resp = self.create_doc_translate_task_with_options(create_doc_translate_task_req, runtime)
        return create_doc_translate_task_resp

    async def create_doc_translate_task_advance_async(
        self,
        request: alimt_20181012_models.CreateDocTranslateTaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.CreateDocTranslateTaskResponse:
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
            'Product': 'alimt',
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
        create_doc_translate_task_req = alimt_20181012_models.CreateDocTranslateTaskRequest()
        OpenApiUtilClient.convert(request, create_doc_translate_task_req)
        if not UtilClient.is_unset(request.file_url_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_url_object,
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
            create_doc_translate_task_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        create_doc_translate_task_resp = await self.create_doc_translate_task_with_options_async(create_doc_translate_task_req, runtime)
        return create_doc_translate_task_resp

    def create_image_translate_task_with_options(
        self,
        request: alimt_20181012_models.CreateImageTranslateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.CreateImageTranslateTaskResponse:
        """
        @summary 创建图片翻译任务
        
        @param request: CreateImageTranslateTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.url_list):
            body['UrlList'] = request.url_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateImageTranslateTask',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.CreateImageTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_translate_task_with_options_async(
        self,
        request: alimt_20181012_models.CreateImageTranslateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.CreateImageTranslateTaskResponse:
        """
        @summary 创建图片翻译任务
        
        @param request: CreateImageTranslateTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.url_list):
            body['UrlList'] = request.url_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateImageTranslateTask',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.CreateImageTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_translate_task(
        self,
        request: alimt_20181012_models.CreateImageTranslateTaskRequest,
    ) -> alimt_20181012_models.CreateImageTranslateTaskResponse:
        """
        @summary 创建图片翻译任务
        
        @param request: CreateImageTranslateTaskRequest
        @return: CreateImageTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_image_translate_task_with_options(request, runtime)

    async def create_image_translate_task_async(
        self,
        request: alimt_20181012_models.CreateImageTranslateTaskRequest,
    ) -> alimt_20181012_models.CreateImageTranslateTaskResponse:
        """
        @summary 创建图片翻译任务
        
        @param request: CreateImageTranslateTaskRequest
        @return: CreateImageTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_image_translate_task_with_options_async(request, runtime)

    def get_async_translate_with_options(
        self,
        request: alimt_20181012_models.GetAsyncTranslateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetAsyncTranslateResponse:
        """
        @summary 大文本异步翻译，支持5000-50000字翻译
        
        @param request: GetAsyncTranslateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncTranslateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAsyncTranslate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetAsyncTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_translate_with_options_async(
        self,
        request: alimt_20181012_models.GetAsyncTranslateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetAsyncTranslateResponse:
        """
        @summary 大文本异步翻译，支持5000-50000字翻译
        
        @param request: GetAsyncTranslateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncTranslateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAsyncTranslate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetAsyncTranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_translate(
        self,
        request: alimt_20181012_models.GetAsyncTranslateRequest,
    ) -> alimt_20181012_models.GetAsyncTranslateResponse:
        """
        @summary 大文本异步翻译，支持5000-50000字翻译
        
        @param request: GetAsyncTranslateRequest
        @return: GetAsyncTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_async_translate_with_options(request, runtime)

    async def get_async_translate_async(
        self,
        request: alimt_20181012_models.GetAsyncTranslateRequest,
    ) -> alimt_20181012_models.GetAsyncTranslateResponse:
        """
        @summary 大文本异步翻译，支持5000-50000字翻译
        
        @param request: GetAsyncTranslateRequest
        @return: GetAsyncTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_async_translate_with_options_async(request, runtime)

    def get_batch_translate_with_options(
        self,
        request: alimt_20181012_models.GetBatchTranslateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetBatchTranslateResponse:
        """
        @summary 批量文本翻译
        
        @param request: GetBatchTranslateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBatchTranslateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_type):
            body['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBatchTranslate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetBatchTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_translate_with_options_async(
        self,
        request: alimt_20181012_models.GetBatchTranslateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetBatchTranslateResponse:
        """
        @summary 批量文本翻译
        
        @param request: GetBatchTranslateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBatchTranslateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_type):
            body['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBatchTranslate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetBatchTranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch_translate(
        self,
        request: alimt_20181012_models.GetBatchTranslateRequest,
    ) -> alimt_20181012_models.GetBatchTranslateResponse:
        """
        @summary 批量文本翻译
        
        @param request: GetBatchTranslateRequest
        @return: GetBatchTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_batch_translate_with_options(request, runtime)

    async def get_batch_translate_async(
        self,
        request: alimt_20181012_models.GetBatchTranslateRequest,
    ) -> alimt_20181012_models.GetBatchTranslateResponse:
        """
        @summary 批量文本翻译
        
        @param request: GetBatchTranslateRequest
        @return: GetBatchTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_batch_translate_with_options_async(request, runtime)

    def get_batch_translate_by_vpcwith_options(
        self,
        request: alimt_20181012_models.GetBatchTranslateByVPCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetBatchTranslateByVPCResponse:
        """
        @summary GetBatchTranslateByVPC
        
        @param request: GetBatchTranslateByVPCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBatchTranslateByVPCResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_type):
            body['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBatchTranslateByVPC',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetBatchTranslateByVPCResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_translate_by_vpcwith_options_async(
        self,
        request: alimt_20181012_models.GetBatchTranslateByVPCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetBatchTranslateByVPCResponse:
        """
        @summary GetBatchTranslateByVPC
        
        @param request: GetBatchTranslateByVPCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBatchTranslateByVPCResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_type):
            body['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBatchTranslateByVPC',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetBatchTranslateByVPCResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch_translate_by_vpc(
        self,
        request: alimt_20181012_models.GetBatchTranslateByVPCRequest,
    ) -> alimt_20181012_models.GetBatchTranslateByVPCResponse:
        """
        @summary GetBatchTranslateByVPC
        
        @param request: GetBatchTranslateByVPCRequest
        @return: GetBatchTranslateByVPCResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_batch_translate_by_vpcwith_options(request, runtime)

    async def get_batch_translate_by_vpc_async(
        self,
        request: alimt_20181012_models.GetBatchTranslateByVPCRequest,
    ) -> alimt_20181012_models.GetBatchTranslateByVPCResponse:
        """
        @summary GetBatchTranslateByVPC
        
        @param request: GetBatchTranslateByVPCRequest
        @return: GetBatchTranslateByVPCResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_batch_translate_by_vpcwith_options_async(request, runtime)

    def get_detect_language_with_options(
        self,
        request: alimt_20181012_models.GetDetectLanguageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetDetectLanguageResponse:
        """
        @summary 语种识别
        
        @param request: GetDetectLanguageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDetectLanguageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDetectLanguage',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetDetectLanguageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_detect_language_with_options_async(
        self,
        request: alimt_20181012_models.GetDetectLanguageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetDetectLanguageResponse:
        """
        @summary 语种识别
        
        @param request: GetDetectLanguageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDetectLanguageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDetectLanguage',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetDetectLanguageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_detect_language(
        self,
        request: alimt_20181012_models.GetDetectLanguageRequest,
    ) -> alimt_20181012_models.GetDetectLanguageResponse:
        """
        @summary 语种识别
        
        @param request: GetDetectLanguageRequest
        @return: GetDetectLanguageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_detect_language_with_options(request, runtime)

    async def get_detect_language_async(
        self,
        request: alimt_20181012_models.GetDetectLanguageRequest,
    ) -> alimt_20181012_models.GetDetectLanguageResponse:
        """
        @summary 语种识别
        
        @param request: GetDetectLanguageRequest
        @return: GetDetectLanguageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_detect_language_with_options_async(request, runtime)

    def get_detect_language_vpc_with_options(
        self,
        request: alimt_20181012_models.GetDetectLanguageVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetDetectLanguageVpcResponse:
        """
        @summary 语种识别
        
        @param request: GetDetectLanguageVpcRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDetectLanguageVpcResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDetectLanguageVpc',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetDetectLanguageVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_detect_language_vpc_with_options_async(
        self,
        request: alimt_20181012_models.GetDetectLanguageVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetDetectLanguageVpcResponse:
        """
        @summary 语种识别
        
        @param request: GetDetectLanguageVpcRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDetectLanguageVpcResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDetectLanguageVpc',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetDetectLanguageVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_detect_language_vpc(
        self,
        request: alimt_20181012_models.GetDetectLanguageVpcRequest,
    ) -> alimt_20181012_models.GetDetectLanguageVpcResponse:
        """
        @summary 语种识别
        
        @param request: GetDetectLanguageVpcRequest
        @return: GetDetectLanguageVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_detect_language_vpc_with_options(request, runtime)

    async def get_detect_language_vpc_async(
        self,
        request: alimt_20181012_models.GetDetectLanguageVpcRequest,
    ) -> alimt_20181012_models.GetDetectLanguageVpcResponse:
        """
        @summary 语种识别
        
        @param request: GetDetectLanguageVpcRequest
        @return: GetDetectLanguageVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_detect_language_vpc_with_options_async(request, runtime)

    def get_doc_translate_task_with_options(
        self,
        request: alimt_20181012_models.GetDocTranslateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetDocTranslateTaskResponse:
        """
        @summary 获取文档翻译任务
        
        @param request: GetDocTranslateTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocTranslateTask',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetDocTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doc_translate_task_with_options_async(
        self,
        request: alimt_20181012_models.GetDocTranslateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetDocTranslateTaskResponse:
        """
        @summary 获取文档翻译任务
        
        @param request: GetDocTranslateTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocTranslateTask',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetDocTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doc_translate_task(
        self,
        request: alimt_20181012_models.GetDocTranslateTaskRequest,
    ) -> alimt_20181012_models.GetDocTranslateTaskResponse:
        """
        @summary 获取文档翻译任务
        
        @param request: GetDocTranslateTaskRequest
        @return: GetDocTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doc_translate_task_with_options(request, runtime)

    async def get_doc_translate_task_async(
        self,
        request: alimt_20181012_models.GetDocTranslateTaskRequest,
    ) -> alimt_20181012_models.GetDocTranslateTaskResponse:
        """
        @summary 获取文档翻译任务
        
        @param request: GetDocTranslateTaskRequest
        @return: GetDocTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doc_translate_task_with_options_async(request, runtime)

    def get_image_diagnose_with_options(
        self,
        request: alimt_20181012_models.GetImageDiagnoseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetImageDiagnoseResponse:
        """
        @param request: GetImageDiagnoseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageDiagnoseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetImageDiagnose',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetImageDiagnoseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_diagnose_with_options_async(
        self,
        request: alimt_20181012_models.GetImageDiagnoseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetImageDiagnoseResponse:
        """
        @param request: GetImageDiagnoseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageDiagnoseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetImageDiagnose',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetImageDiagnoseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_diagnose(
        self,
        request: alimt_20181012_models.GetImageDiagnoseRequest,
    ) -> alimt_20181012_models.GetImageDiagnoseResponse:
        """
        @param request: GetImageDiagnoseRequest
        @return: GetImageDiagnoseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_image_diagnose_with_options(request, runtime)

    async def get_image_diagnose_async(
        self,
        request: alimt_20181012_models.GetImageDiagnoseRequest,
    ) -> alimt_20181012_models.GetImageDiagnoseResponse:
        """
        @param request: GetImageDiagnoseRequest
        @return: GetImageDiagnoseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_image_diagnose_with_options_async(request, runtime)

    def get_image_translate_with_options(
        self,
        request: alimt_20181012_models.GetImageTranslateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetImageTranslateResponse:
        """
        @summary 获取图片翻译结果
        
        @param request: GetImageTranslateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageTranslateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetImageTranslate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetImageTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_translate_with_options_async(
        self,
        request: alimt_20181012_models.GetImageTranslateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetImageTranslateResponse:
        """
        @summary 获取图片翻译结果
        
        @param request: GetImageTranslateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageTranslateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetImageTranslate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetImageTranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_translate(
        self,
        request: alimt_20181012_models.GetImageTranslateRequest,
    ) -> alimt_20181012_models.GetImageTranslateResponse:
        """
        @summary 获取图片翻译结果
        
        @param request: GetImageTranslateRequest
        @return: GetImageTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_image_translate_with_options(request, runtime)

    async def get_image_translate_async(
        self,
        request: alimt_20181012_models.GetImageTranslateRequest,
    ) -> alimt_20181012_models.GetImageTranslateResponse:
        """
        @summary 获取图片翻译结果
        
        @param request: GetImageTranslateRequest
        @return: GetImageTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_image_translate_with_options_async(request, runtime)

    def get_image_translate_task_with_options(
        self,
        request: alimt_20181012_models.GetImageTranslateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetImageTranslateTaskResponse:
        """
        @summary 获取图片翻译任务
        
        @param request: GetImageTranslateTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetImageTranslateTask',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetImageTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_translate_task_with_options_async(
        self,
        request: alimt_20181012_models.GetImageTranslateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetImageTranslateTaskResponse:
        """
        @summary 获取图片翻译任务
        
        @param request: GetImageTranslateTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetImageTranslateTask',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetImageTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_translate_task(
        self,
        request: alimt_20181012_models.GetImageTranslateTaskRequest,
    ) -> alimt_20181012_models.GetImageTranslateTaskResponse:
        """
        @summary 获取图片翻译任务
        
        @param request: GetImageTranslateTaskRequest
        @return: GetImageTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_image_translate_task_with_options(request, runtime)

    async def get_image_translate_task_async(
        self,
        request: alimt_20181012_models.GetImageTranslateTaskRequest,
    ) -> alimt_20181012_models.GetImageTranslateTaskResponse:
        """
        @summary 获取图片翻译任务
        
        @param request: GetImageTranslateTaskRequest
        @return: GetImageTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_image_translate_task_with_options_async(request, runtime)

    def get_title_diagnose_with_options(
        self,
        request: alimt_20181012_models.GetTitleDiagnoseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetTitleDiagnoseResponse:
        """
        @summary GetTitleDiagnose
        
        @param request: GetTitleDiagnoseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTitleDiagnoseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTitleDiagnose',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetTitleDiagnoseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_title_diagnose_with_options_async(
        self,
        request: alimt_20181012_models.GetTitleDiagnoseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetTitleDiagnoseResponse:
        """
        @summary GetTitleDiagnose
        
        @param request: GetTitleDiagnoseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTitleDiagnoseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTitleDiagnose',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetTitleDiagnoseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_title_diagnose(
        self,
        request: alimt_20181012_models.GetTitleDiagnoseRequest,
    ) -> alimt_20181012_models.GetTitleDiagnoseResponse:
        """
        @summary GetTitleDiagnose
        
        @param request: GetTitleDiagnoseRequest
        @return: GetTitleDiagnoseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_title_diagnose_with_options(request, runtime)

    async def get_title_diagnose_async(
        self,
        request: alimt_20181012_models.GetTitleDiagnoseRequest,
    ) -> alimt_20181012_models.GetTitleDiagnoseResponse:
        """
        @summary GetTitleDiagnose
        
        @param request: GetTitleDiagnoseRequest
        @return: GetTitleDiagnoseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_title_diagnose_with_options_async(request, runtime)

    def get_title_generate_with_options(
        self,
        request: alimt_20181012_models.GetTitleGenerateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetTitleGenerateResponse:
        """
        @summary GetTitleGenerate
        
        @param request: GetTitleGenerateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTitleGenerateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attributes):
            body['Attributes'] = request.attributes
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.hot_words):
            body['HotWords'] = request.hot_words
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTitleGenerate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetTitleGenerateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_title_generate_with_options_async(
        self,
        request: alimt_20181012_models.GetTitleGenerateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetTitleGenerateResponse:
        """
        @summary GetTitleGenerate
        
        @param request: GetTitleGenerateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTitleGenerateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attributes):
            body['Attributes'] = request.attributes
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.hot_words):
            body['HotWords'] = request.hot_words
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTitleGenerate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetTitleGenerateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_title_generate(
        self,
        request: alimt_20181012_models.GetTitleGenerateRequest,
    ) -> alimt_20181012_models.GetTitleGenerateResponse:
        """
        @summary GetTitleGenerate
        
        @param request: GetTitleGenerateRequest
        @return: GetTitleGenerateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_title_generate_with_options(request, runtime)

    async def get_title_generate_async(
        self,
        request: alimt_20181012_models.GetTitleGenerateRequest,
    ) -> alimt_20181012_models.GetTitleGenerateResponse:
        """
        @summary GetTitleGenerate
        
        @param request: GetTitleGenerateRequest
        @return: GetTitleGenerateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_title_generate_with_options_async(request, runtime)

    def get_title_intelligence_with_options(
        self,
        request: alimt_20181012_models.GetTitleIntelligenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetTitleIntelligenceResponse:
        """
        @summary GetTitleIntelligence
        
        @param request: GetTitleIntelligenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTitleIntelligenceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cat_level_three_id):
            body['CatLevelThreeId'] = request.cat_level_three_id
        if not UtilClient.is_unset(request.cat_level_two_id):
            body['CatLevelTwoId'] = request.cat_level_two_id
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.keywords):
            body['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTitleIntelligence',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetTitleIntelligenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_title_intelligence_with_options_async(
        self,
        request: alimt_20181012_models.GetTitleIntelligenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetTitleIntelligenceResponse:
        """
        @summary GetTitleIntelligence
        
        @param request: GetTitleIntelligenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTitleIntelligenceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cat_level_three_id):
            body['CatLevelThreeId'] = request.cat_level_three_id
        if not UtilClient.is_unset(request.cat_level_two_id):
            body['CatLevelTwoId'] = request.cat_level_two_id
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.keywords):
            body['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTitleIntelligence',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetTitleIntelligenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_title_intelligence(
        self,
        request: alimt_20181012_models.GetTitleIntelligenceRequest,
    ) -> alimt_20181012_models.GetTitleIntelligenceResponse:
        """
        @summary GetTitleIntelligence
        
        @param request: GetTitleIntelligenceRequest
        @return: GetTitleIntelligenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_title_intelligence_with_options(request, runtime)

    async def get_title_intelligence_async(
        self,
        request: alimt_20181012_models.GetTitleIntelligenceRequest,
    ) -> alimt_20181012_models.GetTitleIntelligenceResponse:
        """
        @summary GetTitleIntelligence
        
        @param request: GetTitleIntelligenceRequest
        @return: GetTitleIntelligenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_title_intelligence_with_options_async(request, runtime)

    def get_translate_image_batch_result_with_options(
        self,
        request: alimt_20181012_models.GetTranslateImageBatchResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetTranslateImageBatchResultResponse:
        """
        @summary 获取图片批量翻译结果
        
        @param request: GetTranslateImageBatchResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTranslateImageBatchResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTranslateImageBatchResult',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetTranslateImageBatchResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_translate_image_batch_result_with_options_async(
        self,
        request: alimt_20181012_models.GetTranslateImageBatchResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetTranslateImageBatchResultResponse:
        """
        @summary 获取图片批量翻译结果
        
        @param request: GetTranslateImageBatchResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTranslateImageBatchResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTranslateImageBatchResult',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetTranslateImageBatchResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_translate_image_batch_result(
        self,
        request: alimt_20181012_models.GetTranslateImageBatchResultRequest,
    ) -> alimt_20181012_models.GetTranslateImageBatchResultResponse:
        """
        @summary 获取图片批量翻译结果
        
        @param request: GetTranslateImageBatchResultRequest
        @return: GetTranslateImageBatchResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_translate_image_batch_result_with_options(request, runtime)

    async def get_translate_image_batch_result_async(
        self,
        request: alimt_20181012_models.GetTranslateImageBatchResultRequest,
    ) -> alimt_20181012_models.GetTranslateImageBatchResultResponse:
        """
        @summary 获取图片批量翻译结果
        
        @param request: GetTranslateImageBatchResultRequest
        @return: GetTranslateImageBatchResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_translate_image_batch_result_with_options_async(request, runtime)

    def get_translate_report_with_options(
        self,
        request: alimt_20181012_models.GetTranslateReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetTranslateReportResponse:
        """
        @summary GetTranslateReport
        
        @param request: GetTranslateReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTranslateReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTranslateReport',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetTranslateReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_translate_report_with_options_async(
        self,
        request: alimt_20181012_models.GetTranslateReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.GetTranslateReportResponse:
        """
        @summary GetTranslateReport
        
        @param request: GetTranslateReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTranslateReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTranslateReport',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetTranslateReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_translate_report(
        self,
        request: alimt_20181012_models.GetTranslateReportRequest,
    ) -> alimt_20181012_models.GetTranslateReportResponse:
        """
        @summary GetTranslateReport
        
        @param request: GetTranslateReportRequest
        @return: GetTranslateReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_translate_report_with_options(request, runtime)

    async def get_translate_report_async(
        self,
        request: alimt_20181012_models.GetTranslateReportRequest,
    ) -> alimt_20181012_models.GetTranslateReportResponse:
        """
        @summary GetTranslateReport
        
        @param request: GetTranslateReportRequest
        @return: GetTranslateReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_translate_report_with_options_async(request, runtime)

    def open_alimt_service_with_options(
        self,
        request: alimt_20181012_models.OpenAlimtServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.OpenAlimtServiceResponse:
        """
        @summary 开通服务
        
        @param request: OpenAlimtServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenAlimtServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenAlimtService',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.OpenAlimtServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_alimt_service_with_options_async(
        self,
        request: alimt_20181012_models.OpenAlimtServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.OpenAlimtServiceResponse:
        """
        @summary 开通服务
        
        @param request: OpenAlimtServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenAlimtServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenAlimtService',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.OpenAlimtServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_alimt_service(
        self,
        request: alimt_20181012_models.OpenAlimtServiceRequest,
    ) -> alimt_20181012_models.OpenAlimtServiceResponse:
        """
        @summary 开通服务
        
        @param request: OpenAlimtServiceRequest
        @return: OpenAlimtServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_alimt_service_with_options(request, runtime)

    async def open_alimt_service_async(
        self,
        request: alimt_20181012_models.OpenAlimtServiceRequest,
    ) -> alimt_20181012_models.OpenAlimtServiceResponse:
        """
        @summary 开通服务
        
        @param request: OpenAlimtServiceRequest
        @return: OpenAlimtServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_alimt_service_with_options_async(request, runtime)

    def translate_with_options(
        self,
        request: alimt_20181012_models.TranslateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateResponse:
        """
        @summary 专业文本翻译
        
        @param request: TranslateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.context):
            query['Context'] = request.context
        body = {}
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Translate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def translate_with_options_async(
        self,
        request: alimt_20181012_models.TranslateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateResponse:
        """
        @summary 专业文本翻译
        
        @param request: TranslateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.context):
            query['Context'] = request.context
        body = {}
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Translate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def translate(
        self,
        request: alimt_20181012_models.TranslateRequest,
    ) -> alimt_20181012_models.TranslateResponse:
        """
        @summary 专业文本翻译
        
        @param request: TranslateRequest
        @return: TranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.translate_with_options(request, runtime)

    async def translate_async(
        self,
        request: alimt_20181012_models.TranslateRequest,
    ) -> alimt_20181012_models.TranslateResponse:
        """
        @summary 专业文本翻译
        
        @param request: TranslateRequest
        @return: TranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.translate_with_options_async(request, runtime)

    def translate_certificate_with_options(
        self,
        request: alimt_20181012_models.TranslateCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateCertificateResponse:
        """
        @summary TranslateCertificate
        
        @param request: TranslateCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateCertificateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.certificate_type):
            body['CertificateType'] = request.certificate_type
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.result_type):
            body['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateCertificate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def translate_certificate_with_options_async(
        self,
        request: alimt_20181012_models.TranslateCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateCertificateResponse:
        """
        @summary TranslateCertificate
        
        @param request: TranslateCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateCertificateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.certificate_type):
            body['CertificateType'] = request.certificate_type
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.result_type):
            body['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateCertificate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def translate_certificate(
        self,
        request: alimt_20181012_models.TranslateCertificateRequest,
    ) -> alimt_20181012_models.TranslateCertificateResponse:
        """
        @summary TranslateCertificate
        
        @param request: TranslateCertificateRequest
        @return: TranslateCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.translate_certificate_with_options(request, runtime)

    async def translate_certificate_async(
        self,
        request: alimt_20181012_models.TranslateCertificateRequest,
    ) -> alimt_20181012_models.TranslateCertificateResponse:
        """
        @summary TranslateCertificate
        
        @param request: TranslateCertificateRequest
        @return: TranslateCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.translate_certificate_with_options_async(request, runtime)

    def translate_certificate_advance(
        self,
        request: alimt_20181012_models.TranslateCertificateAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateCertificateResponse:
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
            'Product': 'alimt',
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
        translate_certificate_req = alimt_20181012_models.TranslateCertificateRequest()
        OpenApiUtilClient.convert(request, translate_certificate_req)
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
            translate_certificate_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        translate_certificate_resp = self.translate_certificate_with_options(translate_certificate_req, runtime)
        return translate_certificate_resp

    async def translate_certificate_advance_async(
        self,
        request: alimt_20181012_models.TranslateCertificateAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateCertificateResponse:
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
            'Product': 'alimt',
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
        translate_certificate_req = alimt_20181012_models.TranslateCertificateRequest()
        OpenApiUtilClient.convert(request, translate_certificate_req)
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
            translate_certificate_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        translate_certificate_resp = await self.translate_certificate_with_options_async(translate_certificate_req, runtime)
        return translate_certificate_resp

    def translate_ecommerce_with_options(
        self,
        request: alimt_20181012_models.TranslateECommerceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateECommerceResponse:
        """
        @deprecated OpenAPI TranslateECommerce is deprecated, please use alimt::2018-10-12::Translate instead.
        
        @summary TranslateECommerce
        
        @param request: TranslateECommerceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateECommerceResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.context):
            query['Context'] = request.context
        body = {}
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateECommerce',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateECommerceResponse(),
            self.call_api(params, req, runtime)
        )

    async def translate_ecommerce_with_options_async(
        self,
        request: alimt_20181012_models.TranslateECommerceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateECommerceResponse:
        """
        @deprecated OpenAPI TranslateECommerce is deprecated, please use alimt::2018-10-12::Translate instead.
        
        @summary TranslateECommerce
        
        @param request: TranslateECommerceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateECommerceResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.context):
            query['Context'] = request.context
        body = {}
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateECommerce',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateECommerceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def translate_ecommerce(
        self,
        request: alimt_20181012_models.TranslateECommerceRequest,
    ) -> alimt_20181012_models.TranslateECommerceResponse:
        """
        @deprecated OpenAPI TranslateECommerce is deprecated, please use alimt::2018-10-12::Translate instead.
        
        @summary TranslateECommerce
        
        @param request: TranslateECommerceRequest
        @return: TranslateECommerceResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.translate_ecommerce_with_options(request, runtime)

    async def translate_ecommerce_async(
        self,
        request: alimt_20181012_models.TranslateECommerceRequest,
    ) -> alimt_20181012_models.TranslateECommerceResponse:
        """
        @deprecated OpenAPI TranslateECommerce is deprecated, please use alimt::2018-10-12::Translate instead.
        
        @summary TranslateECommerce
        
        @param request: TranslateECommerceRequest
        @return: TranslateECommerceResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.translate_ecommerce_with_options_async(request, runtime)

    def translate_general_with_options(
        self,
        request: alimt_20181012_models.TranslateGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateGeneralResponse:
        """
        @summary 文本通用翻译
        
        @param request: TranslateGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateGeneralResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.context):
            query['Context'] = request.context
        body = {}
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateGeneral',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def translate_general_with_options_async(
        self,
        request: alimt_20181012_models.TranslateGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateGeneralResponse:
        """
        @summary 文本通用翻译
        
        @param request: TranslateGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateGeneralResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.context):
            query['Context'] = request.context
        body = {}
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateGeneral',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def translate_general(
        self,
        request: alimt_20181012_models.TranslateGeneralRequest,
    ) -> alimt_20181012_models.TranslateGeneralResponse:
        """
        @summary 文本通用翻译
        
        @param request: TranslateGeneralRequest
        @return: TranslateGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.translate_general_with_options(request, runtime)

    async def translate_general_async(
        self,
        request: alimt_20181012_models.TranslateGeneralRequest,
    ) -> alimt_20181012_models.TranslateGeneralResponse:
        """
        @summary 文本通用翻译
        
        @param request: TranslateGeneralRequest
        @return: TranslateGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.translate_general_with_options_async(request, runtime)

    def translate_general_vpc_with_options(
        self,
        request: alimt_20181012_models.TranslateGeneralVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateGeneralVpcResponse:
        """
        @summary TranslateGeneralVpc
        
        @param request: TranslateGeneralVpcRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateGeneralVpcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.context):
            query['Context'] = request.context
        body = {}
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateGeneralVpc',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateGeneralVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def translate_general_vpc_with_options_async(
        self,
        request: alimt_20181012_models.TranslateGeneralVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateGeneralVpcResponse:
        """
        @summary TranslateGeneralVpc
        
        @param request: TranslateGeneralVpcRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateGeneralVpcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.context):
            query['Context'] = request.context
        body = {}
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateGeneralVpc',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateGeneralVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def translate_general_vpc(
        self,
        request: alimt_20181012_models.TranslateGeneralVpcRequest,
    ) -> alimt_20181012_models.TranslateGeneralVpcResponse:
        """
        @summary TranslateGeneralVpc
        
        @param request: TranslateGeneralVpcRequest
        @return: TranslateGeneralVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.translate_general_vpc_with_options(request, runtime)

    async def translate_general_vpc_async(
        self,
        request: alimt_20181012_models.TranslateGeneralVpcRequest,
    ) -> alimt_20181012_models.TranslateGeneralVpcResponse:
        """
        @summary TranslateGeneralVpc
        
        @param request: TranslateGeneralVpcRequest
        @return: TranslateGeneralVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.translate_general_vpc_with_options_async(request, runtime)

    def translate_image_with_options(
        self,
        request: alimt_20181012_models.TranslateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateImageResponse:
        """
        @summary 公有云图片翻译产品API
        
        @param request: TranslateImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ext):
            body['Ext'] = request.ext
        if not UtilClient.is_unset(request.field):
            body['Field'] = request.field
        if not UtilClient.is_unset(request.image_base_64):
            body['ImageBase64'] = request.image_base_64
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateImage',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def translate_image_with_options_async(
        self,
        request: alimt_20181012_models.TranslateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateImageResponse:
        """
        @summary 公有云图片翻译产品API
        
        @param request: TranslateImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ext):
            body['Ext'] = request.ext
        if not UtilClient.is_unset(request.field):
            body['Field'] = request.field
        if not UtilClient.is_unset(request.image_base_64):
            body['ImageBase64'] = request.image_base_64
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateImage',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def translate_image(
        self,
        request: alimt_20181012_models.TranslateImageRequest,
    ) -> alimt_20181012_models.TranslateImageResponse:
        """
        @summary 公有云图片翻译产品API
        
        @param request: TranslateImageRequest
        @return: TranslateImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.translate_image_with_options(request, runtime)

    async def translate_image_async(
        self,
        request: alimt_20181012_models.TranslateImageRequest,
    ) -> alimt_20181012_models.TranslateImageResponse:
        """
        @summary 公有云图片翻译产品API
        
        @param request: TranslateImageRequest
        @return: TranslateImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.translate_image_with_options_async(request, runtime)

    def translate_image_batch_with_options(
        self,
        request: alimt_20181012_models.TranslateImageBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateImageBatchResponse:
        """
        @summary 批量图片翻译接口
        
        @param request: TranslateImageBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateImageBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_task_id):
            body['CustomTaskId'] = request.custom_task_id
        if not UtilClient.is_unset(request.ext):
            body['Ext'] = request.ext
        if not UtilClient.is_unset(request.field):
            body['Field'] = request.field
        if not UtilClient.is_unset(request.image_urls):
            body['ImageUrls'] = request.image_urls
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateImageBatch',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateImageBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def translate_image_batch_with_options_async(
        self,
        request: alimt_20181012_models.TranslateImageBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateImageBatchResponse:
        """
        @summary 批量图片翻译接口
        
        @param request: TranslateImageBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateImageBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_task_id):
            body['CustomTaskId'] = request.custom_task_id
        if not UtilClient.is_unset(request.ext):
            body['Ext'] = request.ext
        if not UtilClient.is_unset(request.field):
            body['Field'] = request.field
        if not UtilClient.is_unset(request.image_urls):
            body['ImageUrls'] = request.image_urls
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateImageBatch',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateImageBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def translate_image_batch(
        self,
        request: alimt_20181012_models.TranslateImageBatchRequest,
    ) -> alimt_20181012_models.TranslateImageBatchResponse:
        """
        @summary 批量图片翻译接口
        
        @param request: TranslateImageBatchRequest
        @return: TranslateImageBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.translate_image_batch_with_options(request, runtime)

    async def translate_image_batch_async(
        self,
        request: alimt_20181012_models.TranslateImageBatchRequest,
    ) -> alimt_20181012_models.TranslateImageBatchResponse:
        """
        @summary 批量图片翻译接口
        
        @param request: TranslateImageBatchRequest
        @return: TranslateImageBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.translate_image_batch_with_options_async(request, runtime)

    def translate_search_with_options(
        self,
        request: alimt_20181012_models.TranslateSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateSearchResponse:
        """
        @summary 搜索翻译
        
        @param request: TranslateSearchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateSearchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateSearch',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def translate_search_with_options_async(
        self,
        request: alimt_20181012_models.TranslateSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20181012_models.TranslateSearchResponse:
        """
        @summary 搜索翻译
        
        @param request: TranslateSearchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateSearchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateSearch',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def translate_search(
        self,
        request: alimt_20181012_models.TranslateSearchRequest,
    ) -> alimt_20181012_models.TranslateSearchResponse:
        """
        @summary 搜索翻译
        
        @param request: TranslateSearchRequest
        @return: TranslateSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.translate_search_with_options(request, runtime)

    async def translate_search_async(
        self,
        request: alimt_20181012_models.TranslateSearchRequest,
    ) -> alimt_20181012_models.TranslateSearchResponse:
        """
        @summary 搜索翻译
        
        @param request: TranslateSearchRequest
        @return: TranslateSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.translate_search_with_options_async(request, runtime)
