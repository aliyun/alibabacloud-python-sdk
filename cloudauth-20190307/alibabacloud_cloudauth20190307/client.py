# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudauth20190307 import models as cloudauth_20190307_models
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
        params = open_api_models.Params(
            action='CompareFaces',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFacesResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CompareFaces',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFacesResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CompareFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFaceVerifyResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CompareFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFaceVerifyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Model'] = request.model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ContrastFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.ContrastFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def contrast_face_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Model'] = request.model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ContrastFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.ContrastFaceVerifyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['BizType'] = request.biz_type
        query['UserDeviceId'] = request.user_device_id
        query['Test'] = request.test
        query['AuthYears'] = request.auth_years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAuthKey',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateAuthKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_auth_key_with_options_async(
        self,
        request: cloudauth_20190307_models.CreateAuthKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateAuthKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BizType'] = request.biz_type
        query['UserDeviceId'] = request.user_device_id
        query['Test'] = request.test
        query['AuthYears'] = request.auth_years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAuthKey',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateAuthKeyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['SourceIp'] = request.source_ip
        query['Lang'] = request.lang
        query['BizType'] = request.biz_type
        query['BizName'] = request.biz_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFaceConfig',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateFaceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_face_config_with_options_async(
        self,
        request: cloudauth_20190307_models.CreateFaceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateFaceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SourceIp'] = request.source_ip
        query['Lang'] = request.lang
        query['BizType'] = request.biz_type
        query['BizName'] = request.biz_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFaceConfig',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateFaceConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['SourceIp'] = request.source_ip
        query['Lang'] = request.lang
        query['AppUrl'] = request.app_url
        query['Platform'] = request.platform
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRPSDK',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateRPSDKResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rpsdkwith_options_async(
        self,
        request: cloudauth_20190307_models.CreateRPSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateRPSDKResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SourceIp'] = request.source_ip
        query['Lang'] = request.lang
        query['AppUrl'] = request.app_url
        query['Platform'] = request.platform
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRPSDK',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateRPSDKResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppUrl'] = request.app_url
        query['Platform'] = request.platform
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateVerifySDK',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateVerifySDKResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_verify_sdkwith_options_async(
        self,
        request: cloudauth_20190307_models.CreateVerifySDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateVerifySDKResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppUrl'] = request.app_url
        query['Platform'] = request.platform
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateVerifySDK',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateVerifySDKResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['BizType'] = request.biz_type
        query['BizName'] = request.biz_name
        query['Solution'] = request.solution
        query['GuideStep'] = request.guide_step
        query['PrivacyStep'] = request.privacy_step
        query['ResultStep'] = request.result_step
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateVerifySetting',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateVerifySettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_verify_setting_with_options_async(
        self,
        request: cloudauth_20190307_models.CreateVerifySettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateVerifySettingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BizType'] = request.biz_type
        query['BizName'] = request.biz_name
        query['Solution'] = request.solution
        query['GuideStep'] = request.guide_step
        query['PrivacyStep'] = request.privacy_step
        query['ResultStep'] = request.result_step
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateVerifySetting',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateVerifySettingResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['SourceIp'] = request.source_ip
        query['Lang'] = request.lang
        query['BizType'] = request.biz_type
        query['BizId'] = request.biz_id
        query['IdCardNum'] = request.id_card_num
        query['ValidDay'] = request.valid_day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateWhitelist',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_whitelist_with_options_async(
        self,
        request: cloudauth_20190307_models.CreateWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SourceIp'] = request.source_ip
        query['Lang'] = request.lang
        query['BizType'] = request.biz_type
        query['BizId'] = request.biz_id
        query['IdCardNum'] = request.id_card_num
        query['ValidDay'] = request.valid_day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateWhitelist',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['SourceIp'] = request.source_ip
        query['Lang'] = request.lang
        query['Ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteWhitelist',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DeleteWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_whitelist_with_options_async(
        self,
        request: cloudauth_20190307_models.DeleteWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DeleteWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SourceIp'] = request.source_ip
        query['Lang'] = request.lang
        query['Ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteWhitelist',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DeleteWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        query['Platform'] = request.platform
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAppInfo',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_info_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeAppInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        query['Platform'] = request.platform
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAppInfo',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeAppInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        query['DeviceId'] = request.device_id
        query['BizType'] = request.biz_type
        query['UserDeviceId'] = request.user_device_id
        query['ExpiredStartDay'] = request.expired_start_day
        query['ExpiredEndDay'] = request.expired_end_day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDeviceInfo',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_device_info_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        query['DeviceId'] = request.device_id
        query['BizType'] = request.biz_type
        query['UserDeviceId'] = request.user_device_id
        query['ExpiredStartDay'] = request.expired_start_day
        query['ExpiredEndDay'] = request.expired_end_day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDeviceInfo',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['SourceIp'] = request.source_ip
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFaceConfig',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_face_config_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SourceIp'] = request.source_ip
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFaceConfig',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFaceUsage',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_face_usage_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFaceUsage',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceUsageResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['SceneId'] = request.scene_id
        query['CertifyId'] = request.certify_id
        query['PictureReturnType'] = request.picture_return_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_face_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceVerifyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SceneId'] = request.scene_id
        query['CertifyId'] = request.certify_id
        query['PictureReturnType'] = request.picture_return_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceVerifyResponse(),
            await self.call_api_async(params, req, runtime)
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
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeOssUploadTokenResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeOssUploadToken',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeOssUploadTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_upload_token_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeOssUploadTokenResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeOssUploadToken',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeOssUploadTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_upload_token(self) -> cloudauth_20190307_models.DescribeOssUploadTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_upload_token_with_options(runtime)

    async def describe_oss_upload_token_async(self) -> cloudauth_20190307_models.DescribeOssUploadTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_upload_token_with_options_async(runtime)

    def describe_rpsdkwith_options(
        self,
        request: cloudauth_20190307_models.DescribeRPSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeRPSDKResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SourceIp'] = request.source_ip
        query['Lang'] = request.lang
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRPSDK',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeRPSDKResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rpsdkwith_options_async(
        self,
        request: cloudauth_20190307_models.DescribeRPSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeRPSDKResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SourceIp'] = request.source_ip
        query['Lang'] = request.lang
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRPSDK',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeRPSDKResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Id'] = request.id
        query['Debug'] = request.debug
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSdkUrl',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeSdkUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sdk_url_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeSdkUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeSdkUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['Debug'] = request.debug
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSdkUrl',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeSdkUrlResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUpdatePackageResult',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUpdatePackageResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_update_package_result_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeUpdatePackageResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeUpdatePackageResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUpdatePackageResult',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUpdatePackageResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Biz'] = request.biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUploadInfo',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUploadInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_upload_info_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeUploadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeUploadInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Biz'] = request.biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUploadInfo',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUploadInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeUserStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeUserStatus',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeUserStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeUserStatus',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_status(self) -> cloudauth_20190307_models.DescribeUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_status_with_options(runtime)

    async def describe_user_status_async(self) -> cloudauth_20190307_models.DescribeUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_status_with_options_async(runtime)

    def describe_verify_records_with_options(
        self,
        request: cloudauth_20190307_models.DescribeVerifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TotalCount'] = request.total_count
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        query['BizType'] = request.biz_type
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        query['BizId'] = request.biz_id
        query['IdCardNum'] = request.id_card_num
        query['StatusList'] = request.status_list
        query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeVerifyRecords',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_records_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TotalCount'] = request.total_count
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        query['BizType'] = request.biz_type
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        query['BizId'] = request.biz_id
        query['IdCardNum'] = request.id_card_num
        query['StatusList'] = request.status_list
        query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeVerifyRecords',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyRecordsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['BizId'] = request.biz_id
        query['BizType'] = request.biz_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeVerifyResult',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_result_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BizId'] = request.biz_id
        query['BizType'] = request.biz_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeVerifyResult',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeVerifySDK',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifySDKResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_sdkwith_options_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifySDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifySDKResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeVerifySDK',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifySDKResponse(),
            await self.call_api_async(params, req, runtime)
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
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifySettingResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVerifySetting',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifySettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_setting_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifySettingResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVerifySetting',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifySettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_setting(self) -> cloudauth_20190307_models.DescribeVerifySettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_setting_with_options(runtime)

    async def describe_verify_setting_async(self) -> cloudauth_20190307_models.DescribeVerifySettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_setting_with_options_async(runtime)

    def describe_verify_token_with_options(
        self,
        request: cloudauth_20190307_models.DescribeVerifyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IdCardBackImageUrl'] = request.id_card_back_image_url
        query['BizType'] = request.biz_type
        query['FailedRedirectUrl'] = request.failed_redirect_url
        query['FaceRetainedImageUrl'] = request.face_retained_image_url
        query['CallbackSeed'] = request.callback_seed
        query['IdCardFrontImageUrl'] = request.id_card_front_image_url
        query['UserId'] = request.user_id
        query['BizId'] = request.biz_id
        query['Name'] = request.name
        query['IdCardNumber'] = request.id_card_number
        query['PassedRedirectUrl'] = request.passed_redirect_url
        query['CallbackUrl'] = request.callback_url
        query['UserIp'] = request.user_ip
        query['UserPhoneNumber'] = request.user_phone_number
        query['UserRegistTime'] = request.user_regist_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeVerifyToken',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_token_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IdCardBackImageUrl'] = request.id_card_back_image_url
        query['BizType'] = request.biz_type
        query['FailedRedirectUrl'] = request.failed_redirect_url
        query['FaceRetainedImageUrl'] = request.face_retained_image_url
        query['CallbackSeed'] = request.callback_seed
        query['IdCardFrontImageUrl'] = request.id_card_front_image_url
        query['UserId'] = request.user_id
        query['BizId'] = request.biz_id
        query['Name'] = request.name
        query['IdCardNumber'] = request.id_card_number
        query['PassedRedirectUrl'] = request.passed_redirect_url
        query['CallbackUrl'] = request.callback_url
        query['UserIp'] = request.user_ip
        query['UserPhoneNumber'] = request.user_phone_number
        query['UserRegistTime'] = request.user_regist_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeVerifyToken',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyTokenResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['BizType'] = request.biz_type
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeVerifyUsage',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_usage_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BizType'] = request.biz_type
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeVerifyUsage',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyUsageResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['SourceIp'] = request.source_ip
        query['Lang'] = request.lang
        query['BizType'] = request.biz_type
        query['BizId'] = request.biz_id
        query['IdCardNum'] = request.id_card_num
        query['ValidStartDate'] = request.valid_start_date
        query['ValidEndDate'] = request.valid_end_date
        query['Valid'] = request.valid
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWhitelist',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_whitelist_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SourceIp'] = request.source_ip
        query['Lang'] = request.lang
        query['BizType'] = request.biz_type
        query['BizId'] = request.biz_id
        query['IdCardNum'] = request.id_card_num
        query['ValidStartDate'] = request.valid_start_date
        query['ValidEndDate'] = request.valid_end_date
        query['Valid'] = request.valid
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWhitelist',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DetectFaceAttributes',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DetectFaceAttributesResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='DetectFaceAttributes',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DetectFaceAttributesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CertifyId'] = request.certify_id
        query['OuterOrderNo'] = request.outer_order_no
        query['Channel'] = request.channel
        query['Merchant'] = request.merchant
        query['ProductName'] = request.product_name
        query['ProduceNode'] = request.produce_node
        query['BizData'] = request.biz_data
        query['MetaInfo'] = request.meta_info
        query['CertifyPrincipal'] = request.certify_principal
        query['AppVersion'] = request.app_version
        query['DeviceToken'] = request.device_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='InitDevice',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.InitDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_device_with_options_async(
        self,
        request: cloudauth_20190307_models.InitDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.InitDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CertifyId'] = request.certify_id
        query['OuterOrderNo'] = request.outer_order_no
        query['Channel'] = request.channel
        query['Merchant'] = request.merchant
        query['ProductName'] = request.product_name
        query['ProduceNode'] = request.produce_node
        query['BizData'] = request.biz_data
        query['MetaInfo'] = request.meta_info
        query['CertifyPrincipal'] = request.certify_principal
        query['AppVersion'] = request.app_version
        query['DeviceToken'] = request.device_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='InitDevice',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.InitDeviceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['SceneId'] = request.scene_id
        query['OuterOrderNo'] = request.outer_order_no
        query['ProductCode'] = request.product_code
        query['CertType'] = request.cert_type
        query['CertName'] = request.cert_name
        query['CertNo'] = request.cert_no
        query['ReturnUrl'] = request.return_url
        query['MetaInfo'] = request.meta_info
        query['Mobile'] = request.mobile
        query['Ip'] = request.ip
        query['UserId'] = request.user_id
        query['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        query['CertifyId'] = request.certify_id
        query['OssBucketName'] = request.oss_bucket_name
        query['OssObjectName'] = request.oss_object_name
        query['CallbackUrl'] = request.callback_url
        query['CallbackToken'] = request.callback_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='InitFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.InitFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_face_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.InitFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.InitFaceVerifyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SceneId'] = request.scene_id
        query['OuterOrderNo'] = request.outer_order_no
        query['ProductCode'] = request.product_code
        query['CertType'] = request.cert_type
        query['CertName'] = request.cert_name
        query['CertNo'] = request.cert_no
        query['ReturnUrl'] = request.return_url
        query['MetaInfo'] = request.meta_info
        query['Mobile'] = request.mobile
        query['Ip'] = request.ip
        query['UserId'] = request.user_id
        query['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        query['CertifyId'] = request.certify_id
        query['OssBucketName'] = request.oss_bucket_name
        query['OssObjectName'] = request.oss_object_name
        query['CallbackUrl'] = request.callback_url
        query['CallbackToken'] = request.callback_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='InitFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.InitFaceVerifyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Model'] = request.model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='LivenessFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.LivenessFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def liveness_face_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.LivenessFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.LivenessFaceVerifyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Model'] = request.model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='LivenessFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.LivenessFaceVerifyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['DeviceId'] = request.device_id
        query['UserDeviceId'] = request.user_device_id
        query['BizType'] = request.biz_type
        query['Duration'] = request.duration
        query['ExpiredDay'] = request.expired_day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDeviceInfo',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.ModifyDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_device_info_with_options_async(
        self,
        request: cloudauth_20190307_models.ModifyDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ModifyDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeviceId'] = request.device_id
        query['UserDeviceId'] = request.user_device_id
        query['BizType'] = request.biz_type
        query['Duration'] = request.duration
        query['ExpiredDay'] = request.expired_day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDeviceInfo',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.ModifyDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Id'] = request.id
        query['PackageUrl'] = request.package_url
        query['Platform'] = request.platform
        query['Debug'] = request.debug
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAppPackage',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateAppPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_package_with_options_async(
        self,
        request: cloudauth_20190307_models.UpdateAppPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.UpdateAppPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['PackageUrl'] = request.package_url
        query['Platform'] = request.platform
        query['Debug'] = request.debug
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAppPackage',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateAppPackageResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['SourceIp'] = request.source_ip
        query['Lang'] = request.lang
        query['BizType'] = request.biz_type
        query['BizName'] = request.biz_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateFaceConfig',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateFaceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_face_config_with_options_async(
        self,
        request: cloudauth_20190307_models.UpdateFaceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.UpdateFaceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SourceIp'] = request.source_ip
        query['Lang'] = request.lang
        query['BizType'] = request.biz_type
        query['BizName'] = request.biz_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateFaceConfig',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateFaceConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['BizType'] = request.biz_type
        query['BizName'] = request.biz_name
        query['Solution'] = request.solution
        query['GuideStep'] = request.guide_step
        query['PrivacyStep'] = request.privacy_step
        query['ResultStep'] = request.result_step
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateVerifySetting',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateVerifySettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_verify_setting_with_options_async(
        self,
        request: cloudauth_20190307_models.UpdateVerifySettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.UpdateVerifySettingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BizType'] = request.biz_type
        query['BizName'] = request.biz_name
        query['Solution'] = request.solution
        query['GuideStep'] = request.guide_step
        query['PrivacyStep'] = request.privacy_step
        query['ResultStep'] = request.result_step
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateVerifySetting',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateVerifySettingResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CertifyId'] = request.certify_id
        query['CertifyData'] = request.certify_data
        query['AppVersion'] = request.app_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='VerifyDevice',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.VerifyDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_device_with_options_async(
        self,
        request: cloudauth_20190307_models.VerifyDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VerifyDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CertifyId'] = request.certify_id
        query['CertifyData'] = request.certify_data
        query['AppVersion'] = request.app_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='VerifyDevice',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.VerifyDeviceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['IdCardBackImageUrl'] = request.id_card_back_image_url
        query['FaceImageUrl'] = request.face_image_url
        query['BizType'] = request.biz_type
        query['BizId'] = request.biz_id
        query['Name'] = request.name
        query['IdCardNumber'] = request.id_card_number
        query['IdCardFrontImageUrl'] = request.id_card_front_image_url
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='VerifyMaterial',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.VerifyMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_material_with_options_async(
        self,
        request: cloudauth_20190307_models.VerifyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VerifyMaterialResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IdCardBackImageUrl'] = request.id_card_back_image_url
        query['FaceImageUrl'] = request.face_image_url
        query['BizType'] = request.biz_type
        query['BizId'] = request.biz_id
        query['Name'] = request.name
        query['IdCardNumber'] = request.id_card_number
        query['IdCardFrontImageUrl'] = request.id_card_front_image_url
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='VerifyMaterial',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.VerifyMaterialResponse(),
            await self.call_api_async(params, req, runtime)
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
