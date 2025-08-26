# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.request import TeaRequest
from Tea.exceptions import TeaException
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_fileform.client import Client as FileFormClient
from alibabacloud_tea_xml.client import Client as XMLClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ocr20191230 import models as ocr_20191230_models
from alibabacloud_tea_util import models as util_models
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
        self._endpoint = self.get_endpoint('ocr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def _post_ossobject(
        self,
        bucket_name: str,
        data: dict,
    ) -> dict:
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
        _response = TeaCore.do_action(_request)
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

    async def _post_ossobject_async(
        self,
        bucket_name: str,
        data: dict,
    ) -> dict:
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
        _response = await TeaCore.async_do_action(_request)
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

    def get_async_job_result_with_options(
        self,
        request: ocr_20191230_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.GetAsyncJobResultResponse:
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
            ocr_20191230_models.GetAsyncJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_job_result_with_options_async(
        self,
        request: ocr_20191230_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.GetAsyncJobResultResponse:
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
            ocr_20191230_models.GetAsyncJobResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_job_result(
        self,
        request: ocr_20191230_models.GetAsyncJobResultRequest,
    ) -> ocr_20191230_models.GetAsyncJobResultResponse:
        """
        @param request: GetAsyncJobResultRequest
        @return: GetAsyncJobResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result_with_options(request, runtime)

    async def get_async_job_result_async(
        self,
        request: ocr_20191230_models.GetAsyncJobResultRequest,
    ) -> ocr_20191230_models.GetAsyncJobResultResponse:
        """
        @param request: GetAsyncJobResultRequest
        @return: GetAsyncJobResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_async_job_result_with_options_async(request, runtime)

    def recognize_bank_card_with_options(
        self,
        request: ocr_20191230_models.RecognizeBankCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeBankCardResponse:
        """
        @param request: RecognizeBankCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBankCardResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeBankCard',
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
            ocr_20191230_models.RecognizeBankCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_bank_card_with_options_async(
        self,
        request: ocr_20191230_models.RecognizeBankCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeBankCardResponse:
        """
        @param request: RecognizeBankCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBankCardResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeBankCard',
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
            ocr_20191230_models.RecognizeBankCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_bank_card(
        self,
        request: ocr_20191230_models.RecognizeBankCardRequest,
    ) -> ocr_20191230_models.RecognizeBankCardResponse:
        """
        @param request: RecognizeBankCardRequest
        @return: RecognizeBankCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_bank_card_with_options(request, runtime)

    async def recognize_bank_card_async(
        self,
        request: ocr_20191230_models.RecognizeBankCardRequest,
    ) -> ocr_20191230_models.RecognizeBankCardResponse:
        """
        @param request: RecognizeBankCardRequest
        @return: RecognizeBankCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_bank_card_with_options_async(request, runtime)

    def recognize_bank_card_advance(
        self,
        request: ocr_20191230_models.RecognizeBankCardAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeBankCardResponse:
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
            'Product': 'ocr',
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
        recognize_bank_card_req = ocr_20191230_models.RecognizeBankCardRequest()
        OpenApiUtilClient.convert(request, recognize_bank_card_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            recognize_bank_card_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_bank_card_resp = self.recognize_bank_card_with_options(recognize_bank_card_req, runtime)
        return recognize_bank_card_resp

    async def recognize_bank_card_advance_async(
        self,
        request: ocr_20191230_models.RecognizeBankCardAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeBankCardResponse:
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
            'Product': 'ocr',
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
        recognize_bank_card_req = ocr_20191230_models.RecognizeBankCardRequest()
        OpenApiUtilClient.convert(request, recognize_bank_card_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            recognize_bank_card_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_bank_card_resp = await self.recognize_bank_card_with_options_async(recognize_bank_card_req, runtime)
        return recognize_bank_card_resp

    def recognize_business_license_with_options(
        self,
        request: ocr_20191230_models.RecognizeBusinessLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeBusinessLicenseResponse:
        """
        @param request: RecognizeBusinessLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBusinessLicenseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeBusinessLicense',
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
            ocr_20191230_models.RecognizeBusinessLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_business_license_with_options_async(
        self,
        request: ocr_20191230_models.RecognizeBusinessLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeBusinessLicenseResponse:
        """
        @param request: RecognizeBusinessLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBusinessLicenseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeBusinessLicense',
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
            ocr_20191230_models.RecognizeBusinessLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_business_license(
        self,
        request: ocr_20191230_models.RecognizeBusinessLicenseRequest,
    ) -> ocr_20191230_models.RecognizeBusinessLicenseResponse:
        """
        @param request: RecognizeBusinessLicenseRequest
        @return: RecognizeBusinessLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_business_license_with_options(request, runtime)

    async def recognize_business_license_async(
        self,
        request: ocr_20191230_models.RecognizeBusinessLicenseRequest,
    ) -> ocr_20191230_models.RecognizeBusinessLicenseResponse:
        """
        @param request: RecognizeBusinessLicenseRequest
        @return: RecognizeBusinessLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_business_license_with_options_async(request, runtime)

    def recognize_business_license_advance(
        self,
        request: ocr_20191230_models.RecognizeBusinessLicenseAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeBusinessLicenseResponse:
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
            'Product': 'ocr',
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
        recognize_business_license_req = ocr_20191230_models.RecognizeBusinessLicenseRequest()
        OpenApiUtilClient.convert(request, recognize_business_license_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            recognize_business_license_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_business_license_resp = self.recognize_business_license_with_options(recognize_business_license_req, runtime)
        return recognize_business_license_resp

    async def recognize_business_license_advance_async(
        self,
        request: ocr_20191230_models.RecognizeBusinessLicenseAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeBusinessLicenseResponse:
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
            'Product': 'ocr',
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
        recognize_business_license_req = ocr_20191230_models.RecognizeBusinessLicenseRequest()
        OpenApiUtilClient.convert(request, recognize_business_license_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            recognize_business_license_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_business_license_resp = await self.recognize_business_license_with_options_async(recognize_business_license_req, runtime)
        return recognize_business_license_resp

    def recognize_character_with_options(
        self,
        request: ocr_20191230_models.RecognizeCharacterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeCharacterResponse:
        """
        @param request: RecognizeCharacterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeCharacterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.min_height):
            body['MinHeight'] = request.min_height
        if not UtilClient.is_unset(request.output_probability):
            body['OutputProbability'] = request.output_probability
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeCharacter',
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
            ocr_20191230_models.RecognizeCharacterResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_character_with_options_async(
        self,
        request: ocr_20191230_models.RecognizeCharacterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeCharacterResponse:
        """
        @param request: RecognizeCharacterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeCharacterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.min_height):
            body['MinHeight'] = request.min_height
        if not UtilClient.is_unset(request.output_probability):
            body['OutputProbability'] = request.output_probability
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeCharacter',
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
            ocr_20191230_models.RecognizeCharacterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_character(
        self,
        request: ocr_20191230_models.RecognizeCharacterRequest,
    ) -> ocr_20191230_models.RecognizeCharacterResponse:
        """
        @param request: RecognizeCharacterRequest
        @return: RecognizeCharacterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_character_with_options(request, runtime)

    async def recognize_character_async(
        self,
        request: ocr_20191230_models.RecognizeCharacterRequest,
    ) -> ocr_20191230_models.RecognizeCharacterResponse:
        """
        @param request: RecognizeCharacterRequest
        @return: RecognizeCharacterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_character_with_options_async(request, runtime)

    def recognize_character_advance(
        self,
        request: ocr_20191230_models.RecognizeCharacterAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeCharacterResponse:
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
            'Product': 'ocr',
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
        recognize_character_req = ocr_20191230_models.RecognizeCharacterRequest()
        OpenApiUtilClient.convert(request, recognize_character_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            recognize_character_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_character_resp = self.recognize_character_with_options(recognize_character_req, runtime)
        return recognize_character_resp

    async def recognize_character_advance_async(
        self,
        request: ocr_20191230_models.RecognizeCharacterAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeCharacterResponse:
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
            'Product': 'ocr',
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
        recognize_character_req = ocr_20191230_models.RecognizeCharacterRequest()
        OpenApiUtilClient.convert(request, recognize_character_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            recognize_character_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_character_resp = await self.recognize_character_with_options_async(recognize_character_req, runtime)
        return recognize_character_resp

    def recognize_driver_license_with_options(
        self,
        request: ocr_20191230_models.RecognizeDriverLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeDriverLicenseResponse:
        """
        @param request: RecognizeDriverLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeDriverLicenseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.side):
            body['Side'] = request.side
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeDriverLicense',
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
            ocr_20191230_models.RecognizeDriverLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_driver_license_with_options_async(
        self,
        request: ocr_20191230_models.RecognizeDriverLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeDriverLicenseResponse:
        """
        @param request: RecognizeDriverLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeDriverLicenseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.side):
            body['Side'] = request.side
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeDriverLicense',
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
            ocr_20191230_models.RecognizeDriverLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_driver_license(
        self,
        request: ocr_20191230_models.RecognizeDriverLicenseRequest,
    ) -> ocr_20191230_models.RecognizeDriverLicenseResponse:
        """
        @param request: RecognizeDriverLicenseRequest
        @return: RecognizeDriverLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_driver_license_with_options(request, runtime)

    async def recognize_driver_license_async(
        self,
        request: ocr_20191230_models.RecognizeDriverLicenseRequest,
    ) -> ocr_20191230_models.RecognizeDriverLicenseResponse:
        """
        @param request: RecognizeDriverLicenseRequest
        @return: RecognizeDriverLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_driver_license_with_options_async(request, runtime)

    def recognize_driver_license_advance(
        self,
        request: ocr_20191230_models.RecognizeDriverLicenseAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeDriverLicenseResponse:
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
            'Product': 'ocr',
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
        recognize_driver_license_req = ocr_20191230_models.RecognizeDriverLicenseRequest()
        OpenApiUtilClient.convert(request, recognize_driver_license_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            recognize_driver_license_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_driver_license_resp = self.recognize_driver_license_with_options(recognize_driver_license_req, runtime)
        return recognize_driver_license_resp

    async def recognize_driver_license_advance_async(
        self,
        request: ocr_20191230_models.RecognizeDriverLicenseAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeDriverLicenseResponse:
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
            'Product': 'ocr',
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
        recognize_driver_license_req = ocr_20191230_models.RecognizeDriverLicenseRequest()
        OpenApiUtilClient.convert(request, recognize_driver_license_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            recognize_driver_license_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_driver_license_resp = await self.recognize_driver_license_with_options_async(recognize_driver_license_req, runtime)
        return recognize_driver_license_resp

    def recognize_driving_license_with_options(
        self,
        request: ocr_20191230_models.RecognizeDrivingLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeDrivingLicenseResponse:
        """
        @param request: RecognizeDrivingLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeDrivingLicenseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.side):
            body['Side'] = request.side
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeDrivingLicense',
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
            ocr_20191230_models.RecognizeDrivingLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_driving_license_with_options_async(
        self,
        request: ocr_20191230_models.RecognizeDrivingLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeDrivingLicenseResponse:
        """
        @param request: RecognizeDrivingLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeDrivingLicenseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.side):
            body['Side'] = request.side
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeDrivingLicense',
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
            ocr_20191230_models.RecognizeDrivingLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_driving_license(
        self,
        request: ocr_20191230_models.RecognizeDrivingLicenseRequest,
    ) -> ocr_20191230_models.RecognizeDrivingLicenseResponse:
        """
        @param request: RecognizeDrivingLicenseRequest
        @return: RecognizeDrivingLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_driving_license_with_options(request, runtime)

    async def recognize_driving_license_async(
        self,
        request: ocr_20191230_models.RecognizeDrivingLicenseRequest,
    ) -> ocr_20191230_models.RecognizeDrivingLicenseResponse:
        """
        @param request: RecognizeDrivingLicenseRequest
        @return: RecognizeDrivingLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_driving_license_with_options_async(request, runtime)

    def recognize_driving_license_advance(
        self,
        request: ocr_20191230_models.RecognizeDrivingLicenseAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeDrivingLicenseResponse:
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
            'Product': 'ocr',
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
        recognize_driving_license_req = ocr_20191230_models.RecognizeDrivingLicenseRequest()
        OpenApiUtilClient.convert(request, recognize_driving_license_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            recognize_driving_license_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_driving_license_resp = self.recognize_driving_license_with_options(recognize_driving_license_req, runtime)
        return recognize_driving_license_resp

    async def recognize_driving_license_advance_async(
        self,
        request: ocr_20191230_models.RecognizeDrivingLicenseAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeDrivingLicenseResponse:
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
            'Product': 'ocr',
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
        recognize_driving_license_req = ocr_20191230_models.RecognizeDrivingLicenseRequest()
        OpenApiUtilClient.convert(request, recognize_driving_license_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            recognize_driving_license_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_driving_license_resp = await self.recognize_driving_license_with_options_async(recognize_driving_license_req, runtime)
        return recognize_driving_license_resp

    def recognize_identity_card_with_options(
        self,
        request: ocr_20191230_models.RecognizeIdentityCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeIdentityCardResponse:
        """
        @param request: RecognizeIdentityCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeIdentityCardResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.side):
            body['Side'] = request.side
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeIdentityCard',
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
            ocr_20191230_models.RecognizeIdentityCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_identity_card_with_options_async(
        self,
        request: ocr_20191230_models.RecognizeIdentityCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeIdentityCardResponse:
        """
        @param request: RecognizeIdentityCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeIdentityCardResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.side):
            body['Side'] = request.side
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeIdentityCard',
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
            ocr_20191230_models.RecognizeIdentityCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_identity_card(
        self,
        request: ocr_20191230_models.RecognizeIdentityCardRequest,
    ) -> ocr_20191230_models.RecognizeIdentityCardResponse:
        """
        @param request: RecognizeIdentityCardRequest
        @return: RecognizeIdentityCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_identity_card_with_options(request, runtime)

    async def recognize_identity_card_async(
        self,
        request: ocr_20191230_models.RecognizeIdentityCardRequest,
    ) -> ocr_20191230_models.RecognizeIdentityCardResponse:
        """
        @param request: RecognizeIdentityCardRequest
        @return: RecognizeIdentityCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_identity_card_with_options_async(request, runtime)

    def recognize_identity_card_advance(
        self,
        request: ocr_20191230_models.RecognizeIdentityCardAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeIdentityCardResponse:
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
            'Product': 'ocr',
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
        recognize_identity_card_req = ocr_20191230_models.RecognizeIdentityCardRequest()
        OpenApiUtilClient.convert(request, recognize_identity_card_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            recognize_identity_card_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_identity_card_resp = self.recognize_identity_card_with_options(recognize_identity_card_req, runtime)
        return recognize_identity_card_resp

    async def recognize_identity_card_advance_async(
        self,
        request: ocr_20191230_models.RecognizeIdentityCardAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeIdentityCardResponse:
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
            'Product': 'ocr',
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
        recognize_identity_card_req = ocr_20191230_models.RecognizeIdentityCardRequest()
        OpenApiUtilClient.convert(request, recognize_identity_card_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            recognize_identity_card_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_identity_card_resp = await self.recognize_identity_card_with_options_async(recognize_identity_card_req, runtime)
        return recognize_identity_card_resp

    def recognize_license_plate_with_options(
        self,
        request: ocr_20191230_models.RecognizeLicensePlateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeLicensePlateResponse:
        """
        @param request: RecognizeLicensePlateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeLicensePlateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeLicensePlate',
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
            ocr_20191230_models.RecognizeLicensePlateResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_license_plate_with_options_async(
        self,
        request: ocr_20191230_models.RecognizeLicensePlateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeLicensePlateResponse:
        """
        @param request: RecognizeLicensePlateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeLicensePlateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeLicensePlate',
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
            ocr_20191230_models.RecognizeLicensePlateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_license_plate(
        self,
        request: ocr_20191230_models.RecognizeLicensePlateRequest,
    ) -> ocr_20191230_models.RecognizeLicensePlateResponse:
        """
        @param request: RecognizeLicensePlateRequest
        @return: RecognizeLicensePlateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_license_plate_with_options(request, runtime)

    async def recognize_license_plate_async(
        self,
        request: ocr_20191230_models.RecognizeLicensePlateRequest,
    ) -> ocr_20191230_models.RecognizeLicensePlateResponse:
        """
        @param request: RecognizeLicensePlateRequest
        @return: RecognizeLicensePlateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_license_plate_with_options_async(request, runtime)

    def recognize_license_plate_advance(
        self,
        request: ocr_20191230_models.RecognizeLicensePlateAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeLicensePlateResponse:
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
            'Product': 'ocr',
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
        recognize_license_plate_req = ocr_20191230_models.RecognizeLicensePlateRequest()
        OpenApiUtilClient.convert(request, recognize_license_plate_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            recognize_license_plate_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_license_plate_resp = self.recognize_license_plate_with_options(recognize_license_plate_req, runtime)
        return recognize_license_plate_resp

    async def recognize_license_plate_advance_async(
        self,
        request: ocr_20191230_models.RecognizeLicensePlateAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeLicensePlateResponse:
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
            'Product': 'ocr',
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
        recognize_license_plate_req = ocr_20191230_models.RecognizeLicensePlateRequest()
        OpenApiUtilClient.convert(request, recognize_license_plate_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            recognize_license_plate_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_license_plate_resp = await self.recognize_license_plate_with_options_async(recognize_license_plate_req, runtime)
        return recognize_license_plate_resp

    def recognize_pdf_with_options(
        self,
        request: ocr_20191230_models.RecognizePdfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizePdfResponse:
        """
        @summary PDF识别
        
        @param request: RecognizePdfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizePdfResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_url):
            body['FileURL'] = request.file_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizePdf',
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
            ocr_20191230_models.RecognizePdfResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_pdf_with_options_async(
        self,
        request: ocr_20191230_models.RecognizePdfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizePdfResponse:
        """
        @summary PDF识别
        
        @param request: RecognizePdfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizePdfResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_url):
            body['FileURL'] = request.file_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizePdf',
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
            ocr_20191230_models.RecognizePdfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_pdf(
        self,
        request: ocr_20191230_models.RecognizePdfRequest,
    ) -> ocr_20191230_models.RecognizePdfResponse:
        """
        @summary PDF识别
        
        @param request: RecognizePdfRequest
        @return: RecognizePdfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_pdf_with_options(request, runtime)

    async def recognize_pdf_async(
        self,
        request: ocr_20191230_models.RecognizePdfRequest,
    ) -> ocr_20191230_models.RecognizePdfResponse:
        """
        @summary PDF识别
        
        @param request: RecognizePdfRequest
        @return: RecognizePdfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_pdf_with_options_async(request, runtime)

    def recognize_pdf_advance(
        self,
        request: ocr_20191230_models.RecognizePdfAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizePdfResponse:
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
            'Product': 'ocr',
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
        recognize_pdf_req = ocr_20191230_models.RecognizePdfRequest()
        OpenApiUtilClient.convert(request, recognize_pdf_req)
        if not UtilClient.is_unset(request.file_urlobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_urlobject,
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            recognize_pdf_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_pdf_resp = self.recognize_pdf_with_options(recognize_pdf_req, runtime)
        return recognize_pdf_resp

    async def recognize_pdf_advance_async(
        self,
        request: ocr_20191230_models.RecognizePdfAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizePdfResponse:
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
            'Product': 'ocr',
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
        recognize_pdf_req = ocr_20191230_models.RecognizePdfRequest()
        OpenApiUtilClient.convert(request, recognize_pdf_req)
        if not UtilClient.is_unset(request.file_urlobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_urlobject,
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            recognize_pdf_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_pdf_resp = await self.recognize_pdf_with_options_async(recognize_pdf_req, runtime)
        return recognize_pdf_resp

    def recognize_qr_code_with_options(
        self,
        request: ocr_20191230_models.RecognizeQrCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeQrCodeResponse:
        """
        @param request: RecognizeQrCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeQrCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tasks):
            body['Tasks'] = request.tasks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeQrCode',
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
            ocr_20191230_models.RecognizeQrCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_qr_code_with_options_async(
        self,
        request: ocr_20191230_models.RecognizeQrCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeQrCodeResponse:
        """
        @param request: RecognizeQrCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeQrCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tasks):
            body['Tasks'] = request.tasks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeQrCode',
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
            ocr_20191230_models.RecognizeQrCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_qr_code(
        self,
        request: ocr_20191230_models.RecognizeQrCodeRequest,
    ) -> ocr_20191230_models.RecognizeQrCodeResponse:
        """
        @param request: RecognizeQrCodeRequest
        @return: RecognizeQrCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_qr_code_with_options(request, runtime)

    async def recognize_qr_code_async(
        self,
        request: ocr_20191230_models.RecognizeQrCodeRequest,
    ) -> ocr_20191230_models.RecognizeQrCodeResponse:
        """
        @param request: RecognizeQrCodeRequest
        @return: RecognizeQrCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_qr_code_with_options_async(request, runtime)

    def recognize_qr_code_advance(
        self,
        request: ocr_20191230_models.RecognizeQrCodeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeQrCodeResponse:
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
            'Product': 'ocr',
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
        recognize_qr_code_req = ocr_20191230_models.RecognizeQrCodeRequest()
        OpenApiUtilClient.convert(request, recognize_qr_code_req)
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
                    self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
                    tmp = recognize_qr_code_req.tasks[i_0]
                    tmp.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        recognize_qr_code_resp = self.recognize_qr_code_with_options(recognize_qr_code_req, runtime)
        return recognize_qr_code_resp

    async def recognize_qr_code_advance_async(
        self,
        request: ocr_20191230_models.RecognizeQrCodeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeQrCodeResponse:
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
            'Product': 'ocr',
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
        recognize_qr_code_req = ocr_20191230_models.RecognizeQrCodeRequest()
        OpenApiUtilClient.convert(request, recognize_qr_code_req)
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
                    await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
                    tmp = recognize_qr_code_req.tasks[i_0]
                    tmp.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        recognize_qr_code_resp = await self.recognize_qr_code_with_options_async(recognize_qr_code_req, runtime)
        return recognize_qr_code_resp

    def recognize_quota_invoice_with_options(
        self,
        request: ocr_20191230_models.RecognizeQuotaInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeQuotaInvoiceResponse:
        """
        @summary 定额发票识别
        
        @param request: RecognizeQuotaInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeQuotaInvoiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeQuotaInvoice',
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
            ocr_20191230_models.RecognizeQuotaInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_quota_invoice_with_options_async(
        self,
        request: ocr_20191230_models.RecognizeQuotaInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeQuotaInvoiceResponse:
        """
        @summary 定额发票识别
        
        @param request: RecognizeQuotaInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeQuotaInvoiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeQuotaInvoice',
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
            ocr_20191230_models.RecognizeQuotaInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_quota_invoice(
        self,
        request: ocr_20191230_models.RecognizeQuotaInvoiceRequest,
    ) -> ocr_20191230_models.RecognizeQuotaInvoiceResponse:
        """
        @summary 定额发票识别
        
        @param request: RecognizeQuotaInvoiceRequest
        @return: RecognizeQuotaInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_quota_invoice_with_options(request, runtime)

    async def recognize_quota_invoice_async(
        self,
        request: ocr_20191230_models.RecognizeQuotaInvoiceRequest,
    ) -> ocr_20191230_models.RecognizeQuotaInvoiceResponse:
        """
        @summary 定额发票识别
        
        @param request: RecognizeQuotaInvoiceRequest
        @return: RecognizeQuotaInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_quota_invoice_with_options_async(request, runtime)

    def recognize_quota_invoice_advance(
        self,
        request: ocr_20191230_models.RecognizeQuotaInvoiceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeQuotaInvoiceResponse:
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
            'Product': 'ocr',
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
        recognize_quota_invoice_req = ocr_20191230_models.RecognizeQuotaInvoiceRequest()
        OpenApiUtilClient.convert(request, recognize_quota_invoice_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            recognize_quota_invoice_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_quota_invoice_resp = self.recognize_quota_invoice_with_options(recognize_quota_invoice_req, runtime)
        return recognize_quota_invoice_resp

    async def recognize_quota_invoice_advance_async(
        self,
        request: ocr_20191230_models.RecognizeQuotaInvoiceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeQuotaInvoiceResponse:
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
            'Product': 'ocr',
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
        recognize_quota_invoice_req = ocr_20191230_models.RecognizeQuotaInvoiceRequest()
        OpenApiUtilClient.convert(request, recognize_quota_invoice_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            recognize_quota_invoice_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_quota_invoice_resp = await self.recognize_quota_invoice_with_options_async(recognize_quota_invoice_req, runtime)
        return recognize_quota_invoice_resp

    def recognize_table_with_options(
        self,
        request: ocr_20191230_models.RecognizeTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeTableResponse:
        """
        @param request: RecognizeTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTableResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assure_direction):
            body['AssureDirection'] = request.assure_direction
        if not UtilClient.is_unset(request.has_line):
            body['HasLine'] = request.has_line
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.output_format):
            body['OutputFormat'] = request.output_format
        if not UtilClient.is_unset(request.skip_detection):
            body['SkipDetection'] = request.skip_detection
        if not UtilClient.is_unset(request.use_finance_model):
            body['UseFinanceModel'] = request.use_finance_model
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeTable',
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
            ocr_20191230_models.RecognizeTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_table_with_options_async(
        self,
        request: ocr_20191230_models.RecognizeTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeTableResponse:
        """
        @param request: RecognizeTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTableResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assure_direction):
            body['AssureDirection'] = request.assure_direction
        if not UtilClient.is_unset(request.has_line):
            body['HasLine'] = request.has_line
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.output_format):
            body['OutputFormat'] = request.output_format
        if not UtilClient.is_unset(request.skip_detection):
            body['SkipDetection'] = request.skip_detection
        if not UtilClient.is_unset(request.use_finance_model):
            body['UseFinanceModel'] = request.use_finance_model
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeTable',
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
            ocr_20191230_models.RecognizeTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_table(
        self,
        request: ocr_20191230_models.RecognizeTableRequest,
    ) -> ocr_20191230_models.RecognizeTableResponse:
        """
        @param request: RecognizeTableRequest
        @return: RecognizeTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_table_with_options(request, runtime)

    async def recognize_table_async(
        self,
        request: ocr_20191230_models.RecognizeTableRequest,
    ) -> ocr_20191230_models.RecognizeTableResponse:
        """
        @param request: RecognizeTableRequest
        @return: RecognizeTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_table_with_options_async(request, runtime)

    def recognize_table_advance(
        self,
        request: ocr_20191230_models.RecognizeTableAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeTableResponse:
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
            'Product': 'ocr',
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
        recognize_table_req = ocr_20191230_models.RecognizeTableRequest()
        OpenApiUtilClient.convert(request, recognize_table_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            recognize_table_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_table_resp = self.recognize_table_with_options(recognize_table_req, runtime)
        return recognize_table_resp

    async def recognize_table_advance_async(
        self,
        request: ocr_20191230_models.RecognizeTableAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeTableResponse:
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
            'Product': 'ocr',
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
        recognize_table_req = ocr_20191230_models.RecognizeTableRequest()
        OpenApiUtilClient.convert(request, recognize_table_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            recognize_table_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_table_resp = await self.recognize_table_with_options_async(recognize_table_req, runtime)
        return recognize_table_resp

    def recognize_taxi_invoice_with_options(
        self,
        request: ocr_20191230_models.RecognizeTaxiInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeTaxiInvoiceResponse:
        """
        @param request: RecognizeTaxiInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTaxiInvoiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeTaxiInvoice',
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
            ocr_20191230_models.RecognizeTaxiInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_taxi_invoice_with_options_async(
        self,
        request: ocr_20191230_models.RecognizeTaxiInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeTaxiInvoiceResponse:
        """
        @param request: RecognizeTaxiInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTaxiInvoiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeTaxiInvoice',
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
            ocr_20191230_models.RecognizeTaxiInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_taxi_invoice(
        self,
        request: ocr_20191230_models.RecognizeTaxiInvoiceRequest,
    ) -> ocr_20191230_models.RecognizeTaxiInvoiceResponse:
        """
        @param request: RecognizeTaxiInvoiceRequest
        @return: RecognizeTaxiInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_taxi_invoice_with_options(request, runtime)

    async def recognize_taxi_invoice_async(
        self,
        request: ocr_20191230_models.RecognizeTaxiInvoiceRequest,
    ) -> ocr_20191230_models.RecognizeTaxiInvoiceResponse:
        """
        @param request: RecognizeTaxiInvoiceRequest
        @return: RecognizeTaxiInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_taxi_invoice_with_options_async(request, runtime)

    def recognize_taxi_invoice_advance(
        self,
        request: ocr_20191230_models.RecognizeTaxiInvoiceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeTaxiInvoiceResponse:
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
            'Product': 'ocr',
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
        recognize_taxi_invoice_req = ocr_20191230_models.RecognizeTaxiInvoiceRequest()
        OpenApiUtilClient.convert(request, recognize_taxi_invoice_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            recognize_taxi_invoice_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_taxi_invoice_resp = self.recognize_taxi_invoice_with_options(recognize_taxi_invoice_req, runtime)
        return recognize_taxi_invoice_resp

    async def recognize_taxi_invoice_advance_async(
        self,
        request: ocr_20191230_models.RecognizeTaxiInvoiceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeTaxiInvoiceResponse:
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
            'Product': 'ocr',
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
        recognize_taxi_invoice_req = ocr_20191230_models.RecognizeTaxiInvoiceRequest()
        OpenApiUtilClient.convert(request, recognize_taxi_invoice_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            recognize_taxi_invoice_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_taxi_invoice_resp = await self.recognize_taxi_invoice_with_options_async(recognize_taxi_invoice_req, runtime)
        return recognize_taxi_invoice_resp

    def recognize_ticket_invoice_with_options(
        self,
        request: ocr_20191230_models.RecognizeTicketInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeTicketInvoiceResponse:
        """
        @summary 增值税发票卷票
        
        @param request: RecognizeTicketInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTicketInvoiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeTicketInvoice',
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
            ocr_20191230_models.RecognizeTicketInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_ticket_invoice_with_options_async(
        self,
        request: ocr_20191230_models.RecognizeTicketInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeTicketInvoiceResponse:
        """
        @summary 增值税发票卷票
        
        @param request: RecognizeTicketInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTicketInvoiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeTicketInvoice',
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
            ocr_20191230_models.RecognizeTicketInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_ticket_invoice(
        self,
        request: ocr_20191230_models.RecognizeTicketInvoiceRequest,
    ) -> ocr_20191230_models.RecognizeTicketInvoiceResponse:
        """
        @summary 增值税发票卷票
        
        @param request: RecognizeTicketInvoiceRequest
        @return: RecognizeTicketInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_ticket_invoice_with_options(request, runtime)

    async def recognize_ticket_invoice_async(
        self,
        request: ocr_20191230_models.RecognizeTicketInvoiceRequest,
    ) -> ocr_20191230_models.RecognizeTicketInvoiceResponse:
        """
        @summary 增值税发票卷票
        
        @param request: RecognizeTicketInvoiceRequest
        @return: RecognizeTicketInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_ticket_invoice_with_options_async(request, runtime)

    def recognize_ticket_invoice_advance(
        self,
        request: ocr_20191230_models.RecognizeTicketInvoiceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeTicketInvoiceResponse:
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
            'Product': 'ocr',
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
        recognize_ticket_invoice_req = ocr_20191230_models.RecognizeTicketInvoiceRequest()
        OpenApiUtilClient.convert(request, recognize_ticket_invoice_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            recognize_ticket_invoice_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_ticket_invoice_resp = self.recognize_ticket_invoice_with_options(recognize_ticket_invoice_req, runtime)
        return recognize_ticket_invoice_resp

    async def recognize_ticket_invoice_advance_async(
        self,
        request: ocr_20191230_models.RecognizeTicketInvoiceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeTicketInvoiceResponse:
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
            'Product': 'ocr',
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
        recognize_ticket_invoice_req = ocr_20191230_models.RecognizeTicketInvoiceRequest()
        OpenApiUtilClient.convert(request, recognize_ticket_invoice_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            recognize_ticket_invoice_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_ticket_invoice_resp = await self.recognize_ticket_invoice_with_options_async(recognize_ticket_invoice_req, runtime)
        return recognize_ticket_invoice_resp

    def recognize_train_ticket_with_options(
        self,
        request: ocr_20191230_models.RecognizeTrainTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeTrainTicketResponse:
        """
        @param request: RecognizeTrainTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTrainTicketResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeTrainTicket',
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
            ocr_20191230_models.RecognizeTrainTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_train_ticket_with_options_async(
        self,
        request: ocr_20191230_models.RecognizeTrainTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeTrainTicketResponse:
        """
        @param request: RecognizeTrainTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTrainTicketResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeTrainTicket',
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
            ocr_20191230_models.RecognizeTrainTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_train_ticket(
        self,
        request: ocr_20191230_models.RecognizeTrainTicketRequest,
    ) -> ocr_20191230_models.RecognizeTrainTicketResponse:
        """
        @param request: RecognizeTrainTicketRequest
        @return: RecognizeTrainTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_train_ticket_with_options(request, runtime)

    async def recognize_train_ticket_async(
        self,
        request: ocr_20191230_models.RecognizeTrainTicketRequest,
    ) -> ocr_20191230_models.RecognizeTrainTicketResponse:
        """
        @param request: RecognizeTrainTicketRequest
        @return: RecognizeTrainTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_train_ticket_with_options_async(request, runtime)

    def recognize_train_ticket_advance(
        self,
        request: ocr_20191230_models.RecognizeTrainTicketAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeTrainTicketResponse:
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
            'Product': 'ocr',
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
        recognize_train_ticket_req = ocr_20191230_models.RecognizeTrainTicketRequest()
        OpenApiUtilClient.convert(request, recognize_train_ticket_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            recognize_train_ticket_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_train_ticket_resp = self.recognize_train_ticket_with_options(recognize_train_ticket_req, runtime)
        return recognize_train_ticket_resp

    async def recognize_train_ticket_advance_async(
        self,
        request: ocr_20191230_models.RecognizeTrainTicketAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeTrainTicketResponse:
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
            'Product': 'ocr',
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
        recognize_train_ticket_req = ocr_20191230_models.RecognizeTrainTicketRequest()
        OpenApiUtilClient.convert(request, recognize_train_ticket_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            recognize_train_ticket_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_train_ticket_resp = await self.recognize_train_ticket_with_options_async(recognize_train_ticket_req, runtime)
        return recognize_train_ticket_resp

    def recognize_vatinvoice_with_options(
        self,
        request: ocr_20191230_models.RecognizeVATInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeVATInvoiceResponse:
        """
        @param request: RecognizeVATInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeVATInvoiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.file_url):
            body['FileURL'] = request.file_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeVATInvoice',
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
            ocr_20191230_models.RecognizeVATInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_vatinvoice_with_options_async(
        self,
        request: ocr_20191230_models.RecognizeVATInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeVATInvoiceResponse:
        """
        @param request: RecognizeVATInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeVATInvoiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.file_url):
            body['FileURL'] = request.file_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeVATInvoice',
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
            ocr_20191230_models.RecognizeVATInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_vatinvoice(
        self,
        request: ocr_20191230_models.RecognizeVATInvoiceRequest,
    ) -> ocr_20191230_models.RecognizeVATInvoiceResponse:
        """
        @param request: RecognizeVATInvoiceRequest
        @return: RecognizeVATInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_vatinvoice_with_options(request, runtime)

    async def recognize_vatinvoice_async(
        self,
        request: ocr_20191230_models.RecognizeVATInvoiceRequest,
    ) -> ocr_20191230_models.RecognizeVATInvoiceResponse:
        """
        @param request: RecognizeVATInvoiceRequest
        @return: RecognizeVATInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_vatinvoice_with_options_async(request, runtime)

    def recognize_vatinvoice_advance(
        self,
        request: ocr_20191230_models.RecognizeVATInvoiceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeVATInvoiceResponse:
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
            'Product': 'ocr',
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
        recognize_vatinvoice_req = ocr_20191230_models.RecognizeVATInvoiceRequest()
        OpenApiUtilClient.convert(request, recognize_vatinvoice_req)
        if not UtilClient.is_unset(request.file_urlobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_urlobject,
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            recognize_vatinvoice_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_vatinvoice_resp = self.recognize_vatinvoice_with_options(recognize_vatinvoice_req, runtime)
        return recognize_vatinvoice_resp

    async def recognize_vatinvoice_advance_async(
        self,
        request: ocr_20191230_models.RecognizeVATInvoiceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeVATInvoiceResponse:
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
            'Product': 'ocr',
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
        recognize_vatinvoice_req = ocr_20191230_models.RecognizeVATInvoiceRequest()
        OpenApiUtilClient.convert(request, recognize_vatinvoice_req)
        if not UtilClient.is_unset(request.file_urlobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_urlobject,
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            recognize_vatinvoice_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_vatinvoice_resp = await self.recognize_vatinvoice_with_options_async(recognize_vatinvoice_req, runtime)
        return recognize_vatinvoice_resp

    def recognize_vincode_with_options(
        self,
        request: ocr_20191230_models.RecognizeVINCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeVINCodeResponse:
        """
        @param request: RecognizeVINCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeVINCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_url):
            query['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecognizeVINCode',
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
            ocr_20191230_models.RecognizeVINCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_vincode_with_options_async(
        self,
        request: ocr_20191230_models.RecognizeVINCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeVINCodeResponse:
        """
        @param request: RecognizeVINCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeVINCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_url):
            query['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecognizeVINCode',
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
            ocr_20191230_models.RecognizeVINCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_vincode(
        self,
        request: ocr_20191230_models.RecognizeVINCodeRequest,
    ) -> ocr_20191230_models.RecognizeVINCodeResponse:
        """
        @param request: RecognizeVINCodeRequest
        @return: RecognizeVINCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_vincode_with_options(request, runtime)

    async def recognize_vincode_async(
        self,
        request: ocr_20191230_models.RecognizeVINCodeRequest,
    ) -> ocr_20191230_models.RecognizeVINCodeResponse:
        """
        @param request: RecognizeVINCodeRequest
        @return: RecognizeVINCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_vincode_with_options_async(request, runtime)

    def recognize_vincode_advance(
        self,
        request: ocr_20191230_models.RecognizeVINCodeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeVINCodeResponse:
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
            'Product': 'ocr',
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
        recognize_vincode_req = ocr_20191230_models.RecognizeVINCodeRequest()
        OpenApiUtilClient.convert(request, recognize_vincode_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            recognize_vincode_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_vincode_resp = self.recognize_vincode_with_options(recognize_vincode_req, runtime)
        return recognize_vincode_resp

    async def recognize_vincode_advance_async(
        self,
        request: ocr_20191230_models.RecognizeVINCodeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeVINCodeResponse:
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
            'Product': 'ocr',
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
        recognize_vincode_req = ocr_20191230_models.RecognizeVINCodeRequest()
        OpenApiUtilClient.convert(request, recognize_vincode_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            recognize_vincode_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_vincode_resp = await self.recognize_vincode_with_options_async(recognize_vincode_req, runtime)
        return recognize_vincode_resp

    def recognize_video_character_with_options(
        self,
        request: ocr_20191230_models.RecognizeVideoCharacterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeVideoCharacterResponse:
        """
        @summary 通用视频文字识别
        
        @param request: RecognizeVideoCharacterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeVideoCharacterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeVideoCharacter',
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
            ocr_20191230_models.RecognizeVideoCharacterResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_video_character_with_options_async(
        self,
        request: ocr_20191230_models.RecognizeVideoCharacterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeVideoCharacterResponse:
        """
        @summary 通用视频文字识别
        
        @param request: RecognizeVideoCharacterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeVideoCharacterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeVideoCharacter',
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
            ocr_20191230_models.RecognizeVideoCharacterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_video_character(
        self,
        request: ocr_20191230_models.RecognizeVideoCharacterRequest,
    ) -> ocr_20191230_models.RecognizeVideoCharacterResponse:
        """
        @summary 通用视频文字识别
        
        @param request: RecognizeVideoCharacterRequest
        @return: RecognizeVideoCharacterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_video_character_with_options(request, runtime)

    async def recognize_video_character_async(
        self,
        request: ocr_20191230_models.RecognizeVideoCharacterRequest,
    ) -> ocr_20191230_models.RecognizeVideoCharacterResponse:
        """
        @summary 通用视频文字识别
        
        @param request: RecognizeVideoCharacterRequest
        @return: RecognizeVideoCharacterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_video_character_with_options_async(request, runtime)

    def recognize_video_character_advance(
        self,
        request: ocr_20191230_models.RecognizeVideoCharacterAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeVideoCharacterResponse:
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
            'Product': 'ocr',
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
        recognize_video_character_req = ocr_20191230_models.RecognizeVideoCharacterRequest()
        OpenApiUtilClient.convert(request, recognize_video_character_req)
        if not UtilClient.is_unset(request.video_urlobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.video_urlobject,
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            recognize_video_character_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_video_character_resp = self.recognize_video_character_with_options(recognize_video_character_req, runtime)
        return recognize_video_character_resp

    async def recognize_video_character_advance_async(
        self,
        request: ocr_20191230_models.RecognizeVideoCharacterAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_20191230_models.RecognizeVideoCharacterResponse:
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
            'Product': 'ocr',
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
        recognize_video_character_req = ocr_20191230_models.RecognizeVideoCharacterRequest()
        OpenApiUtilClient.convert(request, recognize_video_character_req)
        if not UtilClient.is_unset(request.video_urlobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.video_urlobject,
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            recognize_video_character_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        recognize_video_character_resp = await self.recognize_video_character_with_options_async(recognize_video_character_req, runtime)
        return recognize_video_character_resp
