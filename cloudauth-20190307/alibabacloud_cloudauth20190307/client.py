# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudauth20190307 import models as cloudauth_20190307_models
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
        request: cloudauth_20190307_models.CompareFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CompareFacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.CompareFacesResponse().from_map(
            self.do_rpcrequest('CompareFaces', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def compare_faces_with_options_async(
        self,
        request: cloudauth_20190307_models.CompareFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CompareFacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.CompareFacesResponse().from_map(
            await self.do_rpcrequest_async('CompareFaces', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def compare_faces(
        self,
        request: cloudauth_20190307_models.CompareFacesRequest,
    ) -> cloudauth_20190307_models.CompareFacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.compare_faces_with_options(request, runtime)

    async def compare_faces_async(
        self,
        request: cloudauth_20190307_models.CompareFacesRequest,
    ) -> cloudauth_20190307_models.CompareFacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.compare_faces_with_options_async(request, runtime)

    def compare_face_verify_with_options(
        self,
        request: cloudauth_20190307_models.CompareFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CompareFaceVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.CompareFaceVerifyResponse().from_map(
            self.do_rpcrequest('CompareFaceVerify', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def compare_face_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.CompareFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CompareFaceVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.CompareFaceVerifyResponse().from_map(
            await self.do_rpcrequest_async('CompareFaceVerify', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def compare_face_verify(
        self,
        request: cloudauth_20190307_models.CompareFaceVerifyRequest,
    ) -> cloudauth_20190307_models.CompareFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.compare_face_verify_with_options(request, runtime)

    async def compare_face_verify_async(
        self,
        request: cloudauth_20190307_models.CompareFaceVerifyRequest,
    ) -> cloudauth_20190307_models.CompareFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.compare_face_verify_with_options_async(request, runtime)

    def contrast_face_verify_with_options(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.ContrastFaceVerifyResponse().from_map(
            self.do_rpcrequest('ContrastFaceVerify', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def contrast_face_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.ContrastFaceVerifyResponse().from_map(
            await self.do_rpcrequest_async('ContrastFaceVerify', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def contrast_face_verify(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyRequest,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.contrast_face_verify_with_options(request, runtime)

    async def contrast_face_verify_async(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyRequest,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.contrast_face_verify_with_options_async(request, runtime)

    def contrast_face_verify_advance(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
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
        contrast_face_verify_req = cloudauth_20190307_models.ContrastFaceVerifyRequest()
        OpenApiUtilClient.convert(request, contrast_face_verify_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        contrast_face_verify_resp = self.contrast_face_verify_with_options(contrast_face_verify_req, runtime)
        return contrast_face_verify_resp

    async def contrast_face_verify_advance_async(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
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
        contrast_face_verify_req = cloudauth_20190307_models.ContrastFaceVerifyRequest()
        OpenApiUtilClient.convert(request, contrast_face_verify_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        contrast_face_verify_resp = await self.contrast_face_verify_with_options_async(contrast_face_verify_req, runtime)
        return contrast_face_verify_resp

    def create_auth_key_with_options(
        self,
        request: cloudauth_20190307_models.CreateAuthKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateAuthKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.CreateAuthKeyResponse().from_map(
            self.do_rpcrequest('CreateAuthKey', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_auth_key_with_options_async(
        self,
        request: cloudauth_20190307_models.CreateAuthKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateAuthKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.CreateAuthKeyResponse().from_map(
            await self.do_rpcrequest_async('CreateAuthKey', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_auth_key(
        self,
        request: cloudauth_20190307_models.CreateAuthKeyRequest,
    ) -> cloudauth_20190307_models.CreateAuthKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_auth_key_with_options(request, runtime)

    async def create_auth_key_async(
        self,
        request: cloudauth_20190307_models.CreateAuthKeyRequest,
    ) -> cloudauth_20190307_models.CreateAuthKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_auth_key_with_options_async(request, runtime)

    def create_face_config_with_options(
        self,
        request: cloudauth_20190307_models.CreateFaceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateFaceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.CreateFaceConfigResponse().from_map(
            self.do_rpcrequest('CreateFaceConfig', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_face_config_with_options_async(
        self,
        request: cloudauth_20190307_models.CreateFaceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateFaceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.CreateFaceConfigResponse().from_map(
            await self.do_rpcrequest_async('CreateFaceConfig', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_face_config(
        self,
        request: cloudauth_20190307_models.CreateFaceConfigRequest,
    ) -> cloudauth_20190307_models.CreateFaceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_face_config_with_options(request, runtime)

    async def create_face_config_async(
        self,
        request: cloudauth_20190307_models.CreateFaceConfigRequest,
    ) -> cloudauth_20190307_models.CreateFaceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_face_config_with_options_async(request, runtime)

    def create_rpsdkwith_options(
        self,
        request: cloudauth_20190307_models.CreateRPSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateRPSDKResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.CreateRPSDKResponse().from_map(
            self.do_rpcrequest('CreateRPSDK', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_rpsdkwith_options_async(
        self,
        request: cloudauth_20190307_models.CreateRPSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateRPSDKResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.CreateRPSDKResponse().from_map(
            await self.do_rpcrequest_async('CreateRPSDK', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_rpsdk(
        self,
        request: cloudauth_20190307_models.CreateRPSDKRequest,
    ) -> cloudauth_20190307_models.CreateRPSDKResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rpsdkwith_options(request, runtime)

    async def create_rpsdk_async(
        self,
        request: cloudauth_20190307_models.CreateRPSDKRequest,
    ) -> cloudauth_20190307_models.CreateRPSDKResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rpsdkwith_options_async(request, runtime)

    def create_verify_sdkwith_options(
        self,
        request: cloudauth_20190307_models.CreateVerifySDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateVerifySDKResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.CreateVerifySDKResponse().from_map(
            self.do_rpcrequest('CreateVerifySDK', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_verify_sdkwith_options_async(
        self,
        request: cloudauth_20190307_models.CreateVerifySDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateVerifySDKResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.CreateVerifySDKResponse().from_map(
            await self.do_rpcrequest_async('CreateVerifySDK', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_verify_sdk(
        self,
        request: cloudauth_20190307_models.CreateVerifySDKRequest,
    ) -> cloudauth_20190307_models.CreateVerifySDKResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_verify_sdkwith_options(request, runtime)

    async def create_verify_sdk_async(
        self,
        request: cloudauth_20190307_models.CreateVerifySDKRequest,
    ) -> cloudauth_20190307_models.CreateVerifySDKResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_verify_sdkwith_options_async(request, runtime)

    def create_verify_setting_with_options(
        self,
        request: cloudauth_20190307_models.CreateVerifySettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateVerifySettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.CreateVerifySettingResponse().from_map(
            self.do_rpcrequest('CreateVerifySetting', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_verify_setting_with_options_async(
        self,
        request: cloudauth_20190307_models.CreateVerifySettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateVerifySettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.CreateVerifySettingResponse().from_map(
            await self.do_rpcrequest_async('CreateVerifySetting', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_verify_setting(
        self,
        request: cloudauth_20190307_models.CreateVerifySettingRequest,
    ) -> cloudauth_20190307_models.CreateVerifySettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_verify_setting_with_options(request, runtime)

    async def create_verify_setting_async(
        self,
        request: cloudauth_20190307_models.CreateVerifySettingRequest,
    ) -> cloudauth_20190307_models.CreateVerifySettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_verify_setting_with_options_async(request, runtime)

    def create_whitelist_with_options(
        self,
        request: cloudauth_20190307_models.CreateWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.CreateWhitelistResponse().from_map(
            self.do_rpcrequest('CreateWhitelist', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_whitelist_with_options_async(
        self,
        request: cloudauth_20190307_models.CreateWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.CreateWhitelistResponse().from_map(
            await self.do_rpcrequest_async('CreateWhitelist', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_whitelist(
        self,
        request: cloudauth_20190307_models.CreateWhitelistRequest,
    ) -> cloudauth_20190307_models.CreateWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_whitelist_with_options(request, runtime)

    async def create_whitelist_async(
        self,
        request: cloudauth_20190307_models.CreateWhitelistRequest,
    ) -> cloudauth_20190307_models.CreateWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_whitelist_with_options_async(request, runtime)

    def delete_whitelist_with_options(
        self,
        request: cloudauth_20190307_models.DeleteWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DeleteWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DeleteWhitelistResponse().from_map(
            self.do_rpcrequest('DeleteWhitelist', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_whitelist_with_options_async(
        self,
        request: cloudauth_20190307_models.DeleteWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DeleteWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DeleteWhitelistResponse().from_map(
            await self.do_rpcrequest_async('DeleteWhitelist', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_whitelist(
        self,
        request: cloudauth_20190307_models.DeleteWhitelistRequest,
    ) -> cloudauth_20190307_models.DeleteWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_whitelist_with_options(request, runtime)

    async def delete_whitelist_async(
        self,
        request: cloudauth_20190307_models.DeleteWhitelistRequest,
    ) -> cloudauth_20190307_models.DeleteWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_whitelist_with_options_async(request, runtime)

    def describe_app_info_with_options(
        self,
        request: cloudauth_20190307_models.DescribeAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeAppInfoResponse().from_map(
            self.do_rpcrequest('DescribeAppInfo', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_app_info_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeAppInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeAppInfo', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_app_info(
        self,
        request: cloudauth_20190307_models.DescribeAppInfoRequest,
    ) -> cloudauth_20190307_models.DescribeAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_info_with_options(request, runtime)

    async def describe_app_info_async(
        self,
        request: cloudauth_20190307_models.DescribeAppInfoRequest,
    ) -> cloudauth_20190307_models.DescribeAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_info_with_options_async(request, runtime)

    def describe_device_info_with_options(
        self,
        request: cloudauth_20190307_models.DescribeDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeDeviceInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeDeviceInfoResponse().from_map(
            self.do_rpcrequest('DescribeDeviceInfo', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_device_info_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeDeviceInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeDeviceInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeDeviceInfo', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_device_info(
        self,
        request: cloudauth_20190307_models.DescribeDeviceInfoRequest,
    ) -> cloudauth_20190307_models.DescribeDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_device_info_with_options(request, runtime)

    async def describe_device_info_async(
        self,
        request: cloudauth_20190307_models.DescribeDeviceInfoRequest,
    ) -> cloudauth_20190307_models.DescribeDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_info_with_options_async(request, runtime)

    def describe_face_config_with_options(
        self,
        request: cloudauth_20190307_models.DescribeFaceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeFaceConfigResponse().from_map(
            self.do_rpcrequest('DescribeFaceConfig', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_face_config_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeFaceConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeFaceConfig', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_face_config(
        self,
        request: cloudauth_20190307_models.DescribeFaceConfigRequest,
    ) -> cloudauth_20190307_models.DescribeFaceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_face_config_with_options(request, runtime)

    async def describe_face_config_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceConfigRequest,
    ) -> cloudauth_20190307_models.DescribeFaceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_face_config_with_options_async(request, runtime)

    def describe_face_usage_with_options(
        self,
        request: cloudauth_20190307_models.DescribeFaceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeFaceUsageResponse().from_map(
            self.do_rpcrequest('DescribeFaceUsage', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_face_usage_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeFaceUsageResponse().from_map(
            await self.do_rpcrequest_async('DescribeFaceUsage', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_face_usage(
        self,
        request: cloudauth_20190307_models.DescribeFaceUsageRequest,
    ) -> cloudauth_20190307_models.DescribeFaceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_face_usage_with_options(request, runtime)

    async def describe_face_usage_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceUsageRequest,
    ) -> cloudauth_20190307_models.DescribeFaceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_face_usage_with_options_async(request, runtime)

    def describe_face_verify_with_options(
        self,
        request: cloudauth_20190307_models.DescribeFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeFaceVerifyResponse().from_map(
            self.do_rpcrequest('DescribeFaceVerify', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_face_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeFaceVerifyResponse().from_map(
            await self.do_rpcrequest_async('DescribeFaceVerify', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_face_verify(
        self,
        request: cloudauth_20190307_models.DescribeFaceVerifyRequest,
    ) -> cloudauth_20190307_models.DescribeFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_face_verify_with_options(request, runtime)

    async def describe_face_verify_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceVerifyRequest,
    ) -> cloudauth_20190307_models.DescribeFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_face_verify_with_options_async(request, runtime)

    def describe_oss_upload_token_with_options(
        self,
        request: cloudauth_20190307_models.DescribeOssUploadTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeOssUploadTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeOssUploadTokenResponse().from_map(
            self.do_rpcrequest('DescribeOssUploadToken', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_oss_upload_token_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeOssUploadTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeOssUploadTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeOssUploadTokenResponse().from_map(
            await self.do_rpcrequest_async('DescribeOssUploadToken', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_oss_upload_token(
        self,
        request: cloudauth_20190307_models.DescribeOssUploadTokenRequest,
    ) -> cloudauth_20190307_models.DescribeOssUploadTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_upload_token_with_options(request, runtime)

    async def describe_oss_upload_token_async(
        self,
        request: cloudauth_20190307_models.DescribeOssUploadTokenRequest,
    ) -> cloudauth_20190307_models.DescribeOssUploadTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_upload_token_with_options_async(request, runtime)

    def describe_rpsdkwith_options(
        self,
        request: cloudauth_20190307_models.DescribeRPSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeRPSDKResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeRPSDKResponse().from_map(
            self.do_rpcrequest('DescribeRPSDK', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rpsdkwith_options_async(
        self,
        request: cloudauth_20190307_models.DescribeRPSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeRPSDKResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeRPSDKResponse().from_map(
            await self.do_rpcrequest_async('DescribeRPSDK', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rpsdk(
        self,
        request: cloudauth_20190307_models.DescribeRPSDKRequest,
    ) -> cloudauth_20190307_models.DescribeRPSDKResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rpsdkwith_options(request, runtime)

    async def describe_rpsdk_async(
        self,
        request: cloudauth_20190307_models.DescribeRPSDKRequest,
    ) -> cloudauth_20190307_models.DescribeRPSDKResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rpsdkwith_options_async(request, runtime)

    def describe_sdk_url_with_options(
        self,
        request: cloudauth_20190307_models.DescribeSdkUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeSdkUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeSdkUrlResponse().from_map(
            self.do_rpcrequest('DescribeSdkUrl', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sdk_url_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeSdkUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeSdkUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeSdkUrlResponse().from_map(
            await self.do_rpcrequest_async('DescribeSdkUrl', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sdk_url(
        self,
        request: cloudauth_20190307_models.DescribeSdkUrlRequest,
    ) -> cloudauth_20190307_models.DescribeSdkUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sdk_url_with_options(request, runtime)

    async def describe_sdk_url_async(
        self,
        request: cloudauth_20190307_models.DescribeSdkUrlRequest,
    ) -> cloudauth_20190307_models.DescribeSdkUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sdk_url_with_options_async(request, runtime)

    def describe_update_package_result_with_options(
        self,
        request: cloudauth_20190307_models.DescribeUpdatePackageResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeUpdatePackageResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeUpdatePackageResultResponse().from_map(
            self.do_rpcrequest('DescribeUpdatePackageResult', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_update_package_result_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeUpdatePackageResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeUpdatePackageResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeUpdatePackageResultResponse().from_map(
            await self.do_rpcrequest_async('DescribeUpdatePackageResult', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_update_package_result(
        self,
        request: cloudauth_20190307_models.DescribeUpdatePackageResultRequest,
    ) -> cloudauth_20190307_models.DescribeUpdatePackageResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_update_package_result_with_options(request, runtime)

    async def describe_update_package_result_async(
        self,
        request: cloudauth_20190307_models.DescribeUpdatePackageResultRequest,
    ) -> cloudauth_20190307_models.DescribeUpdatePackageResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_update_package_result_with_options_async(request, runtime)

    def describe_upload_info_with_options(
        self,
        request: cloudauth_20190307_models.DescribeUploadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeUploadInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeUploadInfoResponse().from_map(
            self.do_rpcrequest('DescribeUploadInfo', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_upload_info_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeUploadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeUploadInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeUploadInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeUploadInfo', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_upload_info(
        self,
        request: cloudauth_20190307_models.DescribeUploadInfoRequest,
    ) -> cloudauth_20190307_models.DescribeUploadInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_upload_info_with_options(request, runtime)

    async def describe_upload_info_async(
        self,
        request: cloudauth_20190307_models.DescribeUploadInfoRequest,
    ) -> cloudauth_20190307_models.DescribeUploadInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_upload_info_with_options_async(request, runtime)

    def describe_user_status_with_options(
        self,
        request: cloudauth_20190307_models.DescribeUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeUserStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeUserStatusResponse().from_map(
            self.do_rpcrequest('DescribeUserStatus', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_status_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeUserStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeUserStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserStatus', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_status(
        self,
        request: cloudauth_20190307_models.DescribeUserStatusRequest,
    ) -> cloudauth_20190307_models.DescribeUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_status_with_options(request, runtime)

    async def describe_user_status_async(
        self,
        request: cloudauth_20190307_models.DescribeUserStatusRequest,
    ) -> cloudauth_20190307_models.DescribeUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_status_with_options_async(request, runtime)

    def describe_verify_records_with_options(
        self,
        request: cloudauth_20190307_models.DescribeVerifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeVerifyRecordsResponse().from_map(
            self.do_rpcrequest('DescribeVerifyRecords', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_verify_records_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeVerifyRecordsResponse().from_map(
            await self.do_rpcrequest_async('DescribeVerifyRecords', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_verify_records(
        self,
        request: cloudauth_20190307_models.DescribeVerifyRecordsRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_records_with_options(request, runtime)

    async def describe_verify_records_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyRecordsRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_records_with_options_async(request, runtime)

    def describe_verify_result_with_options(
        self,
        request: cloudauth_20190307_models.DescribeVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeVerifyResultResponse().from_map(
            self.do_rpcrequest('DescribeVerifyResult', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_verify_result_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeVerifyResultResponse().from_map(
            await self.do_rpcrequest_async('DescribeVerifyResult', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_verify_result(
        self,
        request: cloudauth_20190307_models.DescribeVerifyResultRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_result_with_options(request, runtime)

    async def describe_verify_result_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyResultRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_result_with_options_async(request, runtime)

    def describe_verify_sdkwith_options(
        self,
        request: cloudauth_20190307_models.DescribeVerifySDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifySDKResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeVerifySDKResponse().from_map(
            self.do_rpcrequest('DescribeVerifySDK', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_verify_sdkwith_options_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifySDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifySDKResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeVerifySDKResponse().from_map(
            await self.do_rpcrequest_async('DescribeVerifySDK', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_verify_sdk(
        self,
        request: cloudauth_20190307_models.DescribeVerifySDKRequest,
    ) -> cloudauth_20190307_models.DescribeVerifySDKResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_sdkwith_options(request, runtime)

    async def describe_verify_sdk_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifySDKRequest,
    ) -> cloudauth_20190307_models.DescribeVerifySDKResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_sdkwith_options_async(request, runtime)

    def describe_verify_setting_with_options(
        self,
        request: cloudauth_20190307_models.DescribeVerifySettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifySettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeVerifySettingResponse().from_map(
            self.do_rpcrequest('DescribeVerifySetting', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_verify_setting_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifySettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifySettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeVerifySettingResponse().from_map(
            await self.do_rpcrequest_async('DescribeVerifySetting', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_verify_setting(
        self,
        request: cloudauth_20190307_models.DescribeVerifySettingRequest,
    ) -> cloudauth_20190307_models.DescribeVerifySettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_setting_with_options(request, runtime)

    async def describe_verify_setting_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifySettingRequest,
    ) -> cloudauth_20190307_models.DescribeVerifySettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_setting_with_options_async(request, runtime)

    def describe_verify_token_with_options(
        self,
        request: cloudauth_20190307_models.DescribeVerifyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeVerifyTokenResponse().from_map(
            self.do_rpcrequest('DescribeVerifyToken', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_verify_token_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeVerifyTokenResponse().from_map(
            await self.do_rpcrequest_async('DescribeVerifyToken', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_verify_token(
        self,
        request: cloudauth_20190307_models.DescribeVerifyTokenRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_token_with_options(request, runtime)

    async def describe_verify_token_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyTokenRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_token_with_options_async(request, runtime)

    def describe_verify_usage_with_options(
        self,
        request: cloudauth_20190307_models.DescribeVerifyUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeVerifyUsageResponse().from_map(
            self.do_rpcrequest('DescribeVerifyUsage', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_verify_usage_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeVerifyUsageResponse().from_map(
            await self.do_rpcrequest_async('DescribeVerifyUsage', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_verify_usage(
        self,
        request: cloudauth_20190307_models.DescribeVerifyUsageRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_usage_with_options(request, runtime)

    async def describe_verify_usage_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyUsageRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_usage_with_options_async(request, runtime)

    def describe_whitelist_with_options(
        self,
        request: cloudauth_20190307_models.DescribeWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeWhitelistResponse().from_map(
            self.do_rpcrequest('DescribeWhitelist', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_whitelist_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DescribeWhitelistResponse().from_map(
            await self.do_rpcrequest_async('DescribeWhitelist', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_whitelist(
        self,
        request: cloudauth_20190307_models.DescribeWhitelistRequest,
    ) -> cloudauth_20190307_models.DescribeWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_whitelist_with_options(request, runtime)

    async def describe_whitelist_async(
        self,
        request: cloudauth_20190307_models.DescribeWhitelistRequest,
    ) -> cloudauth_20190307_models.DescribeWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_whitelist_with_options_async(request, runtime)

    def detect_face_attributes_with_options(
        self,
        request: cloudauth_20190307_models.DetectFaceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DetectFaceAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DetectFaceAttributesResponse().from_map(
            self.do_rpcrequest('DetectFaceAttributes', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_face_attributes_with_options_async(
        self,
        request: cloudauth_20190307_models.DetectFaceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DetectFaceAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.DetectFaceAttributesResponse().from_map(
            await self.do_rpcrequest_async('DetectFaceAttributes', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_face_attributes(
        self,
        request: cloudauth_20190307_models.DetectFaceAttributesRequest,
    ) -> cloudauth_20190307_models.DetectFaceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_face_attributes_with_options(request, runtime)

    async def detect_face_attributes_async(
        self,
        request: cloudauth_20190307_models.DetectFaceAttributesRequest,
    ) -> cloudauth_20190307_models.DetectFaceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_face_attributes_with_options_async(request, runtime)

    def init_device_with_options(
        self,
        request: cloudauth_20190307_models.InitDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.InitDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.InitDeviceResponse().from_map(
            self.do_rpcrequest('InitDevice', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def init_device_with_options_async(
        self,
        request: cloudauth_20190307_models.InitDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.InitDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.InitDeviceResponse().from_map(
            await self.do_rpcrequest_async('InitDevice', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def init_device(
        self,
        request: cloudauth_20190307_models.InitDeviceRequest,
    ) -> cloudauth_20190307_models.InitDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_device_with_options(request, runtime)

    async def init_device_async(
        self,
        request: cloudauth_20190307_models.InitDeviceRequest,
    ) -> cloudauth_20190307_models.InitDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_device_with_options_async(request, runtime)

    def init_face_verify_with_options(
        self,
        request: cloudauth_20190307_models.InitFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.InitFaceVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.InitFaceVerifyResponse().from_map(
            self.do_rpcrequest('InitFaceVerify', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def init_face_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.InitFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.InitFaceVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.InitFaceVerifyResponse().from_map(
            await self.do_rpcrequest_async('InitFaceVerify', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def init_face_verify(
        self,
        request: cloudauth_20190307_models.InitFaceVerifyRequest,
    ) -> cloudauth_20190307_models.InitFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_face_verify_with_options(request, runtime)

    async def init_face_verify_async(
        self,
        request: cloudauth_20190307_models.InitFaceVerifyRequest,
    ) -> cloudauth_20190307_models.InitFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_face_verify_with_options_async(request, runtime)

    def liveness_face_verify_with_options(
        self,
        request: cloudauth_20190307_models.LivenessFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.LivenessFaceVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.LivenessFaceVerifyResponse().from_map(
            self.do_rpcrequest('LivenessFaceVerify', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def liveness_face_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.LivenessFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.LivenessFaceVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.LivenessFaceVerifyResponse().from_map(
            await self.do_rpcrequest_async('LivenessFaceVerify', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def liveness_face_verify(
        self,
        request: cloudauth_20190307_models.LivenessFaceVerifyRequest,
    ) -> cloudauth_20190307_models.LivenessFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.liveness_face_verify_with_options(request, runtime)

    async def liveness_face_verify_async(
        self,
        request: cloudauth_20190307_models.LivenessFaceVerifyRequest,
    ) -> cloudauth_20190307_models.LivenessFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.liveness_face_verify_with_options_async(request, runtime)

    def modify_device_info_with_options(
        self,
        request: cloudauth_20190307_models.ModifyDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ModifyDeviceInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.ModifyDeviceInfoResponse().from_map(
            self.do_rpcrequest('ModifyDeviceInfo', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_device_info_with_options_async(
        self,
        request: cloudauth_20190307_models.ModifyDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ModifyDeviceInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.ModifyDeviceInfoResponse().from_map(
            await self.do_rpcrequest_async('ModifyDeviceInfo', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_device_info(
        self,
        request: cloudauth_20190307_models.ModifyDeviceInfoRequest,
    ) -> cloudauth_20190307_models.ModifyDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_device_info_with_options(request, runtime)

    async def modify_device_info_async(
        self,
        request: cloudauth_20190307_models.ModifyDeviceInfoRequest,
    ) -> cloudauth_20190307_models.ModifyDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_device_info_with_options_async(request, runtime)

    def update_app_package_with_options(
        self,
        request: cloudauth_20190307_models.UpdateAppPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.UpdateAppPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.UpdateAppPackageResponse().from_map(
            self.do_rpcrequest('UpdateAppPackage', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_app_package_with_options_async(
        self,
        request: cloudauth_20190307_models.UpdateAppPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.UpdateAppPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.UpdateAppPackageResponse().from_map(
            await self.do_rpcrequest_async('UpdateAppPackage', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_package(
        self,
        request: cloudauth_20190307_models.UpdateAppPackageRequest,
    ) -> cloudauth_20190307_models.UpdateAppPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_package_with_options(request, runtime)

    async def update_app_package_async(
        self,
        request: cloudauth_20190307_models.UpdateAppPackageRequest,
    ) -> cloudauth_20190307_models.UpdateAppPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_package_with_options_async(request, runtime)

    def update_face_config_with_options(
        self,
        request: cloudauth_20190307_models.UpdateFaceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.UpdateFaceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.UpdateFaceConfigResponse().from_map(
            self.do_rpcrequest('UpdateFaceConfig', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_face_config_with_options_async(
        self,
        request: cloudauth_20190307_models.UpdateFaceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.UpdateFaceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.UpdateFaceConfigResponse().from_map(
            await self.do_rpcrequest_async('UpdateFaceConfig', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_face_config(
        self,
        request: cloudauth_20190307_models.UpdateFaceConfigRequest,
    ) -> cloudauth_20190307_models.UpdateFaceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_face_config_with_options(request, runtime)

    async def update_face_config_async(
        self,
        request: cloudauth_20190307_models.UpdateFaceConfigRequest,
    ) -> cloudauth_20190307_models.UpdateFaceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_face_config_with_options_async(request, runtime)

    def update_verify_setting_with_options(
        self,
        request: cloudauth_20190307_models.UpdateVerifySettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.UpdateVerifySettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.UpdateVerifySettingResponse().from_map(
            self.do_rpcrequest('UpdateVerifySetting', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_verify_setting_with_options_async(
        self,
        request: cloudauth_20190307_models.UpdateVerifySettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.UpdateVerifySettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.UpdateVerifySettingResponse().from_map(
            await self.do_rpcrequest_async('UpdateVerifySetting', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_verify_setting(
        self,
        request: cloudauth_20190307_models.UpdateVerifySettingRequest,
    ) -> cloudauth_20190307_models.UpdateVerifySettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_verify_setting_with_options(request, runtime)

    async def update_verify_setting_async(
        self,
        request: cloudauth_20190307_models.UpdateVerifySettingRequest,
    ) -> cloudauth_20190307_models.UpdateVerifySettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_verify_setting_with_options_async(request, runtime)

    def verify_device_with_options(
        self,
        request: cloudauth_20190307_models.VerifyDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VerifyDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.VerifyDeviceResponse().from_map(
            self.do_rpcrequest('VerifyDevice', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_device_with_options_async(
        self,
        request: cloudauth_20190307_models.VerifyDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VerifyDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.VerifyDeviceResponse().from_map(
            await self.do_rpcrequest_async('VerifyDevice', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_device(
        self,
        request: cloudauth_20190307_models.VerifyDeviceRequest,
    ) -> cloudauth_20190307_models.VerifyDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_device_with_options(request, runtime)

    async def verify_device_async(
        self,
        request: cloudauth_20190307_models.VerifyDeviceRequest,
    ) -> cloudauth_20190307_models.VerifyDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_device_with_options_async(request, runtime)

    def verify_material_with_options(
        self,
        request: cloudauth_20190307_models.VerifyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VerifyMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.VerifyMaterialResponse().from_map(
            self.do_rpcrequest('VerifyMaterial', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_material_with_options_async(
        self,
        request: cloudauth_20190307_models.VerifyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VerifyMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_20190307_models.VerifyMaterialResponse().from_map(
            await self.do_rpcrequest_async('VerifyMaterial', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_material(
        self,
        request: cloudauth_20190307_models.VerifyMaterialRequest,
    ) -> cloudauth_20190307_models.VerifyMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_material_with_options(request, runtime)

    async def verify_material_async(
        self,
        request: cloudauth_20190307_models.VerifyMaterialRequest,
    ) -> cloudauth_20190307_models.VerifyMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_material_with_options_async(request, runtime)
