# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aisearch20230101 import models as aisearch_20230101_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_oss_sdk.client import Client as OSSClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('aisearch', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_image_with_options(
        self,
        instance_name: str,
        product_id: str,
        tmp_req: aisearch_20230101_models.AddImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.AddImageResponse:
        UtilClient.validate_model(tmp_req)
        request = aisearch_20230101_models.AddImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.boxes):
            request.boxes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.boxes, 'Boxes', 'json')
        query = {}
        if not UtilClient.is_unset(request.custom_content):
            query['CustomContent'] = request.custom_content
        if not UtilClient.is_unset(request.detect_limit):
            query['DetectLimit'] = request.detect_limit
        if not UtilClient.is_unset(request.int_attr):
            query['IntAttr'] = request.int_attr
        if not UtilClient.is_unset(request.pic_content):
            query['PicContent'] = request.pic_content
        if not UtilClient.is_unset(request.pic_name):
            query['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.pic_url):
            query['PicUrl'] = request.pic_url
        if not UtilClient.is_unset(request.str_attr):
            query['StrAttr'] = request.str_attr
        body = {}
        if not UtilClient.is_unset(request.boxes_shrink):
            body['Boxes'] = request.boxes_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddImage',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/entity/{OpenApiUtilClient.get_encode_param(product_id)}/image',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.AddImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_image_with_options_async(
        self,
        instance_name: str,
        product_id: str,
        tmp_req: aisearch_20230101_models.AddImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.AddImageResponse:
        UtilClient.validate_model(tmp_req)
        request = aisearch_20230101_models.AddImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.boxes):
            request.boxes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.boxes, 'Boxes', 'json')
        query = {}
        if not UtilClient.is_unset(request.custom_content):
            query['CustomContent'] = request.custom_content
        if not UtilClient.is_unset(request.detect_limit):
            query['DetectLimit'] = request.detect_limit
        if not UtilClient.is_unset(request.int_attr):
            query['IntAttr'] = request.int_attr
        if not UtilClient.is_unset(request.pic_content):
            query['PicContent'] = request.pic_content
        if not UtilClient.is_unset(request.pic_name):
            query['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.pic_url):
            query['PicUrl'] = request.pic_url
        if not UtilClient.is_unset(request.str_attr):
            query['StrAttr'] = request.str_attr
        body = {}
        if not UtilClient.is_unset(request.boxes_shrink):
            body['Boxes'] = request.boxes_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddImage',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/entity/{OpenApiUtilClient.get_encode_param(product_id)}/image',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.AddImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_image(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.AddImageRequest,
    ) -> aisearch_20230101_models.AddImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_image_with_options(instance_name, product_id, request, headers, runtime)

    async def add_image_async(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.AddImageRequest,
    ) -> aisearch_20230101_models.AddImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_image_with_options_async(instance_name, product_id, request, headers, runtime)

    def add_image_advance(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.AddImageAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.AddImageResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
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
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='aisearch',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        add_image_req = aisearch_20230101_models.AddImageRequest()
        OpenApiUtilClient.convert(request, add_image_req)
        if not UtilClient.is_unset(request.pic_content_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.pic_content_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            add_image_req.pic_content = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        add_image_resp = self.add_image_with_options(instance_name, product_id, add_image_req, headers, runtime)
        return add_image_resp

    async def add_image_advance_async(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.AddImageAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.AddImageResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
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
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='aisearch',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        add_image_req = aisearch_20230101_models.AddImageRequest()
        OpenApiUtilClient.convert(request, add_image_req)
        if not UtilClient.is_unset(request.pic_content_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.pic_content_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            add_image_req.pic_content = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        add_image_resp = await self.add_image_with_options_async(instance_name, product_id, add_image_req, headers, runtime)
        return add_image_resp

    def get_instance_with_options(
        self,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.GetInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.GetInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        instance_name: str,
    ) -> aisearch_20230101_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_name, headers, runtime)

    async def get_instance_async(
        self,
        instance_name: str,
    ) -> aisearch_20230101_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_name, headers, runtime)

    def update_image_with_options(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.UpdateImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.UpdateImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_content):
            query['CustomContent'] = request.custom_content
        if not UtilClient.is_unset(request.int_attr):
            query['IntAttr'] = request.int_attr
        if not UtilClient.is_unset(request.pic_name):
            query['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.str_attr):
            query['StrAttr'] = request.str_attr
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateImage',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/entity/{OpenApiUtilClient.get_encode_param(product_id)}/image',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.UpdateImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_image_with_options_async(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.UpdateImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.UpdateImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_content):
            query['CustomContent'] = request.custom_content
        if not UtilClient.is_unset(request.int_attr):
            query['IntAttr'] = request.int_attr
        if not UtilClient.is_unset(request.pic_name):
            query['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.str_attr):
            query['StrAttr'] = request.str_attr
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateImage',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/entity/{OpenApiUtilClient.get_encode_param(product_id)}/image',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.UpdateImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_image(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.UpdateImageRequest,
    ) -> aisearch_20230101_models.UpdateImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_image_with_options(instance_name, product_id, request, headers, runtime)

    async def update_image_async(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.UpdateImageRequest,
    ) -> aisearch_20230101_models.UpdateImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_image_with_options_async(instance_name, product_id, request, headers, runtime)
