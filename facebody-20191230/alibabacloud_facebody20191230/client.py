# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_facebody20191230 import models as facebody_20191230_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_tea_rpc import models as rpc_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('facebody', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_body_trace_with_options(
        self,
        tmp_req: facebody_20191230_models.AddBodyTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddBodyTraceResponse:
        UtilClient.validate_model(tmp_req)
        request = facebody_20191230_models.AddBodyTraceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.images):
            request.images_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.images, 'Images', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.AddBodyTraceResponse().from_map(
            self.do_rpcrequest('AddBodyTrace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_body_trace_with_options_async(
        self,
        tmp_req: facebody_20191230_models.AddBodyTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddBodyTraceResponse:
        UtilClient.validate_model(tmp_req)
        request = facebody_20191230_models.AddBodyTraceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.images):
            request.images_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.images, 'Images', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.AddBodyTraceResponse().from_map(
            await self.do_rpcrequest_async('AddBodyTrace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_body_trace(
        self,
        request: facebody_20191230_models.AddBodyTraceRequest,
    ) -> facebody_20191230_models.AddBodyTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_body_trace_with_options(request, runtime)

    async def add_body_trace_async(
        self,
        request: facebody_20191230_models.AddBodyTraceRequest,
    ) -> facebody_20191230_models.AddBodyTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_body_trace_with_options_async(request, runtime)

    def add_face_with_options(
        self,
        request: facebody_20191230_models.AddFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.AddFaceResponse().from_map(
            self.do_rpcrequest('AddFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_face_with_options_async(
        self,
        request: facebody_20191230_models.AddFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.AddFaceResponse().from_map(
            await self.do_rpcrequest_async('AddFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_face(
        self,
        request: facebody_20191230_models.AddFaceRequest,
    ) -> facebody_20191230_models.AddFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_face_with_options(request, runtime)

    async def add_face_async(
        self,
        request: facebody_20191230_models.AddFaceRequest,
    ) -> facebody_20191230_models.AddFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_face_with_options_async(request, runtime)

    def add_face_advance(
        self,
        request: facebody_20191230_models.AddFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        add_face_req = facebody_20191230_models.AddFaceRequest()
        OpenApiUtilClient.convert(request, add_face_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_url_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        add_face_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        add_face_resp = self.add_face_with_options(add_face_req, runtime)
        return add_face_resp

    async def add_face_advance_async(
        self,
        request: facebody_20191230_models.AddFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        add_face_req = facebody_20191230_models.AddFaceRequest()
        OpenApiUtilClient.convert(request, add_face_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_url_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        add_face_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        add_face_resp = await self.add_face_with_options_async(add_face_req, runtime)
        return add_face_resp

    def add_face_entity_with_options(
        self,
        request: facebody_20191230_models.AddFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.AddFaceEntityResponse().from_map(
            self.do_rpcrequest('AddFaceEntity', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_face_entity_with_options_async(
        self,
        request: facebody_20191230_models.AddFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.AddFaceEntityResponse().from_map(
            await self.do_rpcrequest_async('AddFaceEntity', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_face_entity(
        self,
        request: facebody_20191230_models.AddFaceEntityRequest,
    ) -> facebody_20191230_models.AddFaceEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_face_entity_with_options(request, runtime)

    async def add_face_entity_async(
        self,
        request: facebody_20191230_models.AddFaceEntityRequest,
    ) -> facebody_20191230_models.AddFaceEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_face_entity_with_options_async(request, runtime)

    def blur_face_with_options(
        self,
        request: facebody_20191230_models.BlurFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BlurFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.BlurFaceResponse().from_map(
            self.do_rpcrequest('BlurFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def blur_face_with_options_async(
        self,
        request: facebody_20191230_models.BlurFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BlurFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.BlurFaceResponse().from_map(
            await self.do_rpcrequest_async('BlurFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def blur_face(
        self,
        request: facebody_20191230_models.BlurFaceRequest,
    ) -> facebody_20191230_models.BlurFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.blur_face_with_options(request, runtime)

    async def blur_face_async(
        self,
        request: facebody_20191230_models.BlurFaceRequest,
    ) -> facebody_20191230_models.BlurFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.blur_face_with_options_async(request, runtime)

    def blur_face_advance(
        self,
        request: facebody_20191230_models.BlurFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BlurFaceResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        blur_face_req = facebody_20191230_models.BlurFaceRequest()
        OpenApiUtilClient.convert(request, blur_face_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        blur_face_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        blur_face_resp = self.blur_face_with_options(blur_face_req, runtime)
        return blur_face_resp

    async def blur_face_advance_async(
        self,
        request: facebody_20191230_models.BlurFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BlurFaceResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        blur_face_req = facebody_20191230_models.BlurFaceRequest()
        OpenApiUtilClient.convert(request, blur_face_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        blur_face_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        blur_face_resp = await self.blur_face_with_options_async(blur_face_req, runtime)
        return blur_face_resp

    def body_posture_with_options(
        self,
        request: facebody_20191230_models.BodyPostureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BodyPostureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.BodyPostureResponse().from_map(
            self.do_rpcrequest('BodyPosture', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def body_posture_with_options_async(
        self,
        request: facebody_20191230_models.BodyPostureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BodyPostureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.BodyPostureResponse().from_map(
            await self.do_rpcrequest_async('BodyPosture', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def body_posture(
        self,
        request: facebody_20191230_models.BodyPostureRequest,
    ) -> facebody_20191230_models.BodyPostureResponse:
        runtime = util_models.RuntimeOptions()
        return self.body_posture_with_options(request, runtime)

    async def body_posture_async(
        self,
        request: facebody_20191230_models.BodyPostureRequest,
    ) -> facebody_20191230_models.BodyPostureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.body_posture_with_options_async(request, runtime)

    def body_posture_advance(
        self,
        request: facebody_20191230_models.BodyPostureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BodyPostureResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        body_posture_req = facebody_20191230_models.BodyPostureRequest()
        OpenApiUtilClient.convert(request, body_posture_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        body_posture_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        body_posture_resp = self.body_posture_with_options(body_posture_req, runtime)
        return body_posture_resp

    async def body_posture_advance_async(
        self,
        request: facebody_20191230_models.BodyPostureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BodyPostureResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        body_posture_req = facebody_20191230_models.BodyPostureRequest()
        OpenApiUtilClient.convert(request, body_posture_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        body_posture_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        body_posture_resp = await self.body_posture_with_options_async(body_posture_req, runtime)
        return body_posture_resp

    def compare_face_with_options(
        self,
        request: facebody_20191230_models.CompareFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CompareFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.CompareFaceResponse().from_map(
            self.do_rpcrequest('CompareFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def compare_face_with_options_async(
        self,
        request: facebody_20191230_models.CompareFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CompareFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.CompareFaceResponse().from_map(
            await self.do_rpcrequest_async('CompareFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def compare_face(
        self,
        request: facebody_20191230_models.CompareFaceRequest,
    ) -> facebody_20191230_models.CompareFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.compare_face_with_options(request, runtime)

    async def compare_face_async(
        self,
        request: facebody_20191230_models.CompareFaceRequest,
    ) -> facebody_20191230_models.CompareFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.compare_face_with_options_async(request, runtime)

    def count_crowd_with_options(
        self,
        request: facebody_20191230_models.CountCrowdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CountCrowdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.CountCrowdResponse().from_map(
            self.do_rpcrequest('CountCrowd', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def count_crowd_with_options_async(
        self,
        request: facebody_20191230_models.CountCrowdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CountCrowdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.CountCrowdResponse().from_map(
            await self.do_rpcrequest_async('CountCrowd', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def count_crowd(
        self,
        request: facebody_20191230_models.CountCrowdRequest,
    ) -> facebody_20191230_models.CountCrowdResponse:
        runtime = util_models.RuntimeOptions()
        return self.count_crowd_with_options(request, runtime)

    async def count_crowd_async(
        self,
        request: facebody_20191230_models.CountCrowdRequest,
    ) -> facebody_20191230_models.CountCrowdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.count_crowd_with_options_async(request, runtime)

    def count_crowd_advance(
        self,
        request: facebody_20191230_models.CountCrowdAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CountCrowdResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        count_crowd_req = facebody_20191230_models.CountCrowdRequest()
        OpenApiUtilClient.convert(request, count_crowd_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        count_crowd_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        count_crowd_resp = self.count_crowd_with_options(count_crowd_req, runtime)
        return count_crowd_resp

    async def count_crowd_advance_async(
        self,
        request: facebody_20191230_models.CountCrowdAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CountCrowdResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        count_crowd_req = facebody_20191230_models.CountCrowdRequest()
        OpenApiUtilClient.convert(request, count_crowd_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        count_crowd_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        count_crowd_resp = await self.count_crowd_with_options_async(count_crowd_req, runtime)
        return count_crowd_resp

    def create_body_db_with_options(
        self,
        request: facebody_20191230_models.CreateBodyDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CreateBodyDbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.CreateBodyDbResponse().from_map(
            self.do_rpcrequest('CreateBodyDb', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_body_db_with_options_async(
        self,
        request: facebody_20191230_models.CreateBodyDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CreateBodyDbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.CreateBodyDbResponse().from_map(
            await self.do_rpcrequest_async('CreateBodyDb', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_body_db(
        self,
        request: facebody_20191230_models.CreateBodyDbRequest,
    ) -> facebody_20191230_models.CreateBodyDbResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_body_db_with_options(request, runtime)

    async def create_body_db_async(
        self,
        request: facebody_20191230_models.CreateBodyDbRequest,
    ) -> facebody_20191230_models.CreateBodyDbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_body_db_with_options_async(request, runtime)

    def create_body_person_with_options(
        self,
        request: facebody_20191230_models.CreateBodyPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CreateBodyPersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.CreateBodyPersonResponse().from_map(
            self.do_rpcrequest('CreateBodyPerson', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_body_person_with_options_async(
        self,
        request: facebody_20191230_models.CreateBodyPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CreateBodyPersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.CreateBodyPersonResponse().from_map(
            await self.do_rpcrequest_async('CreateBodyPerson', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_body_person(
        self,
        request: facebody_20191230_models.CreateBodyPersonRequest,
    ) -> facebody_20191230_models.CreateBodyPersonResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_body_person_with_options(request, runtime)

    async def create_body_person_async(
        self,
        request: facebody_20191230_models.CreateBodyPersonRequest,
    ) -> facebody_20191230_models.CreateBodyPersonResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_body_person_with_options_async(request, runtime)

    def create_face_db_with_options(
        self,
        request: facebody_20191230_models.CreateFaceDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CreateFaceDbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.CreateFaceDbResponse().from_map(
            self.do_rpcrequest('CreateFaceDb', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_face_db_with_options_async(
        self,
        request: facebody_20191230_models.CreateFaceDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CreateFaceDbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.CreateFaceDbResponse().from_map(
            await self.do_rpcrequest_async('CreateFaceDb', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_face_db(
        self,
        request: facebody_20191230_models.CreateFaceDbRequest,
    ) -> facebody_20191230_models.CreateFaceDbResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_face_db_with_options(request, runtime)

    async def create_face_db_async(
        self,
        request: facebody_20191230_models.CreateFaceDbRequest,
    ) -> facebody_20191230_models.CreateFaceDbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_face_db_with_options_async(request, runtime)

    def delete_body_db_with_options(
        self,
        request: facebody_20191230_models.DeleteBodyDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteBodyDbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DeleteBodyDbResponse().from_map(
            self.do_rpcrequest('DeleteBodyDb', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_body_db_with_options_async(
        self,
        request: facebody_20191230_models.DeleteBodyDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteBodyDbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DeleteBodyDbResponse().from_map(
            await self.do_rpcrequest_async('DeleteBodyDb', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_body_db(
        self,
        request: facebody_20191230_models.DeleteBodyDbRequest,
    ) -> facebody_20191230_models.DeleteBodyDbResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_body_db_with_options(request, runtime)

    async def delete_body_db_async(
        self,
        request: facebody_20191230_models.DeleteBodyDbRequest,
    ) -> facebody_20191230_models.DeleteBodyDbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_body_db_with_options_async(request, runtime)

    def delete_body_person_with_options(
        self,
        request: facebody_20191230_models.DeleteBodyPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteBodyPersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DeleteBodyPersonResponse().from_map(
            self.do_rpcrequest('DeleteBodyPerson', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_body_person_with_options_async(
        self,
        request: facebody_20191230_models.DeleteBodyPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteBodyPersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DeleteBodyPersonResponse().from_map(
            await self.do_rpcrequest_async('DeleteBodyPerson', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_body_person(
        self,
        request: facebody_20191230_models.DeleteBodyPersonRequest,
    ) -> facebody_20191230_models.DeleteBodyPersonResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_body_person_with_options(request, runtime)

    async def delete_body_person_async(
        self,
        request: facebody_20191230_models.DeleteBodyPersonRequest,
    ) -> facebody_20191230_models.DeleteBodyPersonResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_body_person_with_options_async(request, runtime)

    def delete_face_with_options(
        self,
        request: facebody_20191230_models.DeleteFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DeleteFaceResponse().from_map(
            self.do_rpcrequest('DeleteFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_face_with_options_async(
        self,
        request: facebody_20191230_models.DeleteFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DeleteFaceResponse().from_map(
            await self.do_rpcrequest_async('DeleteFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_face(
        self,
        request: facebody_20191230_models.DeleteFaceRequest,
    ) -> facebody_20191230_models.DeleteFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_face_with_options(request, runtime)

    async def delete_face_async(
        self,
        request: facebody_20191230_models.DeleteFaceRequest,
    ) -> facebody_20191230_models.DeleteFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_with_options_async(request, runtime)

    def delete_face_db_with_options(
        self,
        request: facebody_20191230_models.DeleteFaceDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceDbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DeleteFaceDbResponse().from_map(
            self.do_rpcrequest('DeleteFaceDb', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_face_db_with_options_async(
        self,
        request: facebody_20191230_models.DeleteFaceDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceDbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DeleteFaceDbResponse().from_map(
            await self.do_rpcrequest_async('DeleteFaceDb', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_face_db(
        self,
        request: facebody_20191230_models.DeleteFaceDbRequest,
    ) -> facebody_20191230_models.DeleteFaceDbResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_face_db_with_options(request, runtime)

    async def delete_face_db_async(
        self,
        request: facebody_20191230_models.DeleteFaceDbRequest,
    ) -> facebody_20191230_models.DeleteFaceDbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_db_with_options_async(request, runtime)

    def delete_face_entity_with_options(
        self,
        request: facebody_20191230_models.DeleteFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DeleteFaceEntityResponse().from_map(
            self.do_rpcrequest('DeleteFaceEntity', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_face_entity_with_options_async(
        self,
        request: facebody_20191230_models.DeleteFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DeleteFaceEntityResponse().from_map(
            await self.do_rpcrequest_async('DeleteFaceEntity', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_face_entity(
        self,
        request: facebody_20191230_models.DeleteFaceEntityRequest,
    ) -> facebody_20191230_models.DeleteFaceEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_face_entity_with_options(request, runtime)

    async def delete_face_entity_async(
        self,
        request: facebody_20191230_models.DeleteFaceEntityRequest,
    ) -> facebody_20191230_models.DeleteFaceEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_entity_with_options_async(request, runtime)

    def detect_body_count_with_options(
        self,
        request: facebody_20191230_models.DetectBodyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectBodyCountResponse().from_map(
            self.do_rpcrequest('DetectBodyCount', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_body_count_with_options_async(
        self,
        request: facebody_20191230_models.DetectBodyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectBodyCountResponse().from_map(
            await self.do_rpcrequest_async('DetectBodyCount', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_body_count(
        self,
        request: facebody_20191230_models.DetectBodyCountRequest,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_body_count_with_options(request, runtime)

    async def detect_body_count_async(
        self,
        request: facebody_20191230_models.DetectBodyCountRequest,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_body_count_with_options_async(request, runtime)

    def detect_body_count_advance(
        self,
        request: facebody_20191230_models.DetectBodyCountAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        detect_body_count_req = facebody_20191230_models.DetectBodyCountRequest()
        OpenApiUtilClient.convert(request, detect_body_count_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        detect_body_count_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_body_count_resp = self.detect_body_count_with_options(detect_body_count_req, runtime)
        return detect_body_count_resp

    async def detect_body_count_advance_async(
        self,
        request: facebody_20191230_models.DetectBodyCountAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        detect_body_count_req = facebody_20191230_models.DetectBodyCountRequest()
        OpenApiUtilClient.convert(request, detect_body_count_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        detect_body_count_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_body_count_resp = await self.detect_body_count_with_options_async(detect_body_count_req, runtime)
        return detect_body_count_resp

    def detect_celebrity_with_options(
        self,
        request: facebody_20191230_models.DetectCelebrityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectCelebrityResponse().from_map(
            self.do_rpcrequest('DetectCelebrity', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_celebrity_with_options_async(
        self,
        request: facebody_20191230_models.DetectCelebrityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectCelebrityResponse().from_map(
            await self.do_rpcrequest_async('DetectCelebrity', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_celebrity(
        self,
        request: facebody_20191230_models.DetectCelebrityRequest,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_celebrity_with_options(request, runtime)

    async def detect_celebrity_async(
        self,
        request: facebody_20191230_models.DetectCelebrityRequest,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_celebrity_with_options_async(request, runtime)

    def detect_celebrity_advance(
        self,
        request: facebody_20191230_models.DetectCelebrityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        detect_celebrity_req = facebody_20191230_models.DetectCelebrityRequest()
        OpenApiUtilClient.convert(request, detect_celebrity_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        detect_celebrity_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_celebrity_resp = self.detect_celebrity_with_options(detect_celebrity_req, runtime)
        return detect_celebrity_resp

    async def detect_celebrity_advance_async(
        self,
        request: facebody_20191230_models.DetectCelebrityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        detect_celebrity_req = facebody_20191230_models.DetectCelebrityRequest()
        OpenApiUtilClient.convert(request, detect_celebrity_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        detect_celebrity_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_celebrity_resp = await self.detect_celebrity_with_options_async(detect_celebrity_req, runtime)
        return detect_celebrity_resp

    def detect_chef_cap_with_options(
        self,
        request: facebody_20191230_models.DetectChefCapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectChefCapResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectChefCapResponse().from_map(
            self.do_rpcrequest('DetectChefCap', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_chef_cap_with_options_async(
        self,
        request: facebody_20191230_models.DetectChefCapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectChefCapResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectChefCapResponse().from_map(
            await self.do_rpcrequest_async('DetectChefCap', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_chef_cap(
        self,
        request: facebody_20191230_models.DetectChefCapRequest,
    ) -> facebody_20191230_models.DetectChefCapResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_chef_cap_with_options(request, runtime)

    async def detect_chef_cap_async(
        self,
        request: facebody_20191230_models.DetectChefCapRequest,
    ) -> facebody_20191230_models.DetectChefCapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_chef_cap_with_options_async(request, runtime)

    def detect_chef_cap_advance(
        self,
        request: facebody_20191230_models.DetectChefCapAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectChefCapResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        detect_chef_cap_req = facebody_20191230_models.DetectChefCapRequest()
        OpenApiUtilClient.convert(request, detect_chef_cap_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        detect_chef_cap_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_chef_cap_resp = self.detect_chef_cap_with_options(detect_chef_cap_req, runtime)
        return detect_chef_cap_resp

    async def detect_chef_cap_advance_async(
        self,
        request: facebody_20191230_models.DetectChefCapAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectChefCapResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        detect_chef_cap_req = facebody_20191230_models.DetectChefCapRequest()
        OpenApiUtilClient.convert(request, detect_chef_cap_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        detect_chef_cap_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_chef_cap_resp = await self.detect_chef_cap_with_options_async(detect_chef_cap_req, runtime)
        return detect_chef_cap_resp

    def detect_face_with_options(
        self,
        request: facebody_20191230_models.DetectFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectFaceResponse().from_map(
            self.do_rpcrequest('DetectFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_face_with_options_async(
        self,
        request: facebody_20191230_models.DetectFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectFaceResponse().from_map(
            await self.do_rpcrequest_async('DetectFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_face(
        self,
        request: facebody_20191230_models.DetectFaceRequest,
    ) -> facebody_20191230_models.DetectFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_face_with_options(request, runtime)

    async def detect_face_async(
        self,
        request: facebody_20191230_models.DetectFaceRequest,
    ) -> facebody_20191230_models.DetectFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_face_with_options_async(request, runtime)

    def detect_face_advance(
        self,
        request: facebody_20191230_models.DetectFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectFaceResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        detect_face_req = facebody_20191230_models.DetectFaceRequest()
        OpenApiUtilClient.convert(request, detect_face_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        detect_face_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_face_resp = self.detect_face_with_options(detect_face_req, runtime)
        return detect_face_resp

    async def detect_face_advance_async(
        self,
        request: facebody_20191230_models.DetectFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectFaceResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        detect_face_req = facebody_20191230_models.DetectFaceRequest()
        OpenApiUtilClient.convert(request, detect_face_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        detect_face_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_face_resp = await self.detect_face_with_options_async(detect_face_req, runtime)
        return detect_face_resp

    def detect_ipcpedestrian_with_options(
        self,
        request: facebody_20191230_models.DetectIPCPedestrianRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectIPCPedestrianResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectIPCPedestrianResponse().from_map(
            self.do_rpcrequest('DetectIPCPedestrian', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_ipcpedestrian_with_options_async(
        self,
        request: facebody_20191230_models.DetectIPCPedestrianRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectIPCPedestrianResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectIPCPedestrianResponse().from_map(
            await self.do_rpcrequest_async('DetectIPCPedestrian', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_ipcpedestrian(
        self,
        request: facebody_20191230_models.DetectIPCPedestrianRequest,
    ) -> facebody_20191230_models.DetectIPCPedestrianResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_ipcpedestrian_with_options(request, runtime)

    async def detect_ipcpedestrian_async(
        self,
        request: facebody_20191230_models.DetectIPCPedestrianRequest,
    ) -> facebody_20191230_models.DetectIPCPedestrianResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_ipcpedestrian_with_options_async(request, runtime)

    def detect_living_face_with_options(
        self,
        request: facebody_20191230_models.DetectLivingFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectLivingFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectLivingFaceResponse().from_map(
            self.do_rpcrequest('DetectLivingFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_living_face_with_options_async(
        self,
        request: facebody_20191230_models.DetectLivingFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectLivingFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectLivingFaceResponse().from_map(
            await self.do_rpcrequest_async('DetectLivingFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_living_face(
        self,
        request: facebody_20191230_models.DetectLivingFaceRequest,
    ) -> facebody_20191230_models.DetectLivingFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_living_face_with_options(request, runtime)

    async def detect_living_face_async(
        self,
        request: facebody_20191230_models.DetectLivingFaceRequest,
    ) -> facebody_20191230_models.DetectLivingFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_living_face_with_options_async(request, runtime)

    def detect_mask_with_options(
        self,
        request: facebody_20191230_models.DetectMaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectMaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectMaskResponse().from_map(
            self.do_rpcrequest('DetectMask', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_mask_with_options_async(
        self,
        request: facebody_20191230_models.DetectMaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectMaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectMaskResponse().from_map(
            await self.do_rpcrequest_async('DetectMask', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_mask(
        self,
        request: facebody_20191230_models.DetectMaskRequest,
    ) -> facebody_20191230_models.DetectMaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_mask_with_options(request, runtime)

    async def detect_mask_async(
        self,
        request: facebody_20191230_models.DetectMaskRequest,
    ) -> facebody_20191230_models.DetectMaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_mask_with_options_async(request, runtime)

    def detect_mask_advance(
        self,
        request: facebody_20191230_models.DetectMaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectMaskResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        detect_mask_req = facebody_20191230_models.DetectMaskRequest()
        OpenApiUtilClient.convert(request, detect_mask_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        detect_mask_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_mask_resp = self.detect_mask_with_options(detect_mask_req, runtime)
        return detect_mask_resp

    async def detect_mask_advance_async(
        self,
        request: facebody_20191230_models.DetectMaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectMaskResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        detect_mask_req = facebody_20191230_models.DetectMaskRequest()
        OpenApiUtilClient.convert(request, detect_mask_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        detect_mask_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_mask_resp = await self.detect_mask_with_options_async(detect_mask_req, runtime)
        return detect_mask_resp

    def detect_pedestrian_with_options(
        self,
        request: facebody_20191230_models.DetectPedestrianRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectPedestrianResponse().from_map(
            self.do_rpcrequest('DetectPedestrian', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_pedestrian_with_options_async(
        self,
        request: facebody_20191230_models.DetectPedestrianRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectPedestrianResponse().from_map(
            await self.do_rpcrequest_async('DetectPedestrian', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_pedestrian(
        self,
        request: facebody_20191230_models.DetectPedestrianRequest,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_pedestrian_with_options(request, runtime)

    async def detect_pedestrian_async(
        self,
        request: facebody_20191230_models.DetectPedestrianRequest,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_pedestrian_with_options_async(request, runtime)

    def detect_pedestrian_advance(
        self,
        request: facebody_20191230_models.DetectPedestrianAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        detect_pedestrian_req = facebody_20191230_models.DetectPedestrianRequest()
        OpenApiUtilClient.convert(request, detect_pedestrian_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        detect_pedestrian_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_pedestrian_resp = self.detect_pedestrian_with_options(detect_pedestrian_req, runtime)
        return detect_pedestrian_resp

    async def detect_pedestrian_advance_async(
        self,
        request: facebody_20191230_models.DetectPedestrianAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        detect_pedestrian_req = facebody_20191230_models.DetectPedestrianRequest()
        OpenApiUtilClient.convert(request, detect_pedestrian_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        detect_pedestrian_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_pedestrian_resp = await self.detect_pedestrian_with_options_async(detect_pedestrian_req, runtime)
        return detect_pedestrian_resp

    def detect_pedestrian_intrusion_with_options(
        self,
        tmp_req: facebody_20191230_models.DetectPedestrianIntrusionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianIntrusionResponse:
        UtilClient.validate_model(tmp_req)
        request = facebody_20191230_models.DetectPedestrianIntrusionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.detect_region):
            request.detect_region_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detect_region, 'DetectRegion', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectPedestrianIntrusionResponse().from_map(
            self.do_rpcrequest('DetectPedestrianIntrusion', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_pedestrian_intrusion_with_options_async(
        self,
        tmp_req: facebody_20191230_models.DetectPedestrianIntrusionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianIntrusionResponse:
        UtilClient.validate_model(tmp_req)
        request = facebody_20191230_models.DetectPedestrianIntrusionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.detect_region):
            request.detect_region_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detect_region, 'DetectRegion', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectPedestrianIntrusionResponse().from_map(
            await self.do_rpcrequest_async('DetectPedestrianIntrusion', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_pedestrian_intrusion(
        self,
        request: facebody_20191230_models.DetectPedestrianIntrusionRequest,
    ) -> facebody_20191230_models.DetectPedestrianIntrusionResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_pedestrian_intrusion_with_options(request, runtime)

    async def detect_pedestrian_intrusion_async(
        self,
        request: facebody_20191230_models.DetectPedestrianIntrusionRequest,
    ) -> facebody_20191230_models.DetectPedestrianIntrusionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_pedestrian_intrusion_with_options_async(request, runtime)

    def detect_pedestrian_intrusion_advance(
        self,
        request: facebody_20191230_models.DetectPedestrianIntrusionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianIntrusionResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        detect_pedestrian_intrusion_req = facebody_20191230_models.DetectPedestrianIntrusionRequest()
        OpenApiUtilClient.convert(request, detect_pedestrian_intrusion_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        detect_pedestrian_intrusion_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_pedestrian_intrusion_resp = self.detect_pedestrian_intrusion_with_options(detect_pedestrian_intrusion_req, runtime)
        return detect_pedestrian_intrusion_resp

    async def detect_pedestrian_intrusion_advance_async(
        self,
        request: facebody_20191230_models.DetectPedestrianIntrusionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianIntrusionResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        detect_pedestrian_intrusion_req = facebody_20191230_models.DetectPedestrianIntrusionRequest()
        OpenApiUtilClient.convert(request, detect_pedestrian_intrusion_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        detect_pedestrian_intrusion_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_pedestrian_intrusion_resp = await self.detect_pedestrian_intrusion_with_options_async(detect_pedestrian_intrusion_req, runtime)
        return detect_pedestrian_intrusion_resp

    def detect_video_living_face_with_options(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectVideoLivingFaceResponse().from_map(
            self.do_rpcrequest('DetectVideoLivingFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_video_living_face_with_options_async(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.DetectVideoLivingFaceResponse().from_map(
            await self.do_rpcrequest_async('DetectVideoLivingFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_video_living_face(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceRequest,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_video_living_face_with_options(request, runtime)

    async def detect_video_living_face_async(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceRequest,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_video_living_face_with_options_async(request, runtime)

    def detect_video_living_face_advance(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        detect_video_living_face_req = facebody_20191230_models.DetectVideoLivingFaceRequest()
        OpenApiUtilClient.convert(request, detect_video_living_face_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_url_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        detect_video_living_face_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_video_living_face_resp = self.detect_video_living_face_with_options(detect_video_living_face_req, runtime)
        return detect_video_living_face_resp

    async def detect_video_living_face_advance_async(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        detect_video_living_face_req = facebody_20191230_models.DetectVideoLivingFaceRequest()
        OpenApiUtilClient.convert(request, detect_video_living_face_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_url_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        detect_video_living_face_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_video_living_face_resp = await self.detect_video_living_face_with_options_async(detect_video_living_face_req, runtime)
        return detect_video_living_face_resp

    def enhance_face_with_options(
        self,
        request: facebody_20191230_models.EnhanceFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.EnhanceFaceResponse().from_map(
            self.do_rpcrequest('EnhanceFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enhance_face_with_options_async(
        self,
        request: facebody_20191230_models.EnhanceFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.EnhanceFaceResponse().from_map(
            await self.do_rpcrequest_async('EnhanceFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enhance_face(
        self,
        request: facebody_20191230_models.EnhanceFaceRequest,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.enhance_face_with_options(request, runtime)

    async def enhance_face_async(
        self,
        request: facebody_20191230_models.EnhanceFaceRequest,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enhance_face_with_options_async(request, runtime)

    def enhance_face_advance(
        self,
        request: facebody_20191230_models.EnhanceFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        enhance_face_req = facebody_20191230_models.EnhanceFaceRequest()
        OpenApiUtilClient.convert(request, enhance_face_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        enhance_face_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        enhance_face_resp = self.enhance_face_with_options(enhance_face_req, runtime)
        return enhance_face_resp

    async def enhance_face_advance_async(
        self,
        request: facebody_20191230_models.EnhanceFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        enhance_face_req = facebody_20191230_models.EnhanceFaceRequest()
        OpenApiUtilClient.convert(request, enhance_face_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        enhance_face_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        enhance_face_resp = await self.enhance_face_with_options_async(enhance_face_req, runtime)
        return enhance_face_resp

    def extract_pedestrian_feature_attr_with_options(
        self,
        request: facebody_20191230_models.ExtractPedestrianFeatureAttrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractPedestrianFeatureAttrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.ExtractPedestrianFeatureAttrResponse().from_map(
            self.do_rpcrequest('ExtractPedestrianFeatureAttr', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def extract_pedestrian_feature_attr_with_options_async(
        self,
        request: facebody_20191230_models.ExtractPedestrianFeatureAttrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractPedestrianFeatureAttrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.ExtractPedestrianFeatureAttrResponse().from_map(
            await self.do_rpcrequest_async('ExtractPedestrianFeatureAttr', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def extract_pedestrian_feature_attr(
        self,
        request: facebody_20191230_models.ExtractPedestrianFeatureAttrRequest,
    ) -> facebody_20191230_models.ExtractPedestrianFeatureAttrResponse:
        runtime = util_models.RuntimeOptions()
        return self.extract_pedestrian_feature_attr_with_options(request, runtime)

    async def extract_pedestrian_feature_attr_async(
        self,
        request: facebody_20191230_models.ExtractPedestrianFeatureAttrRequest,
    ) -> facebody_20191230_models.ExtractPedestrianFeatureAttrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.extract_pedestrian_feature_attr_with_options_async(request, runtime)

    def extract_pedestrian_feature_attr_advance(
        self,
        request: facebody_20191230_models.ExtractPedestrianFeatureAttrAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractPedestrianFeatureAttrResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        extract_pedestrian_feature_attr_req = facebody_20191230_models.ExtractPedestrianFeatureAttrRequest()
        OpenApiUtilClient.convert(request, extract_pedestrian_feature_attr_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        extract_pedestrian_feature_attr_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        extract_pedestrian_feature_attr_resp = self.extract_pedestrian_feature_attr_with_options(extract_pedestrian_feature_attr_req, runtime)
        return extract_pedestrian_feature_attr_resp

    async def extract_pedestrian_feature_attr_advance_async(
        self,
        request: facebody_20191230_models.ExtractPedestrianFeatureAttrAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractPedestrianFeatureAttrResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        extract_pedestrian_feature_attr_req = facebody_20191230_models.ExtractPedestrianFeatureAttrRequest()
        OpenApiUtilClient.convert(request, extract_pedestrian_feature_attr_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        extract_pedestrian_feature_attr_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        extract_pedestrian_feature_attr_resp = await self.extract_pedestrian_feature_attr_with_options_async(extract_pedestrian_feature_attr_req, runtime)
        return extract_pedestrian_feature_attr_resp

    def extract_pedestrian_feature_attribute_with_options(
        self,
        request: facebody_20191230_models.ExtractPedestrianFeatureAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractPedestrianFeatureAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.ExtractPedestrianFeatureAttributeResponse().from_map(
            self.do_rpcrequest('ExtractPedestrianFeatureAttribute', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def extract_pedestrian_feature_attribute_with_options_async(
        self,
        request: facebody_20191230_models.ExtractPedestrianFeatureAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractPedestrianFeatureAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.ExtractPedestrianFeatureAttributeResponse().from_map(
            await self.do_rpcrequest_async('ExtractPedestrianFeatureAttribute', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def extract_pedestrian_feature_attribute(
        self,
        request: facebody_20191230_models.ExtractPedestrianFeatureAttributeRequest,
    ) -> facebody_20191230_models.ExtractPedestrianFeatureAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.extract_pedestrian_feature_attribute_with_options(request, runtime)

    async def extract_pedestrian_feature_attribute_async(
        self,
        request: facebody_20191230_models.ExtractPedestrianFeatureAttributeRequest,
    ) -> facebody_20191230_models.ExtractPedestrianFeatureAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.extract_pedestrian_feature_attribute_with_options_async(request, runtime)

    def face_beauty_with_options(
        self,
        request: facebody_20191230_models.FaceBeautyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceBeautyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.FaceBeautyResponse().from_map(
            self.do_rpcrequest('FaceBeauty', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def face_beauty_with_options_async(
        self,
        request: facebody_20191230_models.FaceBeautyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceBeautyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.FaceBeautyResponse().from_map(
            await self.do_rpcrequest_async('FaceBeauty', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def face_beauty(
        self,
        request: facebody_20191230_models.FaceBeautyRequest,
    ) -> facebody_20191230_models.FaceBeautyResponse:
        runtime = util_models.RuntimeOptions()
        return self.face_beauty_with_options(request, runtime)

    async def face_beauty_async(
        self,
        request: facebody_20191230_models.FaceBeautyRequest,
    ) -> facebody_20191230_models.FaceBeautyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.face_beauty_with_options_async(request, runtime)

    def face_beauty_advance(
        self,
        request: facebody_20191230_models.FaceBeautyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceBeautyResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        face_beauty_req = facebody_20191230_models.FaceBeautyRequest()
        OpenApiUtilClient.convert(request, face_beauty_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        face_beauty_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        face_beauty_resp = self.face_beauty_with_options(face_beauty_req, runtime)
        return face_beauty_resp

    async def face_beauty_advance_async(
        self,
        request: facebody_20191230_models.FaceBeautyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceBeautyResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        face_beauty_req = facebody_20191230_models.FaceBeautyRequest()
        OpenApiUtilClient.convert(request, face_beauty_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        face_beauty_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        face_beauty_resp = await self.face_beauty_with_options_async(face_beauty_req, runtime)
        return face_beauty_resp

    def face_filter_with_options(
        self,
        request: facebody_20191230_models.FaceFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.FaceFilterResponse().from_map(
            self.do_rpcrequest('FaceFilter', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def face_filter_with_options_async(
        self,
        request: facebody_20191230_models.FaceFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.FaceFilterResponse().from_map(
            await self.do_rpcrequest_async('FaceFilter', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def face_filter(
        self,
        request: facebody_20191230_models.FaceFilterRequest,
    ) -> facebody_20191230_models.FaceFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.face_filter_with_options(request, runtime)

    async def face_filter_async(
        self,
        request: facebody_20191230_models.FaceFilterRequest,
    ) -> facebody_20191230_models.FaceFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.face_filter_with_options_async(request, runtime)

    def face_filter_advance(
        self,
        request: facebody_20191230_models.FaceFilterAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceFilterResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        face_filter_req = facebody_20191230_models.FaceFilterRequest()
        OpenApiUtilClient.convert(request, face_filter_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        face_filter_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        face_filter_resp = self.face_filter_with_options(face_filter_req, runtime)
        return face_filter_resp

    async def face_filter_advance_async(
        self,
        request: facebody_20191230_models.FaceFilterAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceFilterResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        face_filter_req = facebody_20191230_models.FaceFilterRequest()
        OpenApiUtilClient.convert(request, face_filter_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        face_filter_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        face_filter_resp = await self.face_filter_with_options_async(face_filter_req, runtime)
        return face_filter_resp

    def face_makeup_with_options(
        self,
        request: facebody_20191230_models.FaceMakeupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceMakeupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.FaceMakeupResponse().from_map(
            self.do_rpcrequest('FaceMakeup', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def face_makeup_with_options_async(
        self,
        request: facebody_20191230_models.FaceMakeupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceMakeupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.FaceMakeupResponse().from_map(
            await self.do_rpcrequest_async('FaceMakeup', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def face_makeup(
        self,
        request: facebody_20191230_models.FaceMakeupRequest,
    ) -> facebody_20191230_models.FaceMakeupResponse:
        runtime = util_models.RuntimeOptions()
        return self.face_makeup_with_options(request, runtime)

    async def face_makeup_async(
        self,
        request: facebody_20191230_models.FaceMakeupRequest,
    ) -> facebody_20191230_models.FaceMakeupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.face_makeup_with_options_async(request, runtime)

    def face_makeup_advance(
        self,
        request: facebody_20191230_models.FaceMakeupAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceMakeupResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        face_makeup_req = facebody_20191230_models.FaceMakeupRequest()
        OpenApiUtilClient.convert(request, face_makeup_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        face_makeup_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        face_makeup_resp = self.face_makeup_with_options(face_makeup_req, runtime)
        return face_makeup_resp

    async def face_makeup_advance_async(
        self,
        request: facebody_20191230_models.FaceMakeupAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceMakeupResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        face_makeup_req = facebody_20191230_models.FaceMakeupRequest()
        OpenApiUtilClient.convert(request, face_makeup_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        face_makeup_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        face_makeup_resp = await self.face_makeup_with_options_async(face_makeup_req, runtime)
        return face_makeup_resp

    def face_tidyup_with_options(
        self,
        request: facebody_20191230_models.FaceTidyupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceTidyupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.FaceTidyupResponse().from_map(
            self.do_rpcrequest('FaceTidyup', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def face_tidyup_with_options_async(
        self,
        request: facebody_20191230_models.FaceTidyupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceTidyupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.FaceTidyupResponse().from_map(
            await self.do_rpcrequest_async('FaceTidyup', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def face_tidyup(
        self,
        request: facebody_20191230_models.FaceTidyupRequest,
    ) -> facebody_20191230_models.FaceTidyupResponse:
        runtime = util_models.RuntimeOptions()
        return self.face_tidyup_with_options(request, runtime)

    async def face_tidyup_async(
        self,
        request: facebody_20191230_models.FaceTidyupRequest,
    ) -> facebody_20191230_models.FaceTidyupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.face_tidyup_with_options_async(request, runtime)

    def face_tidyup_advance(
        self,
        request: facebody_20191230_models.FaceTidyupAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceTidyupResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        face_tidyup_req = facebody_20191230_models.FaceTidyupRequest()
        OpenApiUtilClient.convert(request, face_tidyup_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        face_tidyup_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        face_tidyup_resp = self.face_tidyup_with_options(face_tidyup_req, runtime)
        return face_tidyup_resp

    async def face_tidyup_advance_async(
        self,
        request: facebody_20191230_models.FaceTidyupAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceTidyupResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        face_tidyup_req = facebody_20191230_models.FaceTidyupRequest()
        OpenApiUtilClient.convert(request, face_tidyup_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        face_tidyup_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        face_tidyup_resp = await self.face_tidyup_with_options_async(face_tidyup_req, runtime)
        return face_tidyup_resp

    def generate_human_anime_style_with_options(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.GenerateHumanAnimeStyleResponse().from_map(
            self.do_rpcrequest('GenerateHumanAnimeStyle', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_human_anime_style_with_options_async(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.GenerateHumanAnimeStyleResponse().from_map(
            await self.do_rpcrequest_async('GenerateHumanAnimeStyle', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_human_anime_style(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleRequest,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_human_anime_style_with_options(request, runtime)

    async def generate_human_anime_style_async(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleRequest,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_human_anime_style_with_options_async(request, runtime)

    def generate_human_anime_style_advance(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        generate_human_anime_style_req = facebody_20191230_models.GenerateHumanAnimeStyleRequest()
        OpenApiUtilClient.convert(request, generate_human_anime_style_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        generate_human_anime_style_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        generate_human_anime_style_resp = self.generate_human_anime_style_with_options(generate_human_anime_style_req, runtime)
        return generate_human_anime_style_resp

    async def generate_human_anime_style_advance_async(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        generate_human_anime_style_req = facebody_20191230_models.GenerateHumanAnimeStyleRequest()
        OpenApiUtilClient.convert(request, generate_human_anime_style_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        generate_human_anime_style_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        generate_human_anime_style_resp = await self.generate_human_anime_style_with_options_async(generate_human_anime_style_req, runtime)
        return generate_human_anime_style_resp

    def gen_real_person_verification_token_with_options(
        self,
        request: facebody_20191230_models.GenRealPersonVerificationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenRealPersonVerificationTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.GenRealPersonVerificationTokenResponse().from_map(
            self.do_rpcrequest('GenRealPersonVerificationToken', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def gen_real_person_verification_token_with_options_async(
        self,
        request: facebody_20191230_models.GenRealPersonVerificationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenRealPersonVerificationTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.GenRealPersonVerificationTokenResponse().from_map(
            await self.do_rpcrequest_async('GenRealPersonVerificationToken', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def gen_real_person_verification_token(
        self,
        request: facebody_20191230_models.GenRealPersonVerificationTokenRequest,
    ) -> facebody_20191230_models.GenRealPersonVerificationTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.gen_real_person_verification_token_with_options(request, runtime)

    async def gen_real_person_verification_token_async(
        self,
        request: facebody_20191230_models.GenRealPersonVerificationTokenRequest,
    ) -> facebody_20191230_models.GenRealPersonVerificationTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.gen_real_person_verification_token_with_options_async(request, runtime)

    def get_body_person_with_options(
        self,
        request: facebody_20191230_models.GetBodyPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GetBodyPersonResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return facebody_20191230_models.GetBodyPersonResponse().from_map(
            self.do_rpcrequest('GetBodyPerson', '2019-12-30', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_body_person_with_options_async(
        self,
        request: facebody_20191230_models.GetBodyPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GetBodyPersonResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return facebody_20191230_models.GetBodyPersonResponse().from_map(
            await self.do_rpcrequest_async('GetBodyPerson', '2019-12-30', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_body_person(
        self,
        request: facebody_20191230_models.GetBodyPersonRequest,
    ) -> facebody_20191230_models.GetBodyPersonResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_body_person_with_options(request, runtime)

    async def get_body_person_async(
        self,
        request: facebody_20191230_models.GetBodyPersonRequest,
    ) -> facebody_20191230_models.GetBodyPersonResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_body_person_with_options_async(request, runtime)

    def get_face_entity_with_options(
        self,
        request: facebody_20191230_models.GetFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GetFaceEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.GetFaceEntityResponse().from_map(
            self.do_rpcrequest('GetFaceEntity', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_face_entity_with_options_async(
        self,
        request: facebody_20191230_models.GetFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GetFaceEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.GetFaceEntityResponse().from_map(
            await self.do_rpcrequest_async('GetFaceEntity', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_face_entity(
        self,
        request: facebody_20191230_models.GetFaceEntityRequest,
    ) -> facebody_20191230_models.GetFaceEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_face_entity_with_options(request, runtime)

    async def get_face_entity_async(
        self,
        request: facebody_20191230_models.GetFaceEntityRequest,
    ) -> facebody_20191230_models.GetFaceEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_face_entity_with_options_async(request, runtime)

    def get_real_person_verification_result_with_options(
        self,
        request: facebody_20191230_models.GetRealPersonVerificationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GetRealPersonVerificationResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.GetRealPersonVerificationResultResponse().from_map(
            self.do_rpcrequest('GetRealPersonVerificationResult', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_real_person_verification_result_with_options_async(
        self,
        request: facebody_20191230_models.GetRealPersonVerificationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GetRealPersonVerificationResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.GetRealPersonVerificationResultResponse().from_map(
            await self.do_rpcrequest_async('GetRealPersonVerificationResult', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_real_person_verification_result(
        self,
        request: facebody_20191230_models.GetRealPersonVerificationResultRequest,
    ) -> facebody_20191230_models.GetRealPersonVerificationResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_real_person_verification_result_with_options(request, runtime)

    async def get_real_person_verification_result_async(
        self,
        request: facebody_20191230_models.GetRealPersonVerificationResultRequest,
    ) -> facebody_20191230_models.GetRealPersonVerificationResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_real_person_verification_result_with_options_async(request, runtime)

    def hand_posture_with_options(
        self,
        request: facebody_20191230_models.HandPostureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.HandPostureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.HandPostureResponse().from_map(
            self.do_rpcrequest('HandPosture', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def hand_posture_with_options_async(
        self,
        request: facebody_20191230_models.HandPostureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.HandPostureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.HandPostureResponse().from_map(
            await self.do_rpcrequest_async('HandPosture', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def hand_posture(
        self,
        request: facebody_20191230_models.HandPostureRequest,
    ) -> facebody_20191230_models.HandPostureResponse:
        runtime = util_models.RuntimeOptions()
        return self.hand_posture_with_options(request, runtime)

    async def hand_posture_async(
        self,
        request: facebody_20191230_models.HandPostureRequest,
    ) -> facebody_20191230_models.HandPostureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.hand_posture_with_options_async(request, runtime)

    def hand_posture_advance(
        self,
        request: facebody_20191230_models.HandPostureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.HandPostureResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        hand_posture_req = facebody_20191230_models.HandPostureRequest()
        OpenApiUtilClient.convert(request, hand_posture_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        hand_posture_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        hand_posture_resp = self.hand_posture_with_options(hand_posture_req, runtime)
        return hand_posture_resp

    async def hand_posture_advance_async(
        self,
        request: facebody_20191230_models.HandPostureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.HandPostureResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        hand_posture_req = facebody_20191230_models.HandPostureRequest()
        OpenApiUtilClient.convert(request, hand_posture_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        hand_posture_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        hand_posture_resp = await self.hand_posture_with_options_async(hand_posture_req, runtime)
        return hand_posture_resp

    def list_body_dbs_with_options(
        self,
        request: facebody_20191230_models.ListBodyDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ListBodyDbsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return facebody_20191230_models.ListBodyDbsResponse().from_map(
            self.do_rpcrequest('ListBodyDbs', '2019-12-30', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_body_dbs_with_options_async(
        self,
        request: facebody_20191230_models.ListBodyDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ListBodyDbsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return facebody_20191230_models.ListBodyDbsResponse().from_map(
            await self.do_rpcrequest_async('ListBodyDbs', '2019-12-30', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_body_dbs(
        self,
        request: facebody_20191230_models.ListBodyDbsRequest,
    ) -> facebody_20191230_models.ListBodyDbsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_body_dbs_with_options(request, runtime)

    async def list_body_dbs_async(
        self,
        request: facebody_20191230_models.ListBodyDbsRequest,
    ) -> facebody_20191230_models.ListBodyDbsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_body_dbs_with_options_async(request, runtime)

    def list_body_person_with_options(
        self,
        request: facebody_20191230_models.ListBodyPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ListBodyPersonResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return facebody_20191230_models.ListBodyPersonResponse().from_map(
            self.do_rpcrequest('ListBodyPerson', '2019-12-30', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_body_person_with_options_async(
        self,
        request: facebody_20191230_models.ListBodyPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ListBodyPersonResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return facebody_20191230_models.ListBodyPersonResponse().from_map(
            await self.do_rpcrequest_async('ListBodyPerson', '2019-12-30', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_body_person(
        self,
        request: facebody_20191230_models.ListBodyPersonRequest,
    ) -> facebody_20191230_models.ListBodyPersonResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_body_person_with_options(request, runtime)

    async def list_body_person_async(
        self,
        request: facebody_20191230_models.ListBodyPersonRequest,
    ) -> facebody_20191230_models.ListBodyPersonResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_body_person_with_options_async(request, runtime)

    def list_face_dbs_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ListFaceDbsResponse:
        req = open_api_models.OpenApiRequest()
        return facebody_20191230_models.ListFaceDbsResponse().from_map(
            self.do_rpcrequest('ListFaceDbs', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_face_dbs_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ListFaceDbsResponse:
        req = open_api_models.OpenApiRequest()
        return facebody_20191230_models.ListFaceDbsResponse().from_map(
            await self.do_rpcrequest_async('ListFaceDbs', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_face_dbs(self) -> facebody_20191230_models.ListFaceDbsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_face_dbs_with_options(runtime)

    async def list_face_dbs_async(self) -> facebody_20191230_models.ListFaceDbsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_face_dbs_with_options_async(runtime)

    def list_face_entities_with_options(
        self,
        request: facebody_20191230_models.ListFaceEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ListFaceEntitiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.ListFaceEntitiesResponse().from_map(
            self.do_rpcrequest('ListFaceEntities', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_face_entities_with_options_async(
        self,
        request: facebody_20191230_models.ListFaceEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ListFaceEntitiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.ListFaceEntitiesResponse().from_map(
            await self.do_rpcrequest_async('ListFaceEntities', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_face_entities(
        self,
        request: facebody_20191230_models.ListFaceEntitiesRequest,
    ) -> facebody_20191230_models.ListFaceEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_face_entities_with_options(request, runtime)

    async def list_face_entities_async(
        self,
        request: facebody_20191230_models.ListFaceEntitiesRequest,
    ) -> facebody_20191230_models.ListFaceEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_face_entities_with_options_async(request, runtime)

    def pedestrian_detect_attribute_with_options(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.PedestrianDetectAttributeResponse().from_map(
            self.do_rpcrequest('PedestrianDetectAttribute', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def pedestrian_detect_attribute_with_options_async(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.PedestrianDetectAttributeResponse().from_map(
            await self.do_rpcrequest_async('PedestrianDetectAttribute', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pedestrian_detect_attribute(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeRequest,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.pedestrian_detect_attribute_with_options(request, runtime)

    async def pedestrian_detect_attribute_async(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeRequest,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pedestrian_detect_attribute_with_options_async(request, runtime)

    def pedestrian_detect_attribute_advance(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        pedestrian_detect_attribute_req = facebody_20191230_models.PedestrianDetectAttributeRequest()
        OpenApiUtilClient.convert(request, pedestrian_detect_attribute_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        pedestrian_detect_attribute_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        pedestrian_detect_attribute_resp = self.pedestrian_detect_attribute_with_options(pedestrian_detect_attribute_req, runtime)
        return pedestrian_detect_attribute_resp

    async def pedestrian_detect_attribute_advance_async(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        pedestrian_detect_attribute_req = facebody_20191230_models.PedestrianDetectAttributeRequest()
        OpenApiUtilClient.convert(request, pedestrian_detect_attribute_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        pedestrian_detect_attribute_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        pedestrian_detect_attribute_resp = await self.pedestrian_detect_attribute_with_options_async(pedestrian_detect_attribute_req, runtime)
        return pedestrian_detect_attribute_resp

    def recognize_action_with_options(
        self,
        request: facebody_20191230_models.RecognizeActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.RecognizeActionResponse().from_map(
            self.do_rpcrequest('RecognizeAction', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_action_with_options_async(
        self,
        request: facebody_20191230_models.RecognizeActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.RecognizeActionResponse().from_map(
            await self.do_rpcrequest_async('RecognizeAction', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_action(
        self,
        request: facebody_20191230_models.RecognizeActionRequest,
    ) -> facebody_20191230_models.RecognizeActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_action_with_options(request, runtime)

    async def recognize_action_async(
        self,
        request: facebody_20191230_models.RecognizeActionRequest,
    ) -> facebody_20191230_models.RecognizeActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_action_with_options_async(request, runtime)

    def recognize_expression_with_options(
        self,
        request: facebody_20191230_models.RecognizeExpressionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.RecognizeExpressionResponse().from_map(
            self.do_rpcrequest('RecognizeExpression', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_expression_with_options_async(
        self,
        request: facebody_20191230_models.RecognizeExpressionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.RecognizeExpressionResponse().from_map(
            await self.do_rpcrequest_async('RecognizeExpression', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_expression(
        self,
        request: facebody_20191230_models.RecognizeExpressionRequest,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_expression_with_options(request, runtime)

    async def recognize_expression_async(
        self,
        request: facebody_20191230_models.RecognizeExpressionRequest,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_expression_with_options_async(request, runtime)

    def recognize_expression_advance(
        self,
        request: facebody_20191230_models.RecognizeExpressionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        recognize_expression_req = facebody_20191230_models.RecognizeExpressionRequest()
        OpenApiUtilClient.convert(request, recognize_expression_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        recognize_expression_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_expression_resp = self.recognize_expression_with_options(recognize_expression_req, runtime)
        return recognize_expression_resp

    async def recognize_expression_advance_async(
        self,
        request: facebody_20191230_models.RecognizeExpressionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        recognize_expression_req = facebody_20191230_models.RecognizeExpressionRequest()
        OpenApiUtilClient.convert(request, recognize_expression_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        recognize_expression_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_expression_resp = await self.recognize_expression_with_options_async(recognize_expression_req, runtime)
        return recognize_expression_resp

    def recognize_face_with_options(
        self,
        request: facebody_20191230_models.RecognizeFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.RecognizeFaceResponse().from_map(
            self.do_rpcrequest('RecognizeFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_face_with_options_async(
        self,
        request: facebody_20191230_models.RecognizeFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.RecognizeFaceResponse().from_map(
            await self.do_rpcrequest_async('RecognizeFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_face(
        self,
        request: facebody_20191230_models.RecognizeFaceRequest,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_face_with_options(request, runtime)

    async def recognize_face_async(
        self,
        request: facebody_20191230_models.RecognizeFaceRequest,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_face_with_options_async(request, runtime)

    def recognize_face_advance(
        self,
        request: facebody_20191230_models.RecognizeFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        recognize_face_req = facebody_20191230_models.RecognizeFaceRequest()
        OpenApiUtilClient.convert(request, recognize_face_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        recognize_face_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_face_resp = self.recognize_face_with_options(recognize_face_req, runtime)
        return recognize_face_resp

    async def recognize_face_advance_async(
        self,
        request: facebody_20191230_models.RecognizeFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        recognize_face_req = facebody_20191230_models.RecognizeFaceRequest()
        OpenApiUtilClient.convert(request, recognize_face_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        recognize_face_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_face_resp = await self.recognize_face_with_options_async(recognize_face_req, runtime)
        return recognize_face_resp

    def recognize_public_face_with_options(
        self,
        request: facebody_20191230_models.RecognizePublicFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizePublicFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.RecognizePublicFaceResponse().from_map(
            self.do_rpcrequest('RecognizePublicFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_public_face_with_options_async(
        self,
        request: facebody_20191230_models.RecognizePublicFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizePublicFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.RecognizePublicFaceResponse().from_map(
            await self.do_rpcrequest_async('RecognizePublicFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_public_face(
        self,
        request: facebody_20191230_models.RecognizePublicFaceRequest,
    ) -> facebody_20191230_models.RecognizePublicFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_public_face_with_options(request, runtime)

    async def recognize_public_face_async(
        self,
        request: facebody_20191230_models.RecognizePublicFaceRequest,
    ) -> facebody_20191230_models.RecognizePublicFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_public_face_with_options_async(request, runtime)

    def search_body_trace_with_options(
        self,
        tmp_req: facebody_20191230_models.SearchBodyTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SearchBodyTraceResponse:
        UtilClient.validate_model(tmp_req)
        request = facebody_20191230_models.SearchBodyTraceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.images):
            request.images_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.images, 'Images', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.SearchBodyTraceResponse().from_map(
            self.do_rpcrequest('SearchBodyTrace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_body_trace_with_options_async(
        self,
        tmp_req: facebody_20191230_models.SearchBodyTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SearchBodyTraceResponse:
        UtilClient.validate_model(tmp_req)
        request = facebody_20191230_models.SearchBodyTraceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.images):
            request.images_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.images, 'Images', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.SearchBodyTraceResponse().from_map(
            await self.do_rpcrequest_async('SearchBodyTrace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_body_trace(
        self,
        request: facebody_20191230_models.SearchBodyTraceRequest,
    ) -> facebody_20191230_models.SearchBodyTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_body_trace_with_options(request, runtime)

    async def search_body_trace_async(
        self,
        request: facebody_20191230_models.SearchBodyTraceRequest,
    ) -> facebody_20191230_models.SearchBodyTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_body_trace_with_options_async(request, runtime)

    def search_face_with_options(
        self,
        request: facebody_20191230_models.SearchFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SearchFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.SearchFaceResponse().from_map(
            self.do_rpcrequest('SearchFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_face_with_options_async(
        self,
        request: facebody_20191230_models.SearchFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SearchFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.SearchFaceResponse().from_map(
            await self.do_rpcrequest_async('SearchFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_face(
        self,
        request: facebody_20191230_models.SearchFaceRequest,
    ) -> facebody_20191230_models.SearchFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_face_with_options(request, runtime)

    async def search_face_async(
        self,
        request: facebody_20191230_models.SearchFaceRequest,
    ) -> facebody_20191230_models.SearchFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_face_with_options_async(request, runtime)

    def search_face_advance(
        self,
        request: facebody_20191230_models.SearchFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SearchFaceResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        search_face_req = facebody_20191230_models.SearchFaceRequest()
        OpenApiUtilClient.convert(request, search_face_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_url_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        search_face_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        search_face_resp = self.search_face_with_options(search_face_req, runtime)
        return search_face_resp

    async def search_face_advance_async(
        self,
        request: facebody_20191230_models.SearchFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SearchFaceResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        search_face_req = facebody_20191230_models.SearchFaceRequest()
        OpenApiUtilClient.convert(request, search_face_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_url_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        search_face_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        search_face_resp = await self.search_face_with_options_async(search_face_req, runtime)
        return search_face_resp

    def swap_facial_features_with_options(
        self,
        request: facebody_20191230_models.SwapFacialFeaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SwapFacialFeaturesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.SwapFacialFeaturesResponse().from_map(
            self.do_rpcrequest('SwapFacialFeatures', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def swap_facial_features_with_options_async(
        self,
        request: facebody_20191230_models.SwapFacialFeaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SwapFacialFeaturesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.SwapFacialFeaturesResponse().from_map(
            await self.do_rpcrequest_async('SwapFacialFeatures', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def swap_facial_features(
        self,
        request: facebody_20191230_models.SwapFacialFeaturesRequest,
    ) -> facebody_20191230_models.SwapFacialFeaturesResponse:
        runtime = util_models.RuntimeOptions()
        return self.swap_facial_features_with_options(request, runtime)

    async def swap_facial_features_async(
        self,
        request: facebody_20191230_models.SwapFacialFeaturesRequest,
    ) -> facebody_20191230_models.SwapFacialFeaturesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.swap_facial_features_with_options_async(request, runtime)

    def swap_facial_features_advance(
        self,
        request: facebody_20191230_models.SwapFacialFeaturesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SwapFacialFeaturesResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        swap_facial_features_req = facebody_20191230_models.SwapFacialFeaturesRequest()
        OpenApiUtilClient.convert(request, swap_facial_features_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.source_image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        swap_facial_features_req.source_image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        swap_facial_features_resp = self.swap_facial_features_with_options(swap_facial_features_req, runtime)
        return swap_facial_features_resp

    async def swap_facial_features_advance_async(
        self,
        request: facebody_20191230_models.SwapFacialFeaturesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SwapFacialFeaturesResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        swap_facial_features_req = facebody_20191230_models.SwapFacialFeaturesRequest()
        OpenApiUtilClient.convert(request, swap_facial_features_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.source_image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        swap_facial_features_req.source_image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        swap_facial_features_resp = await self.swap_facial_features_with_options_async(swap_facial_features_req, runtime)
        return swap_facial_features_resp

    def update_face_entity_with_options(
        self,
        request: facebody_20191230_models.UpdateFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.UpdateFaceEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.UpdateFaceEntityResponse().from_map(
            self.do_rpcrequest('UpdateFaceEntity', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_face_entity_with_options_async(
        self,
        request: facebody_20191230_models.UpdateFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.UpdateFaceEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.UpdateFaceEntityResponse().from_map(
            await self.do_rpcrequest_async('UpdateFaceEntity', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_face_entity(
        self,
        request: facebody_20191230_models.UpdateFaceEntityRequest,
    ) -> facebody_20191230_models.UpdateFaceEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_face_entity_with_options(request, runtime)

    async def update_face_entity_async(
        self,
        request: facebody_20191230_models.UpdateFaceEntityRequest,
    ) -> facebody_20191230_models.UpdateFaceEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_face_entity_with_options_async(request, runtime)

    def verify_face_mask_with_options(
        self,
        request: facebody_20191230_models.VerifyFaceMaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.VerifyFaceMaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.VerifyFaceMaskResponse().from_map(
            self.do_rpcrequest('VerifyFaceMask', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_face_mask_with_options_async(
        self,
        request: facebody_20191230_models.VerifyFaceMaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.VerifyFaceMaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return facebody_20191230_models.VerifyFaceMaskResponse().from_map(
            await self.do_rpcrequest_async('VerifyFaceMask', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_face_mask(
        self,
        request: facebody_20191230_models.VerifyFaceMaskRequest,
    ) -> facebody_20191230_models.VerifyFaceMaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_face_mask_with_options(request, runtime)

    async def verify_face_mask_async(
        self,
        request: facebody_20191230_models.VerifyFaceMaskRequest,
    ) -> facebody_20191230_models.VerifyFaceMaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_face_mask_with_options_async(request, runtime)

    def verify_face_mask_advance(
        self,
        request: facebody_20191230_models.VerifyFaceMaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.VerifyFaceMaskResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        verify_face_mask_req = facebody_20191230_models.VerifyFaceMaskRequest()
        OpenApiUtilClient.convert(request, verify_face_mask_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        verify_face_mask_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        verify_face_mask_resp = self.verify_face_mask_with_options(verify_face_mask_req, runtime)
        return verify_face_mask_resp

    async def verify_face_mask_advance_async(
        self,
        request: facebody_20191230_models.VerifyFaceMaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.VerifyFaceMaskResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='facebody',
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
        verify_face_mask_req = facebody_20191230_models.VerifyFaceMaskRequest()
        OpenApiUtilClient.convert(request, verify_face_mask_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        verify_face_mask_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        verify_face_mask_resp = await self.verify_face_mask_with_options_async(verify_face_mask_req, runtime)
        return verify_face_mask_resp
