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
from alibabacloud_imageaudit20191230 import models as imageaudit_20191230_models
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
        self._endpoint = self.get_endpoint('imageaudit', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def scan_image_with_options(
        self,
        request: imageaudit_20191230_models.ScanImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageaudit_20191230_models.ScanImageResponse:
        """
        @summary 图片审核接口
        
        @param request: ScanImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScanImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScanImage',
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
            imageaudit_20191230_models.ScanImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def scan_image_with_options_async(
        self,
        request: imageaudit_20191230_models.ScanImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageaudit_20191230_models.ScanImageResponse:
        """
        @summary 图片审核接口
        
        @param request: ScanImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScanImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScanImage',
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
            imageaudit_20191230_models.ScanImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scan_image(
        self,
        request: imageaudit_20191230_models.ScanImageRequest,
    ) -> imageaudit_20191230_models.ScanImageResponse:
        """
        @summary 图片审核接口
        
        @param request: ScanImageRequest
        @return: ScanImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.scan_image_with_options(request, runtime)

    async def scan_image_async(
        self,
        request: imageaudit_20191230_models.ScanImageRequest,
    ) -> imageaudit_20191230_models.ScanImageResponse:
        """
        @summary 图片审核接口
        
        @param request: ScanImageRequest
        @return: ScanImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.scan_image_with_options_async(request, runtime)

    def scan_image_advance(
        self,
        request: imageaudit_20191230_models.ScanImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageaudit_20191230_models.ScanImageResponse:
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
            'Product': 'imageaudit',
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
        scan_image_req = imageaudit_20191230_models.ScanImageRequest()
        OpenApiUtilClient.convert(request, scan_image_req)
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
                    self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
                    tmp = scan_image_req.task[i_0]
                    tmp.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        scan_image_resp = self.scan_image_with_options(scan_image_req, runtime)
        return scan_image_resp

    async def scan_image_advance_async(
        self,
        request: imageaudit_20191230_models.ScanImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageaudit_20191230_models.ScanImageResponse:
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
            'Product': 'imageaudit',
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
        scan_image_req = imageaudit_20191230_models.ScanImageRequest()
        OpenApiUtilClient.convert(request, scan_image_req)
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
                    await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
                    tmp = scan_image_req.task[i_0]
                    tmp.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        scan_image_resp = await self.scan_image_with_options_async(scan_image_req, runtime)
        return scan_image_resp

    def scan_text_with_options(
        self,
        request: imageaudit_20191230_models.ScanTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageaudit_20191230_models.ScanTextResponse:
        """
        @param request: ScanTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScanTextResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.tasks):
            body['Tasks'] = request.tasks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScanText',
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
            imageaudit_20191230_models.ScanTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def scan_text_with_options_async(
        self,
        request: imageaudit_20191230_models.ScanTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageaudit_20191230_models.ScanTextResponse:
        """
        @param request: ScanTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScanTextResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.tasks):
            body['Tasks'] = request.tasks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScanText',
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
            imageaudit_20191230_models.ScanTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scan_text(
        self,
        request: imageaudit_20191230_models.ScanTextRequest,
    ) -> imageaudit_20191230_models.ScanTextResponse:
        """
        @param request: ScanTextRequest
        @return: ScanTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.scan_text_with_options(request, runtime)

    async def scan_text_async(
        self,
        request: imageaudit_20191230_models.ScanTextRequest,
    ) -> imageaudit_20191230_models.ScanTextResponse:
        """
        @param request: ScanTextRequest
        @return: ScanTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.scan_text_with_options_async(request, runtime)
