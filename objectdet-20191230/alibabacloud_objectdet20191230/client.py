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
from alibabacloud_objectdet20191230 import models as objectdet_20191230_models
from alibabacloud_tea_util import models as util_models
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
        self._endpoint = self.get_endpoint('objectdet', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def detect_ipcobject_with_options(
        self,
        request: objectdet_20191230_models.DetectIPCObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectIPCObjectResponse:
        """
        @summary IPC目标检测
        
        @param request: DetectIPCObjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectIPCObjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectIPCObject',
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
            objectdet_20191230_models.DetectIPCObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_ipcobject_with_options_async(
        self,
        request: objectdet_20191230_models.DetectIPCObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectIPCObjectResponse:
        """
        @summary IPC目标检测
        
        @param request: DetectIPCObjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectIPCObjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectIPCObject',
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
            objectdet_20191230_models.DetectIPCObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_ipcobject(
        self,
        request: objectdet_20191230_models.DetectIPCObjectRequest,
    ) -> objectdet_20191230_models.DetectIPCObjectResponse:
        """
        @summary IPC目标检测
        
        @param request: DetectIPCObjectRequest
        @return: DetectIPCObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_ipcobject_with_options(request, runtime)

    async def detect_ipcobject_async(
        self,
        request: objectdet_20191230_models.DetectIPCObjectRequest,
    ) -> objectdet_20191230_models.DetectIPCObjectResponse:
        """
        @summary IPC目标检测
        
        @param request: DetectIPCObjectRequest
        @return: DetectIPCObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_ipcobject_with_options_async(request, runtime)

    def detect_ipcobject_advance(
        self,
        request: objectdet_20191230_models.DetectIPCObjectAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectIPCObjectResponse:
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
            'Product': 'objectdet',
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
        detect_ipcobject_req = objectdet_20191230_models.DetectIPCObjectRequest()
        OpenApiUtilClient.convert(request, detect_ipcobject_req)
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
            detect_ipcobject_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_ipcobject_resp = self.detect_ipcobject_with_options(detect_ipcobject_req, runtime)
        return detect_ipcobject_resp

    async def detect_ipcobject_advance_async(
        self,
        request: objectdet_20191230_models.DetectIPCObjectAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectIPCObjectResponse:
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
            'Product': 'objectdet',
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
        detect_ipcobject_req = objectdet_20191230_models.DetectIPCObjectRequest()
        OpenApiUtilClient.convert(request, detect_ipcobject_req)
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
            detect_ipcobject_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_ipcobject_resp = await self.detect_ipcobject_with_options_async(detect_ipcobject_req, runtime)
        return detect_ipcobject_resp

    def detect_kitchen_animals_with_options(
        self,
        request: objectdet_20191230_models.DetectKitchenAnimalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectKitchenAnimalsResponse:
        """
        @summary 猫鼠识别
        
        @param request: DetectKitchenAnimalsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectKitchenAnimalsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_urla):
            body['ImageURLA'] = request.image_urla
        if not UtilClient.is_unset(request.image_urlb):
            body['ImageURLB'] = request.image_urlb
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectKitchenAnimals',
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
            objectdet_20191230_models.DetectKitchenAnimalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_kitchen_animals_with_options_async(
        self,
        request: objectdet_20191230_models.DetectKitchenAnimalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectKitchenAnimalsResponse:
        """
        @summary 猫鼠识别
        
        @param request: DetectKitchenAnimalsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectKitchenAnimalsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_urla):
            body['ImageURLA'] = request.image_urla
        if not UtilClient.is_unset(request.image_urlb):
            body['ImageURLB'] = request.image_urlb
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectKitchenAnimals',
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
            objectdet_20191230_models.DetectKitchenAnimalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_kitchen_animals(
        self,
        request: objectdet_20191230_models.DetectKitchenAnimalsRequest,
    ) -> objectdet_20191230_models.DetectKitchenAnimalsResponse:
        """
        @summary 猫鼠识别
        
        @param request: DetectKitchenAnimalsRequest
        @return: DetectKitchenAnimalsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_kitchen_animals_with_options(request, runtime)

    async def detect_kitchen_animals_async(
        self,
        request: objectdet_20191230_models.DetectKitchenAnimalsRequest,
    ) -> objectdet_20191230_models.DetectKitchenAnimalsResponse:
        """
        @summary 猫鼠识别
        
        @param request: DetectKitchenAnimalsRequest
        @return: DetectKitchenAnimalsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_kitchen_animals_with_options_async(request, runtime)

    def detect_kitchen_animals_advance(
        self,
        request: objectdet_20191230_models.DetectKitchenAnimalsAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectKitchenAnimalsResponse:
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
            'Product': 'objectdet',
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
        detect_kitchen_animals_req = objectdet_20191230_models.DetectKitchenAnimalsRequest()
        OpenApiUtilClient.convert(request, detect_kitchen_animals_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            detect_kitchen_animals_req.image_urla = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            detect_kitchen_animals_req.image_urlb = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_kitchen_animals_resp = self.detect_kitchen_animals_with_options(detect_kitchen_animals_req, runtime)
        return detect_kitchen_animals_resp

    async def detect_kitchen_animals_advance_async(
        self,
        request: objectdet_20191230_models.DetectKitchenAnimalsAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectKitchenAnimalsResponse:
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
            'Product': 'objectdet',
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
        detect_kitchen_animals_req = objectdet_20191230_models.DetectKitchenAnimalsRequest()
        OpenApiUtilClient.convert(request, detect_kitchen_animals_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            detect_kitchen_animals_req.image_urla = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            detect_kitchen_animals_req.image_urlb = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_kitchen_animals_resp = await self.detect_kitchen_animals_with_options_async(detect_kitchen_animals_req, runtime)
        return detect_kitchen_animals_resp

    def detect_main_body_with_options(
        self,
        request: objectdet_20191230_models.DetectMainBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectMainBodyResponse:
        """
        @param request: DetectMainBodyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectMainBodyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_url):
            query['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectMainBody',
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
            objectdet_20191230_models.DetectMainBodyResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_main_body_with_options_async(
        self,
        request: objectdet_20191230_models.DetectMainBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectMainBodyResponse:
        """
        @param request: DetectMainBodyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectMainBodyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_url):
            query['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectMainBody',
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
            objectdet_20191230_models.DetectMainBodyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_main_body(
        self,
        request: objectdet_20191230_models.DetectMainBodyRequest,
    ) -> objectdet_20191230_models.DetectMainBodyResponse:
        """
        @param request: DetectMainBodyRequest
        @return: DetectMainBodyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_main_body_with_options(request, runtime)

    async def detect_main_body_async(
        self,
        request: objectdet_20191230_models.DetectMainBodyRequest,
    ) -> objectdet_20191230_models.DetectMainBodyResponse:
        """
        @param request: DetectMainBodyRequest
        @return: DetectMainBodyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_main_body_with_options_async(request, runtime)

    def detect_main_body_advance(
        self,
        request: objectdet_20191230_models.DetectMainBodyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectMainBodyResponse:
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
            'Product': 'objectdet',
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
        detect_main_body_req = objectdet_20191230_models.DetectMainBodyRequest()
        OpenApiUtilClient.convert(request, detect_main_body_req)
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
            detect_main_body_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_main_body_resp = self.detect_main_body_with_options(detect_main_body_req, runtime)
        return detect_main_body_resp

    async def detect_main_body_advance_async(
        self,
        request: objectdet_20191230_models.DetectMainBodyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectMainBodyResponse:
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
            'Product': 'objectdet',
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
        detect_main_body_req = objectdet_20191230_models.DetectMainBodyRequest()
        OpenApiUtilClient.convert(request, detect_main_body_req)
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
            detect_main_body_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_main_body_resp = await self.detect_main_body_with_options_async(detect_main_body_req, runtime)
        return detect_main_body_resp

    def detect_object_with_options(
        self,
        request: objectdet_20191230_models.DetectObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectObjectResponse:
        """
        @param request: DetectObjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectObjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectObject',
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
            objectdet_20191230_models.DetectObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_object_with_options_async(
        self,
        request: objectdet_20191230_models.DetectObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectObjectResponse:
        """
        @param request: DetectObjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectObjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectObject',
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
            objectdet_20191230_models.DetectObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_object(
        self,
        request: objectdet_20191230_models.DetectObjectRequest,
    ) -> objectdet_20191230_models.DetectObjectResponse:
        """
        @param request: DetectObjectRequest
        @return: DetectObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_object_with_options(request, runtime)

    async def detect_object_async(
        self,
        request: objectdet_20191230_models.DetectObjectRequest,
    ) -> objectdet_20191230_models.DetectObjectResponse:
        """
        @param request: DetectObjectRequest
        @return: DetectObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_object_with_options_async(request, runtime)

    def detect_object_advance(
        self,
        request: objectdet_20191230_models.DetectObjectAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectObjectResponse:
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
            'Product': 'objectdet',
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
        detect_object_req = objectdet_20191230_models.DetectObjectRequest()
        OpenApiUtilClient.convert(request, detect_object_req)
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
            detect_object_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_object_resp = self.detect_object_with_options(detect_object_req, runtime)
        return detect_object_resp

    async def detect_object_advance_async(
        self,
        request: objectdet_20191230_models.DetectObjectAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectObjectResponse:
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
            'Product': 'objectdet',
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
        detect_object_req = objectdet_20191230_models.DetectObjectRequest()
        OpenApiUtilClient.convert(request, detect_object_req)
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
            detect_object_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_object_resp = await self.detect_object_with_options_async(detect_object_req, runtime)
        return detect_object_resp

    def detect_vehicle_icongestion_with_options(
        self,
        tmp_req: objectdet_20191230_models.DetectVehicleICongestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVehicleICongestionResponse:
        """
        @summary 车辆拥堵检测
        
        @param tmp_req: DetectVehicleICongestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectVehicleICongestionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = objectdet_20191230_models.DetectVehicleICongestionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.pre_region_intersect_features):
            request.pre_region_intersect_features_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.pre_region_intersect_features, 'PreRegionIntersectFeatures', 'json')
        if not UtilClient.is_unset(tmp_req.road_regions):
            request.road_regions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.road_regions, 'RoadRegions', 'json')
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.pre_region_intersect_features_shrink):
            body['PreRegionIntersectFeatures'] = request.pre_region_intersect_features_shrink
        if not UtilClient.is_unset(request.road_regions_shrink):
            body['RoadRegions'] = request.road_regions_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectVehicleICongestion',
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
            objectdet_20191230_models.DetectVehicleICongestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_vehicle_icongestion_with_options_async(
        self,
        tmp_req: objectdet_20191230_models.DetectVehicleICongestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVehicleICongestionResponse:
        """
        @summary 车辆拥堵检测
        
        @param tmp_req: DetectVehicleICongestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectVehicleICongestionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = objectdet_20191230_models.DetectVehicleICongestionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.pre_region_intersect_features):
            request.pre_region_intersect_features_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.pre_region_intersect_features, 'PreRegionIntersectFeatures', 'json')
        if not UtilClient.is_unset(tmp_req.road_regions):
            request.road_regions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.road_regions, 'RoadRegions', 'json')
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.pre_region_intersect_features_shrink):
            body['PreRegionIntersectFeatures'] = request.pre_region_intersect_features_shrink
        if not UtilClient.is_unset(request.road_regions_shrink):
            body['RoadRegions'] = request.road_regions_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectVehicleICongestion',
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
            objectdet_20191230_models.DetectVehicleICongestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_vehicle_icongestion(
        self,
        request: objectdet_20191230_models.DetectVehicleICongestionRequest,
    ) -> objectdet_20191230_models.DetectVehicleICongestionResponse:
        """
        @summary 车辆拥堵检测
        
        @param request: DetectVehicleICongestionRequest
        @return: DetectVehicleICongestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_vehicle_icongestion_with_options(request, runtime)

    async def detect_vehicle_icongestion_async(
        self,
        request: objectdet_20191230_models.DetectVehicleICongestionRequest,
    ) -> objectdet_20191230_models.DetectVehicleICongestionResponse:
        """
        @summary 车辆拥堵检测
        
        @param request: DetectVehicleICongestionRequest
        @return: DetectVehicleICongestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_vehicle_icongestion_with_options_async(request, runtime)

    def detect_vehicle_icongestion_advance(
        self,
        request: objectdet_20191230_models.DetectVehicleICongestionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVehicleICongestionResponse:
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
            'Product': 'objectdet',
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
        detect_vehicle_icongestion_req = objectdet_20191230_models.DetectVehicleICongestionRequest()
        OpenApiUtilClient.convert(request, detect_vehicle_icongestion_req)
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
            detect_vehicle_icongestion_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_vehicle_icongestion_resp = self.detect_vehicle_icongestion_with_options(detect_vehicle_icongestion_req, runtime)
        return detect_vehicle_icongestion_resp

    async def detect_vehicle_icongestion_advance_async(
        self,
        request: objectdet_20191230_models.DetectVehicleICongestionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVehicleICongestionResponse:
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
            'Product': 'objectdet',
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
        detect_vehicle_icongestion_req = objectdet_20191230_models.DetectVehicleICongestionRequest()
        OpenApiUtilClient.convert(request, detect_vehicle_icongestion_req)
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
            detect_vehicle_icongestion_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_vehicle_icongestion_resp = await self.detect_vehicle_icongestion_with_options_async(detect_vehicle_icongestion_req, runtime)
        return detect_vehicle_icongestion_resp

    def detect_vehicle_illegal_parking_with_options(
        self,
        tmp_req: objectdet_20191230_models.DetectVehicleIllegalParkingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVehicleIllegalParkingResponse:
        """
        @summary 车辆违停检测
        
        @param tmp_req: DetectVehicleIllegalParkingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectVehicleIllegalParkingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = objectdet_20191230_models.DetectVehicleIllegalParkingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.road_regions):
            request.road_regions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.road_regions, 'RoadRegions', 'json')
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.road_regions_shrink):
            body['RoadRegions'] = request.road_regions_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectVehicleIllegalParking',
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
            objectdet_20191230_models.DetectVehicleIllegalParkingResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_vehicle_illegal_parking_with_options_async(
        self,
        tmp_req: objectdet_20191230_models.DetectVehicleIllegalParkingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVehicleIllegalParkingResponse:
        """
        @summary 车辆违停检测
        
        @param tmp_req: DetectVehicleIllegalParkingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectVehicleIllegalParkingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = objectdet_20191230_models.DetectVehicleIllegalParkingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.road_regions):
            request.road_regions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.road_regions, 'RoadRegions', 'json')
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.road_regions_shrink):
            body['RoadRegions'] = request.road_regions_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectVehicleIllegalParking',
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
            objectdet_20191230_models.DetectVehicleIllegalParkingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_vehicle_illegal_parking(
        self,
        request: objectdet_20191230_models.DetectVehicleIllegalParkingRequest,
    ) -> objectdet_20191230_models.DetectVehicleIllegalParkingResponse:
        """
        @summary 车辆违停检测
        
        @param request: DetectVehicleIllegalParkingRequest
        @return: DetectVehicleIllegalParkingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_vehicle_illegal_parking_with_options(request, runtime)

    async def detect_vehicle_illegal_parking_async(
        self,
        request: objectdet_20191230_models.DetectVehicleIllegalParkingRequest,
    ) -> objectdet_20191230_models.DetectVehicleIllegalParkingResponse:
        """
        @summary 车辆违停检测
        
        @param request: DetectVehicleIllegalParkingRequest
        @return: DetectVehicleIllegalParkingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_vehicle_illegal_parking_with_options_async(request, runtime)

    def detect_vehicle_illegal_parking_advance(
        self,
        request: objectdet_20191230_models.DetectVehicleIllegalParkingAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVehicleIllegalParkingResponse:
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
            'Product': 'objectdet',
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
        detect_vehicle_illegal_parking_req = objectdet_20191230_models.DetectVehicleIllegalParkingRequest()
        OpenApiUtilClient.convert(request, detect_vehicle_illegal_parking_req)
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
            detect_vehicle_illegal_parking_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_vehicle_illegal_parking_resp = self.detect_vehicle_illegal_parking_with_options(detect_vehicle_illegal_parking_req, runtime)
        return detect_vehicle_illegal_parking_resp

    async def detect_vehicle_illegal_parking_advance_async(
        self,
        request: objectdet_20191230_models.DetectVehicleIllegalParkingAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVehicleIllegalParkingResponse:
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
            'Product': 'objectdet',
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
        detect_vehicle_illegal_parking_req = objectdet_20191230_models.DetectVehicleIllegalParkingRequest()
        OpenApiUtilClient.convert(request, detect_vehicle_illegal_parking_req)
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
            detect_vehicle_illegal_parking_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_vehicle_illegal_parking_resp = await self.detect_vehicle_illegal_parking_with_options_async(detect_vehicle_illegal_parking_req, runtime)
        return detect_vehicle_illegal_parking_resp

    def detect_video_ipcobject_with_options(
        self,
        request: objectdet_20191230_models.DetectVideoIPCObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVideoIPCObjectResponse:
        """
        @summary IPC视频文件目标检测
        
        @param request: DetectVideoIPCObjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectVideoIPCObjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_only_has_object):
            body['CallbackOnlyHasObject'] = request.callback_only_has_object
        if not UtilClient.is_unset(request.start_timestamp):
            body['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectVideoIPCObject',
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
            objectdet_20191230_models.DetectVideoIPCObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_video_ipcobject_with_options_async(
        self,
        request: objectdet_20191230_models.DetectVideoIPCObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVideoIPCObjectResponse:
        """
        @summary IPC视频文件目标检测
        
        @param request: DetectVideoIPCObjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectVideoIPCObjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_only_has_object):
            body['CallbackOnlyHasObject'] = request.callback_only_has_object
        if not UtilClient.is_unset(request.start_timestamp):
            body['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectVideoIPCObject',
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
            objectdet_20191230_models.DetectVideoIPCObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_video_ipcobject(
        self,
        request: objectdet_20191230_models.DetectVideoIPCObjectRequest,
    ) -> objectdet_20191230_models.DetectVideoIPCObjectResponse:
        """
        @summary IPC视频文件目标检测
        
        @param request: DetectVideoIPCObjectRequest
        @return: DetectVideoIPCObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_video_ipcobject_with_options(request, runtime)

    async def detect_video_ipcobject_async(
        self,
        request: objectdet_20191230_models.DetectVideoIPCObjectRequest,
    ) -> objectdet_20191230_models.DetectVideoIPCObjectResponse:
        """
        @summary IPC视频文件目标检测
        
        @param request: DetectVideoIPCObjectRequest
        @return: DetectVideoIPCObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_video_ipcobject_with_options_async(request, runtime)

    def detect_video_ipcobject_advance(
        self,
        request: objectdet_20191230_models.DetectVideoIPCObjectAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVideoIPCObjectResponse:
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
            'Product': 'objectdet',
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
        detect_video_ipcobject_req = objectdet_20191230_models.DetectVideoIPCObjectRequest()
        OpenApiUtilClient.convert(request, detect_video_ipcobject_req)
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
            detect_video_ipcobject_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_video_ipcobject_resp = self.detect_video_ipcobject_with_options(detect_video_ipcobject_req, runtime)
        return detect_video_ipcobject_resp

    async def detect_video_ipcobject_advance_async(
        self,
        request: objectdet_20191230_models.DetectVideoIPCObjectAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVideoIPCObjectResponse:
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
            'Product': 'objectdet',
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
        detect_video_ipcobject_req = objectdet_20191230_models.DetectVideoIPCObjectRequest()
        OpenApiUtilClient.convert(request, detect_video_ipcobject_req)
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
            detect_video_ipcobject_req.video_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_video_ipcobject_resp = await self.detect_video_ipcobject_with_options_async(detect_video_ipcobject_req, runtime)
        return detect_video_ipcobject_resp

    def detect_white_base_image_with_options(
        self,
        request: objectdet_20191230_models.DetectWhiteBaseImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectWhiteBaseImageResponse:
        """
        @param request: DetectWhiteBaseImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectWhiteBaseImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectWhiteBaseImage',
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
            objectdet_20191230_models.DetectWhiteBaseImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_white_base_image_with_options_async(
        self,
        request: objectdet_20191230_models.DetectWhiteBaseImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectWhiteBaseImageResponse:
        """
        @param request: DetectWhiteBaseImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectWhiteBaseImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectWhiteBaseImage',
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
            objectdet_20191230_models.DetectWhiteBaseImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_white_base_image(
        self,
        request: objectdet_20191230_models.DetectWhiteBaseImageRequest,
    ) -> objectdet_20191230_models.DetectWhiteBaseImageResponse:
        """
        @param request: DetectWhiteBaseImageRequest
        @return: DetectWhiteBaseImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_white_base_image_with_options(request, runtime)

    async def detect_white_base_image_async(
        self,
        request: objectdet_20191230_models.DetectWhiteBaseImageRequest,
    ) -> objectdet_20191230_models.DetectWhiteBaseImageResponse:
        """
        @param request: DetectWhiteBaseImageRequest
        @return: DetectWhiteBaseImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_white_base_image_with_options_async(request, runtime)

    def detect_white_base_image_advance(
        self,
        request: objectdet_20191230_models.DetectWhiteBaseImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectWhiteBaseImageResponse:
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
            'Product': 'objectdet',
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
        detect_white_base_image_req = objectdet_20191230_models.DetectWhiteBaseImageRequest()
        OpenApiUtilClient.convert(request, detect_white_base_image_req)
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
            detect_white_base_image_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_white_base_image_resp = self.detect_white_base_image_with_options(detect_white_base_image_req, runtime)
        return detect_white_base_image_resp

    async def detect_white_base_image_advance_async(
        self,
        request: objectdet_20191230_models.DetectWhiteBaseImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectWhiteBaseImageResponse:
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
            'Product': 'objectdet',
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
        detect_white_base_image_req = objectdet_20191230_models.DetectWhiteBaseImageRequest()
        OpenApiUtilClient.convert(request, detect_white_base_image_req)
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
            detect_white_base_image_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_white_base_image_resp = await self.detect_white_base_image_with_options_async(detect_white_base_image_req, runtime)
        return detect_white_base_image_resp

    def detect_workwear_with_options(
        self,
        tmp_req: objectdet_20191230_models.DetectWorkwearRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectWorkwearResponse:
        """
        @summary 着装检测
        
        @param tmp_req: DetectWorkwearRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectWorkwearResponse
        """
        UtilClient.validate_model(tmp_req)
        request = objectdet_20191230_models.DetectWorkwearShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.clothes):
            request.clothes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.clothes, 'Clothes', 'json')
        body = {}
        if not UtilClient.is_unset(request.clothes_shrink):
            body['Clothes'] = request.clothes_shrink
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectWorkwear',
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
            objectdet_20191230_models.DetectWorkwearResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_workwear_with_options_async(
        self,
        tmp_req: objectdet_20191230_models.DetectWorkwearRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectWorkwearResponse:
        """
        @summary 着装检测
        
        @param tmp_req: DetectWorkwearRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectWorkwearResponse
        """
        UtilClient.validate_model(tmp_req)
        request = objectdet_20191230_models.DetectWorkwearShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.clothes):
            request.clothes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.clothes, 'Clothes', 'json')
        body = {}
        if not UtilClient.is_unset(request.clothes_shrink):
            body['Clothes'] = request.clothes_shrink
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectWorkwear',
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
            objectdet_20191230_models.DetectWorkwearResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_workwear(
        self,
        request: objectdet_20191230_models.DetectWorkwearRequest,
    ) -> objectdet_20191230_models.DetectWorkwearResponse:
        """
        @summary 着装检测
        
        @param request: DetectWorkwearRequest
        @return: DetectWorkwearResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_workwear_with_options(request, runtime)

    async def detect_workwear_async(
        self,
        request: objectdet_20191230_models.DetectWorkwearRequest,
    ) -> objectdet_20191230_models.DetectWorkwearResponse:
        """
        @summary 着装检测
        
        @param request: DetectWorkwearRequest
        @return: DetectWorkwearResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_workwear_with_options_async(request, runtime)

    def detect_workwear_advance(
        self,
        request: objectdet_20191230_models.DetectWorkwearAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectWorkwearResponse:
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
            'Product': 'objectdet',
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
        detect_workwear_req = objectdet_20191230_models.DetectWorkwearRequest()
        OpenApiUtilClient.convert(request, detect_workwear_req)
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
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            detect_workwear_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_workwear_resp = self.detect_workwear_with_options(detect_workwear_req, runtime)
        return detect_workwear_resp

    async def detect_workwear_advance_async(
        self,
        request: objectdet_20191230_models.DetectWorkwearAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectWorkwearResponse:
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
            'Product': 'objectdet',
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
        detect_workwear_req = objectdet_20191230_models.DetectWorkwearRequest()
        OpenApiUtilClient.convert(request, detect_workwear_req)
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
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            detect_workwear_req.image_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        detect_workwear_resp = await self.detect_workwear_with_options_async(detect_workwear_req, runtime)
        return detect_workwear_resp

    def get_async_job_result_with_options(
        self,
        request: objectdet_20191230_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.GetAsyncJobResultResponse:
        """
        @summary 查询异步任务结果
        
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
            objectdet_20191230_models.GetAsyncJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_job_result_with_options_async(
        self,
        request: objectdet_20191230_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.GetAsyncJobResultResponse:
        """
        @summary 查询异步任务结果
        
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
            objectdet_20191230_models.GetAsyncJobResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_job_result(
        self,
        request: objectdet_20191230_models.GetAsyncJobResultRequest,
    ) -> objectdet_20191230_models.GetAsyncJobResultResponse:
        """
        @summary 查询异步任务结果
        
        @param request: GetAsyncJobResultRequest
        @return: GetAsyncJobResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result_with_options(request, runtime)

    async def get_async_job_result_async(
        self,
        request: objectdet_20191230_models.GetAsyncJobResultRequest,
    ) -> objectdet_20191230_models.GetAsyncJobResultResponse:
        """
        @summary 查询异步任务结果
        
        @param request: GetAsyncJobResultRequest
        @return: GetAsyncJobResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_async_job_result_with_options_async(request, runtime)
