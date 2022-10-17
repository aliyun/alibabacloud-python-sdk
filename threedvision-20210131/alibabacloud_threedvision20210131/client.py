# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_threedvision20210131 import models as threedvision_20210131_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('threedvision', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def estimate_monocular_image_depth_with_options(
        self,
        request: threedvision_20210131_models.EstimateMonocularImageDepthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.EstimateMonocularImageDepthResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EstimateMonocularImageDepth',
            version='2021-01-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            threedvision_20210131_models.EstimateMonocularImageDepthResponse(),
            self.call_api(params, req, runtime)
        )

    async def estimate_monocular_image_depth_with_options_async(
        self,
        request: threedvision_20210131_models.EstimateMonocularImageDepthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.EstimateMonocularImageDepthResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EstimateMonocularImageDepth',
            version='2021-01-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            threedvision_20210131_models.EstimateMonocularImageDepthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def estimate_monocular_image_depth(
        self,
        request: threedvision_20210131_models.EstimateMonocularImageDepthRequest,
    ) -> threedvision_20210131_models.EstimateMonocularImageDepthResponse:
        runtime = util_models.RuntimeOptions()
        return self.estimate_monocular_image_depth_with_options(request, runtime)

    async def estimate_monocular_image_depth_async(
        self,
        request: threedvision_20210131_models.EstimateMonocularImageDepthRequest,
    ) -> threedvision_20210131_models.EstimateMonocularImageDepthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.estimate_monocular_image_depth_with_options_async(request, runtime)

    def estimate_monocular_image_depth_advance(
        self,
        request: threedvision_20210131_models.EstimateMonocularImageDepthAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.EstimateMonocularImageDepthResponse:
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
            product='threedvision',
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
        estimate_monocular_image_depth_req = threedvision_20210131_models.EstimateMonocularImageDepthRequest()
        OpenApiUtilClient.convert(request, estimate_monocular_image_depth_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            estimate_monocular_image_depth_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        estimate_monocular_image_depth_resp = self.estimate_monocular_image_depth_with_options(estimate_monocular_image_depth_req, runtime)
        return estimate_monocular_image_depth_resp

    async def estimate_monocular_image_depth_advance_async(
        self,
        request: threedvision_20210131_models.EstimateMonocularImageDepthAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.EstimateMonocularImageDepthResponse:
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
            product='threedvision',
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
        estimate_monocular_image_depth_req = threedvision_20210131_models.EstimateMonocularImageDepthRequest()
        OpenApiUtilClient.convert(request, estimate_monocular_image_depth_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            estimate_monocular_image_depth_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        estimate_monocular_image_depth_resp = await self.estimate_monocular_image_depth_with_options_async(estimate_monocular_image_depth_req, runtime)
        return estimate_monocular_image_depth_resp

    def estimate_monocular_video_depth_with_options(
        self,
        request: threedvision_20210131_models.EstimateMonocularVideoDepthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.EstimateMonocularVideoDepthResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EstimateMonocularVideoDepth',
            version='2021-01-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            threedvision_20210131_models.EstimateMonocularVideoDepthResponse(),
            self.call_api(params, req, runtime)
        )

    async def estimate_monocular_video_depth_with_options_async(
        self,
        request: threedvision_20210131_models.EstimateMonocularVideoDepthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.EstimateMonocularVideoDepthResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.video_url):
            body['VideoURL'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EstimateMonocularVideoDepth',
            version='2021-01-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            threedvision_20210131_models.EstimateMonocularVideoDepthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def estimate_monocular_video_depth(
        self,
        request: threedvision_20210131_models.EstimateMonocularVideoDepthRequest,
    ) -> threedvision_20210131_models.EstimateMonocularVideoDepthResponse:
        runtime = util_models.RuntimeOptions()
        return self.estimate_monocular_video_depth_with_options(request, runtime)

    async def estimate_monocular_video_depth_async(
        self,
        request: threedvision_20210131_models.EstimateMonocularVideoDepthRequest,
    ) -> threedvision_20210131_models.EstimateMonocularVideoDepthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.estimate_monocular_video_depth_with_options_async(request, runtime)

    def estimate_monocular_video_depth_advance(
        self,
        request: threedvision_20210131_models.EstimateMonocularVideoDepthAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.EstimateMonocularVideoDepthResponse:
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
            product='threedvision',
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
        estimate_monocular_video_depth_req = threedvision_20210131_models.EstimateMonocularVideoDepthRequest()
        OpenApiUtilClient.convert(request, estimate_monocular_video_depth_req)
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
            estimate_monocular_video_depth_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        estimate_monocular_video_depth_resp = self.estimate_monocular_video_depth_with_options(estimate_monocular_video_depth_req, runtime)
        return estimate_monocular_video_depth_resp

    async def estimate_monocular_video_depth_advance_async(
        self,
        request: threedvision_20210131_models.EstimateMonocularVideoDepthAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.EstimateMonocularVideoDepthResponse:
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
            product='threedvision',
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
        estimate_monocular_video_depth_req = threedvision_20210131_models.EstimateMonocularVideoDepthRequest()
        OpenApiUtilClient.convert(request, estimate_monocular_video_depth_req)
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
            estimate_monocular_video_depth_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        estimate_monocular_video_depth_resp = await self.estimate_monocular_video_depth_with_options_async(estimate_monocular_video_depth_req, runtime)
        return estimate_monocular_video_depth_resp

    def estimate_stereo_image_depth_with_options(
        self,
        request: threedvision_20210131_models.EstimateStereoImageDepthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.EstimateStereoImageDepthResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.left_image_url):
            body['LeftImageURL'] = request.left_image_url
        if not UtilClient.is_unset(request.right_image_url):
            body['RightImageURL'] = request.right_image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EstimateStereoImageDepth',
            version='2021-01-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            threedvision_20210131_models.EstimateStereoImageDepthResponse(),
            self.call_api(params, req, runtime)
        )

    async def estimate_stereo_image_depth_with_options_async(
        self,
        request: threedvision_20210131_models.EstimateStereoImageDepthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.EstimateStereoImageDepthResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.left_image_url):
            body['LeftImageURL'] = request.left_image_url
        if not UtilClient.is_unset(request.right_image_url):
            body['RightImageURL'] = request.right_image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EstimateStereoImageDepth',
            version='2021-01-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            threedvision_20210131_models.EstimateStereoImageDepthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def estimate_stereo_image_depth(
        self,
        request: threedvision_20210131_models.EstimateStereoImageDepthRequest,
    ) -> threedvision_20210131_models.EstimateStereoImageDepthResponse:
        runtime = util_models.RuntimeOptions()
        return self.estimate_stereo_image_depth_with_options(request, runtime)

    async def estimate_stereo_image_depth_async(
        self,
        request: threedvision_20210131_models.EstimateStereoImageDepthRequest,
    ) -> threedvision_20210131_models.EstimateStereoImageDepthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.estimate_stereo_image_depth_with_options_async(request, runtime)

    def get_async_job_result_with_options(
        self,
        request: threedvision_20210131_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAsyncJobResult',
            version='2021-01-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            threedvision_20210131_models.GetAsyncJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_job_result_with_options_async(
        self,
        request: threedvision_20210131_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAsyncJobResult',
            version='2021-01-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            threedvision_20210131_models.GetAsyncJobResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_job_result(
        self,
        request: threedvision_20210131_models.GetAsyncJobResultRequest,
    ) -> threedvision_20210131_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result_with_options(request, runtime)

    async def get_async_job_result_async(
        self,
        request: threedvision_20210131_models.GetAsyncJobResultRequest,
    ) -> threedvision_20210131_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_job_result_with_options_async(request, runtime)

    def reconstruct_body_by_single_image_with_options(
        self,
        request: threedvision_20210131_models.ReconstructBodyBySingleImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.ReconstructBodyBySingleImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReconstructBodyBySingleImage',
            version='2021-01-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            threedvision_20210131_models.ReconstructBodyBySingleImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def reconstruct_body_by_single_image_with_options_async(
        self,
        request: threedvision_20210131_models.ReconstructBodyBySingleImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.ReconstructBodyBySingleImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReconstructBodyBySingleImage',
            version='2021-01-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            threedvision_20210131_models.ReconstructBodyBySingleImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reconstruct_body_by_single_image(
        self,
        request: threedvision_20210131_models.ReconstructBodyBySingleImageRequest,
    ) -> threedvision_20210131_models.ReconstructBodyBySingleImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.reconstruct_body_by_single_image_with_options(request, runtime)

    async def reconstruct_body_by_single_image_async(
        self,
        request: threedvision_20210131_models.ReconstructBodyBySingleImageRequest,
    ) -> threedvision_20210131_models.ReconstructBodyBySingleImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reconstruct_body_by_single_image_with_options_async(request, runtime)

    def reconstruct_body_by_single_image_advance(
        self,
        request: threedvision_20210131_models.ReconstructBodyBySingleImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.ReconstructBodyBySingleImageResponse:
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
            product='threedvision',
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
        reconstruct_body_by_single_image_req = threedvision_20210131_models.ReconstructBodyBySingleImageRequest()
        OpenApiUtilClient.convert(request, reconstruct_body_by_single_image_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            reconstruct_body_by_single_image_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        reconstruct_body_by_single_image_resp = self.reconstruct_body_by_single_image_with_options(reconstruct_body_by_single_image_req, runtime)
        return reconstruct_body_by_single_image_resp

    async def reconstruct_body_by_single_image_advance_async(
        self,
        request: threedvision_20210131_models.ReconstructBodyBySingleImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.ReconstructBodyBySingleImageResponse:
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
            product='threedvision',
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
        reconstruct_body_by_single_image_req = threedvision_20210131_models.ReconstructBodyBySingleImageRequest()
        OpenApiUtilClient.convert(request, reconstruct_body_by_single_image_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            reconstruct_body_by_single_image_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        reconstruct_body_by_single_image_resp = await self.reconstruct_body_by_single_image_with_options_async(reconstruct_body_by_single_image_req, runtime)
        return reconstruct_body_by_single_image_resp

    def reconstruct_three_dmulti_view_with_options(
        self,
        request: threedvision_20210131_models.ReconstructThreeDMultiViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.ReconstructThreeDMultiViewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.zip_file_url):
            body['ZipFileUrl'] = request.zip_file_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReconstructThreeDMultiView',
            version='2021-01-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            threedvision_20210131_models.ReconstructThreeDMultiViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def reconstruct_three_dmulti_view_with_options_async(
        self,
        request: threedvision_20210131_models.ReconstructThreeDMultiViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.ReconstructThreeDMultiViewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.zip_file_url):
            body['ZipFileUrl'] = request.zip_file_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReconstructThreeDMultiView',
            version='2021-01-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            threedvision_20210131_models.ReconstructThreeDMultiViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reconstruct_three_dmulti_view(
        self,
        request: threedvision_20210131_models.ReconstructThreeDMultiViewRequest,
    ) -> threedvision_20210131_models.ReconstructThreeDMultiViewResponse:
        runtime = util_models.RuntimeOptions()
        return self.reconstruct_three_dmulti_view_with_options(request, runtime)

    async def reconstruct_three_dmulti_view_async(
        self,
        request: threedvision_20210131_models.ReconstructThreeDMultiViewRequest,
    ) -> threedvision_20210131_models.ReconstructThreeDMultiViewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reconstruct_three_dmulti_view_with_options_async(request, runtime)

    def reconstruct_three_dmulti_view_advance(
        self,
        request: threedvision_20210131_models.ReconstructThreeDMultiViewAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.ReconstructThreeDMultiViewResponse:
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
            product='threedvision',
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
        reconstruct_three_dmulti_view_req = threedvision_20210131_models.ReconstructThreeDMultiViewRequest()
        OpenApiUtilClient.convert(request, reconstruct_three_dmulti_view_req)
        if not UtilClient.is_unset(request.zip_file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.zip_file_url_object,
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
            reconstruct_three_dmulti_view_req.zip_file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        reconstruct_three_dmulti_view_resp = self.reconstruct_three_dmulti_view_with_options(reconstruct_three_dmulti_view_req, runtime)
        return reconstruct_three_dmulti_view_resp

    async def reconstruct_three_dmulti_view_advance_async(
        self,
        request: threedvision_20210131_models.ReconstructThreeDMultiViewAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> threedvision_20210131_models.ReconstructThreeDMultiViewResponse:
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
            product='threedvision',
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
        reconstruct_three_dmulti_view_req = threedvision_20210131_models.ReconstructThreeDMultiViewRequest()
        OpenApiUtilClient.convert(request, reconstruct_three_dmulti_view_req)
        if not UtilClient.is_unset(request.zip_file_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.zip_file_url_object,
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
            reconstruct_three_dmulti_view_req.zip_file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        reconstruct_three_dmulti_view_resp = await self.reconstruct_three_dmulti_view_with_options_async(reconstruct_three_dmulti_view_req, runtime)
        return reconstruct_three_dmulti_view_resp
