# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_videoenhan20200320 import models as videoenhan_20200320_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_oss_sdk.client import Client as OSSClient
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
        runtime = util_models.RuntimeOptions()
        return self.abstract_ecommerce_video_with_options(request, runtime)

    async def abstract_ecommerce_video_async(
        self,
        request: videoenhan_20200320_models.AbstractEcommerceVideoRequest,
    ) -> videoenhan_20200320_models.AbstractEcommerceVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.abstract_ecommerce_video_with_options_async(request, runtime)

    def abstract_ecommerce_video_advance(
        self,
        request: videoenhan_20200320_models.AbstractEcommerceVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractEcommerceVideoResponse:
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
            product='videoenhan',
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
        abstract_ecommerce_video_req = videoenhan_20200320_models.AbstractEcommerceVideoRequest()
        OpenApiUtilClient.convert(request, abstract_ecommerce_video_req)
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            abstract_ecommerce_video_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        abstract_ecommerce_video_resp = self.abstract_ecommerce_video_with_options(abstract_ecommerce_video_req, runtime)
        return abstract_ecommerce_video_resp

    async def abstract_ecommerce_video_advance_async(
        self,
        request: videoenhan_20200320_models.AbstractEcommerceVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractEcommerceVideoResponse:
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
            product='videoenhan',
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
        abstract_ecommerce_video_req = videoenhan_20200320_models.AbstractEcommerceVideoRequest()
        OpenApiUtilClient.convert(request, abstract_ecommerce_video_req)
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            abstract_ecommerce_video_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        abstract_ecommerce_video_resp = await self.abstract_ecommerce_video_with_options_async(abstract_ecommerce_video_req, runtime)
        return abstract_ecommerce_video_resp

    def abstract_film_video_with_options(
        self,
        request: videoenhan_20200320_models.AbstractFilmVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractFilmVideoResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.abstract_film_video_with_options(request, runtime)

    async def abstract_film_video_async(
        self,
        request: videoenhan_20200320_models.AbstractFilmVideoRequest,
    ) -> videoenhan_20200320_models.AbstractFilmVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.abstract_film_video_with_options_async(request, runtime)

    def abstract_film_video_advance(
        self,
        request: videoenhan_20200320_models.AbstractFilmVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractFilmVideoResponse:
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
            product='videoenhan',
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
        abstract_film_video_req = videoenhan_20200320_models.AbstractFilmVideoRequest()
        OpenApiUtilClient.convert(request, abstract_film_video_req)
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            abstract_film_video_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        abstract_film_video_resp = self.abstract_film_video_with_options(abstract_film_video_req, runtime)
        return abstract_film_video_resp

    async def abstract_film_video_advance_async(
        self,
        request: videoenhan_20200320_models.AbstractFilmVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractFilmVideoResponse:
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
            product='videoenhan',
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
        abstract_film_video_req = videoenhan_20200320_models.AbstractFilmVideoRequest()
        OpenApiUtilClient.convert(request, abstract_film_video_req)
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            abstract_film_video_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        abstract_film_video_resp = await self.abstract_film_video_with_options_async(abstract_film_video_req, runtime)
        return abstract_film_video_resp

    def add_face_video_template_with_options(
        self,
        request: videoenhan_20200320_models.AddFaceVideoTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AddFaceVideoTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
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
        runtime = util_models.RuntimeOptions()
        return self.add_face_video_template_with_options(request, runtime)

    async def add_face_video_template_async(
        self,
        request: videoenhan_20200320_models.AddFaceVideoTemplateRequest,
    ) -> videoenhan_20200320_models.AddFaceVideoTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_face_video_template_with_options_async(request, runtime)

    def add_face_video_template_advance(
        self,
        request: videoenhan_20200320_models.AddFaceVideoTemplateAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AddFaceVideoTemplateResponse:
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
            product='videoenhan',
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
        add_face_video_template_req = videoenhan_20200320_models.AddFaceVideoTemplateRequest()
        OpenApiUtilClient.convert(request, add_face_video_template_req)
        if not UtilClient.is_unset(request.video_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_urlobject,
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
            add_face_video_template_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        add_face_video_template_resp = self.add_face_video_template_with_options(add_face_video_template_req, runtime)
        return add_face_video_template_resp

    async def add_face_video_template_advance_async(
        self,
        request: videoenhan_20200320_models.AddFaceVideoTemplateAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AddFaceVideoTemplateResponse:
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
            product='videoenhan',
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
        add_face_video_template_req = videoenhan_20200320_models.AddFaceVideoTemplateRequest()
        OpenApiUtilClient.convert(request, add_face_video_template_req)
        if not UtilClient.is_unset(request.video_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_urlobject,
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
            add_face_video_template_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        add_face_video_template_resp = await self.add_face_video_template_with_options_async(add_face_video_template_req, runtime)
        return add_face_video_template_resp

    def adjust_video_color_with_options(
        self,
        request: videoenhan_20200320_models.AdjustVideoColorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AdjustVideoColorResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.adjust_video_color_with_options(request, runtime)

    async def adjust_video_color_async(
        self,
        request: videoenhan_20200320_models.AdjustVideoColorRequest,
    ) -> videoenhan_20200320_models.AdjustVideoColorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.adjust_video_color_with_options_async(request, runtime)

    def adjust_video_color_advance(
        self,
        request: videoenhan_20200320_models.AdjustVideoColorAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AdjustVideoColorResponse:
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
            product='videoenhan',
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
        adjust_video_color_req = videoenhan_20200320_models.AdjustVideoColorRequest()
        OpenApiUtilClient.convert(request, adjust_video_color_req)
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            adjust_video_color_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        adjust_video_color_resp = self.adjust_video_color_with_options(adjust_video_color_req, runtime)
        return adjust_video_color_resp

    async def adjust_video_color_advance_async(
        self,
        request: videoenhan_20200320_models.AdjustVideoColorAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AdjustVideoColorResponse:
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
            product='videoenhan',
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
        adjust_video_color_req = videoenhan_20200320_models.AdjustVideoColorRequest()
        OpenApiUtilClient.convert(request, adjust_video_color_req)
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            adjust_video_color_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        adjust_video_color_resp = await self.adjust_video_color_with_options_async(adjust_video_color_req, runtime)
        return adjust_video_color_resp

    def change_video_size_with_options(
        self,
        request: videoenhan_20200320_models.ChangeVideoSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ChangeVideoSizeResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.change_video_size_with_options(request, runtime)

    async def change_video_size_async(
        self,
        request: videoenhan_20200320_models.ChangeVideoSizeRequest,
    ) -> videoenhan_20200320_models.ChangeVideoSizeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_video_size_with_options_async(request, runtime)

    def change_video_size_advance(
        self,
        request: videoenhan_20200320_models.ChangeVideoSizeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ChangeVideoSizeResponse:
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
            product='videoenhan',
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
        change_video_size_req = videoenhan_20200320_models.ChangeVideoSizeRequest()
        OpenApiUtilClient.convert(request, change_video_size_req)
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            change_video_size_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        change_video_size_resp = self.change_video_size_with_options(change_video_size_req, runtime)
        return change_video_size_resp

    async def change_video_size_advance_async(
        self,
        request: videoenhan_20200320_models.ChangeVideoSizeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ChangeVideoSizeResponse:
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
            product='videoenhan',
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
        change_video_size_req = videoenhan_20200320_models.ChangeVideoSizeRequest()
        OpenApiUtilClient.convert(request, change_video_size_req)
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            change_video_size_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        change_video_size_resp = await self.change_video_size_with_options_async(change_video_size_req, runtime)
        return change_video_size_resp

    def convert_hdr_video_with_options(
        self,
        request: videoenhan_20200320_models.ConvertHdrVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ConvertHdrVideoResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.convert_hdr_video_with_options(request, runtime)

    async def convert_hdr_video_async(
        self,
        request: videoenhan_20200320_models.ConvertHdrVideoRequest,
    ) -> videoenhan_20200320_models.ConvertHdrVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.convert_hdr_video_with_options_async(request, runtime)

    def convert_hdr_video_advance(
        self,
        request: videoenhan_20200320_models.ConvertHdrVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ConvertHdrVideoResponse:
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
            product='videoenhan',
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
        convert_hdr_video_req = videoenhan_20200320_models.ConvertHdrVideoRequest()
        OpenApiUtilClient.convert(request, convert_hdr_video_req)
        if not UtilClient.is_unset(request.video_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_urlobject,
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
            convert_hdr_video_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        convert_hdr_video_resp = self.convert_hdr_video_with_options(convert_hdr_video_req, runtime)
        return convert_hdr_video_resp

    async def convert_hdr_video_advance_async(
        self,
        request: videoenhan_20200320_models.ConvertHdrVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ConvertHdrVideoResponse:
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
            product='videoenhan',
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
        convert_hdr_video_req = videoenhan_20200320_models.ConvertHdrVideoRequest()
        OpenApiUtilClient.convert(request, convert_hdr_video_req)
        if not UtilClient.is_unset(request.video_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_urlobject,
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
            convert_hdr_video_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        convert_hdr_video_resp = await self.convert_hdr_video_with_options_async(convert_hdr_video_req, runtime)
        return convert_hdr_video_resp

    def delete_face_video_template_with_options(
        self,
        request: videoenhan_20200320_models.DeleteFaceVideoTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.DeleteFaceVideoTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
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
        runtime = util_models.RuntimeOptions()
        return self.delete_face_video_template_with_options(request, runtime)

    async def delete_face_video_template_async(
        self,
        request: videoenhan_20200320_models.DeleteFaceVideoTemplateRequest,
    ) -> videoenhan_20200320_models.DeleteFaceVideoTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_video_template_with_options_async(request, runtime)

    def enhance_video_quality_with_options(
        self,
        request: videoenhan_20200320_models.EnhanceVideoQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EnhanceVideoQualityResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.enhance_video_quality_with_options(request, runtime)

    async def enhance_video_quality_async(
        self,
        request: videoenhan_20200320_models.EnhanceVideoQualityRequest,
    ) -> videoenhan_20200320_models.EnhanceVideoQualityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enhance_video_quality_with_options_async(request, runtime)

    def enhance_video_quality_advance(
        self,
        request: videoenhan_20200320_models.EnhanceVideoQualityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EnhanceVideoQualityResponse:
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
            product='videoenhan',
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
        enhance_video_quality_req = videoenhan_20200320_models.EnhanceVideoQualityRequest()
        OpenApiUtilClient.convert(request, enhance_video_quality_req)
        if not UtilClient.is_unset(request.video_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_urlobject,
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
            enhance_video_quality_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        enhance_video_quality_resp = self.enhance_video_quality_with_options(enhance_video_quality_req, runtime)
        return enhance_video_quality_resp

    async def enhance_video_quality_advance_async(
        self,
        request: videoenhan_20200320_models.EnhanceVideoQualityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EnhanceVideoQualityResponse:
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
            product='videoenhan',
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
        enhance_video_quality_req = videoenhan_20200320_models.EnhanceVideoQualityRequest()
        OpenApiUtilClient.convert(request, enhance_video_quality_req)
        if not UtilClient.is_unset(request.video_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_urlobject,
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
            enhance_video_quality_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        enhance_video_quality_resp = await self.enhance_video_quality_with_options_async(enhance_video_quality_req, runtime)
        return enhance_video_quality_resp

    def erase_video_logo_with_options(
        self,
        request: videoenhan_20200320_models.EraseVideoLogoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoLogoResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.erase_video_logo_with_options(request, runtime)

    async def erase_video_logo_async(
        self,
        request: videoenhan_20200320_models.EraseVideoLogoRequest,
    ) -> videoenhan_20200320_models.EraseVideoLogoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.erase_video_logo_with_options_async(request, runtime)

    def erase_video_logo_advance(
        self,
        request: videoenhan_20200320_models.EraseVideoLogoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoLogoResponse:
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
            product='videoenhan',
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
        erase_video_logo_req = videoenhan_20200320_models.EraseVideoLogoRequest()
        OpenApiUtilClient.convert(request, erase_video_logo_req)
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            erase_video_logo_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        erase_video_logo_resp = self.erase_video_logo_with_options(erase_video_logo_req, runtime)
        return erase_video_logo_resp

    async def erase_video_logo_advance_async(
        self,
        request: videoenhan_20200320_models.EraseVideoLogoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoLogoResponse:
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
            product='videoenhan',
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
        erase_video_logo_req = videoenhan_20200320_models.EraseVideoLogoRequest()
        OpenApiUtilClient.convert(request, erase_video_logo_req)
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            erase_video_logo_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        erase_video_logo_resp = await self.erase_video_logo_with_options_async(erase_video_logo_req, runtime)
        return erase_video_logo_resp

    def erase_video_subtitles_with_options(
        self,
        request: videoenhan_20200320_models.EraseVideoSubtitlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoSubtitlesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.erase_video_subtitles_with_options(request, runtime)

    async def erase_video_subtitles_async(
        self,
        request: videoenhan_20200320_models.EraseVideoSubtitlesRequest,
    ) -> videoenhan_20200320_models.EraseVideoSubtitlesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.erase_video_subtitles_with_options_async(request, runtime)

    def erase_video_subtitles_advance(
        self,
        request: videoenhan_20200320_models.EraseVideoSubtitlesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoSubtitlesResponse:
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
            product='videoenhan',
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
        erase_video_subtitles_req = videoenhan_20200320_models.EraseVideoSubtitlesRequest()
        OpenApiUtilClient.convert(request, erase_video_subtitles_req)
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            erase_video_subtitles_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        erase_video_subtitles_resp = self.erase_video_subtitles_with_options(erase_video_subtitles_req, runtime)
        return erase_video_subtitles_resp

    async def erase_video_subtitles_advance_async(
        self,
        request: videoenhan_20200320_models.EraseVideoSubtitlesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoSubtitlesResponse:
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
            product='videoenhan',
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
        erase_video_subtitles_req = videoenhan_20200320_models.EraseVideoSubtitlesRequest()
        OpenApiUtilClient.convert(request, erase_video_subtitles_req)
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            erase_video_subtitles_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        erase_video_subtitles_resp = await self.erase_video_subtitles_with_options_async(erase_video_subtitles_req, runtime)
        return erase_video_subtitles_resp

    def generate_video_with_options(
        self,
        request: videoenhan_20200320_models.GenerateVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GenerateVideoResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.generate_video_with_options(request, runtime)

    async def generate_video_async(
        self,
        request: videoenhan_20200320_models.GenerateVideoRequest,
    ) -> videoenhan_20200320_models.GenerateVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_video_with_options_async(request, runtime)

    def generate_video_advance(
        self,
        request: videoenhan_20200320_models.GenerateVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GenerateVideoResponse:
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
            product='videoenhan',
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
        generate_video_req = videoenhan_20200320_models.GenerateVideoRequest()
        OpenApiUtilClient.convert(request, generate_video_req)
        if not UtilClient.is_unset(request.file_list):
            i = 0
            for item_0 in request.file_list:
                if not UtilClient.is_unset(item_0.file_url_object):
                    auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.file_url_object,
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
                    tmp = generate_video_req.file_list[i]
                    tmp.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i), NumberClient.itol(1)))
        generate_video_resp = self.generate_video_with_options(generate_video_req, runtime)
        return generate_video_resp

    async def generate_video_advance_async(
        self,
        request: videoenhan_20200320_models.GenerateVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GenerateVideoResponse:
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
            product='videoenhan',
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
        generate_video_req = videoenhan_20200320_models.GenerateVideoRequest()
        OpenApiUtilClient.convert(request, generate_video_req)
        if not UtilClient.is_unset(request.file_list):
            i = 0
            for item_0 in request.file_list:
                if not UtilClient.is_unset(item_0.file_url_object):
                    auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.file_url_object,
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
                    tmp = generate_video_req.file_list[i]
                    tmp.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i), NumberClient.itol(1)))
        generate_video_resp = await self.generate_video_with_options_async(generate_video_req, runtime)
        return generate_video_resp

    def get_async_job_result_with_options(
        self,
        request: videoenhan_20200320_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GetAsyncJobResultResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result_with_options(request, runtime)

    async def get_async_job_result_async(
        self,
        request: videoenhan_20200320_models.GetAsyncJobResultRequest,
    ) -> videoenhan_20200320_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_job_result_with_options_async(request, runtime)

    def interpolate_video_frame_with_options(
        self,
        request: videoenhan_20200320_models.InterpolateVideoFrameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.InterpolateVideoFrameResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.interpolate_video_frame_with_options(request, runtime)

    async def interpolate_video_frame_async(
        self,
        request: videoenhan_20200320_models.InterpolateVideoFrameRequest,
    ) -> videoenhan_20200320_models.InterpolateVideoFrameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.interpolate_video_frame_with_options_async(request, runtime)

    def interpolate_video_frame_advance(
        self,
        request: videoenhan_20200320_models.InterpolateVideoFrameAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.InterpolateVideoFrameResponse:
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
            product='videoenhan',
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
        interpolate_video_frame_req = videoenhan_20200320_models.InterpolateVideoFrameRequest()
        OpenApiUtilClient.convert(request, interpolate_video_frame_req)
        if not UtilClient.is_unset(request.video_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_urlobject,
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
            interpolate_video_frame_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        interpolate_video_frame_resp = self.interpolate_video_frame_with_options(interpolate_video_frame_req, runtime)
        return interpolate_video_frame_resp

    async def interpolate_video_frame_advance_async(
        self,
        request: videoenhan_20200320_models.InterpolateVideoFrameAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.InterpolateVideoFrameResponse:
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
            product='videoenhan',
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
        interpolate_video_frame_req = videoenhan_20200320_models.InterpolateVideoFrameRequest()
        OpenApiUtilClient.convert(request, interpolate_video_frame_req)
        if not UtilClient.is_unset(request.video_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_urlobject,
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
            interpolate_video_frame_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        interpolate_video_frame_resp = await self.interpolate_video_frame_with_options_async(interpolate_video_frame_req, runtime)
        return interpolate_video_frame_resp

    def merge_video_face_with_options(
        self,
        request: videoenhan_20200320_models.MergeVideoFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.post_url):
            body['PostURL'] = request.post_url
        if not UtilClient.is_unset(request.reference_url):
            body['ReferenceURL'] = request.reference_url
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.post_url):
            body['PostURL'] = request.post_url
        if not UtilClient.is_unset(request.reference_url):
            body['ReferenceURL'] = request.reference_url
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
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
        runtime = util_models.RuntimeOptions()
        return self.merge_video_face_with_options(request, runtime)

    async def merge_video_face_async(
        self,
        request: videoenhan_20200320_models.MergeVideoFaceRequest,
    ) -> videoenhan_20200320_models.MergeVideoFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.merge_video_face_with_options_async(request, runtime)

    def merge_video_face_advance(
        self,
        request: videoenhan_20200320_models.MergeVideoFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoFaceResponse:
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
            product='videoenhan',
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
        merge_video_face_req = videoenhan_20200320_models.MergeVideoFaceRequest()
        OpenApiUtilClient.convert(request, merge_video_face_req)
        if not UtilClient.is_unset(request.post_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.post_urlobject,
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
            merge_video_face_req.post_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        if not UtilClient.is_unset(request.reference_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.reference_urlobject,
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
            merge_video_face_req.reference_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        if not UtilClient.is_unset(request.video_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_urlobject,
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
            merge_video_face_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        merge_video_face_resp = self.merge_video_face_with_options(merge_video_face_req, runtime)
        return merge_video_face_resp

    async def merge_video_face_advance_async(
        self,
        request: videoenhan_20200320_models.MergeVideoFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoFaceResponse:
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
            product='videoenhan',
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
        merge_video_face_req = videoenhan_20200320_models.MergeVideoFaceRequest()
        OpenApiUtilClient.convert(request, merge_video_face_req)
        if not UtilClient.is_unset(request.post_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.post_urlobject,
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
            merge_video_face_req.post_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        if not UtilClient.is_unset(request.reference_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.reference_urlobject,
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
            merge_video_face_req.reference_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        if not UtilClient.is_unset(request.video_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_urlobject,
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
            merge_video_face_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        merge_video_face_resp = await self.merge_video_face_with_options_async(merge_video_face_req, runtime)
        return merge_video_face_resp

    def merge_video_model_face_with_options(
        self,
        request: videoenhan_20200320_models.MergeVideoModelFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoModelFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.face_image_url):
            body['FaceImageURL'] = request.face_image_url
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.face_image_url):
            body['FaceImageURL'] = request.face_image_url
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
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
        runtime = util_models.RuntimeOptions()
        return self.merge_video_model_face_with_options(request, runtime)

    async def merge_video_model_face_async(
        self,
        request: videoenhan_20200320_models.MergeVideoModelFaceRequest,
    ) -> videoenhan_20200320_models.MergeVideoModelFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.merge_video_model_face_with_options_async(request, runtime)

    def merge_video_model_face_advance(
        self,
        request: videoenhan_20200320_models.MergeVideoModelFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoModelFaceResponse:
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
            product='videoenhan',
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
        merge_video_model_face_req = videoenhan_20200320_models.MergeVideoModelFaceRequest()
        OpenApiUtilClient.convert(request, merge_video_model_face_req)
        if not UtilClient.is_unset(request.face_image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.face_image_urlobject,
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
            merge_video_model_face_req.face_image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        merge_video_model_face_resp = self.merge_video_model_face_with_options(merge_video_model_face_req, runtime)
        return merge_video_model_face_resp

    async def merge_video_model_face_advance_async(
        self,
        request: videoenhan_20200320_models.MergeVideoModelFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoModelFaceResponse:
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
            product='videoenhan',
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
        merge_video_model_face_req = videoenhan_20200320_models.MergeVideoModelFaceRequest()
        OpenApiUtilClient.convert(request, merge_video_model_face_req)
        if not UtilClient.is_unset(request.face_image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.face_image_urlobject,
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
            merge_video_model_face_req.face_image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        merge_video_model_face_resp = await self.merge_video_model_face_with_options_async(merge_video_model_face_req, runtime)
        return merge_video_model_face_resp

    def query_face_video_template_with_options(
        self,
        request: videoenhan_20200320_models.QueryFaceVideoTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.QueryFaceVideoTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
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
        runtime = util_models.RuntimeOptions()
        return self.query_face_video_template_with_options(request, runtime)

    async def query_face_video_template_async(
        self,
        request: videoenhan_20200320_models.QueryFaceVideoTemplateRequest,
    ) -> videoenhan_20200320_models.QueryFaceVideoTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_face_video_template_with_options_async(request, runtime)

    def super_resolve_video_with_options(
        self,
        request: videoenhan_20200320_models.SuperResolveVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.SuperResolveVideoResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.super_resolve_video_with_options(request, runtime)

    async def super_resolve_video_async(
        self,
        request: videoenhan_20200320_models.SuperResolveVideoRequest,
    ) -> videoenhan_20200320_models.SuperResolveVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.super_resolve_video_with_options_async(request, runtime)

    def super_resolve_video_advance(
        self,
        request: videoenhan_20200320_models.SuperResolveVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.SuperResolveVideoResponse:
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
            product='videoenhan',
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
        super_resolve_video_req = videoenhan_20200320_models.SuperResolveVideoRequest()
        OpenApiUtilClient.convert(request, super_resolve_video_req)
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            super_resolve_video_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        super_resolve_video_resp = self.super_resolve_video_with_options(super_resolve_video_req, runtime)
        return super_resolve_video_resp

    async def super_resolve_video_advance_async(
        self,
        request: videoenhan_20200320_models.SuperResolveVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.SuperResolveVideoResponse:
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
            product='videoenhan',
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
        super_resolve_video_req = videoenhan_20200320_models.SuperResolveVideoRequest()
        OpenApiUtilClient.convert(request, super_resolve_video_req)
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            super_resolve_video_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        super_resolve_video_resp = await self.super_resolve_video_with_options_async(super_resolve_video_req, runtime)
        return super_resolve_video_resp

    def tone_sdr_video_with_options(
        self,
        request: videoenhan_20200320_models.ToneSdrVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ToneSdrVideoResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.tone_sdr_video_with_options(request, runtime)

    async def tone_sdr_video_async(
        self,
        request: videoenhan_20200320_models.ToneSdrVideoRequest,
    ) -> videoenhan_20200320_models.ToneSdrVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tone_sdr_video_with_options_async(request, runtime)

    def tone_sdr_video_advance(
        self,
        request: videoenhan_20200320_models.ToneSdrVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ToneSdrVideoResponse:
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
            product='videoenhan',
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
        tone_sdr_video_req = videoenhan_20200320_models.ToneSdrVideoRequest()
        OpenApiUtilClient.convert(request, tone_sdr_video_req)
        if not UtilClient.is_unset(request.video_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_urlobject,
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
            tone_sdr_video_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        tone_sdr_video_resp = self.tone_sdr_video_with_options(tone_sdr_video_req, runtime)
        return tone_sdr_video_resp

    async def tone_sdr_video_advance_async(
        self,
        request: videoenhan_20200320_models.ToneSdrVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ToneSdrVideoResponse:
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
            product='videoenhan',
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
        tone_sdr_video_req = videoenhan_20200320_models.ToneSdrVideoRequest()
        OpenApiUtilClient.convert(request, tone_sdr_video_req)
        if not UtilClient.is_unset(request.video_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_urlobject,
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
            tone_sdr_video_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        tone_sdr_video_resp = await self.tone_sdr_video_with_options_async(tone_sdr_video_req, runtime)
        return tone_sdr_video_resp
