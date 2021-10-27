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

    def create_face_config(
        self,
        request: cloudauth_20190307_models.CreateFaceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateFaceConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateFaceConfigResponse(),
            self.do_request('CreateFaceConfig', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_face_config_async(
        self,
        request: cloudauth_20190307_models.CreateFaceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateFaceConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateFaceConfigResponse(),
            await self.do_request_async('CreateFaceConfig', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_face_config_simply(
        self,
        request: cloudauth_20190307_models.CreateFaceConfigRequest,
    ) -> cloudauth_20190307_models.CreateFaceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_face_config(request, runtime)

    async def create_face_config_simply_async(
        self,
        request: cloudauth_20190307_models.CreateFaceConfigRequest,
    ) -> cloudauth_20190307_models.CreateFaceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_face_config_async(request, runtime)

    def create_rpsdk(
        self,
        request: cloudauth_20190307_models.CreateRPSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateRPSDKResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateRPSDKResponse(),
            self.do_request('CreateRPSDK', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_rpsdk_async(
        self,
        request: cloudauth_20190307_models.CreateRPSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateRPSDKResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateRPSDKResponse(),
            await self.do_request_async('CreateRPSDK', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_rpsdksimply(
        self,
        request: cloudauth_20190307_models.CreateRPSDKRequest,
    ) -> cloudauth_20190307_models.CreateRPSDKResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rpsdk(request, runtime)

    async def create_rpsdksimply_async(
        self,
        request: cloudauth_20190307_models.CreateRPSDKRequest,
    ) -> cloudauth_20190307_models.CreateRPSDKResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rpsdk_async(request, runtime)

    def create_verify_sdk(
        self,
        request: cloudauth_20190307_models.CreateVerifySDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateVerifySDKResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateVerifySDKResponse(),
            self.do_request('CreateVerifySDK', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_verify_sdk_async(
        self,
        request: cloudauth_20190307_models.CreateVerifySDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateVerifySDKResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateVerifySDKResponse(),
            await self.do_request_async('CreateVerifySDK', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_verify_sdksimply(
        self,
        request: cloudauth_20190307_models.CreateVerifySDKRequest,
    ) -> cloudauth_20190307_models.CreateVerifySDKResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_verify_sdk(request, runtime)

    async def create_verify_sdksimply_async(
        self,
        request: cloudauth_20190307_models.CreateVerifySDKRequest,
    ) -> cloudauth_20190307_models.CreateVerifySDKResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_verify_sdk_async(request, runtime)

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

    def create_whitelist(
        self,
        request: cloudauth_20190307_models.CreateWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateWhitelistResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateWhitelistResponse(),
            self.do_request('CreateWhitelist', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_whitelist_async(
        self,
        request: cloudauth_20190307_models.CreateWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateWhitelistResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateWhitelistResponse(),
            await self.do_request_async('CreateWhitelist', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_whitelist_simply(
        self,
        request: cloudauth_20190307_models.CreateWhitelistRequest,
    ) -> cloudauth_20190307_models.CreateWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_whitelist(request, runtime)

    async def create_whitelist_simply_async(
        self,
        request: cloudauth_20190307_models.CreateWhitelistRequest,
    ) -> cloudauth_20190307_models.CreateWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_whitelist_async(request, runtime)

    def create_whitelist_setting(
        self,
        request: cloudauth_20190307_models.CreateWhitelistSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateWhitelistSettingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateWhitelistSettingResponse(),
            self.do_request('CreateWhitelistSetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_whitelist_setting_async(
        self,
        request: cloudauth_20190307_models.CreateWhitelistSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateWhitelistSettingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateWhitelistSettingResponse(),
            await self.do_request_async('CreateWhitelistSetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_whitelist_setting_simply(
        self,
        request: cloudauth_20190307_models.CreateWhitelistSettingRequest,
    ) -> cloudauth_20190307_models.CreateWhitelistSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_whitelist_setting(request, runtime)

    async def create_whitelist_setting_simply_async(
        self,
        request: cloudauth_20190307_models.CreateWhitelistSettingRequest,
    ) -> cloudauth_20190307_models.CreateWhitelistSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_whitelist_setting_async(request, runtime)

    def delete_whitelist(
        self,
        request: cloudauth_20190307_models.DeleteWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DeleteWhitelistResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DeleteWhitelistResponse(),
            self.do_request('DeleteWhitelist', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_whitelist_async(
        self,
        request: cloudauth_20190307_models.DeleteWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DeleteWhitelistResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DeleteWhitelistResponse(),
            await self.do_request_async('DeleteWhitelist', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_whitelist_simply(
        self,
        request: cloudauth_20190307_models.DeleteWhitelistRequest,
    ) -> cloudauth_20190307_models.DeleteWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_whitelist(request, runtime)

    async def delete_whitelist_simply_async(
        self,
        request: cloudauth_20190307_models.DeleteWhitelistRequest,
    ) -> cloudauth_20190307_models.DeleteWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_whitelist_async(request, runtime)

    def delete_whitelist_setting(
        self,
        request: cloudauth_20190307_models.DeleteWhitelistSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DeleteWhitelistSettingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DeleteWhitelistSettingResponse(),
            self.do_request('DeleteWhitelistSetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_whitelist_setting_async(
        self,
        request: cloudauth_20190307_models.DeleteWhitelistSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DeleteWhitelistSettingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DeleteWhitelistSettingResponse(),
            await self.do_request_async('DeleteWhitelistSetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_whitelist_setting_simply(
        self,
        request: cloudauth_20190307_models.DeleteWhitelistSettingRequest,
    ) -> cloudauth_20190307_models.DeleteWhitelistSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_whitelist_setting(request, runtime)

    async def delete_whitelist_setting_simply_async(
        self,
        request: cloudauth_20190307_models.DeleteWhitelistSettingRequest,
    ) -> cloudauth_20190307_models.DeleteWhitelistSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_whitelist_setting_async(request, runtime)

    def describe_app_info(
        self,
        request: cloudauth_20190307_models.DescribeAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeAppInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeAppInfoResponse(),
            self.do_request('DescribeAppInfo', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_app_info_async(
        self,
        request: cloudauth_20190307_models.DescribeAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeAppInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeAppInfoResponse(),
            await self.do_request_async('DescribeAppInfo', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_app_info_simply(
        self,
        request: cloudauth_20190307_models.DescribeAppInfoRequest,
    ) -> cloudauth_20190307_models.DescribeAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_info(request, runtime)

    async def describe_app_info_simply_async(
        self,
        request: cloudauth_20190307_models.DescribeAppInfoRequest,
    ) -> cloudauth_20190307_models.DescribeAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_info_async(request, runtime)

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

    def describe_face_config(
        self,
        request: cloudauth_20190307_models.DescribeFaceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceConfigResponse(),
            self.do_request('DescribeFaceConfig', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_face_config_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceConfigResponse(),
            await self.do_request_async('DescribeFaceConfig', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_face_config_simply(
        self,
        request: cloudauth_20190307_models.DescribeFaceConfigRequest,
    ) -> cloudauth_20190307_models.DescribeFaceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_face_config(request, runtime)

    async def describe_face_config_simply_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceConfigRequest,
    ) -> cloudauth_20190307_models.DescribeFaceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_face_config_async(request, runtime)

    def describe_face_usage(
        self,
        request: cloudauth_20190307_models.DescribeFaceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceUsageResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceUsageResponse(),
            self.do_request('DescribeFaceUsage', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_face_usage_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceUsageResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceUsageResponse(),
            await self.do_request_async('DescribeFaceUsage', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_face_usage_simply(
        self,
        request: cloudauth_20190307_models.DescribeFaceUsageRequest,
    ) -> cloudauth_20190307_models.DescribeFaceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_face_usage(request, runtime)

    async def describe_face_usage_simply_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceUsageRequest,
    ) -> cloudauth_20190307_models.DescribeFaceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_face_usage_async(request, runtime)

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

    def describe_rpsdk(
        self,
        request: cloudauth_20190307_models.DescribeRPSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeRPSDKResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeRPSDKResponse(),
            self.do_request('DescribeRPSDK', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_rpsdk_async(
        self,
        request: cloudauth_20190307_models.DescribeRPSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeRPSDKResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeRPSDKResponse(),
            await self.do_request_async('DescribeRPSDK', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_rpsdksimply(
        self,
        request: cloudauth_20190307_models.DescribeRPSDKRequest,
    ) -> cloudauth_20190307_models.DescribeRPSDKResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rpsdk(request, runtime)

    async def describe_rpsdksimply_async(
        self,
        request: cloudauth_20190307_models.DescribeRPSDKRequest,
    ) -> cloudauth_20190307_models.DescribeRPSDKResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rpsdk_async(request, runtime)

    def describe_sdk_url(
        self,
        request: cloudauth_20190307_models.DescribeSdkUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeSdkUrlResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeSdkUrlResponse(),
            self.do_request('DescribeSdkUrl', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_sdk_url_async(
        self,
        request: cloudauth_20190307_models.DescribeSdkUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeSdkUrlResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeSdkUrlResponse(),
            await self.do_request_async('DescribeSdkUrl', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_sdk_url_simply(
        self,
        request: cloudauth_20190307_models.DescribeSdkUrlRequest,
    ) -> cloudauth_20190307_models.DescribeSdkUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sdk_url(request, runtime)

    async def describe_sdk_url_simply_async(
        self,
        request: cloudauth_20190307_models.DescribeSdkUrlRequest,
    ) -> cloudauth_20190307_models.DescribeSdkUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sdk_url_async(request, runtime)

    def describe_update_package_result(
        self,
        request: cloudauth_20190307_models.DescribeUpdatePackageResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeUpdatePackageResultResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUpdatePackageResultResponse(),
            self.do_request('DescribeUpdatePackageResult', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_update_package_result_async(
        self,
        request: cloudauth_20190307_models.DescribeUpdatePackageResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeUpdatePackageResultResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUpdatePackageResultResponse(),
            await self.do_request_async('DescribeUpdatePackageResult', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_update_package_result_simply(
        self,
        request: cloudauth_20190307_models.DescribeUpdatePackageResultRequest,
    ) -> cloudauth_20190307_models.DescribeUpdatePackageResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_update_package_result(request, runtime)

    async def describe_update_package_result_simply_async(
        self,
        request: cloudauth_20190307_models.DescribeUpdatePackageResultRequest,
    ) -> cloudauth_20190307_models.DescribeUpdatePackageResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_update_package_result_async(request, runtime)

    def describe_upload_info(
        self,
        request: cloudauth_20190307_models.DescribeUploadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeUploadInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUploadInfoResponse(),
            self.do_request('DescribeUploadInfo', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_upload_info_async(
        self,
        request: cloudauth_20190307_models.DescribeUploadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeUploadInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUploadInfoResponse(),
            await self.do_request_async('DescribeUploadInfo', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_upload_info_simply(
        self,
        request: cloudauth_20190307_models.DescribeUploadInfoRequest,
    ) -> cloudauth_20190307_models.DescribeUploadInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_upload_info(request, runtime)

    async def describe_upload_info_simply_async(
        self,
        request: cloudauth_20190307_models.DescribeUploadInfoRequest,
    ) -> cloudauth_20190307_models.DescribeUploadInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_upload_info_async(request, runtime)

    def describe_user_status(
        self,
        request: cloudauth_20190307_models.DescribeUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeUserStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUserStatusResponse(),
            self.do_request('DescribeUserStatus', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_user_status_async(
        self,
        request: cloudauth_20190307_models.DescribeUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeUserStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUserStatusResponse(),
            await self.do_request_async('DescribeUserStatus', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_user_status_simply(
        self,
        request: cloudauth_20190307_models.DescribeUserStatusRequest,
    ) -> cloudauth_20190307_models.DescribeUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_status(request, runtime)

    async def describe_user_status_simply_async(
        self,
        request: cloudauth_20190307_models.DescribeUserStatusRequest,
    ) -> cloudauth_20190307_models.DescribeUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_status_async(request, runtime)

    def describe_verify_records(
        self,
        request: cloudauth_20190307_models.DescribeVerifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyRecordsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyRecordsResponse(),
            self.do_request('DescribeVerifyRecords', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_verify_records_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyRecordsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyRecordsResponse(),
            await self.do_request_async('DescribeVerifyRecords', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_verify_records_simply(
        self,
        request: cloudauth_20190307_models.DescribeVerifyRecordsRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_records(request, runtime)

    async def describe_verify_records_simply_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyRecordsRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_records_async(request, runtime)

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

    def describe_verify_setting(
        self,
        request: cloudauth_20190307_models.DescribeVerifySettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifySettingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifySettingResponse(),
            self.do_request('DescribeVerifySetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_verify_setting_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifySettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifySettingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifySettingResponse(),
            await self.do_request_async('DescribeVerifySetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_verify_setting_simply(
        self,
        request: cloudauth_20190307_models.DescribeVerifySettingRequest,
    ) -> cloudauth_20190307_models.DescribeVerifySettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_setting(request, runtime)

    async def describe_verify_setting_simply_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifySettingRequest,
    ) -> cloudauth_20190307_models.DescribeVerifySettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_setting_async(request, runtime)

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

    def describe_verify_usage(
        self,
        request: cloudauth_20190307_models.DescribeVerifyUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyUsageResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyUsageResponse(),
            self.do_request('DescribeVerifyUsage', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_verify_usage_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyUsageResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyUsageResponse(),
            await self.do_request_async('DescribeVerifyUsage', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_verify_usage_simply(
        self,
        request: cloudauth_20190307_models.DescribeVerifyUsageRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_usage(request, runtime)

    async def describe_verify_usage_simply_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyUsageRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_usage_async(request, runtime)

    def describe_whitelist(
        self,
        request: cloudauth_20190307_models.DescribeWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeWhitelistResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeWhitelistResponse(),
            self.do_request('DescribeWhitelist', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_whitelist_async(
        self,
        request: cloudauth_20190307_models.DescribeWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeWhitelistResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeWhitelistResponse(),
            await self.do_request_async('DescribeWhitelist', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_whitelist_simply(
        self,
        request: cloudauth_20190307_models.DescribeWhitelistRequest,
    ) -> cloudauth_20190307_models.DescribeWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_whitelist(request, runtime)

    async def describe_whitelist_simply_async(
        self,
        request: cloudauth_20190307_models.DescribeWhitelistRequest,
    ) -> cloudauth_20190307_models.DescribeWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_whitelist_async(request, runtime)

    def describe_whitelist_setting(
        self,
        request: cloudauth_20190307_models.DescribeWhitelistSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeWhitelistSettingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeWhitelistSettingResponse(),
            self.do_request('DescribeWhitelistSetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_whitelist_setting_async(
        self,
        request: cloudauth_20190307_models.DescribeWhitelistSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeWhitelistSettingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeWhitelistSettingResponse(),
            await self.do_request_async('DescribeWhitelistSetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_whitelist_setting_simply(
        self,
        request: cloudauth_20190307_models.DescribeWhitelistSettingRequest,
    ) -> cloudauth_20190307_models.DescribeWhitelistSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_whitelist_setting(request, runtime)

    async def describe_whitelist_setting_simply_async(
        self,
        request: cloudauth_20190307_models.DescribeWhitelistSettingRequest,
    ) -> cloudauth_20190307_models.DescribeWhitelistSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_whitelist_setting_async(request, runtime)

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

    def init_device(
        self,
        request: cloudauth_20190307_models.InitDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.InitDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.InitDeviceResponse(),
            self.do_request('InitDevice', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def init_device_async(
        self,
        request: cloudauth_20190307_models.InitDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.InitDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.InitDeviceResponse(),
            await self.do_request_async('InitDevice', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def init_device_simply(
        self,
        request: cloudauth_20190307_models.InitDeviceRequest,
    ) -> cloudauth_20190307_models.InitDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_device(request, runtime)

    async def init_device_simply_async(
        self,
        request: cloudauth_20190307_models.InitDeviceRequest,
    ) -> cloudauth_20190307_models.InitDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_device_async(request, runtime)

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

    def update_app_package(
        self,
        request: cloudauth_20190307_models.UpdateAppPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.UpdateAppPackageResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateAppPackageResponse(),
            self.do_request('UpdateAppPackage', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_app_package_async(
        self,
        request: cloudauth_20190307_models.UpdateAppPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.UpdateAppPackageResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateAppPackageResponse(),
            await self.do_request_async('UpdateAppPackage', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_app_package_simply(
        self,
        request: cloudauth_20190307_models.UpdateAppPackageRequest,
    ) -> cloudauth_20190307_models.UpdateAppPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_package(request, runtime)

    async def update_app_package_simply_async(
        self,
        request: cloudauth_20190307_models.UpdateAppPackageRequest,
    ) -> cloudauth_20190307_models.UpdateAppPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_package_async(request, runtime)

    def update_face_config(
        self,
        request: cloudauth_20190307_models.UpdateFaceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.UpdateFaceConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateFaceConfigResponse(),
            self.do_request('UpdateFaceConfig', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_face_config_async(
        self,
        request: cloudauth_20190307_models.UpdateFaceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.UpdateFaceConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateFaceConfigResponse(),
            await self.do_request_async('UpdateFaceConfig', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_face_config_simply(
        self,
        request: cloudauth_20190307_models.UpdateFaceConfigRequest,
    ) -> cloudauth_20190307_models.UpdateFaceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_face_config(request, runtime)

    async def update_face_config_simply_async(
        self,
        request: cloudauth_20190307_models.UpdateFaceConfigRequest,
    ) -> cloudauth_20190307_models.UpdateFaceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_face_config_async(request, runtime)

    def update_verify_setting(
        self,
        request: cloudauth_20190307_models.UpdateVerifySettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.UpdateVerifySettingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateVerifySettingResponse(),
            self.do_request('UpdateVerifySetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_verify_setting_async(
        self,
        request: cloudauth_20190307_models.UpdateVerifySettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.UpdateVerifySettingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateVerifySettingResponse(),
            await self.do_request_async('UpdateVerifySetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_verify_setting_simply(
        self,
        request: cloudauth_20190307_models.UpdateVerifySettingRequest,
    ) -> cloudauth_20190307_models.UpdateVerifySettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_verify_setting(request, runtime)

    async def update_verify_setting_simply_async(
        self,
        request: cloudauth_20190307_models.UpdateVerifySettingRequest,
    ) -> cloudauth_20190307_models.UpdateVerifySettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_verify_setting_async(request, runtime)

    def verify_device(
        self,
        request: cloudauth_20190307_models.VerifyDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VerifyDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.VerifyDeviceResponse(),
            self.do_request('VerifyDevice', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def verify_device_async(
        self,
        request: cloudauth_20190307_models.VerifyDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VerifyDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.VerifyDeviceResponse(),
            await self.do_request_async('VerifyDevice', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def verify_device_simply(
        self,
        request: cloudauth_20190307_models.VerifyDeviceRequest,
    ) -> cloudauth_20190307_models.VerifyDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_device(request, runtime)

    async def verify_device_simply_async(
        self,
        request: cloudauth_20190307_models.VerifyDeviceRequest,
    ) -> cloudauth_20190307_models.VerifyDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_device_async(request, runtime)

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
