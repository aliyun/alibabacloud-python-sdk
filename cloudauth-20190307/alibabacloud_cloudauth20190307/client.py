# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_cloudauth20190307 import models as cloudauth_20190307_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudauth', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def compare_face_verify(
        self,
        request: cloudauth_20190307_models.CompareFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CompareFaceVerifyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFaceVerifyResponse(),
            self.do_request('CompareFaceVerify', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def compare_face_verify_async(
        self,
        request: cloudauth_20190307_models.CompareFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CompareFaceVerifyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFaceVerifyResponse(),
            await self.do_request_async('CompareFaceVerify', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def compare_face_verify_simply(
        self,
        request: cloudauth_20190307_models.CompareFaceVerifyRequest,
    ) -> cloudauth_20190307_models.CompareFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.compare_face_verify(request, runtime)

    async def compare_face_verify_simply_async(
        self,
        request: cloudauth_20190307_models.CompareFaceVerifyRequest,
    ) -> cloudauth_20190307_models.CompareFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.compare_face_verify_async(request, runtime)

    def compare_faces(
        self,
        request: cloudauth_20190307_models.CompareFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CompareFacesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFacesResponse(),
            self.do_request('CompareFaces', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def compare_faces_async(
        self,
        request: cloudauth_20190307_models.CompareFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CompareFacesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFacesResponse(),
            await self.do_request_async('CompareFaces', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def compare_faces_simply(
        self,
        request: cloudauth_20190307_models.CompareFacesRequest,
    ) -> cloudauth_20190307_models.CompareFacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.compare_faces(request, runtime)

    async def compare_faces_simply_async(
        self,
        request: cloudauth_20190307_models.CompareFacesRequest,
    ) -> cloudauth_20190307_models.CompareFacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.compare_faces_async(request, runtime)

    def contrast_face_verify(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.ContrastFaceVerifyResponse(),
            self.do_request('ContrastFaceVerify', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def contrast_face_verify_async(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.ContrastFaceVerifyResponse(),
            await self.do_request_async('ContrastFaceVerify', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def contrast_face_verify_simply(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyRequest,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.contrast_face_verify(request, runtime)

    async def contrast_face_verify_simply_async(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyRequest,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.contrast_face_verify_async(request, runtime)

    def contrast_face_verify_advance(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        open_platform_endpoint = self._open_platform_endpoint
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
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
        RPCUtilClient.convert(runtime, oss_runtime)
        contrast_face_verify_req = cloudauth_20190307_models.ContrastFaceVerifyRequest()
        RPCUtilClient.convert(request, contrast_face_verify_req)
        if not UtilClient.is_unset(request.face_contrast_file_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.face_contrast_file_object,
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
            contrast_face_verify_req.face_contrast_file = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        contrast_face_verify_resp = self.contrast_face_verify(contrast_face_verify_req, runtime)
        return contrast_face_verify_resp

    async def contrast_face_verify_advance_async(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        open_platform_endpoint = self._open_platform_endpoint
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
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
        RPCUtilClient.convert(runtime, oss_runtime)
        contrast_face_verify_req = cloudauth_20190307_models.ContrastFaceVerifyRequest()
        RPCUtilClient.convert(request, contrast_face_verify_req)
        if not UtilClient.is_unset(request.face_contrast_file_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.face_contrast_file_object,
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
            contrast_face_verify_req.face_contrast_file = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        contrast_face_verify_resp = await self.contrast_face_verify_async(contrast_face_verify_req, runtime)
        return contrast_face_verify_resp

    def create_auth_key(
        self,
        request: cloudauth_20190307_models.CreateAuthKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateAuthKeyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateAuthKeyResponse(),
            self.do_request('CreateAuthKey', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_auth_key_async(
        self,
        request: cloudauth_20190307_models.CreateAuthKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateAuthKeyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateAuthKeyResponse(),
            await self.do_request_async('CreateAuthKey', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_auth_key_simply(
        self,
        request: cloudauth_20190307_models.CreateAuthKeyRequest,
    ) -> cloudauth_20190307_models.CreateAuthKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_auth_key(request, runtime)

    async def create_auth_key_simply_async(
        self,
        request: cloudauth_20190307_models.CreateAuthKeyRequest,
    ) -> cloudauth_20190307_models.CreateAuthKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_auth_key_async(request, runtime)

    def create_verify_setting(
        self,
        request: cloudauth_20190307_models.CreateVerifySettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateVerifySettingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateVerifySettingResponse(),
            self.do_request('CreateVerifySetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_verify_setting_async(
        self,
        request: cloudauth_20190307_models.CreateVerifySettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateVerifySettingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateVerifySettingResponse(),
            await self.do_request_async('CreateVerifySetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_verify_setting_simply(
        self,
        request: cloudauth_20190307_models.CreateVerifySettingRequest,
    ) -> cloudauth_20190307_models.CreateVerifySettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_verify_setting(request, runtime)

    async def create_verify_setting_simply_async(
        self,
        request: cloudauth_20190307_models.CreateVerifySettingRequest,
    ) -> cloudauth_20190307_models.CreateVerifySettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_verify_setting_async(request, runtime)

    def describe_device_info(
        self,
        request: cloudauth_20190307_models.DescribeDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeDeviceInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeDeviceInfoResponse(),
            self.do_request('DescribeDeviceInfo', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_device_info_async(
        self,
        request: cloudauth_20190307_models.DescribeDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeDeviceInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeDeviceInfoResponse(),
            await self.do_request_async('DescribeDeviceInfo', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_device_info_simply(
        self,
        request: cloudauth_20190307_models.DescribeDeviceInfoRequest,
    ) -> cloudauth_20190307_models.DescribeDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_device_info(request, runtime)

    async def describe_device_info_simply_async(
        self,
        request: cloudauth_20190307_models.DescribeDeviceInfoRequest,
    ) -> cloudauth_20190307_models.DescribeDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_info_async(request, runtime)

    def describe_face_verify(
        self,
        request: cloudauth_20190307_models.DescribeFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceVerifyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceVerifyResponse(),
            self.do_request('DescribeFaceVerify', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_face_verify_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceVerifyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceVerifyResponse(),
            await self.do_request_async('DescribeFaceVerify', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_face_verify_simply(
        self,
        request: cloudauth_20190307_models.DescribeFaceVerifyRequest,
    ) -> cloudauth_20190307_models.DescribeFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_face_verify(request, runtime)

    async def describe_face_verify_simply_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceVerifyRequest,
    ) -> cloudauth_20190307_models.DescribeFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_face_verify_async(request, runtime)

    def describe_oss_upload_token(
        self,
        request: cloudauth_20190307_models.DescribeOssUploadTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeOssUploadTokenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeOssUploadTokenResponse(),
            self.do_request('DescribeOssUploadToken', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_oss_upload_token_async(
        self,
        request: cloudauth_20190307_models.DescribeOssUploadTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeOssUploadTokenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeOssUploadTokenResponse(),
            await self.do_request_async('DescribeOssUploadToken', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_oss_upload_token_simply(
        self,
        request: cloudauth_20190307_models.DescribeOssUploadTokenRequest,
    ) -> cloudauth_20190307_models.DescribeOssUploadTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_upload_token(request, runtime)

    async def describe_oss_upload_token_simply_async(
        self,
        request: cloudauth_20190307_models.DescribeOssUploadTokenRequest,
    ) -> cloudauth_20190307_models.DescribeOssUploadTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_upload_token_async(request, runtime)

    def describe_verify_result(
        self,
        request: cloudauth_20190307_models.DescribeVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyResultResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyResultResponse(),
            self.do_request('DescribeVerifyResult', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_verify_result_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyResultResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyResultResponse(),
            await self.do_request_async('DescribeVerifyResult', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_verify_result_simply(
        self,
        request: cloudauth_20190307_models.DescribeVerifyResultRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_result(request, runtime)

    async def describe_verify_result_simply_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyResultRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_result_async(request, runtime)

    def describe_verify_sdk(
        self,
        request: cloudauth_20190307_models.DescribeVerifySDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifySDKResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifySDKResponse(),
            self.do_request('DescribeVerifySDK', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_verify_sdk_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifySDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifySDKResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifySDKResponse(),
            await self.do_request_async('DescribeVerifySDK', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_verify_sdksimply(
        self,
        request: cloudauth_20190307_models.DescribeVerifySDKRequest,
    ) -> cloudauth_20190307_models.DescribeVerifySDKResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_sdk(request, runtime)

    async def describe_verify_sdksimply_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifySDKRequest,
    ) -> cloudauth_20190307_models.DescribeVerifySDKResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_sdk_async(request, runtime)

    def describe_verify_token(
        self,
        request: cloudauth_20190307_models.DescribeVerifyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyTokenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyTokenResponse(),
            self.do_request('DescribeVerifyToken', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_verify_token_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyTokenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyTokenResponse(),
            await self.do_request_async('DescribeVerifyToken', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_verify_token_simply(
        self,
        request: cloudauth_20190307_models.DescribeVerifyTokenRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_token(request, runtime)

    async def describe_verify_token_simply_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyTokenRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_token_async(request, runtime)

    def detect_face_attributes(
        self,
        request: cloudauth_20190307_models.DetectFaceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DetectFaceAttributesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DetectFaceAttributesResponse(),
            self.do_request('DetectFaceAttributes', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def detect_face_attributes_async(
        self,
        request: cloudauth_20190307_models.DetectFaceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DetectFaceAttributesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DetectFaceAttributesResponse(),
            await self.do_request_async('DetectFaceAttributes', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def detect_face_attributes_simply(
        self,
        request: cloudauth_20190307_models.DetectFaceAttributesRequest,
    ) -> cloudauth_20190307_models.DetectFaceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_face_attributes(request, runtime)

    async def detect_face_attributes_simply_async(
        self,
        request: cloudauth_20190307_models.DetectFaceAttributesRequest,
    ) -> cloudauth_20190307_models.DetectFaceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_face_attributes_async(request, runtime)

    def init_face_verify(
        self,
        request: cloudauth_20190307_models.InitFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.InitFaceVerifyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.InitFaceVerifyResponse(),
            self.do_request('InitFaceVerify', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def init_face_verify_async(
        self,
        request: cloudauth_20190307_models.InitFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.InitFaceVerifyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.InitFaceVerifyResponse(),
            await self.do_request_async('InitFaceVerify', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def init_face_verify_simply(
        self,
        request: cloudauth_20190307_models.InitFaceVerifyRequest,
    ) -> cloudauth_20190307_models.InitFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_face_verify(request, runtime)

    async def init_face_verify_simply_async(
        self,
        request: cloudauth_20190307_models.InitFaceVerifyRequest,
    ) -> cloudauth_20190307_models.InitFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_face_verify_async(request, runtime)

    def liveness_face_verify(
        self,
        request: cloudauth_20190307_models.LivenessFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.LivenessFaceVerifyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.LivenessFaceVerifyResponse(),
            self.do_request('LivenessFaceVerify', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def liveness_face_verify_async(
        self,
        request: cloudauth_20190307_models.LivenessFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.LivenessFaceVerifyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.LivenessFaceVerifyResponse(),
            await self.do_request_async('LivenessFaceVerify', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def liveness_face_verify_simply(
        self,
        request: cloudauth_20190307_models.LivenessFaceVerifyRequest,
    ) -> cloudauth_20190307_models.LivenessFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.liveness_face_verify(request, runtime)

    async def liveness_face_verify_simply_async(
        self,
        request: cloudauth_20190307_models.LivenessFaceVerifyRequest,
    ) -> cloudauth_20190307_models.LivenessFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.liveness_face_verify_async(request, runtime)

    def modify_device_info(
        self,
        request: cloudauth_20190307_models.ModifyDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ModifyDeviceInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.ModifyDeviceInfoResponse(),
            self.do_request('ModifyDeviceInfo', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def modify_device_info_async(
        self,
        request: cloudauth_20190307_models.ModifyDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ModifyDeviceInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.ModifyDeviceInfoResponse(),
            await self.do_request_async('ModifyDeviceInfo', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def modify_device_info_simply(
        self,
        request: cloudauth_20190307_models.ModifyDeviceInfoRequest,
    ) -> cloudauth_20190307_models.ModifyDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_device_info(request, runtime)

    async def modify_device_info_simply_async(
        self,
        request: cloudauth_20190307_models.ModifyDeviceInfoRequest,
    ) -> cloudauth_20190307_models.ModifyDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_device_info_async(request, runtime)

    def verify_material(
        self,
        request: cloudauth_20190307_models.VerifyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VerifyMaterialResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.VerifyMaterialResponse(),
            self.do_request('VerifyMaterial', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def verify_material_async(
        self,
        request: cloudauth_20190307_models.VerifyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VerifyMaterialResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.VerifyMaterialResponse(),
            await self.do_request_async('VerifyMaterial', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def verify_material_simply(
        self,
        request: cloudauth_20190307_models.VerifyMaterialRequest,
    ) -> cloudauth_20190307_models.VerifyMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_material(request, runtime)

    async def verify_material_simply_async(
        self,
        request: cloudauth_20190307_models.VerifyMaterialRequest,
    ) -> cloudauth_20190307_models.VerifyMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_material_async(request, runtime)

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
