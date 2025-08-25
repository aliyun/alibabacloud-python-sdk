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
from alibabacloud_videoenhan20200320 import models as videoenhan_20200320_models
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
        self._endpoint = self.get_endpoint('videoenhan', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abstract_ecommerce_video_with_options(
        self,
        request: videoenhan_20200320_models.AbstractEcommerceVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractEcommerceVideoResponse:
        """
        @param request: AbstractEcommerceVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbstractEcommerceVideoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        if not UtilClient.is_unset(request.width):
            body['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AbstractEcommerceVideo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.AbstractEcommerceVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def abstract_ecommerce_video_with_options_async(
        self,
        request: videoenhan_20200320_models.AbstractEcommerceVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractEcommerceVideoResponse:
        """
        @param request: AbstractEcommerceVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbstractEcommerceVideoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        if not UtilClient.is_unset(request.width):
            body['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AbstractEcommerceVideo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.AbstractEcommerceVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abstract_ecommerce_video(
        self,
        request: videoenhan_20200320_models.AbstractEcommerceVideoRequest,
    ) -> videoenhan_20200320_models.AbstractEcommerceVideoResponse:
        """
        @param request: AbstractEcommerceVideoRequest
        @return: AbstractEcommerceVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.abstract_ecommerce_video_with_options(request, runtime)

    async def abstract_ecommerce_video_async(
        self,
        request: videoenhan_20200320_models.AbstractEcommerceVideoRequest,
    ) -> videoenhan_20200320_models.AbstractEcommerceVideoResponse:
        """
        @param request: AbstractEcommerceVideoRequest
        @return: AbstractEcommerceVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.abstract_ecommerce_video_with_options_async(request, runtime)

    def abstract_ecommerce_video_advance(
        self,
        request: videoenhan_20200320_models.AbstractEcommerceVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractEcommerceVideoResponse:
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
            'Product': 'videoenhan',
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
        abstract_ecommerce_video_req = videoenhan_20200320_models.AbstractEcommerceVideoRequest()
        OpenApiUtilClient.convert(request, abstract_ecommerce_video_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            abstract_ecommerce_video_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        abstract_ecommerce_video_resp = self.abstract_ecommerce_video_with_options(abstract_ecommerce_video_req, runtime)
        return abstract_ecommerce_video_resp

    async def abstract_ecommerce_video_advance_async(
        self,
        request: videoenhan_20200320_models.AbstractEcommerceVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractEcommerceVideoResponse:
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
            'Product': 'videoenhan',
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
        abstract_ecommerce_video_req = videoenhan_20200320_models.AbstractEcommerceVideoRequest()
        OpenApiUtilClient.convert(request, abstract_ecommerce_video_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            abstract_ecommerce_video_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        abstract_ecommerce_video_resp = await self.abstract_ecommerce_video_with_options_async(abstract_ecommerce_video_req, runtime)
        return abstract_ecommerce_video_resp

    def abstract_film_video_with_options(
        self,
        request: videoenhan_20200320_models.AbstractFilmVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractFilmVideoResponse:
        """
        @param request: AbstractFilmVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbstractFilmVideoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.length):
            body['Length'] = request.length
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AbstractFilmVideo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.AbstractFilmVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def abstract_film_video_with_options_async(
        self,
        request: videoenhan_20200320_models.AbstractFilmVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractFilmVideoResponse:
        """
        @param request: AbstractFilmVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbstractFilmVideoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.length):
            body['Length'] = request.length
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AbstractFilmVideo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.AbstractFilmVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abstract_film_video(
        self,
        request: videoenhan_20200320_models.AbstractFilmVideoRequest,
    ) -> videoenhan_20200320_models.AbstractFilmVideoResponse:
        """
        @param request: AbstractFilmVideoRequest
        @return: AbstractFilmVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.abstract_film_video_with_options(request, runtime)

    async def abstract_film_video_async(
        self,
        request: videoenhan_20200320_models.AbstractFilmVideoRequest,
    ) -> videoenhan_20200320_models.AbstractFilmVideoResponse:
        """
        @param request: AbstractFilmVideoRequest
        @return: AbstractFilmVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.abstract_film_video_with_options_async(request, runtime)

    def abstract_film_video_advance(
        self,
        request: videoenhan_20200320_models.AbstractFilmVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractFilmVideoResponse:
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
            'Product': 'videoenhan',
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
        abstract_film_video_req = videoenhan_20200320_models.AbstractFilmVideoRequest()
        OpenApiUtilClient.convert(request, abstract_film_video_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            abstract_film_video_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        abstract_film_video_resp = self.abstract_film_video_with_options(abstract_film_video_req, runtime)
        return abstract_film_video_resp

    async def abstract_film_video_advance_async(
        self,
        request: videoenhan_20200320_models.AbstractFilmVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractFilmVideoResponse:
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
            'Product': 'videoenhan',
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
        abstract_film_video_req = videoenhan_20200320_models.AbstractFilmVideoRequest()
        OpenApiUtilClient.convert(request, abstract_film_video_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            abstract_film_video_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        abstract_film_video_resp = await self.abstract_film_video_with_options_async(abstract_film_video_req, runtime)
        return abstract_film_video_resp

    def add_face_video_template_with_options(
        self,
        request: videoenhan_20200320_models.AddFaceVideoTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AddFaceVideoTemplateResponse:
        """
        @summary 视频人脸融合模板增加
        
        @param request: AddFaceVideoTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFaceVideoTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.video_scene):
            body['VideoScene'] = request.video_scene
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFaceVideoTemplate',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.AddFaceVideoTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_video_template_with_options_async(
        self,
        request: videoenhan_20200320_models.AddFaceVideoTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AddFaceVideoTemplateResponse:
        """
        @summary 视频人脸融合模板增加
        
        @param request: AddFaceVideoTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFaceVideoTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.video_scene):
            body['VideoScene'] = request.video_scene
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFaceVideoTemplate',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.AddFaceVideoTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_face_video_template(
        self,
        request: videoenhan_20200320_models.AddFaceVideoTemplateRequest,
    ) -> videoenhan_20200320_models.AddFaceVideoTemplateResponse:
        """
        @summary 视频人脸融合模板增加
        
        @param request: AddFaceVideoTemplateRequest
        @return: AddFaceVideoTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_face_video_template_with_options(request, runtime)

    async def add_face_video_template_async(
        self,
        request: videoenhan_20200320_models.AddFaceVideoTemplateRequest,
    ) -> videoenhan_20200320_models.AddFaceVideoTemplateResponse:
        """
        @summary 视频人脸融合模板增加
        
        @param request: AddFaceVideoTemplateRequest
        @return: AddFaceVideoTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_face_video_template_with_options_async(request, runtime)

    def add_face_video_template_advance(
        self,
        request: videoenhan_20200320_models.AddFaceVideoTemplateAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AddFaceVideoTemplateResponse:
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
            'Product': 'videoenhan',
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
        add_face_video_template_req = videoenhan_20200320_models.AddFaceVideoTemplateRequest()
        OpenApiUtilClient.convert(request, add_face_video_template_req)
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
            add_face_video_template_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        add_face_video_template_resp = self.add_face_video_template_with_options(add_face_video_template_req, runtime)
        return add_face_video_template_resp

    async def add_face_video_template_advance_async(
        self,
        request: videoenhan_20200320_models.AddFaceVideoTemplateAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AddFaceVideoTemplateResponse:
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
            'Product': 'videoenhan',
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
        add_face_video_template_req = videoenhan_20200320_models.AddFaceVideoTemplateRequest()
        OpenApiUtilClient.convert(request, add_face_video_template_req)
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
            add_face_video_template_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        add_face_video_template_resp = await self.add_face_video_template_with_options_async(add_face_video_template_req, runtime)
        return add_face_video_template_resp

    def adjust_video_color_with_options(
        self,
        request: videoenhan_20200320_models.AdjustVideoColorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AdjustVideoColorResponse:
        """
        @param request: AdjustVideoColorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AdjustVideoColorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.video_bitrate):
            body['VideoBitrate'] = request.video_bitrate
        if not UtilClient.is_unset(request.video_codec):
            body['VideoCodec'] = request.video_codec
        if not UtilClient.is_unset(request.video_format):
            body['VideoFormat'] = request.video_format
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AdjustVideoColor',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.AdjustVideoColorResponse(),
            self.call_api(params, req, runtime)
        )

    async def adjust_video_color_with_options_async(
        self,
        request: videoenhan_20200320_models.AdjustVideoColorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AdjustVideoColorResponse:
        """
        @param request: AdjustVideoColorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AdjustVideoColorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.video_bitrate):
            body['VideoBitrate'] = request.video_bitrate
        if not UtilClient.is_unset(request.video_codec):
            body['VideoCodec'] = request.video_codec
        if not UtilClient.is_unset(request.video_format):
            body['VideoFormat'] = request.video_format
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AdjustVideoColor',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.AdjustVideoColorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def adjust_video_color(
        self,
        request: videoenhan_20200320_models.AdjustVideoColorRequest,
    ) -> videoenhan_20200320_models.AdjustVideoColorResponse:
        """
        @param request: AdjustVideoColorRequest
        @return: AdjustVideoColorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.adjust_video_color_with_options(request, runtime)

    async def adjust_video_color_async(
        self,
        request: videoenhan_20200320_models.AdjustVideoColorRequest,
    ) -> videoenhan_20200320_models.AdjustVideoColorResponse:
        """
        @param request: AdjustVideoColorRequest
        @return: AdjustVideoColorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.adjust_video_color_with_options_async(request, runtime)

    def adjust_video_color_advance(
        self,
        request: videoenhan_20200320_models.AdjustVideoColorAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AdjustVideoColorResponse:
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
            'Product': 'videoenhan',
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
        adjust_video_color_req = videoenhan_20200320_models.AdjustVideoColorRequest()
        OpenApiUtilClient.convert(request, adjust_video_color_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            adjust_video_color_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        adjust_video_color_resp = self.adjust_video_color_with_options(adjust_video_color_req, runtime)
        return adjust_video_color_resp

    async def adjust_video_color_advance_async(
        self,
        request: videoenhan_20200320_models.AdjustVideoColorAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AdjustVideoColorResponse:
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
            'Product': 'videoenhan',
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
        adjust_video_color_req = videoenhan_20200320_models.AdjustVideoColorRequest()
        OpenApiUtilClient.convert(request, adjust_video_color_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            adjust_video_color_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        adjust_video_color_resp = await self.adjust_video_color_with_options_async(adjust_video_color_req, runtime)
        return adjust_video_color_resp

    def change_video_size_with_options(
        self,
        request: videoenhan_20200320_models.ChangeVideoSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ChangeVideoSizeResponse:
        """
        @param request: ChangeVideoSizeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeVideoSizeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.b):
            body['B'] = request.b
        if not UtilClient.is_unset(request.crop_type):
            body['CropType'] = request.crop_type
        if not UtilClient.is_unset(request.fill_type):
            body['FillType'] = request.fill_type
        if not UtilClient.is_unset(request.g):
            body['G'] = request.g
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        if not UtilClient.is_unset(request.r):
            body['R'] = request.r
        if not UtilClient.is_unset(request.tightness):
            body['Tightness'] = request.tightness
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        if not UtilClient.is_unset(request.width):
            body['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeVideoSize',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.ChangeVideoSizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_video_size_with_options_async(
        self,
        request: videoenhan_20200320_models.ChangeVideoSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ChangeVideoSizeResponse:
        """
        @param request: ChangeVideoSizeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeVideoSizeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.b):
            body['B'] = request.b
        if not UtilClient.is_unset(request.crop_type):
            body['CropType'] = request.crop_type
        if not UtilClient.is_unset(request.fill_type):
            body['FillType'] = request.fill_type
        if not UtilClient.is_unset(request.g):
            body['G'] = request.g
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        if not UtilClient.is_unset(request.r):
            body['R'] = request.r
        if not UtilClient.is_unset(request.tightness):
            body['Tightness'] = request.tightness
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        if not UtilClient.is_unset(request.width):
            body['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeVideoSize',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.ChangeVideoSizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_video_size(
        self,
        request: videoenhan_20200320_models.ChangeVideoSizeRequest,
    ) -> videoenhan_20200320_models.ChangeVideoSizeResponse:
        """
        @param request: ChangeVideoSizeRequest
        @return: ChangeVideoSizeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_video_size_with_options(request, runtime)

    async def change_video_size_async(
        self,
        request: videoenhan_20200320_models.ChangeVideoSizeRequest,
    ) -> videoenhan_20200320_models.ChangeVideoSizeResponse:
        """
        @param request: ChangeVideoSizeRequest
        @return: ChangeVideoSizeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_video_size_with_options_async(request, runtime)

    def change_video_size_advance(
        self,
        request: videoenhan_20200320_models.ChangeVideoSizeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ChangeVideoSizeResponse:
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
            'Product': 'videoenhan',
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
        change_video_size_req = videoenhan_20200320_models.ChangeVideoSizeRequest()
        OpenApiUtilClient.convert(request, change_video_size_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            change_video_size_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        change_video_size_resp = self.change_video_size_with_options(change_video_size_req, runtime)
        return change_video_size_resp

    async def change_video_size_advance_async(
        self,
        request: videoenhan_20200320_models.ChangeVideoSizeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ChangeVideoSizeResponse:
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
            'Product': 'videoenhan',
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
        change_video_size_req = videoenhan_20200320_models.ChangeVideoSizeRequest()
        OpenApiUtilClient.convert(request, change_video_size_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            change_video_size_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        change_video_size_resp = await self.change_video_size_with_options_async(change_video_size_req, runtime)
        return change_video_size_resp

    def convert_hdr_video_with_options(
        self,
        request: videoenhan_20200320_models.ConvertHdrVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ConvertHdrVideoResponse:
        """
        @param request: ConvertHdrVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertHdrVideoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bitrate):
            body['Bitrate'] = request.bitrate
        if not UtilClient.is_unset(request.hdrformat):
            body['HDRFormat'] = request.hdrformat
        if not UtilClient.is_unset(request.max_illuminance):
            body['MaxIlluminance'] = request.max_illuminance
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConvertHdrVideo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.ConvertHdrVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_hdr_video_with_options_async(
        self,
        request: videoenhan_20200320_models.ConvertHdrVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ConvertHdrVideoResponse:
        """
        @param request: ConvertHdrVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertHdrVideoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bitrate):
            body['Bitrate'] = request.bitrate
        if not UtilClient.is_unset(request.hdrformat):
            body['HDRFormat'] = request.hdrformat
        if not UtilClient.is_unset(request.max_illuminance):
            body['MaxIlluminance'] = request.max_illuminance
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConvertHdrVideo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.ConvertHdrVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_hdr_video(
        self,
        request: videoenhan_20200320_models.ConvertHdrVideoRequest,
    ) -> videoenhan_20200320_models.ConvertHdrVideoResponse:
        """
        @param request: ConvertHdrVideoRequest
        @return: ConvertHdrVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.convert_hdr_video_with_options(request, runtime)

    async def convert_hdr_video_async(
        self,
        request: videoenhan_20200320_models.ConvertHdrVideoRequest,
    ) -> videoenhan_20200320_models.ConvertHdrVideoResponse:
        """
        @param request: ConvertHdrVideoRequest
        @return: ConvertHdrVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.convert_hdr_video_with_options_async(request, runtime)

    def convert_hdr_video_advance(
        self,
        request: videoenhan_20200320_models.ConvertHdrVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ConvertHdrVideoResponse:
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
            'Product': 'videoenhan',
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
        convert_hdr_video_req = videoenhan_20200320_models.ConvertHdrVideoRequest()
        OpenApiUtilClient.convert(request, convert_hdr_video_req)
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
            convert_hdr_video_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        convert_hdr_video_resp = self.convert_hdr_video_with_options(convert_hdr_video_req, runtime)
        return convert_hdr_video_resp

    async def convert_hdr_video_advance_async(
        self,
        request: videoenhan_20200320_models.ConvertHdrVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ConvertHdrVideoResponse:
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
            'Product': 'videoenhan',
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
        convert_hdr_video_req = videoenhan_20200320_models.ConvertHdrVideoRequest()
        OpenApiUtilClient.convert(request, convert_hdr_video_req)
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
            convert_hdr_video_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        convert_hdr_video_resp = await self.convert_hdr_video_with_options_async(convert_hdr_video_req, runtime)
        return convert_hdr_video_resp

    def delete_face_video_template_with_options(
        self,
        request: videoenhan_20200320_models.DeleteFaceVideoTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.DeleteFaceVideoTemplateResponse:
        """
        @summary 视频人脸融合模板删除
        
        @param request: DeleteFaceVideoTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFaceVideoTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFaceVideoTemplate',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.DeleteFaceVideoTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_video_template_with_options_async(
        self,
        request: videoenhan_20200320_models.DeleteFaceVideoTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.DeleteFaceVideoTemplateResponse:
        """
        @summary 视频人脸融合模板删除
        
        @param request: DeleteFaceVideoTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFaceVideoTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFaceVideoTemplate',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.DeleteFaceVideoTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face_video_template(
        self,
        request: videoenhan_20200320_models.DeleteFaceVideoTemplateRequest,
    ) -> videoenhan_20200320_models.DeleteFaceVideoTemplateResponse:
        """
        @summary 视频人脸融合模板删除
        
        @param request: DeleteFaceVideoTemplateRequest
        @return: DeleteFaceVideoTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_face_video_template_with_options(request, runtime)

    async def delete_face_video_template_async(
        self,
        request: videoenhan_20200320_models.DeleteFaceVideoTemplateRequest,
    ) -> videoenhan_20200320_models.DeleteFaceVideoTemplateResponse:
        """
        @summary 视频人脸融合模板删除
        
        @param request: DeleteFaceVideoTemplateRequest
        @return: DeleteFaceVideoTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_video_template_with_options_async(request, runtime)

    def enhance_portrait_video_with_options(
        self,
        request: videoenhan_20200320_models.EnhancePortraitVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EnhancePortraitVideoResponse:
        """
        @summary 视频人像增强
        
        @param request: EnhancePortraitVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnhancePortraitVideoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnhancePortraitVideo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.EnhancePortraitVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def enhance_portrait_video_with_options_async(
        self,
        request: videoenhan_20200320_models.EnhancePortraitVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EnhancePortraitVideoResponse:
        """
        @summary 视频人像增强
        
        @param request: EnhancePortraitVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnhancePortraitVideoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnhancePortraitVideo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.EnhancePortraitVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enhance_portrait_video(
        self,
        request: videoenhan_20200320_models.EnhancePortraitVideoRequest,
    ) -> videoenhan_20200320_models.EnhancePortraitVideoResponse:
        """
        @summary 视频人像增强
        
        @param request: EnhancePortraitVideoRequest
        @return: EnhancePortraitVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enhance_portrait_video_with_options(request, runtime)

    async def enhance_portrait_video_async(
        self,
        request: videoenhan_20200320_models.EnhancePortraitVideoRequest,
    ) -> videoenhan_20200320_models.EnhancePortraitVideoResponse:
        """
        @summary 视频人像增强
        
        @param request: EnhancePortraitVideoRequest
        @return: EnhancePortraitVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enhance_portrait_video_with_options_async(request, runtime)

    def enhance_portrait_video_advance(
        self,
        request: videoenhan_20200320_models.EnhancePortraitVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EnhancePortraitVideoResponse:
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
            'Product': 'videoenhan',
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
        enhance_portrait_video_req = videoenhan_20200320_models.EnhancePortraitVideoRequest()
        OpenApiUtilClient.convert(request, enhance_portrait_video_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            enhance_portrait_video_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        enhance_portrait_video_resp = self.enhance_portrait_video_with_options(enhance_portrait_video_req, runtime)
        return enhance_portrait_video_resp

    async def enhance_portrait_video_advance_async(
        self,
        request: videoenhan_20200320_models.EnhancePortraitVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EnhancePortraitVideoResponse:
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
            'Product': 'videoenhan',
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
        enhance_portrait_video_req = videoenhan_20200320_models.EnhancePortraitVideoRequest()
        OpenApiUtilClient.convert(request, enhance_portrait_video_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            enhance_portrait_video_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        enhance_portrait_video_resp = await self.enhance_portrait_video_with_options_async(enhance_portrait_video_req, runtime)
        return enhance_portrait_video_resp

    def enhance_video_quality_with_options(
        self,
        request: videoenhan_20200320_models.EnhanceVideoQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EnhanceVideoQualityResponse:
        """
        @param request: EnhanceVideoQualityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnhanceVideoQualityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bitrate):
            body['Bitrate'] = request.bitrate
        if not UtilClient.is_unset(request.frame_rate):
            body['FrameRate'] = request.frame_rate
        if not UtilClient.is_unset(request.hdrformat):
            body['HDRFormat'] = request.hdrformat
        if not UtilClient.is_unset(request.max_illuminance):
            body['MaxIlluminance'] = request.max_illuminance
        if not UtilClient.is_unset(request.out_put_height):
            body['OutPutHeight'] = request.out_put_height
        if not UtilClient.is_unset(request.out_put_width):
            body['OutPutWidth'] = request.out_put_width
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnhanceVideoQuality',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.EnhanceVideoQualityResponse(),
            self.call_api(params, req, runtime)
        )

    async def enhance_video_quality_with_options_async(
        self,
        request: videoenhan_20200320_models.EnhanceVideoQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EnhanceVideoQualityResponse:
        """
        @param request: EnhanceVideoQualityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnhanceVideoQualityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bitrate):
            body['Bitrate'] = request.bitrate
        if not UtilClient.is_unset(request.frame_rate):
            body['FrameRate'] = request.frame_rate
        if not UtilClient.is_unset(request.hdrformat):
            body['HDRFormat'] = request.hdrformat
        if not UtilClient.is_unset(request.max_illuminance):
            body['MaxIlluminance'] = request.max_illuminance
        if not UtilClient.is_unset(request.out_put_height):
            body['OutPutHeight'] = request.out_put_height
        if not UtilClient.is_unset(request.out_put_width):
            body['OutPutWidth'] = request.out_put_width
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnhanceVideoQuality',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.EnhanceVideoQualityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enhance_video_quality(
        self,
        request: videoenhan_20200320_models.EnhanceVideoQualityRequest,
    ) -> videoenhan_20200320_models.EnhanceVideoQualityResponse:
        """
        @param request: EnhanceVideoQualityRequest
        @return: EnhanceVideoQualityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enhance_video_quality_with_options(request, runtime)

    async def enhance_video_quality_async(
        self,
        request: videoenhan_20200320_models.EnhanceVideoQualityRequest,
    ) -> videoenhan_20200320_models.EnhanceVideoQualityResponse:
        """
        @param request: EnhanceVideoQualityRequest
        @return: EnhanceVideoQualityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enhance_video_quality_with_options_async(request, runtime)

    def enhance_video_quality_advance(
        self,
        request: videoenhan_20200320_models.EnhanceVideoQualityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EnhanceVideoQualityResponse:
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
            'Product': 'videoenhan',
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
        enhance_video_quality_req = videoenhan_20200320_models.EnhanceVideoQualityRequest()
        OpenApiUtilClient.convert(request, enhance_video_quality_req)
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
            enhance_video_quality_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        enhance_video_quality_resp = self.enhance_video_quality_with_options(enhance_video_quality_req, runtime)
        return enhance_video_quality_resp

    async def enhance_video_quality_advance_async(
        self,
        request: videoenhan_20200320_models.EnhanceVideoQualityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EnhanceVideoQualityResponse:
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
            'Product': 'videoenhan',
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
        enhance_video_quality_req = videoenhan_20200320_models.EnhanceVideoQualityRequest()
        OpenApiUtilClient.convert(request, enhance_video_quality_req)
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
            enhance_video_quality_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        enhance_video_quality_resp = await self.enhance_video_quality_with_options_async(enhance_video_quality_req, runtime)
        return enhance_video_quality_resp

    def erase_video_logo_with_options(
        self,
        request: videoenhan_20200320_models.EraseVideoLogoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoLogoResponse:
        """
        @param request: EraseVideoLogoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EraseVideoLogoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.boxes):
            body['Boxes'] = request.boxes
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EraseVideoLogo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.EraseVideoLogoResponse(),
            self.call_api(params, req, runtime)
        )

    async def erase_video_logo_with_options_async(
        self,
        request: videoenhan_20200320_models.EraseVideoLogoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoLogoResponse:
        """
        @param request: EraseVideoLogoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EraseVideoLogoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.boxes):
            body['Boxes'] = request.boxes
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EraseVideoLogo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.EraseVideoLogoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def erase_video_logo(
        self,
        request: videoenhan_20200320_models.EraseVideoLogoRequest,
    ) -> videoenhan_20200320_models.EraseVideoLogoResponse:
        """
        @param request: EraseVideoLogoRequest
        @return: EraseVideoLogoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.erase_video_logo_with_options(request, runtime)

    async def erase_video_logo_async(
        self,
        request: videoenhan_20200320_models.EraseVideoLogoRequest,
    ) -> videoenhan_20200320_models.EraseVideoLogoResponse:
        """
        @param request: EraseVideoLogoRequest
        @return: EraseVideoLogoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.erase_video_logo_with_options_async(request, runtime)

    def erase_video_logo_advance(
        self,
        request: videoenhan_20200320_models.EraseVideoLogoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoLogoResponse:
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
            'Product': 'videoenhan',
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
        erase_video_logo_req = videoenhan_20200320_models.EraseVideoLogoRequest()
        OpenApiUtilClient.convert(request, erase_video_logo_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            erase_video_logo_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        erase_video_logo_resp = self.erase_video_logo_with_options(erase_video_logo_req, runtime)
        return erase_video_logo_resp

    async def erase_video_logo_advance_async(
        self,
        request: videoenhan_20200320_models.EraseVideoLogoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoLogoResponse:
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
            'Product': 'videoenhan',
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
        erase_video_logo_req = videoenhan_20200320_models.EraseVideoLogoRequest()
        OpenApiUtilClient.convert(request, erase_video_logo_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            erase_video_logo_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        erase_video_logo_resp = await self.erase_video_logo_with_options_async(erase_video_logo_req, runtime)
        return erase_video_logo_resp

    def erase_video_subtitles_with_options(
        self,
        request: videoenhan_20200320_models.EraseVideoSubtitlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoSubtitlesResponse:
        """
        @param request: EraseVideoSubtitlesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EraseVideoSubtitlesResponse
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
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EraseVideoSubtitles',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.EraseVideoSubtitlesResponse(),
            self.call_api(params, req, runtime)
        )

    async def erase_video_subtitles_with_options_async(
        self,
        request: videoenhan_20200320_models.EraseVideoSubtitlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoSubtitlesResponse:
        """
        @param request: EraseVideoSubtitlesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EraseVideoSubtitlesResponse
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
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EraseVideoSubtitles',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.EraseVideoSubtitlesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def erase_video_subtitles(
        self,
        request: videoenhan_20200320_models.EraseVideoSubtitlesRequest,
    ) -> videoenhan_20200320_models.EraseVideoSubtitlesResponse:
        """
        @param request: EraseVideoSubtitlesRequest
        @return: EraseVideoSubtitlesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.erase_video_subtitles_with_options(request, runtime)

    async def erase_video_subtitles_async(
        self,
        request: videoenhan_20200320_models.EraseVideoSubtitlesRequest,
    ) -> videoenhan_20200320_models.EraseVideoSubtitlesResponse:
        """
        @param request: EraseVideoSubtitlesRequest
        @return: EraseVideoSubtitlesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.erase_video_subtitles_with_options_async(request, runtime)

    def erase_video_subtitles_advance(
        self,
        request: videoenhan_20200320_models.EraseVideoSubtitlesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoSubtitlesResponse:
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
            'Product': 'videoenhan',
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
        erase_video_subtitles_req = videoenhan_20200320_models.EraseVideoSubtitlesRequest()
        OpenApiUtilClient.convert(request, erase_video_subtitles_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            erase_video_subtitles_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        erase_video_subtitles_resp = self.erase_video_subtitles_with_options(erase_video_subtitles_req, runtime)
        return erase_video_subtitles_resp

    async def erase_video_subtitles_advance_async(
        self,
        request: videoenhan_20200320_models.EraseVideoSubtitlesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoSubtitlesResponse:
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
            'Product': 'videoenhan',
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
        erase_video_subtitles_req = videoenhan_20200320_models.EraseVideoSubtitlesRequest()
        OpenApiUtilClient.convert(request, erase_video_subtitles_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            erase_video_subtitles_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        erase_video_subtitles_resp = await self.erase_video_subtitles_with_options_async(erase_video_subtitles_req, runtime)
        return erase_video_subtitles_resp

    def generate_human_anime_style_video_with_options(
        self,
        request: videoenhan_20200320_models.GenerateHumanAnimeStyleVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GenerateHumanAnimeStyleVideoResponse:
        """
        @summary 视频人像卡通化
        
        @param request: GenerateHumanAnimeStyleVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateHumanAnimeStyleVideoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cartoon_style):
            body['CartoonStyle'] = request.cartoon_style
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateHumanAnimeStyleVideo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.GenerateHumanAnimeStyleVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_human_anime_style_video_with_options_async(
        self,
        request: videoenhan_20200320_models.GenerateHumanAnimeStyleVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GenerateHumanAnimeStyleVideoResponse:
        """
        @summary 视频人像卡通化
        
        @param request: GenerateHumanAnimeStyleVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateHumanAnimeStyleVideoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cartoon_style):
            body['CartoonStyle'] = request.cartoon_style
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateHumanAnimeStyleVideo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.GenerateHumanAnimeStyleVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_human_anime_style_video(
        self,
        request: videoenhan_20200320_models.GenerateHumanAnimeStyleVideoRequest,
    ) -> videoenhan_20200320_models.GenerateHumanAnimeStyleVideoResponse:
        """
        @summary 视频人像卡通化
        
        @param request: GenerateHumanAnimeStyleVideoRequest
        @return: GenerateHumanAnimeStyleVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_human_anime_style_video_with_options(request, runtime)

    async def generate_human_anime_style_video_async(
        self,
        request: videoenhan_20200320_models.GenerateHumanAnimeStyleVideoRequest,
    ) -> videoenhan_20200320_models.GenerateHumanAnimeStyleVideoResponse:
        """
        @summary 视频人像卡通化
        
        @param request: GenerateHumanAnimeStyleVideoRequest
        @return: GenerateHumanAnimeStyleVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_human_anime_style_video_with_options_async(request, runtime)

    def generate_human_anime_style_video_advance(
        self,
        request: videoenhan_20200320_models.GenerateHumanAnimeStyleVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GenerateHumanAnimeStyleVideoResponse:
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
            'Product': 'videoenhan',
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
        generate_human_anime_style_video_req = videoenhan_20200320_models.GenerateHumanAnimeStyleVideoRequest()
        OpenApiUtilClient.convert(request, generate_human_anime_style_video_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            generate_human_anime_style_video_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        generate_human_anime_style_video_resp = self.generate_human_anime_style_video_with_options(generate_human_anime_style_video_req, runtime)
        return generate_human_anime_style_video_resp

    async def generate_human_anime_style_video_advance_async(
        self,
        request: videoenhan_20200320_models.GenerateHumanAnimeStyleVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GenerateHumanAnimeStyleVideoResponse:
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
            'Product': 'videoenhan',
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
        generate_human_anime_style_video_req = videoenhan_20200320_models.GenerateHumanAnimeStyleVideoRequest()
        OpenApiUtilClient.convert(request, generate_human_anime_style_video_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            generate_human_anime_style_video_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        generate_human_anime_style_video_resp = await self.generate_human_anime_style_video_with_options_async(generate_human_anime_style_video_req, runtime)
        return generate_human_anime_style_video_resp

    def generate_video_with_options(
        self,
        request: videoenhan_20200320_models.GenerateVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GenerateVideoResponse:
        """
        @param request: GenerateVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateVideoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.duration_adaption):
            body['DurationAdaption'] = request.duration_adaption
        if not UtilClient.is_unset(request.file_list):
            body['FileList'] = request.file_list
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        if not UtilClient.is_unset(request.mute):
            body['Mute'] = request.mute
        if not UtilClient.is_unset(request.puzzle_effect):
            body['PuzzleEffect'] = request.puzzle_effect
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.smart_effect):
            body['SmartEffect'] = request.smart_effect
        if not UtilClient.is_unset(request.style):
            body['Style'] = request.style
        if not UtilClient.is_unset(request.transition_style):
            body['TransitionStyle'] = request.transition_style
        if not UtilClient.is_unset(request.width):
            body['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateVideo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.GenerateVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_video_with_options_async(
        self,
        request: videoenhan_20200320_models.GenerateVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GenerateVideoResponse:
        """
        @param request: GenerateVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateVideoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.duration_adaption):
            body['DurationAdaption'] = request.duration_adaption
        if not UtilClient.is_unset(request.file_list):
            body['FileList'] = request.file_list
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        if not UtilClient.is_unset(request.mute):
            body['Mute'] = request.mute
        if not UtilClient.is_unset(request.puzzle_effect):
            body['PuzzleEffect'] = request.puzzle_effect
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.smart_effect):
            body['SmartEffect'] = request.smart_effect
        if not UtilClient.is_unset(request.style):
            body['Style'] = request.style
        if not UtilClient.is_unset(request.transition_style):
            body['TransitionStyle'] = request.transition_style
        if not UtilClient.is_unset(request.width):
            body['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateVideo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.GenerateVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_video(
        self,
        request: videoenhan_20200320_models.GenerateVideoRequest,
    ) -> videoenhan_20200320_models.GenerateVideoResponse:
        """
        @param request: GenerateVideoRequest
        @return: GenerateVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_video_with_options(request, runtime)

    async def generate_video_async(
        self,
        request: videoenhan_20200320_models.GenerateVideoRequest,
    ) -> videoenhan_20200320_models.GenerateVideoResponse:
        """
        @param request: GenerateVideoRequest
        @return: GenerateVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_video_with_options_async(request, runtime)

    def generate_video_advance(
        self,
        request: videoenhan_20200320_models.GenerateVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GenerateVideoResponse:
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
            'Product': 'videoenhan',
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
        generate_video_req = videoenhan_20200320_models.GenerateVideoRequest()
        OpenApiUtilClient.convert(request, generate_video_req)
        if not UtilClient.is_unset(request.file_list):
            i_0 = 0
            for item_0 in request.file_list:
                if not UtilClient.is_unset(item_0.file_url_object):
                    tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
                    auth_response = UtilClient.assert_as_map(tmp_resp_0)
                    tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
                    use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
                    auth_response_body = UtilClient.stringify_map_value(tmp_body)
                    file_obj = file_form_models.FileField(
                        filename=auth_response_body.get('ObjectKey'),
                        content=item_0.file_url_object,
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
                    tmp = generate_video_req.file_list[i_0]
                    tmp.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        generate_video_resp = self.generate_video_with_options(generate_video_req, runtime)
        return generate_video_resp

    async def generate_video_advance_async(
        self,
        request: videoenhan_20200320_models.GenerateVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GenerateVideoResponse:
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
            'Product': 'videoenhan',
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
        generate_video_req = videoenhan_20200320_models.GenerateVideoRequest()
        OpenApiUtilClient.convert(request, generate_video_req)
        if not UtilClient.is_unset(request.file_list):
            i_0 = 0
            for item_0 in request.file_list:
                if not UtilClient.is_unset(item_0.file_url_object):
                    tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
                    auth_response = UtilClient.assert_as_map(tmp_resp_0)
                    tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
                    use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
                    auth_response_body = UtilClient.stringify_map_value(tmp_body)
                    file_obj = file_form_models.FileField(
                        filename=auth_response_body.get('ObjectKey'),
                        content=item_0.file_url_object,
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
                    tmp = generate_video_req.file_list[i_0]
                    tmp.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        generate_video_resp = await self.generate_video_with_options_async(generate_video_req, runtime)
        return generate_video_resp

    def get_async_job_result_with_options(
        self,
        request: videoenhan_20200320_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GetAsyncJobResultResponse:
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
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.GetAsyncJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_job_result_with_options_async(
        self,
        request: videoenhan_20200320_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GetAsyncJobResultResponse:
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
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.GetAsyncJobResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_job_result(
        self,
        request: videoenhan_20200320_models.GetAsyncJobResultRequest,
    ) -> videoenhan_20200320_models.GetAsyncJobResultResponse:
        """
        @param request: GetAsyncJobResultRequest
        @return: GetAsyncJobResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result_with_options(request, runtime)

    async def get_async_job_result_async(
        self,
        request: videoenhan_20200320_models.GetAsyncJobResultRequest,
    ) -> videoenhan_20200320_models.GetAsyncJobResultResponse:
        """
        @param request: GetAsyncJobResultRequest
        @return: GetAsyncJobResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_async_job_result_with_options_async(request, runtime)

    def interpolate_video_frame_with_options(
        self,
        request: videoenhan_20200320_models.InterpolateVideoFrameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.InterpolateVideoFrameResponse:
        """
        @param request: InterpolateVideoFrameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InterpolateVideoFrameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bitrate):
            body['Bitrate'] = request.bitrate
        if not UtilClient.is_unset(request.frame_rate):
            body['FrameRate'] = request.frame_rate
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InterpolateVideoFrame',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.InterpolateVideoFrameResponse(),
            self.call_api(params, req, runtime)
        )

    async def interpolate_video_frame_with_options_async(
        self,
        request: videoenhan_20200320_models.InterpolateVideoFrameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.InterpolateVideoFrameResponse:
        """
        @param request: InterpolateVideoFrameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InterpolateVideoFrameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bitrate):
            body['Bitrate'] = request.bitrate
        if not UtilClient.is_unset(request.frame_rate):
            body['FrameRate'] = request.frame_rate
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InterpolateVideoFrame',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.InterpolateVideoFrameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def interpolate_video_frame(
        self,
        request: videoenhan_20200320_models.InterpolateVideoFrameRequest,
    ) -> videoenhan_20200320_models.InterpolateVideoFrameResponse:
        """
        @param request: InterpolateVideoFrameRequest
        @return: InterpolateVideoFrameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.interpolate_video_frame_with_options(request, runtime)

    async def interpolate_video_frame_async(
        self,
        request: videoenhan_20200320_models.InterpolateVideoFrameRequest,
    ) -> videoenhan_20200320_models.InterpolateVideoFrameResponse:
        """
        @param request: InterpolateVideoFrameRequest
        @return: InterpolateVideoFrameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.interpolate_video_frame_with_options_async(request, runtime)

    def interpolate_video_frame_advance(
        self,
        request: videoenhan_20200320_models.InterpolateVideoFrameAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.InterpolateVideoFrameResponse:
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
            'Product': 'videoenhan',
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
        interpolate_video_frame_req = videoenhan_20200320_models.InterpolateVideoFrameRequest()
        OpenApiUtilClient.convert(request, interpolate_video_frame_req)
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
            interpolate_video_frame_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        interpolate_video_frame_resp = self.interpolate_video_frame_with_options(interpolate_video_frame_req, runtime)
        return interpolate_video_frame_resp

    async def interpolate_video_frame_advance_async(
        self,
        request: videoenhan_20200320_models.InterpolateVideoFrameAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.InterpolateVideoFrameResponse:
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
            'Product': 'videoenhan',
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
        interpolate_video_frame_req = videoenhan_20200320_models.InterpolateVideoFrameRequest()
        OpenApiUtilClient.convert(request, interpolate_video_frame_req)
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
            interpolate_video_frame_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        interpolate_video_frame_resp = await self.interpolate_video_frame_with_options_async(interpolate_video_frame_req, runtime)
        return interpolate_video_frame_resp

    def merge_video_face_with_options(
        self,
        request: videoenhan_20200320_models.MergeVideoFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoFaceResponse:
        """
        @param request: MergeVideoFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MergeVideoFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.add_watermark):
            body['AddWatermark'] = request.add_watermark
        if not UtilClient.is_unset(request.enhance):
            body['Enhance'] = request.enhance
        if not UtilClient.is_unset(request.reference_url):
            body['ReferenceURL'] = request.reference_url
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        if not UtilClient.is_unset(request.watermark_type):
            body['WatermarkType'] = request.watermark_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MergeVideoFace',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.MergeVideoFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def merge_video_face_with_options_async(
        self,
        request: videoenhan_20200320_models.MergeVideoFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoFaceResponse:
        """
        @param request: MergeVideoFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MergeVideoFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.add_watermark):
            body['AddWatermark'] = request.add_watermark
        if not UtilClient.is_unset(request.enhance):
            body['Enhance'] = request.enhance
        if not UtilClient.is_unset(request.reference_url):
            body['ReferenceURL'] = request.reference_url
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        if not UtilClient.is_unset(request.watermark_type):
            body['WatermarkType'] = request.watermark_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MergeVideoFace',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.MergeVideoFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def merge_video_face(
        self,
        request: videoenhan_20200320_models.MergeVideoFaceRequest,
    ) -> videoenhan_20200320_models.MergeVideoFaceResponse:
        """
        @param request: MergeVideoFaceRequest
        @return: MergeVideoFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.merge_video_face_with_options(request, runtime)

    async def merge_video_face_async(
        self,
        request: videoenhan_20200320_models.MergeVideoFaceRequest,
    ) -> videoenhan_20200320_models.MergeVideoFaceResponse:
        """
        @param request: MergeVideoFaceRequest
        @return: MergeVideoFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.merge_video_face_with_options_async(request, runtime)

    def merge_video_face_advance(
        self,
        request: videoenhan_20200320_models.MergeVideoFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoFaceResponse:
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
            'Product': 'videoenhan',
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
        merge_video_face_req = videoenhan_20200320_models.MergeVideoFaceRequest()
        OpenApiUtilClient.convert(request, merge_video_face_req)
        if not UtilClient.is_unset(request.reference_urlobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.reference_urlobject,
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
            merge_video_face_req.reference_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.video_urlobject):
            tmp_resp_1 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
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
            merge_video_face_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        merge_video_face_resp = self.merge_video_face_with_options(merge_video_face_req, runtime)
        return merge_video_face_resp

    async def merge_video_face_advance_async(
        self,
        request: videoenhan_20200320_models.MergeVideoFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoFaceResponse:
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
            'Product': 'videoenhan',
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
        merge_video_face_req = videoenhan_20200320_models.MergeVideoFaceRequest()
        OpenApiUtilClient.convert(request, merge_video_face_req)
        if not UtilClient.is_unset(request.reference_urlobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.reference_urlobject,
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
            merge_video_face_req.reference_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.video_urlobject):
            tmp_resp_1 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
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
            merge_video_face_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        merge_video_face_resp = await self.merge_video_face_with_options_async(merge_video_face_req, runtime)
        return merge_video_face_resp

    def merge_video_model_face_with_options(
        self,
        request: videoenhan_20200320_models.MergeVideoModelFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoModelFaceResponse:
        """
        @summary 视频模板融合换脸
        
        @param request: MergeVideoModelFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MergeVideoModelFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.add_watermark):
            body['AddWatermark'] = request.add_watermark
        if not UtilClient.is_unset(request.enhance):
            body['Enhance'] = request.enhance
        if not UtilClient.is_unset(request.face_image_url):
            body['FaceImageURL'] = request.face_image_url
        if not UtilClient.is_unset(request.merge_infos):
            body['MergeInfos'] = request.merge_infos
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.watermark_type):
            body['WatermarkType'] = request.watermark_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MergeVideoModelFace',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.MergeVideoModelFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def merge_video_model_face_with_options_async(
        self,
        request: videoenhan_20200320_models.MergeVideoModelFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoModelFaceResponse:
        """
        @summary 视频模板融合换脸
        
        @param request: MergeVideoModelFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MergeVideoModelFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.add_watermark):
            body['AddWatermark'] = request.add_watermark
        if not UtilClient.is_unset(request.enhance):
            body['Enhance'] = request.enhance
        if not UtilClient.is_unset(request.face_image_url):
            body['FaceImageURL'] = request.face_image_url
        if not UtilClient.is_unset(request.merge_infos):
            body['MergeInfos'] = request.merge_infos
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.watermark_type):
            body['WatermarkType'] = request.watermark_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MergeVideoModelFace',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.MergeVideoModelFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def merge_video_model_face(
        self,
        request: videoenhan_20200320_models.MergeVideoModelFaceRequest,
    ) -> videoenhan_20200320_models.MergeVideoModelFaceResponse:
        """
        @summary 视频模板融合换脸
        
        @param request: MergeVideoModelFaceRequest
        @return: MergeVideoModelFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.merge_video_model_face_with_options(request, runtime)

    async def merge_video_model_face_async(
        self,
        request: videoenhan_20200320_models.MergeVideoModelFaceRequest,
    ) -> videoenhan_20200320_models.MergeVideoModelFaceResponse:
        """
        @summary 视频模板融合换脸
        
        @param request: MergeVideoModelFaceRequest
        @return: MergeVideoModelFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.merge_video_model_face_with_options_async(request, runtime)

    def merge_video_model_face_advance(
        self,
        request: videoenhan_20200320_models.MergeVideoModelFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoModelFaceResponse:
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
            'Product': 'videoenhan',
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
        merge_video_model_face_req = videoenhan_20200320_models.MergeVideoModelFaceRequest()
        OpenApiUtilClient.convert(request, merge_video_model_face_req)
        if not UtilClient.is_unset(request.face_image_urlobject):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.face_image_urlobject,
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
            merge_video_model_face_req.face_image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        merge_video_model_face_resp = self.merge_video_model_face_with_options(merge_video_model_face_req, runtime)
        return merge_video_model_face_resp

    async def merge_video_model_face_advance_async(
        self,
        request: videoenhan_20200320_models.MergeVideoModelFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoModelFaceResponse:
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
            'Product': 'videoenhan',
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
        merge_video_model_face_req = videoenhan_20200320_models.MergeVideoModelFaceRequest()
        OpenApiUtilClient.convert(request, merge_video_model_face_req)
        if not UtilClient.is_unset(request.face_image_urlobject):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.face_image_urlobject,
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
            merge_video_model_face_req.face_image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        merge_video_model_face_resp = await self.merge_video_model_face_with_options_async(merge_video_model_face_req, runtime)
        return merge_video_model_face_resp

    def query_face_video_template_with_options(
        self,
        request: videoenhan_20200320_models.QueryFaceVideoTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.QueryFaceVideoTemplateResponse:
        """
        @summary 视频人脸融合模板查询
        
        @param request: QueryFaceVideoTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFaceVideoTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceVideoTemplate',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.QueryFaceVideoTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_video_template_with_options_async(
        self,
        request: videoenhan_20200320_models.QueryFaceVideoTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.QueryFaceVideoTemplateResponse:
        """
        @summary 视频人脸融合模板查询
        
        @param request: QueryFaceVideoTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFaceVideoTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceVideoTemplate',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.QueryFaceVideoTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_video_template(
        self,
        request: videoenhan_20200320_models.QueryFaceVideoTemplateRequest,
    ) -> videoenhan_20200320_models.QueryFaceVideoTemplateResponse:
        """
        @summary 视频人脸融合模板查询
        
        @param request: QueryFaceVideoTemplateRequest
        @return: QueryFaceVideoTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_face_video_template_with_options(request, runtime)

    async def query_face_video_template_async(
        self,
        request: videoenhan_20200320_models.QueryFaceVideoTemplateRequest,
    ) -> videoenhan_20200320_models.QueryFaceVideoTemplateResponse:
        """
        @summary 视频人脸融合模板查询
        
        @param request: QueryFaceVideoTemplateRequest
        @return: QueryFaceVideoTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_face_video_template_with_options_async(request, runtime)

    def reduce_video_noise_with_options(
        self,
        request: videoenhan_20200320_models.ReduceVideoNoiseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ReduceVideoNoiseResponse:
        """
        @summary 视频降噪
        
        @param request: ReduceVideoNoiseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReduceVideoNoiseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReduceVideoNoise',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.ReduceVideoNoiseResponse(),
            self.call_api(params, req, runtime)
        )

    async def reduce_video_noise_with_options_async(
        self,
        request: videoenhan_20200320_models.ReduceVideoNoiseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ReduceVideoNoiseResponse:
        """
        @summary 视频降噪
        
        @param request: ReduceVideoNoiseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReduceVideoNoiseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReduceVideoNoise',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.ReduceVideoNoiseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reduce_video_noise(
        self,
        request: videoenhan_20200320_models.ReduceVideoNoiseRequest,
    ) -> videoenhan_20200320_models.ReduceVideoNoiseResponse:
        """
        @summary 视频降噪
        
        @param request: ReduceVideoNoiseRequest
        @return: ReduceVideoNoiseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reduce_video_noise_with_options(request, runtime)

    async def reduce_video_noise_async(
        self,
        request: videoenhan_20200320_models.ReduceVideoNoiseRequest,
    ) -> videoenhan_20200320_models.ReduceVideoNoiseResponse:
        """
        @summary 视频降噪
        
        @param request: ReduceVideoNoiseRequest
        @return: ReduceVideoNoiseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reduce_video_noise_with_options_async(request, runtime)

    def reduce_video_noise_advance(
        self,
        request: videoenhan_20200320_models.ReduceVideoNoiseAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ReduceVideoNoiseResponse:
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
            'Product': 'videoenhan',
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
        reduce_video_noise_req = videoenhan_20200320_models.ReduceVideoNoiseRequest()
        OpenApiUtilClient.convert(request, reduce_video_noise_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            reduce_video_noise_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        reduce_video_noise_resp = self.reduce_video_noise_with_options(reduce_video_noise_req, runtime)
        return reduce_video_noise_resp

    async def reduce_video_noise_advance_async(
        self,
        request: videoenhan_20200320_models.ReduceVideoNoiseAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ReduceVideoNoiseResponse:
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
            'Product': 'videoenhan',
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
        reduce_video_noise_req = videoenhan_20200320_models.ReduceVideoNoiseRequest()
        OpenApiUtilClient.convert(request, reduce_video_noise_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            reduce_video_noise_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        reduce_video_noise_resp = await self.reduce_video_noise_with_options_async(reduce_video_noise_req, runtime)
        return reduce_video_noise_resp

    def super_resolve_video_with_options(
        self,
        request: videoenhan_20200320_models.SuperResolveVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.SuperResolveVideoResponse:
        """
        @param request: SuperResolveVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuperResolveVideoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bit_rate):
            body['BitRate'] = request.bit_rate
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuperResolveVideo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.SuperResolveVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def super_resolve_video_with_options_async(
        self,
        request: videoenhan_20200320_models.SuperResolveVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.SuperResolveVideoResponse:
        """
        @param request: SuperResolveVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuperResolveVideoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bit_rate):
            body['BitRate'] = request.bit_rate
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuperResolveVideo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.SuperResolveVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def super_resolve_video(
        self,
        request: videoenhan_20200320_models.SuperResolveVideoRequest,
    ) -> videoenhan_20200320_models.SuperResolveVideoResponse:
        """
        @param request: SuperResolveVideoRequest
        @return: SuperResolveVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.super_resolve_video_with_options(request, runtime)

    async def super_resolve_video_async(
        self,
        request: videoenhan_20200320_models.SuperResolveVideoRequest,
    ) -> videoenhan_20200320_models.SuperResolveVideoResponse:
        """
        @param request: SuperResolveVideoRequest
        @return: SuperResolveVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.super_resolve_video_with_options_async(request, runtime)

    def super_resolve_video_advance(
        self,
        request: videoenhan_20200320_models.SuperResolveVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.SuperResolveVideoResponse:
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
            'Product': 'videoenhan',
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
        super_resolve_video_req = videoenhan_20200320_models.SuperResolveVideoRequest()
        OpenApiUtilClient.convert(request, super_resolve_video_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            super_resolve_video_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        super_resolve_video_resp = self.super_resolve_video_with_options(super_resolve_video_req, runtime)
        return super_resolve_video_resp

    async def super_resolve_video_advance_async(
        self,
        request: videoenhan_20200320_models.SuperResolveVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.SuperResolveVideoResponse:
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
            'Product': 'videoenhan',
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
        super_resolve_video_req = videoenhan_20200320_models.SuperResolveVideoRequest()
        OpenApiUtilClient.convert(request, super_resolve_video_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            super_resolve_video_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        super_resolve_video_resp = await self.super_resolve_video_with_options_async(super_resolve_video_req, runtime)
        return super_resolve_video_resp

    def tone_sdr_video_with_options(
        self,
        request: videoenhan_20200320_models.ToneSdrVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ToneSdrVideoResponse:
        """
        @param request: ToneSdrVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ToneSdrVideoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bitrate):
            body['Bitrate'] = request.bitrate
        if not UtilClient.is_unset(request.recolor_model):
            body['RecolorModel'] = request.recolor_model
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ToneSdrVideo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.ToneSdrVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def tone_sdr_video_with_options_async(
        self,
        request: videoenhan_20200320_models.ToneSdrVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ToneSdrVideoResponse:
        """
        @param request: ToneSdrVideoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ToneSdrVideoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bitrate):
            body['Bitrate'] = request.bitrate
        if not UtilClient.is_unset(request.recolor_model):
            body['RecolorModel'] = request.recolor_model
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ToneSdrVideo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videoenhan_20200320_models.ToneSdrVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tone_sdr_video(
        self,
        request: videoenhan_20200320_models.ToneSdrVideoRequest,
    ) -> videoenhan_20200320_models.ToneSdrVideoResponse:
        """
        @param request: ToneSdrVideoRequest
        @return: ToneSdrVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tone_sdr_video_with_options(request, runtime)

    async def tone_sdr_video_async(
        self,
        request: videoenhan_20200320_models.ToneSdrVideoRequest,
    ) -> videoenhan_20200320_models.ToneSdrVideoResponse:
        """
        @param request: ToneSdrVideoRequest
        @return: ToneSdrVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tone_sdr_video_with_options_async(request, runtime)

    def tone_sdr_video_advance(
        self,
        request: videoenhan_20200320_models.ToneSdrVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ToneSdrVideoResponse:
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
            'Product': 'videoenhan',
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
        tone_sdr_video_req = videoenhan_20200320_models.ToneSdrVideoRequest()
        OpenApiUtilClient.convert(request, tone_sdr_video_req)
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
            tone_sdr_video_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        tone_sdr_video_resp = self.tone_sdr_video_with_options(tone_sdr_video_req, runtime)
        return tone_sdr_video_resp

    async def tone_sdr_video_advance_async(
        self,
        request: videoenhan_20200320_models.ToneSdrVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ToneSdrVideoResponse:
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
            'Product': 'videoenhan',
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
        tone_sdr_video_req = videoenhan_20200320_models.ToneSdrVideoRequest()
        OpenApiUtilClient.convert(request, tone_sdr_video_req)
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
            tone_sdr_video_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        tone_sdr_video_resp = await self.tone_sdr_video_with_options_async(tone_sdr_video_req, runtime)
        return tone_sdr_video_resp
