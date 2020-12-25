# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_videoenhan20200320 import models as videoenhan_20200320_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_rpc_util.client import Client as RPCUtilClient
from alibabacloud_oss_sdk.client import Client as OSSClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(
        self, 
        config: rpc_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('videoenhan', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def convert_hdr_video(
        self,
        request: videoenhan_20200320_models.ConvertHdrVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ConvertHdrVideoResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.ConvertHdrVideoResponse().from_map(
            self.do_request('ConvertHdrVideo', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def convert_hdr_video_async(
        self,
        request: videoenhan_20200320_models.ConvertHdrVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ConvertHdrVideoResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.ConvertHdrVideoResponse().from_map(
            await self.do_request_async('ConvertHdrVideo', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def convert_hdr_video_simply(
        self,
        request: videoenhan_20200320_models.ConvertHdrVideoRequest,
    ) -> videoenhan_20200320_models.ConvertHdrVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.convert_hdr_video(request, runtime)

    async def convert_hdr_video_simply_async(
        self,
        request: videoenhan_20200320_models.ConvertHdrVideoRequest,
    ) -> videoenhan_20200320_models.ConvertHdrVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.convert_hdr_video_async(request, runtime)

    def convert_hdr_video_advance(
        self,
        request: videoenhan_20200320_models.ConvertHdrVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ConvertHdrVideoResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        convert_hdr_video_req = videoenhan_20200320_models.ConvertHdrVideoRequest()
        RPCUtilClient.convert(request, convert_hdr_video_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_urlobject,
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
        convert_hdr_video_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        convert_hdr_video_resp = self.convert_hdr_video(convert_hdr_video_req, runtime)
        return convert_hdr_video_resp

    async def convert_hdr_video_advance_async(
        self,
        request: videoenhan_20200320_models.ConvertHdrVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ConvertHdrVideoResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        convert_hdr_video_req = videoenhan_20200320_models.ConvertHdrVideoRequest()
        RPCUtilClient.convert(request, convert_hdr_video_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_urlobject,
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
        convert_hdr_video_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        convert_hdr_video_resp = await self.convert_hdr_video_async(convert_hdr_video_req, runtime)
        return convert_hdr_video_resp

    def interpolate_video_frame(
        self,
        request: videoenhan_20200320_models.InterpolateVideoFrameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.InterpolateVideoFrameResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.InterpolateVideoFrameResponse().from_map(
            self.do_request('InterpolateVideoFrame', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def interpolate_video_frame_async(
        self,
        request: videoenhan_20200320_models.InterpolateVideoFrameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.InterpolateVideoFrameResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.InterpolateVideoFrameResponse().from_map(
            await self.do_request_async('InterpolateVideoFrame', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def interpolate_video_frame_simply(
        self,
        request: videoenhan_20200320_models.InterpolateVideoFrameRequest,
    ) -> videoenhan_20200320_models.InterpolateVideoFrameResponse:
        runtime = util_models.RuntimeOptions()
        return self.interpolate_video_frame(request, runtime)

    async def interpolate_video_frame_simply_async(
        self,
        request: videoenhan_20200320_models.InterpolateVideoFrameRequest,
    ) -> videoenhan_20200320_models.InterpolateVideoFrameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.interpolate_video_frame_async(request, runtime)

    def interpolate_video_frame_advance(
        self,
        request: videoenhan_20200320_models.InterpolateVideoFrameAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.InterpolateVideoFrameResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        interpolate_video_frame_req = videoenhan_20200320_models.InterpolateVideoFrameRequest()
        RPCUtilClient.convert(request, interpolate_video_frame_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_urlobject,
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
        interpolate_video_frame_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        interpolate_video_frame_resp = self.interpolate_video_frame(interpolate_video_frame_req, runtime)
        return interpolate_video_frame_resp

    async def interpolate_video_frame_advance_async(
        self,
        request: videoenhan_20200320_models.InterpolateVideoFrameAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.InterpolateVideoFrameResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        interpolate_video_frame_req = videoenhan_20200320_models.InterpolateVideoFrameRequest()
        RPCUtilClient.convert(request, interpolate_video_frame_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_urlobject,
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
        interpolate_video_frame_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        interpolate_video_frame_resp = await self.interpolate_video_frame_async(interpolate_video_frame_req, runtime)
        return interpolate_video_frame_resp

    def tone_sdr_video(
        self,
        request: videoenhan_20200320_models.ToneSdrVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ToneSdrVideoResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.ToneSdrVideoResponse().from_map(
            self.do_request('ToneSdrVideo', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def tone_sdr_video_async(
        self,
        request: videoenhan_20200320_models.ToneSdrVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ToneSdrVideoResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.ToneSdrVideoResponse().from_map(
            await self.do_request_async('ToneSdrVideo', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def tone_sdr_video_simply(
        self,
        request: videoenhan_20200320_models.ToneSdrVideoRequest,
    ) -> videoenhan_20200320_models.ToneSdrVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.tone_sdr_video(request, runtime)

    async def tone_sdr_video_simply_async(
        self,
        request: videoenhan_20200320_models.ToneSdrVideoRequest,
    ) -> videoenhan_20200320_models.ToneSdrVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tone_sdr_video_async(request, runtime)

    def tone_sdr_video_advance(
        self,
        request: videoenhan_20200320_models.ToneSdrVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ToneSdrVideoResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        tone_sdr_video_req = videoenhan_20200320_models.ToneSdrVideoRequest()
        RPCUtilClient.convert(request, tone_sdr_video_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_urlobject,
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
        tone_sdr_video_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        tone_sdr_video_resp = self.tone_sdr_video(tone_sdr_video_req, runtime)
        return tone_sdr_video_resp

    async def tone_sdr_video_advance_async(
        self,
        request: videoenhan_20200320_models.ToneSdrVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ToneSdrVideoResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        tone_sdr_video_req = videoenhan_20200320_models.ToneSdrVideoRequest()
        RPCUtilClient.convert(request, tone_sdr_video_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_urlobject,
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
        tone_sdr_video_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        tone_sdr_video_resp = await self.tone_sdr_video_async(tone_sdr_video_req, runtime)
        return tone_sdr_video_resp

    def enhance_video_quality(
        self,
        request: videoenhan_20200320_models.EnhanceVideoQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EnhanceVideoQualityResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.EnhanceVideoQualityResponse().from_map(
            self.do_request('EnhanceVideoQuality', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def enhance_video_quality_async(
        self,
        request: videoenhan_20200320_models.EnhanceVideoQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EnhanceVideoQualityResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.EnhanceVideoQualityResponse().from_map(
            await self.do_request_async('EnhanceVideoQuality', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def enhance_video_quality_simply(
        self,
        request: videoenhan_20200320_models.EnhanceVideoQualityRequest,
    ) -> videoenhan_20200320_models.EnhanceVideoQualityResponse:
        runtime = util_models.RuntimeOptions()
        return self.enhance_video_quality(request, runtime)

    async def enhance_video_quality_simply_async(
        self,
        request: videoenhan_20200320_models.EnhanceVideoQualityRequest,
    ) -> videoenhan_20200320_models.EnhanceVideoQualityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enhance_video_quality_async(request, runtime)

    def enhance_video_quality_advance(
        self,
        request: videoenhan_20200320_models.EnhanceVideoQualityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EnhanceVideoQualityResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        enhance_video_quality_req = videoenhan_20200320_models.EnhanceVideoQualityRequest()
        RPCUtilClient.convert(request, enhance_video_quality_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_urlobject,
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
        enhance_video_quality_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        enhance_video_quality_resp = self.enhance_video_quality(enhance_video_quality_req, runtime)
        return enhance_video_quality_resp

    async def enhance_video_quality_advance_async(
        self,
        request: videoenhan_20200320_models.EnhanceVideoQualityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EnhanceVideoQualityResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        enhance_video_quality_req = videoenhan_20200320_models.EnhanceVideoQualityRequest()
        RPCUtilClient.convert(request, enhance_video_quality_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_urlobject,
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
        enhance_video_quality_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        enhance_video_quality_resp = await self.enhance_video_quality_async(enhance_video_quality_req, runtime)
        return enhance_video_quality_resp

    def merge_video_face(
        self,
        request: videoenhan_20200320_models.MergeVideoFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoFaceResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.MergeVideoFaceResponse().from_map(
            self.do_request('MergeVideoFace', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def merge_video_face_async(
        self,
        request: videoenhan_20200320_models.MergeVideoFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoFaceResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.MergeVideoFaceResponse().from_map(
            await self.do_request_async('MergeVideoFace', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def merge_video_face_simply(
        self,
        request: videoenhan_20200320_models.MergeVideoFaceRequest,
    ) -> videoenhan_20200320_models.MergeVideoFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.merge_video_face(request, runtime)

    async def merge_video_face_simply_async(
        self,
        request: videoenhan_20200320_models.MergeVideoFaceRequest,
    ) -> videoenhan_20200320_models.MergeVideoFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.merge_video_face_async(request, runtime)

    def merge_video_face_advance(
        self,
        request: videoenhan_20200320_models.MergeVideoFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoFaceResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        merge_video_face_req = videoenhan_20200320_models.MergeVideoFaceRequest()
        RPCUtilClient.convert(request, merge_video_face_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_urlobject,
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
        merge_video_face_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        merge_video_face_resp = self.merge_video_face(merge_video_face_req, runtime)
        return merge_video_face_resp

    async def merge_video_face_advance_async(
        self,
        request: videoenhan_20200320_models.MergeVideoFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.MergeVideoFaceResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        merge_video_face_req = videoenhan_20200320_models.MergeVideoFaceRequest()
        RPCUtilClient.convert(request, merge_video_face_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_urlobject,
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
        merge_video_face_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        merge_video_face_resp = await self.merge_video_face_async(merge_video_face_req, runtime)
        return merge_video_face_resp

    def change_video_size(
        self,
        request: videoenhan_20200320_models.ChangeVideoSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ChangeVideoSizeResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.ChangeVideoSizeResponse().from_map(
            self.do_request('ChangeVideoSize', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def change_video_size_async(
        self,
        request: videoenhan_20200320_models.ChangeVideoSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ChangeVideoSizeResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.ChangeVideoSizeResponse().from_map(
            await self.do_request_async('ChangeVideoSize', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def change_video_size_simply(
        self,
        request: videoenhan_20200320_models.ChangeVideoSizeRequest,
    ) -> videoenhan_20200320_models.ChangeVideoSizeResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_video_size(request, runtime)

    async def change_video_size_simply_async(
        self,
        request: videoenhan_20200320_models.ChangeVideoSizeRequest,
    ) -> videoenhan_20200320_models.ChangeVideoSizeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_video_size_async(request, runtime)

    def change_video_size_advance(
        self,
        request: videoenhan_20200320_models.ChangeVideoSizeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ChangeVideoSizeResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        change_video_size_req = videoenhan_20200320_models.ChangeVideoSizeRequest()
        RPCUtilClient.convert(request, change_video_size_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        change_video_size_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        change_video_size_resp = self.change_video_size(change_video_size_req, runtime)
        return change_video_size_resp

    async def change_video_size_advance_async(
        self,
        request: videoenhan_20200320_models.ChangeVideoSizeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.ChangeVideoSizeResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        change_video_size_req = videoenhan_20200320_models.ChangeVideoSizeRequest()
        RPCUtilClient.convert(request, change_video_size_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        change_video_size_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        change_video_size_resp = await self.change_video_size_async(change_video_size_req, runtime)
        return change_video_size_resp

    def generate_video(
        self,
        request: videoenhan_20200320_models.GenerateVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GenerateVideoResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.GenerateVideoResponse().from_map(
            self.do_request('GenerateVideo', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def generate_video_async(
        self,
        request: videoenhan_20200320_models.GenerateVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GenerateVideoResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.GenerateVideoResponse().from_map(
            await self.do_request_async('GenerateVideo', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def generate_video_simply(
        self,
        request: videoenhan_20200320_models.GenerateVideoRequest,
    ) -> videoenhan_20200320_models.GenerateVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_video(request, runtime)

    async def generate_video_simply_async(
        self,
        request: videoenhan_20200320_models.GenerateVideoRequest,
    ) -> videoenhan_20200320_models.GenerateVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_video_async(request, runtime)

    def get_async_job_result(
        self,
        request: videoenhan_20200320_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.GetAsyncJobResultResponse().from_map(
            self.do_request('GetAsyncJobResult', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_async_job_result_async(
        self,
        request: videoenhan_20200320_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.GetAsyncJobResultResponse().from_map(
            await self.do_request_async('GetAsyncJobResult', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_async_job_result_simply(
        self,
        request: videoenhan_20200320_models.GetAsyncJobResultRequest,
    ) -> videoenhan_20200320_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result(request, runtime)

    async def get_async_job_result_simply_async(
        self,
        request: videoenhan_20200320_models.GetAsyncJobResultRequest,
    ) -> videoenhan_20200320_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_job_result_async(request, runtime)

    def super_resolve_video(
        self,
        request: videoenhan_20200320_models.SuperResolveVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.SuperResolveVideoResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.SuperResolveVideoResponse().from_map(
            self.do_request('SuperResolveVideo', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def super_resolve_video_async(
        self,
        request: videoenhan_20200320_models.SuperResolveVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.SuperResolveVideoResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.SuperResolveVideoResponse().from_map(
            await self.do_request_async('SuperResolveVideo', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def super_resolve_video_simply(
        self,
        request: videoenhan_20200320_models.SuperResolveVideoRequest,
    ) -> videoenhan_20200320_models.SuperResolveVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.super_resolve_video(request, runtime)

    async def super_resolve_video_simply_async(
        self,
        request: videoenhan_20200320_models.SuperResolveVideoRequest,
    ) -> videoenhan_20200320_models.SuperResolveVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.super_resolve_video_async(request, runtime)

    def super_resolve_video_advance(
        self,
        request: videoenhan_20200320_models.SuperResolveVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.SuperResolveVideoResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        super_resolve_video_req = videoenhan_20200320_models.SuperResolveVideoRequest()
        RPCUtilClient.convert(request, super_resolve_video_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        super_resolve_video_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        super_resolve_video_resp = self.super_resolve_video(super_resolve_video_req, runtime)
        return super_resolve_video_resp

    async def super_resolve_video_advance_async(
        self,
        request: videoenhan_20200320_models.SuperResolveVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.SuperResolveVideoResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        super_resolve_video_req = videoenhan_20200320_models.SuperResolveVideoRequest()
        RPCUtilClient.convert(request, super_resolve_video_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        super_resolve_video_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        super_resolve_video_resp = await self.super_resolve_video_async(super_resolve_video_req, runtime)
        return super_resolve_video_resp

    def erase_video_logo(
        self,
        request: videoenhan_20200320_models.EraseVideoLogoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoLogoResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.EraseVideoLogoResponse().from_map(
            self.do_request('EraseVideoLogo', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def erase_video_logo_async(
        self,
        request: videoenhan_20200320_models.EraseVideoLogoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoLogoResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.EraseVideoLogoResponse().from_map(
            await self.do_request_async('EraseVideoLogo', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def erase_video_logo_simply(
        self,
        request: videoenhan_20200320_models.EraseVideoLogoRequest,
    ) -> videoenhan_20200320_models.EraseVideoLogoResponse:
        runtime = util_models.RuntimeOptions()
        return self.erase_video_logo(request, runtime)

    async def erase_video_logo_simply_async(
        self,
        request: videoenhan_20200320_models.EraseVideoLogoRequest,
    ) -> videoenhan_20200320_models.EraseVideoLogoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.erase_video_logo_async(request, runtime)

    def erase_video_logo_advance(
        self,
        request: videoenhan_20200320_models.EraseVideoLogoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoLogoResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        erase_video_logo_req = videoenhan_20200320_models.EraseVideoLogoRequest()
        RPCUtilClient.convert(request, erase_video_logo_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        erase_video_logo_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        erase_video_logo_resp = self.erase_video_logo(erase_video_logo_req, runtime)
        return erase_video_logo_resp

    async def erase_video_logo_advance_async(
        self,
        request: videoenhan_20200320_models.EraseVideoLogoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoLogoResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        erase_video_logo_req = videoenhan_20200320_models.EraseVideoLogoRequest()
        RPCUtilClient.convert(request, erase_video_logo_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        erase_video_logo_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        erase_video_logo_resp = await self.erase_video_logo_async(erase_video_logo_req, runtime)
        return erase_video_logo_resp

    def erase_video_subtitles(
        self,
        request: videoenhan_20200320_models.EraseVideoSubtitlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoSubtitlesResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.EraseVideoSubtitlesResponse().from_map(
            self.do_request('EraseVideoSubtitles', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def erase_video_subtitles_async(
        self,
        request: videoenhan_20200320_models.EraseVideoSubtitlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoSubtitlesResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.EraseVideoSubtitlesResponse().from_map(
            await self.do_request_async('EraseVideoSubtitles', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def erase_video_subtitles_simply(
        self,
        request: videoenhan_20200320_models.EraseVideoSubtitlesRequest,
    ) -> videoenhan_20200320_models.EraseVideoSubtitlesResponse:
        runtime = util_models.RuntimeOptions()
        return self.erase_video_subtitles(request, runtime)

    async def erase_video_subtitles_simply_async(
        self,
        request: videoenhan_20200320_models.EraseVideoSubtitlesRequest,
    ) -> videoenhan_20200320_models.EraseVideoSubtitlesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.erase_video_subtitles_async(request, runtime)

    def erase_video_subtitles_advance(
        self,
        request: videoenhan_20200320_models.EraseVideoSubtitlesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoSubtitlesResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        erase_video_subtitles_req = videoenhan_20200320_models.EraseVideoSubtitlesRequest()
        RPCUtilClient.convert(request, erase_video_subtitles_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        erase_video_subtitles_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        erase_video_subtitles_resp = self.erase_video_subtitles(erase_video_subtitles_req, runtime)
        return erase_video_subtitles_resp

    async def erase_video_subtitles_advance_async(
        self,
        request: videoenhan_20200320_models.EraseVideoSubtitlesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.EraseVideoSubtitlesResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        erase_video_subtitles_req = videoenhan_20200320_models.EraseVideoSubtitlesRequest()
        RPCUtilClient.convert(request, erase_video_subtitles_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        erase_video_subtitles_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        erase_video_subtitles_resp = await self.erase_video_subtitles_async(erase_video_subtitles_req, runtime)
        return erase_video_subtitles_resp

    def abstract_ecommerce_video(
        self,
        request: videoenhan_20200320_models.AbstractEcommerceVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractEcommerceVideoResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.AbstractEcommerceVideoResponse().from_map(
            self.do_request('AbstractEcommerceVideo', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def abstract_ecommerce_video_async(
        self,
        request: videoenhan_20200320_models.AbstractEcommerceVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractEcommerceVideoResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.AbstractEcommerceVideoResponse().from_map(
            await self.do_request_async('AbstractEcommerceVideo', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def abstract_ecommerce_video_simply(
        self,
        request: videoenhan_20200320_models.AbstractEcommerceVideoRequest,
    ) -> videoenhan_20200320_models.AbstractEcommerceVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.abstract_ecommerce_video(request, runtime)

    async def abstract_ecommerce_video_simply_async(
        self,
        request: videoenhan_20200320_models.AbstractEcommerceVideoRequest,
    ) -> videoenhan_20200320_models.AbstractEcommerceVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.abstract_ecommerce_video_async(request, runtime)

    def abstract_ecommerce_video_advance(
        self,
        request: videoenhan_20200320_models.AbstractEcommerceVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractEcommerceVideoResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        abstract_ecommerce_video_req = videoenhan_20200320_models.AbstractEcommerceVideoRequest()
        RPCUtilClient.convert(request, abstract_ecommerce_video_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        abstract_ecommerce_video_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        abstract_ecommerce_video_resp = self.abstract_ecommerce_video(abstract_ecommerce_video_req, runtime)
        return abstract_ecommerce_video_resp

    async def abstract_ecommerce_video_advance_async(
        self,
        request: videoenhan_20200320_models.AbstractEcommerceVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractEcommerceVideoResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        abstract_ecommerce_video_req = videoenhan_20200320_models.AbstractEcommerceVideoRequest()
        RPCUtilClient.convert(request, abstract_ecommerce_video_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        abstract_ecommerce_video_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        abstract_ecommerce_video_resp = await self.abstract_ecommerce_video_async(abstract_ecommerce_video_req, runtime)
        return abstract_ecommerce_video_resp

    def abstract_film_video(
        self,
        request: videoenhan_20200320_models.AbstractFilmVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractFilmVideoResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.AbstractFilmVideoResponse().from_map(
            self.do_request('AbstractFilmVideo', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def abstract_film_video_async(
        self,
        request: videoenhan_20200320_models.AbstractFilmVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractFilmVideoResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.AbstractFilmVideoResponse().from_map(
            await self.do_request_async('AbstractFilmVideo', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def abstract_film_video_simply(
        self,
        request: videoenhan_20200320_models.AbstractFilmVideoRequest,
    ) -> videoenhan_20200320_models.AbstractFilmVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.abstract_film_video(request, runtime)

    async def abstract_film_video_simply_async(
        self,
        request: videoenhan_20200320_models.AbstractFilmVideoRequest,
    ) -> videoenhan_20200320_models.AbstractFilmVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.abstract_film_video_async(request, runtime)

    def abstract_film_video_advance(
        self,
        request: videoenhan_20200320_models.AbstractFilmVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractFilmVideoResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        abstract_film_video_req = videoenhan_20200320_models.AbstractFilmVideoRequest()
        RPCUtilClient.convert(request, abstract_film_video_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        abstract_film_video_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        abstract_film_video_resp = self.abstract_film_video(abstract_film_video_req, runtime)
        return abstract_film_video_resp

    async def abstract_film_video_advance_async(
        self,
        request: videoenhan_20200320_models.AbstractFilmVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AbstractFilmVideoResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        abstract_film_video_req = videoenhan_20200320_models.AbstractFilmVideoRequest()
        RPCUtilClient.convert(request, abstract_film_video_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        abstract_film_video_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        abstract_film_video_resp = await self.abstract_film_video_async(abstract_film_video_req, runtime)
        return abstract_film_video_resp

    def adjust_video_color(
        self,
        request: videoenhan_20200320_models.AdjustVideoColorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AdjustVideoColorResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.AdjustVideoColorResponse().from_map(
            self.do_request('AdjustVideoColor', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def adjust_video_color_async(
        self,
        request: videoenhan_20200320_models.AdjustVideoColorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AdjustVideoColorResponse:
        UtilClient.validate_model(request)
        return videoenhan_20200320_models.AdjustVideoColorResponse().from_map(
            await self.do_request_async('AdjustVideoColor', 'HTTPS', 'POST', '2020-03-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def adjust_video_color_simply(
        self,
        request: videoenhan_20200320_models.AdjustVideoColorRequest,
    ) -> videoenhan_20200320_models.AdjustVideoColorResponse:
        runtime = util_models.RuntimeOptions()
        return self.adjust_video_color(request, runtime)

    async def adjust_video_color_simply_async(
        self,
        request: videoenhan_20200320_models.AdjustVideoColorRequest,
    ) -> videoenhan_20200320_models.AdjustVideoColorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.adjust_video_color_async(request, runtime)

    def adjust_video_color_advance(
        self,
        request: videoenhan_20200320_models.AdjustVideoColorAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AdjustVideoColorResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        adjust_video_color_req = videoenhan_20200320_models.AdjustVideoColorRequest()
        RPCUtilClient.convert(request, adjust_video_color_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        adjust_video_color_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        adjust_video_color_resp = self.adjust_video_color(adjust_video_color_req, runtime)
        return adjust_video_color_resp

    async def adjust_video_color_advance_async(
        self,
        request: videoenhan_20200320_models.AdjustVideoColorAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videoenhan_20200320_models.AdjustVideoColorResponse:
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
        RPCUtilClient.convert(runtime, oss_runtime)
        adjust_video_color_req = videoenhan_20200320_models.AdjustVideoColorRequest()
        RPCUtilClient.convert(request, adjust_video_color_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        adjust_video_color_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        adjust_video_color_resp = await self.adjust_video_color_async(adjust_video_color_req, runtime)
        return adjust_video_color_resp

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
