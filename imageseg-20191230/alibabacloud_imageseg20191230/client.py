# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imageseg20191230 import models as imageseg_20191230_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
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
        self._endpoint = self.get_endpoint('imageseg', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def change_sky_with_options(
        self,
        request: imageseg_20191230_models.ChangeSkyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.ChangeSkyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.ChangeSkyResponse().from_map(
            self.do_rpcrequest('ChangeSky', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_sky_with_options_async(
        self,
        request: imageseg_20191230_models.ChangeSkyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.ChangeSkyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.ChangeSkyResponse().from_map(
            await self.do_rpcrequest_async('ChangeSky', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_sky(
        self,
        request: imageseg_20191230_models.ChangeSkyRequest,
    ) -> imageseg_20191230_models.ChangeSkyResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_sky_with_options(request, runtime)

    async def change_sky_async(
        self,
        request: imageseg_20191230_models.ChangeSkyRequest,
    ) -> imageseg_20191230_models.ChangeSkyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_sky_with_options_async(request, runtime)

    def change_sky_advance(
        self,
        request: imageseg_20191230_models.ChangeSkyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.ChangeSkyResponse:
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
            product='imageseg',
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
        change_sky_req = imageseg_20191230_models.ChangeSkyRequest()
        OpenApiUtilClient.convert(request, change_sky_req)
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
        change_sky_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        change_sky_resp = self.change_sky_with_options(change_sky_req, runtime)
        return change_sky_resp

    async def change_sky_advance_async(
        self,
        request: imageseg_20191230_models.ChangeSkyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.ChangeSkyResponse:
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
            product='imageseg',
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
        change_sky_req = imageseg_20191230_models.ChangeSkyRequest()
        OpenApiUtilClient.convert(request, change_sky_req)
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
        change_sky_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        change_sky_resp = await self.change_sky_with_options_async(change_sky_req, runtime)
        return change_sky_resp

    def get_async_job_result_with_options(
        self,
        request: imageseg_20191230_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.GetAsyncJobResultResponse().from_map(
            self.do_rpcrequest('GetAsyncJobResult', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_async_job_result_with_options_async(
        self,
        request: imageseg_20191230_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.GetAsyncJobResultResponse().from_map(
            await self.do_rpcrequest_async('GetAsyncJobResult', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_async_job_result(
        self,
        request: imageseg_20191230_models.GetAsyncJobResultRequest,
    ) -> imageseg_20191230_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result_with_options(request, runtime)

    async def get_async_job_result_async(
        self,
        request: imageseg_20191230_models.GetAsyncJobResultRequest,
    ) -> imageseg_20191230_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_job_result_with_options_async(request, runtime)

    def parse_face_with_options(
        self,
        request: imageseg_20191230_models.ParseFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.ParseFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.ParseFaceResponse().from_map(
            self.do_rpcrequest('ParseFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def parse_face_with_options_async(
        self,
        request: imageseg_20191230_models.ParseFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.ParseFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.ParseFaceResponse().from_map(
            await self.do_rpcrequest_async('ParseFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def parse_face(
        self,
        request: imageseg_20191230_models.ParseFaceRequest,
    ) -> imageseg_20191230_models.ParseFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.parse_face_with_options(request, runtime)

    async def parse_face_async(
        self,
        request: imageseg_20191230_models.ParseFaceRequest,
    ) -> imageseg_20191230_models.ParseFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.parse_face_with_options_async(request, runtime)

    def parse_face_advance(
        self,
        request: imageseg_20191230_models.ParseFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.ParseFaceResponse:
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
            product='imageseg',
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
        parse_face_req = imageseg_20191230_models.ParseFaceRequest()
        OpenApiUtilClient.convert(request, parse_face_req)
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
        parse_face_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        parse_face_resp = self.parse_face_with_options(parse_face_req, runtime)
        return parse_face_resp

    async def parse_face_advance_async(
        self,
        request: imageseg_20191230_models.ParseFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.ParseFaceResponse:
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
            product='imageseg',
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
        parse_face_req = imageseg_20191230_models.ParseFaceRequest()
        OpenApiUtilClient.convert(request, parse_face_req)
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
        parse_face_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        parse_face_resp = await self.parse_face_with_options_async(parse_face_req, runtime)
        return parse_face_resp

    def refine_mask_with_options(
        self,
        request: imageseg_20191230_models.RefineMaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.RefineMaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.RefineMaskResponse().from_map(
            self.do_rpcrequest('RefineMask', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refine_mask_with_options_async(
        self,
        request: imageseg_20191230_models.RefineMaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.RefineMaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.RefineMaskResponse().from_map(
            await self.do_rpcrequest_async('RefineMask', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refine_mask(
        self,
        request: imageseg_20191230_models.RefineMaskRequest,
    ) -> imageseg_20191230_models.RefineMaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.refine_mask_with_options(request, runtime)

    async def refine_mask_async(
        self,
        request: imageseg_20191230_models.RefineMaskRequest,
    ) -> imageseg_20191230_models.RefineMaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refine_mask_with_options_async(request, runtime)

    def refine_mask_advance(
        self,
        request: imageseg_20191230_models.RefineMaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.RefineMaskResponse:
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
            product='imageseg',
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
        refine_mask_req = imageseg_20191230_models.RefineMaskRequest()
        OpenApiUtilClient.convert(request, refine_mask_req)
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
        refine_mask_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        refine_mask_resp = self.refine_mask_with_options(refine_mask_req, runtime)
        return refine_mask_resp

    async def refine_mask_advance_async(
        self,
        request: imageseg_20191230_models.RefineMaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.RefineMaskResponse:
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
            product='imageseg',
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
        refine_mask_req = imageseg_20191230_models.RefineMaskRequest()
        OpenApiUtilClient.convert(request, refine_mask_req)
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
        refine_mask_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        refine_mask_resp = await self.refine_mask_with_options_async(refine_mask_req, runtime)
        return refine_mask_resp

    def segment_animal_with_options(
        self,
        request: imageseg_20191230_models.SegmentAnimalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentAnimalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentAnimalResponse().from_map(
            self.do_rpcrequest('SegmentAnimal', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_animal_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentAnimalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentAnimalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentAnimalResponse().from_map(
            await self.do_rpcrequest_async('SegmentAnimal', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_animal(
        self,
        request: imageseg_20191230_models.SegmentAnimalRequest,
    ) -> imageseg_20191230_models.SegmentAnimalResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_animal_with_options(request, runtime)

    async def segment_animal_async(
        self,
        request: imageseg_20191230_models.SegmentAnimalRequest,
    ) -> imageseg_20191230_models.SegmentAnimalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_animal_with_options_async(request, runtime)

    def segment_animal_advance(
        self,
        request: imageseg_20191230_models.SegmentAnimalAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentAnimalResponse:
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
            product='imageseg',
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
        segment_animal_req = imageseg_20191230_models.SegmentAnimalRequest()
        OpenApiUtilClient.convert(request, segment_animal_req)
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
        segment_animal_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_animal_resp = self.segment_animal_with_options(segment_animal_req, runtime)
        return segment_animal_resp

    async def segment_animal_advance_async(
        self,
        request: imageseg_20191230_models.SegmentAnimalAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentAnimalResponse:
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
            product='imageseg',
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
        segment_animal_req = imageseg_20191230_models.SegmentAnimalRequest()
        OpenApiUtilClient.convert(request, segment_animal_req)
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
        segment_animal_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_animal_resp = await self.segment_animal_with_options_async(segment_animal_req, runtime)
        return segment_animal_resp

    def segment_body_with_options(
        self,
        request: imageseg_20191230_models.SegmentBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentBodyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentBodyResponse().from_map(
            self.do_rpcrequest('SegmentBody', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_body_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentBodyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentBodyResponse().from_map(
            await self.do_rpcrequest_async('SegmentBody', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_body(
        self,
        request: imageseg_20191230_models.SegmentBodyRequest,
    ) -> imageseg_20191230_models.SegmentBodyResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_body_with_options(request, runtime)

    async def segment_body_async(
        self,
        request: imageseg_20191230_models.SegmentBodyRequest,
    ) -> imageseg_20191230_models.SegmentBodyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_body_with_options_async(request, runtime)

    def segment_body_advance(
        self,
        request: imageseg_20191230_models.SegmentBodyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentBodyResponse:
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
            product='imageseg',
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
        segment_body_req = imageseg_20191230_models.SegmentBodyRequest()
        OpenApiUtilClient.convert(request, segment_body_req)
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
        segment_body_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_body_resp = self.segment_body_with_options(segment_body_req, runtime)
        return segment_body_resp

    async def segment_body_advance_async(
        self,
        request: imageseg_20191230_models.SegmentBodyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentBodyResponse:
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
            product='imageseg',
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
        segment_body_req = imageseg_20191230_models.SegmentBodyRequest()
        OpenApiUtilClient.convert(request, segment_body_req)
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
        segment_body_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_body_resp = await self.segment_body_with_options_async(segment_body_req, runtime)
        return segment_body_resp

    def segment_cloth_with_options(
        self,
        request: imageseg_20191230_models.SegmentClothRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentClothResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentClothResponse().from_map(
            self.do_rpcrequest('SegmentCloth', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_cloth_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentClothRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentClothResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentClothResponse().from_map(
            await self.do_rpcrequest_async('SegmentCloth', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_cloth(
        self,
        request: imageseg_20191230_models.SegmentClothRequest,
    ) -> imageseg_20191230_models.SegmentClothResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_cloth_with_options(request, runtime)

    async def segment_cloth_async(
        self,
        request: imageseg_20191230_models.SegmentClothRequest,
    ) -> imageseg_20191230_models.SegmentClothResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_cloth_with_options_async(request, runtime)

    def segment_cloth_advance(
        self,
        request: imageseg_20191230_models.SegmentClothAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentClothResponse:
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
            product='imageseg',
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
        segment_cloth_req = imageseg_20191230_models.SegmentClothRequest()
        OpenApiUtilClient.convert(request, segment_cloth_req)
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
        segment_cloth_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_cloth_resp = self.segment_cloth_with_options(segment_cloth_req, runtime)
        return segment_cloth_resp

    async def segment_cloth_advance_async(
        self,
        request: imageseg_20191230_models.SegmentClothAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentClothResponse:
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
            product='imageseg',
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
        segment_cloth_req = imageseg_20191230_models.SegmentClothRequest()
        OpenApiUtilClient.convert(request, segment_cloth_req)
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
        segment_cloth_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_cloth_resp = await self.segment_cloth_with_options_async(segment_cloth_req, runtime)
        return segment_cloth_resp

    def segment_commodity_with_options(
        self,
        request: imageseg_20191230_models.SegmentCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentCommodityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentCommodityResponse().from_map(
            self.do_rpcrequest('SegmentCommodity', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_commodity_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentCommodityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentCommodityResponse().from_map(
            await self.do_rpcrequest_async('SegmentCommodity', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_commodity(
        self,
        request: imageseg_20191230_models.SegmentCommodityRequest,
    ) -> imageseg_20191230_models.SegmentCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_commodity_with_options(request, runtime)

    async def segment_commodity_async(
        self,
        request: imageseg_20191230_models.SegmentCommodityRequest,
    ) -> imageseg_20191230_models.SegmentCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_commodity_with_options_async(request, runtime)

    def segment_commodity_advance(
        self,
        request: imageseg_20191230_models.SegmentCommodityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentCommodityResponse:
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
            product='imageseg',
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
        segment_commodity_req = imageseg_20191230_models.SegmentCommodityRequest()
        OpenApiUtilClient.convert(request, segment_commodity_req)
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
        segment_commodity_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_commodity_resp = self.segment_commodity_with_options(segment_commodity_req, runtime)
        return segment_commodity_resp

    async def segment_commodity_advance_async(
        self,
        request: imageseg_20191230_models.SegmentCommodityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentCommodityResponse:
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
            product='imageseg',
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
        segment_commodity_req = imageseg_20191230_models.SegmentCommodityRequest()
        OpenApiUtilClient.convert(request, segment_commodity_req)
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
        segment_commodity_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_commodity_resp = await self.segment_commodity_with_options_async(segment_commodity_req, runtime)
        return segment_commodity_resp

    def segment_common_image_with_options(
        self,
        request: imageseg_20191230_models.SegmentCommonImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentCommonImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentCommonImageResponse().from_map(
            self.do_rpcrequest('SegmentCommonImage', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_common_image_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentCommonImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentCommonImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentCommonImageResponse().from_map(
            await self.do_rpcrequest_async('SegmentCommonImage', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_common_image(
        self,
        request: imageseg_20191230_models.SegmentCommonImageRequest,
    ) -> imageseg_20191230_models.SegmentCommonImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_common_image_with_options(request, runtime)

    async def segment_common_image_async(
        self,
        request: imageseg_20191230_models.SegmentCommonImageRequest,
    ) -> imageseg_20191230_models.SegmentCommonImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_common_image_with_options_async(request, runtime)

    def segment_common_image_advance(
        self,
        request: imageseg_20191230_models.SegmentCommonImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentCommonImageResponse:
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
            product='imageseg',
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
        segment_common_image_req = imageseg_20191230_models.SegmentCommonImageRequest()
        OpenApiUtilClient.convert(request, segment_common_image_req)
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
        segment_common_image_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_common_image_resp = self.segment_common_image_with_options(segment_common_image_req, runtime)
        return segment_common_image_resp

    async def segment_common_image_advance_async(
        self,
        request: imageseg_20191230_models.SegmentCommonImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentCommonImageResponse:
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
            product='imageseg',
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
        segment_common_image_req = imageseg_20191230_models.SegmentCommonImageRequest()
        OpenApiUtilClient.convert(request, segment_common_image_req)
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
        segment_common_image_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_common_image_resp = await self.segment_common_image_with_options_async(segment_common_image_req, runtime)
        return segment_common_image_resp

    def segment_face_with_options(
        self,
        request: imageseg_20191230_models.SegmentFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentFaceResponse().from_map(
            self.do_rpcrequest('SegmentFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_face_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentFaceResponse().from_map(
            await self.do_rpcrequest_async('SegmentFace', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_face(
        self,
        request: imageseg_20191230_models.SegmentFaceRequest,
    ) -> imageseg_20191230_models.SegmentFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_face_with_options(request, runtime)

    async def segment_face_async(
        self,
        request: imageseg_20191230_models.SegmentFaceRequest,
    ) -> imageseg_20191230_models.SegmentFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_face_with_options_async(request, runtime)

    def segment_face_advance(
        self,
        request: imageseg_20191230_models.SegmentFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentFaceResponse:
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
            product='imageseg',
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
        segment_face_req = imageseg_20191230_models.SegmentFaceRequest()
        OpenApiUtilClient.convert(request, segment_face_req)
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
        segment_face_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_face_resp = self.segment_face_with_options(segment_face_req, runtime)
        return segment_face_resp

    async def segment_face_advance_async(
        self,
        request: imageseg_20191230_models.SegmentFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentFaceResponse:
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
            product='imageseg',
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
        segment_face_req = imageseg_20191230_models.SegmentFaceRequest()
        OpenApiUtilClient.convert(request, segment_face_req)
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
        segment_face_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_face_resp = await self.segment_face_with_options_async(segment_face_req, runtime)
        return segment_face_resp

    def segment_food_with_options(
        self,
        request: imageseg_20191230_models.SegmentFoodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentFoodResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentFoodResponse().from_map(
            self.do_rpcrequest('SegmentFood', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_food_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentFoodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentFoodResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentFoodResponse().from_map(
            await self.do_rpcrequest_async('SegmentFood', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_food(
        self,
        request: imageseg_20191230_models.SegmentFoodRequest,
    ) -> imageseg_20191230_models.SegmentFoodResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_food_with_options(request, runtime)

    async def segment_food_async(
        self,
        request: imageseg_20191230_models.SegmentFoodRequest,
    ) -> imageseg_20191230_models.SegmentFoodResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_food_with_options_async(request, runtime)

    def segment_food_advance(
        self,
        request: imageseg_20191230_models.SegmentFoodAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentFoodResponse:
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
            product='imageseg',
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
        segment_food_req = imageseg_20191230_models.SegmentFoodRequest()
        OpenApiUtilClient.convert(request, segment_food_req)
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
        segment_food_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_food_resp = self.segment_food_with_options(segment_food_req, runtime)
        return segment_food_resp

    async def segment_food_advance_async(
        self,
        request: imageseg_20191230_models.SegmentFoodAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentFoodResponse:
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
            product='imageseg',
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
        segment_food_req = imageseg_20191230_models.SegmentFoodRequest()
        OpenApiUtilClient.convert(request, segment_food_req)
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
        segment_food_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_food_resp = await self.segment_food_with_options_async(segment_food_req, runtime)
        return segment_food_resp

    def segment_furniture_with_options(
        self,
        request: imageseg_20191230_models.SegmentFurnitureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentFurnitureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentFurnitureResponse().from_map(
            self.do_rpcrequest('SegmentFurniture', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_furniture_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentFurnitureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentFurnitureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentFurnitureResponse().from_map(
            await self.do_rpcrequest_async('SegmentFurniture', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_furniture(
        self,
        request: imageseg_20191230_models.SegmentFurnitureRequest,
    ) -> imageseg_20191230_models.SegmentFurnitureResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_furniture_with_options(request, runtime)

    async def segment_furniture_async(
        self,
        request: imageseg_20191230_models.SegmentFurnitureRequest,
    ) -> imageseg_20191230_models.SegmentFurnitureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_furniture_with_options_async(request, runtime)

    def segment_furniture_advance(
        self,
        request: imageseg_20191230_models.SegmentFurnitureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentFurnitureResponse:
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
            product='imageseg',
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
        segment_furniture_req = imageseg_20191230_models.SegmentFurnitureRequest()
        OpenApiUtilClient.convert(request, segment_furniture_req)
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
        segment_furniture_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_furniture_resp = self.segment_furniture_with_options(segment_furniture_req, runtime)
        return segment_furniture_resp

    async def segment_furniture_advance_async(
        self,
        request: imageseg_20191230_models.SegmentFurnitureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentFurnitureResponse:
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
            product='imageseg',
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
        segment_furniture_req = imageseg_20191230_models.SegmentFurnitureRequest()
        OpenApiUtilClient.convert(request, segment_furniture_req)
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
        segment_furniture_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_furniture_resp = await self.segment_furniture_with_options_async(segment_furniture_req, runtime)
        return segment_furniture_resp

    def segment_hair_with_options(
        self,
        request: imageseg_20191230_models.SegmentHairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentHairResponse().from_map(
            self.do_rpcrequest('SegmentHair', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_hair_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentHairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentHairResponse().from_map(
            await self.do_rpcrequest_async('SegmentHair', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_hair(
        self,
        request: imageseg_20191230_models.SegmentHairRequest,
    ) -> imageseg_20191230_models.SegmentHairResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_hair_with_options(request, runtime)

    async def segment_hair_async(
        self,
        request: imageseg_20191230_models.SegmentHairRequest,
    ) -> imageseg_20191230_models.SegmentHairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_hair_with_options_async(request, runtime)

    def segment_hair_advance(
        self,
        request: imageseg_20191230_models.SegmentHairAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHairResponse:
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
            product='imageseg',
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
        segment_hair_req = imageseg_20191230_models.SegmentHairRequest()
        OpenApiUtilClient.convert(request, segment_hair_req)
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
        segment_hair_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_hair_resp = self.segment_hair_with_options(segment_hair_req, runtime)
        return segment_hair_resp

    async def segment_hair_advance_async(
        self,
        request: imageseg_20191230_models.SegmentHairAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHairResponse:
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
            product='imageseg',
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
        segment_hair_req = imageseg_20191230_models.SegmentHairRequest()
        OpenApiUtilClient.convert(request, segment_hair_req)
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
        segment_hair_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_hair_resp = await self.segment_hair_with_options_async(segment_hair_req, runtime)
        return segment_hair_resp

    def segment_hdbody_with_options(
        self,
        request: imageseg_20191230_models.SegmentHDBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHDBodyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentHDBodyResponse().from_map(
            self.do_rpcrequest('SegmentHDBody', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_hdbody_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentHDBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHDBodyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentHDBodyResponse().from_map(
            await self.do_rpcrequest_async('SegmentHDBody', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_hdbody(
        self,
        request: imageseg_20191230_models.SegmentHDBodyRequest,
    ) -> imageseg_20191230_models.SegmentHDBodyResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_hdbody_with_options(request, runtime)

    async def segment_hdbody_async(
        self,
        request: imageseg_20191230_models.SegmentHDBodyRequest,
    ) -> imageseg_20191230_models.SegmentHDBodyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_hdbody_with_options_async(request, runtime)

    def segment_hdbody_advance(
        self,
        request: imageseg_20191230_models.SegmentHDBodyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHDBodyResponse:
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
            product='imageseg',
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
        segment_hdbody_req = imageseg_20191230_models.SegmentHDBodyRequest()
        OpenApiUtilClient.convert(request, segment_hdbody_req)
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
        segment_hdbody_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_hdbody_resp = self.segment_hdbody_with_options(segment_hdbody_req, runtime)
        return segment_hdbody_resp

    async def segment_hdbody_advance_async(
        self,
        request: imageseg_20191230_models.SegmentHDBodyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHDBodyResponse:
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
            product='imageseg',
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
        segment_hdbody_req = imageseg_20191230_models.SegmentHDBodyRequest()
        OpenApiUtilClient.convert(request, segment_hdbody_req)
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
        segment_hdbody_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_hdbody_resp = await self.segment_hdbody_with_options_async(segment_hdbody_req, runtime)
        return segment_hdbody_resp

    def segment_hdcommon_image_with_options(
        self,
        request: imageseg_20191230_models.SegmentHDCommonImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHDCommonImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentHDCommonImageResponse().from_map(
            self.do_rpcrequest('SegmentHDCommonImage', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_hdcommon_image_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentHDCommonImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHDCommonImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentHDCommonImageResponse().from_map(
            await self.do_rpcrequest_async('SegmentHDCommonImage', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_hdcommon_image(
        self,
        request: imageseg_20191230_models.SegmentHDCommonImageRequest,
    ) -> imageseg_20191230_models.SegmentHDCommonImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_hdcommon_image_with_options(request, runtime)

    async def segment_hdcommon_image_async(
        self,
        request: imageseg_20191230_models.SegmentHDCommonImageRequest,
    ) -> imageseg_20191230_models.SegmentHDCommonImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_hdcommon_image_with_options_async(request, runtime)

    def segment_hdcommon_image_advance(
        self,
        request: imageseg_20191230_models.SegmentHDCommonImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHDCommonImageResponse:
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
            product='imageseg',
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
        segment_hdcommon_image_req = imageseg_20191230_models.SegmentHDCommonImageRequest()
        OpenApiUtilClient.convert(request, segment_hdcommon_image_req)
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
        segment_hdcommon_image_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_hdcommon_image_resp = self.segment_hdcommon_image_with_options(segment_hdcommon_image_req, runtime)
        return segment_hdcommon_image_resp

    async def segment_hdcommon_image_advance_async(
        self,
        request: imageseg_20191230_models.SegmentHDCommonImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHDCommonImageResponse:
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
            product='imageseg',
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
        segment_hdcommon_image_req = imageseg_20191230_models.SegmentHDCommonImageRequest()
        OpenApiUtilClient.convert(request, segment_hdcommon_image_req)
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
        segment_hdcommon_image_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_hdcommon_image_resp = await self.segment_hdcommon_image_with_options_async(segment_hdcommon_image_req, runtime)
        return segment_hdcommon_image_resp

    def segment_hdsky_with_options(
        self,
        request: imageseg_20191230_models.SegmentHDSkyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHDSkyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentHDSkyResponse().from_map(
            self.do_rpcrequest('SegmentHDSky', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_hdsky_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentHDSkyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHDSkyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentHDSkyResponse().from_map(
            await self.do_rpcrequest_async('SegmentHDSky', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_hdsky(
        self,
        request: imageseg_20191230_models.SegmentHDSkyRequest,
    ) -> imageseg_20191230_models.SegmentHDSkyResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_hdsky_with_options(request, runtime)

    async def segment_hdsky_async(
        self,
        request: imageseg_20191230_models.SegmentHDSkyRequest,
    ) -> imageseg_20191230_models.SegmentHDSkyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_hdsky_with_options_async(request, runtime)

    def segment_hdsky_advance(
        self,
        request: imageseg_20191230_models.SegmentHDSkyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHDSkyResponse:
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
            product='imageseg',
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
        segment_hdsky_req = imageseg_20191230_models.SegmentHDSkyRequest()
        OpenApiUtilClient.convert(request, segment_hdsky_req)
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
        segment_hdsky_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_hdsky_resp = self.segment_hdsky_with_options(segment_hdsky_req, runtime)
        return segment_hdsky_resp

    async def segment_hdsky_advance_async(
        self,
        request: imageseg_20191230_models.SegmentHDSkyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHDSkyResponse:
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
            product='imageseg',
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
        segment_hdsky_req = imageseg_20191230_models.SegmentHDSkyRequest()
        OpenApiUtilClient.convert(request, segment_hdsky_req)
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
        segment_hdsky_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_hdsky_resp = await self.segment_hdsky_with_options_async(segment_hdsky_req, runtime)
        return segment_hdsky_resp

    def segment_head_with_options(
        self,
        request: imageseg_20191230_models.SegmentHeadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHeadResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentHeadResponse().from_map(
            self.do_rpcrequest('SegmentHead', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_head_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentHeadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHeadResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentHeadResponse().from_map(
            await self.do_rpcrequest_async('SegmentHead', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_head(
        self,
        request: imageseg_20191230_models.SegmentHeadRequest,
    ) -> imageseg_20191230_models.SegmentHeadResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_head_with_options(request, runtime)

    async def segment_head_async(
        self,
        request: imageseg_20191230_models.SegmentHeadRequest,
    ) -> imageseg_20191230_models.SegmentHeadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_head_with_options_async(request, runtime)

    def segment_head_advance(
        self,
        request: imageseg_20191230_models.SegmentHeadAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHeadResponse:
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
            product='imageseg',
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
        segment_head_req = imageseg_20191230_models.SegmentHeadRequest()
        OpenApiUtilClient.convert(request, segment_head_req)
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
        segment_head_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_head_resp = self.segment_head_with_options(segment_head_req, runtime)
        return segment_head_resp

    async def segment_head_advance_async(
        self,
        request: imageseg_20191230_models.SegmentHeadAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentHeadResponse:
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
            product='imageseg',
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
        segment_head_req = imageseg_20191230_models.SegmentHeadRequest()
        OpenApiUtilClient.convert(request, segment_head_req)
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
        segment_head_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_head_resp = await self.segment_head_with_options_async(segment_head_req, runtime)
        return segment_head_resp

    def segment_logo_with_options(
        self,
        request: imageseg_20191230_models.SegmentLogoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentLogoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentLogoResponse().from_map(
            self.do_rpcrequest('SegmentLogo', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_logo_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentLogoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentLogoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentLogoResponse().from_map(
            await self.do_rpcrequest_async('SegmentLogo', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_logo(
        self,
        request: imageseg_20191230_models.SegmentLogoRequest,
    ) -> imageseg_20191230_models.SegmentLogoResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_logo_with_options(request, runtime)

    async def segment_logo_async(
        self,
        request: imageseg_20191230_models.SegmentLogoRequest,
    ) -> imageseg_20191230_models.SegmentLogoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_logo_with_options_async(request, runtime)

    def segment_logo_advance(
        self,
        request: imageseg_20191230_models.SegmentLogoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentLogoResponse:
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
            product='imageseg',
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
        segment_logo_req = imageseg_20191230_models.SegmentLogoRequest()
        OpenApiUtilClient.convert(request, segment_logo_req)
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
        segment_logo_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_logo_resp = self.segment_logo_with_options(segment_logo_req, runtime)
        return segment_logo_resp

    async def segment_logo_advance_async(
        self,
        request: imageseg_20191230_models.SegmentLogoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentLogoResponse:
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
            product='imageseg',
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
        segment_logo_req = imageseg_20191230_models.SegmentLogoRequest()
        OpenApiUtilClient.convert(request, segment_logo_req)
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
        segment_logo_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_logo_resp = await self.segment_logo_with_options_async(segment_logo_req, runtime)
        return segment_logo_resp

    def segment_scene_with_options(
        self,
        request: imageseg_20191230_models.SegmentSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentSceneResponse().from_map(
            self.do_rpcrequest('SegmentScene', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_scene_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentSceneResponse().from_map(
            await self.do_rpcrequest_async('SegmentScene', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_scene(
        self,
        request: imageseg_20191230_models.SegmentSceneRequest,
    ) -> imageseg_20191230_models.SegmentSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_scene_with_options(request, runtime)

    async def segment_scene_async(
        self,
        request: imageseg_20191230_models.SegmentSceneRequest,
    ) -> imageseg_20191230_models.SegmentSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_scene_with_options_async(request, runtime)

    def segment_scene_advance(
        self,
        request: imageseg_20191230_models.SegmentSceneAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentSceneResponse:
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
            product='imageseg',
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
        segment_scene_req = imageseg_20191230_models.SegmentSceneRequest()
        OpenApiUtilClient.convert(request, segment_scene_req)
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
        segment_scene_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_scene_resp = self.segment_scene_with_options(segment_scene_req, runtime)
        return segment_scene_resp

    async def segment_scene_advance_async(
        self,
        request: imageseg_20191230_models.SegmentSceneAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentSceneResponse:
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
            product='imageseg',
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
        segment_scene_req = imageseg_20191230_models.SegmentSceneRequest()
        OpenApiUtilClient.convert(request, segment_scene_req)
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
        segment_scene_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_scene_resp = await self.segment_scene_with_options_async(segment_scene_req, runtime)
        return segment_scene_resp

    def segment_skin_with_options(
        self,
        request: imageseg_20191230_models.SegmentSkinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentSkinResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentSkinResponse().from_map(
            self.do_rpcrequest('SegmentSkin', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_skin_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentSkinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentSkinResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentSkinResponse().from_map(
            await self.do_rpcrequest_async('SegmentSkin', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_skin(
        self,
        request: imageseg_20191230_models.SegmentSkinRequest,
    ) -> imageseg_20191230_models.SegmentSkinResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_skin_with_options(request, runtime)

    async def segment_skin_async(
        self,
        request: imageseg_20191230_models.SegmentSkinRequest,
    ) -> imageseg_20191230_models.SegmentSkinResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_skin_with_options_async(request, runtime)

    def segment_skin_advance(
        self,
        request: imageseg_20191230_models.SegmentSkinAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentSkinResponse:
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
            product='imageseg',
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
        segment_skin_req = imageseg_20191230_models.SegmentSkinRequest()
        OpenApiUtilClient.convert(request, segment_skin_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.urlobject,
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
        segment_skin_req.url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_skin_resp = self.segment_skin_with_options(segment_skin_req, runtime)
        return segment_skin_resp

    async def segment_skin_advance_async(
        self,
        request: imageseg_20191230_models.SegmentSkinAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentSkinResponse:
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
            product='imageseg',
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
        segment_skin_req = imageseg_20191230_models.SegmentSkinRequest()
        OpenApiUtilClient.convert(request, segment_skin_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.urlobject,
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
        segment_skin_req.url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_skin_resp = await self.segment_skin_with_options_async(segment_skin_req, runtime)
        return segment_skin_resp

    def segment_sky_with_options(
        self,
        request: imageseg_20191230_models.SegmentSkyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentSkyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentSkyResponse().from_map(
            self.do_rpcrequest('SegmentSky', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_sky_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentSkyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentSkyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentSkyResponse().from_map(
            await self.do_rpcrequest_async('SegmentSky', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_sky(
        self,
        request: imageseg_20191230_models.SegmentSkyRequest,
    ) -> imageseg_20191230_models.SegmentSkyResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_sky_with_options(request, runtime)

    async def segment_sky_async(
        self,
        request: imageseg_20191230_models.SegmentSkyRequest,
    ) -> imageseg_20191230_models.SegmentSkyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_sky_with_options_async(request, runtime)

    def segment_sky_advance(
        self,
        request: imageseg_20191230_models.SegmentSkyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentSkyResponse:
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
            product='imageseg',
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
        segment_sky_req = imageseg_20191230_models.SegmentSkyRequest()
        OpenApiUtilClient.convert(request, segment_sky_req)
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
        segment_sky_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_sky_resp = self.segment_sky_with_options(segment_sky_req, runtime)
        return segment_sky_resp

    async def segment_sky_advance_async(
        self,
        request: imageseg_20191230_models.SegmentSkyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentSkyResponse:
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
            product='imageseg',
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
        segment_sky_req = imageseg_20191230_models.SegmentSkyRequest()
        OpenApiUtilClient.convert(request, segment_sky_req)
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
        segment_sky_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_sky_resp = await self.segment_sky_with_options_async(segment_sky_req, runtime)
        return segment_sky_resp

    def segment_vehicle_with_options(
        self,
        request: imageseg_20191230_models.SegmentVehicleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentVehicleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentVehicleResponse().from_map(
            self.do_rpcrequest('SegmentVehicle', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_vehicle_with_options_async(
        self,
        request: imageseg_20191230_models.SegmentVehicleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentVehicleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageseg_20191230_models.SegmentVehicleResponse().from_map(
            await self.do_rpcrequest_async('SegmentVehicle', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_vehicle(
        self,
        request: imageseg_20191230_models.SegmentVehicleRequest,
    ) -> imageseg_20191230_models.SegmentVehicleResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_vehicle_with_options(request, runtime)

    async def segment_vehicle_async(
        self,
        request: imageseg_20191230_models.SegmentVehicleRequest,
    ) -> imageseg_20191230_models.SegmentVehicleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_vehicle_with_options_async(request, runtime)

    def segment_vehicle_advance(
        self,
        request: imageseg_20191230_models.SegmentVehicleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentVehicleResponse:
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
            product='imageseg',
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
        segment_vehicle_req = imageseg_20191230_models.SegmentVehicleRequest()
        OpenApiUtilClient.convert(request, segment_vehicle_req)
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
        segment_vehicle_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_vehicle_resp = self.segment_vehicle_with_options(segment_vehicle_req, runtime)
        return segment_vehicle_resp

    async def segment_vehicle_advance_async(
        self,
        request: imageseg_20191230_models.SegmentVehicleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageseg_20191230_models.SegmentVehicleResponse:
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
            product='imageseg',
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
        segment_vehicle_req = imageseg_20191230_models.SegmentVehicleRequest()
        OpenApiUtilClient.convert(request, segment_vehicle_req)
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
        segment_vehicle_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_vehicle_resp = await self.segment_vehicle_with_options_async(segment_vehicle_req, runtime)
        return segment_vehicle_resp
