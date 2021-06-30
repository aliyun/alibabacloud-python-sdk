# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudauth20201112 import models as cloudauth_20201112_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudauth', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def compare_faces_with_options(
        self,
        request: cloudauth_20201112_models.CompareFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20201112_models.CompareFacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20201112_models.CompareFacesResponse(),
            self.do_rpcrequest('CompareFaces', '2020-11-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def compare_faces_with_options_async(
        self,
        request: cloudauth_20201112_models.CompareFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20201112_models.CompareFacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20201112_models.CompareFacesResponse(),
            await self.do_rpcrequest_async('CompareFaces', '2020-11-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def compare_faces(
        self,
        request: cloudauth_20201112_models.CompareFacesRequest,
    ) -> cloudauth_20201112_models.CompareFacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.compare_faces_with_options(request, runtime)

    async def compare_faces_async(
        self,
        request: cloudauth_20201112_models.CompareFacesRequest,
    ) -> cloudauth_20201112_models.CompareFacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.compare_faces_with_options_async(request, runtime)

    def describe_verify_result_with_options(
        self,
        request: cloudauth_20201112_models.DescribeVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20201112_models.DescribeVerifyResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20201112_models.DescribeVerifyResultResponse(),
            self.do_rpcrequest('DescribeVerifyResult', '2020-11-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_verify_result_with_options_async(
        self,
        request: cloudauth_20201112_models.DescribeVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20201112_models.DescribeVerifyResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20201112_models.DescribeVerifyResultResponse(),
            await self.do_rpcrequest_async('DescribeVerifyResult', '2020-11-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_verify_result(
        self,
        request: cloudauth_20201112_models.DescribeVerifyResultRequest,
    ) -> cloudauth_20201112_models.DescribeVerifyResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_result_with_options(request, runtime)

    async def describe_verify_result_async(
        self,
        request: cloudauth_20201112_models.DescribeVerifyResultRequest,
    ) -> cloudauth_20201112_models.DescribeVerifyResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_result_with_options_async(request, runtime)

    def describe_verify_token_with_options(
        self,
        request: cloudauth_20201112_models.DescribeVerifyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20201112_models.DescribeVerifyTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20201112_models.DescribeVerifyTokenResponse(),
            self.do_rpcrequest('DescribeVerifyToken', '2020-11-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_verify_token_with_options_async(
        self,
        request: cloudauth_20201112_models.DescribeVerifyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20201112_models.DescribeVerifyTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20201112_models.DescribeVerifyTokenResponse(),
            await self.do_rpcrequest_async('DescribeVerifyToken', '2020-11-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_verify_token(
        self,
        request: cloudauth_20201112_models.DescribeVerifyTokenRequest,
    ) -> cloudauth_20201112_models.DescribeVerifyTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_token_with_options(request, runtime)

    async def describe_verify_token_async(
        self,
        request: cloudauth_20201112_models.DescribeVerifyTokenRequest,
    ) -> cloudauth_20201112_models.DescribeVerifyTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_token_with_options_async(request, runtime)

    def detect_face_attributes_with_options(
        self,
        request: cloudauth_20201112_models.DetectFaceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20201112_models.DetectFaceAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20201112_models.DetectFaceAttributesResponse(),
            self.do_rpcrequest('DetectFaceAttributes', '2020-11-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_face_attributes_with_options_async(
        self,
        request: cloudauth_20201112_models.DetectFaceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20201112_models.DetectFaceAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20201112_models.DetectFaceAttributesResponse(),
            await self.do_rpcrequest_async('DetectFaceAttributes', '2020-11-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_face_attributes(
        self,
        request: cloudauth_20201112_models.DetectFaceAttributesRequest,
    ) -> cloudauth_20201112_models.DetectFaceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_face_attributes_with_options(request, runtime)

    async def detect_face_attributes_async(
        self,
        request: cloudauth_20201112_models.DetectFaceAttributesRequest,
    ) -> cloudauth_20201112_models.DetectFaceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_face_attributes_with_options_async(request, runtime)

    def detect_face_attributes_advance(
        self,
        request: cloudauth_20201112_models.DetectFaceAttributesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20201112_models.DetectFaceAttributesResponse:
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
        auth_config = rpc_models.Config(
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
            product='Cloudauth',
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
        detect_face_attributes_req = cloudauth_20201112_models.DetectFaceAttributesRequest()
        OpenApiUtilClient.convert(request, detect_face_attributes_req)
        if not UtilClient.is_unset(request.image_file_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_file_object,
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
            detect_face_attributes_req.image_file = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_face_attributes_resp = self.detect_face_attributes_with_options(detect_face_attributes_req, runtime)
        return detect_face_attributes_resp

    async def detect_face_attributes_advance_async(
        self,
        request: cloudauth_20201112_models.DetectFaceAttributesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20201112_models.DetectFaceAttributesResponse:
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
        auth_config = rpc_models.Config(
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
            product='Cloudauth',
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
        detect_face_attributes_req = cloudauth_20201112_models.DetectFaceAttributesRequest()
        OpenApiUtilClient.convert(request, detect_face_attributes_req)
        if not UtilClient.is_unset(request.image_file_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_file_object,
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
            detect_face_attributes_req.image_file = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_face_attributes_resp = await self.detect_face_attributes_with_options_async(detect_face_attributes_req, runtime)
        return detect_face_attributes_resp

    def liveness_detect_with_options(
        self,
        request: cloudauth_20201112_models.LivenessDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20201112_models.LivenessDetectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20201112_models.LivenessDetectResponse(),
            self.do_rpcrequest('LivenessDetect', '2020-11-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def liveness_detect_with_options_async(
        self,
        request: cloudauth_20201112_models.LivenessDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20201112_models.LivenessDetectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20201112_models.LivenessDetectResponse(),
            await self.do_rpcrequest_async('LivenessDetect', '2020-11-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def liveness_detect(
        self,
        request: cloudauth_20201112_models.LivenessDetectRequest,
    ) -> cloudauth_20201112_models.LivenessDetectResponse:
        runtime = util_models.RuntimeOptions()
        return self.liveness_detect_with_options(request, runtime)

    async def liveness_detect_async(
        self,
        request: cloudauth_20201112_models.LivenessDetectRequest,
    ) -> cloudauth_20201112_models.LivenessDetectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.liveness_detect_with_options_async(request, runtime)

    def liveness_detect_advance(
        self,
        request: cloudauth_20201112_models.LivenessDetectAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20201112_models.LivenessDetectResponse:
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
        auth_config = rpc_models.Config(
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
            product='Cloudauth',
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
        liveness_detect_req = cloudauth_20201112_models.LivenessDetectRequest()
        OpenApiUtilClient.convert(request, liveness_detect_req)
        if not UtilClient.is_unset(request.media_file_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.media_file_object,
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
            liveness_detect_req.media_file = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        liveness_detect_resp = self.liveness_detect_with_options(liveness_detect_req, runtime)
        return liveness_detect_resp

    async def liveness_detect_advance_async(
        self,
        request: cloudauth_20201112_models.LivenessDetectAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20201112_models.LivenessDetectResponse:
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
        auth_config = rpc_models.Config(
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
            product='Cloudauth',
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
        liveness_detect_req = cloudauth_20201112_models.LivenessDetectRequest()
        OpenApiUtilClient.convert(request, liveness_detect_req)
        if not UtilClient.is_unset(request.media_file_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.media_file_object,
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
            liveness_detect_req.media_file = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        liveness_detect_resp = await self.liveness_detect_with_options_async(liveness_detect_req, runtime)
        return liveness_detect_resp

    def verify_material_with_options(
        self,
        request: cloudauth_20201112_models.VerifyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20201112_models.VerifyMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20201112_models.VerifyMaterialResponse(),
            self.do_rpcrequest('VerifyMaterial', '2020-11-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_material_with_options_async(
        self,
        request: cloudauth_20201112_models.VerifyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20201112_models.VerifyMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20201112_models.VerifyMaterialResponse(),
            await self.do_rpcrequest_async('VerifyMaterial', '2020-11-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_material(
        self,
        request: cloudauth_20201112_models.VerifyMaterialRequest,
    ) -> cloudauth_20201112_models.VerifyMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_material_with_options(request, runtime)

    async def verify_material_async(
        self,
        request: cloudauth_20201112_models.VerifyMaterialRequest,
    ) -> cloudauth_20201112_models.VerifyMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_material_with_options_async(request, runtime)
