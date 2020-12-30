# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_videoseg20200320 import models as videoseg_20200320_models
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
        self._endpoint = self.get_endpoint('videoseg', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        request: videoseg_20200320_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoseg_20200320_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return videoseg_20200320_models.GetAsyncJobResultResponse().from_map(
            self.do_rpcrequest('GetAsyncJobResult', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_async_job_result_with_options_async(
        self,
        request: videoseg_20200320_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoseg_20200320_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return videoseg_20200320_models.GetAsyncJobResultResponse().from_map(
            await self.do_rpcrequest_async('GetAsyncJobResult', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_async_job_result(
        self,
        request: videoseg_20200320_models.GetAsyncJobResultRequest,
    ) -> videoseg_20200320_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result_with_options(request, runtime)

    async def get_async_job_result_async(
        self,
        request: videoseg_20200320_models.GetAsyncJobResultRequest,
    ) -> videoseg_20200320_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_job_result_with_options_async(request, runtime)

    def segment_half_body_with_options(
        self,
        request: videoseg_20200320_models.SegmentHalfBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoseg_20200320_models.SegmentHalfBodyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return videoseg_20200320_models.SegmentHalfBodyResponse().from_map(
            self.do_rpcrequest('SegmentHalfBody', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_half_body_with_options_async(
        self,
        request: videoseg_20200320_models.SegmentHalfBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoseg_20200320_models.SegmentHalfBodyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return videoseg_20200320_models.SegmentHalfBodyResponse().from_map(
            await self.do_rpcrequest_async('SegmentHalfBody', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_half_body(
        self,
        request: videoseg_20200320_models.SegmentHalfBodyRequest,
    ) -> videoseg_20200320_models.SegmentHalfBodyResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_half_body_with_options(request, runtime)

    async def segment_half_body_async(
        self,
        request: videoseg_20200320_models.SegmentHalfBodyRequest,
    ) -> videoseg_20200320_models.SegmentHalfBodyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_half_body_with_options_async(request, runtime)

    def segment_half_body_advance(
        self,
        request: videoseg_20200320_models.SegmentHalfBodyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoseg_20200320_models.SegmentHalfBodyResponse:
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
            product='videoseg',
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
        segment_half_body_req = videoseg_20200320_models.SegmentHalfBodyRequest()
        OpenApiUtilClient.convert(request, segment_half_body_req)
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
        segment_half_body_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_half_body_resp = self.segment_half_body_with_options(segment_half_body_req, runtime)
        return segment_half_body_resp

    async def segment_half_body_advance_async(
        self,
        request: videoseg_20200320_models.SegmentHalfBodyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoseg_20200320_models.SegmentHalfBodyResponse:
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
            product='videoseg',
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
        segment_half_body_req = videoseg_20200320_models.SegmentHalfBodyRequest()
        OpenApiUtilClient.convert(request, segment_half_body_req)
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
        segment_half_body_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_half_body_resp = await self.segment_half_body_with_options_async(segment_half_body_req, runtime)
        return segment_half_body_resp

    def segment_video_body_with_options(
        self,
        request: videoseg_20200320_models.SegmentVideoBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoseg_20200320_models.SegmentVideoBodyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return videoseg_20200320_models.SegmentVideoBodyResponse().from_map(
            self.do_rpcrequest('SegmentVideoBody', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_video_body_with_options_async(
        self,
        request: videoseg_20200320_models.SegmentVideoBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoseg_20200320_models.SegmentVideoBodyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return videoseg_20200320_models.SegmentVideoBodyResponse().from_map(
            await self.do_rpcrequest_async('SegmentVideoBody', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_video_body(
        self,
        request: videoseg_20200320_models.SegmentVideoBodyRequest,
    ) -> videoseg_20200320_models.SegmentVideoBodyResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_video_body_with_options(request, runtime)

    async def segment_video_body_async(
        self,
        request: videoseg_20200320_models.SegmentVideoBodyRequest,
    ) -> videoseg_20200320_models.SegmentVideoBodyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_video_body_with_options_async(request, runtime)

    def segment_video_body_advance(
        self,
        request: videoseg_20200320_models.SegmentVideoBodyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoseg_20200320_models.SegmentVideoBodyResponse:
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
            product='videoseg',
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
        segment_video_body_req = videoseg_20200320_models.SegmentVideoBodyRequest()
        OpenApiUtilClient.convert(request, segment_video_body_req)
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
        segment_video_body_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_video_body_resp = self.segment_video_body_with_options(segment_video_body_req, runtime)
        return segment_video_body_resp

    async def segment_video_body_advance_async(
        self,
        request: videoseg_20200320_models.SegmentVideoBodyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoseg_20200320_models.SegmentVideoBodyResponse:
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
            product='videoseg',
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
        segment_video_body_req = videoseg_20200320_models.SegmentVideoBodyRequest()
        OpenApiUtilClient.convert(request, segment_video_body_req)
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
        segment_video_body_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        segment_video_body_resp = await self.segment_video_body_with_options_async(segment_video_body_req, runtime)
        return segment_video_body_resp
