# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_cloudauth20190307 import models as cloudauth_20190307_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_rpc_util.client import Client as RPCUtilClient
from alibabacloud_oss_sdk.client import Client as OSSClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "central"
        self.check_config(config)
        self._endpoint = self.get_endpoint("cloudauth", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def describe_face_config(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DescribeFaceConfigResponse().from_map(self.do_request("DescribeFaceConfig", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def describe_face_config_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_face_config(request, runtime)

    def update_face_config(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.UpdateFaceConfigResponse().from_map(self.do_request("UpdateFaceConfig", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def update_face_config_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_face_config(request, runtime)

    def create_face_config(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.CreateFaceConfigResponse().from_map(self.do_request("CreateFaceConfig", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def create_face_config_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_face_config(request, runtime)

    def liveness_face_verify(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.LivenessFaceVerifyResponse().from_map(self.do_request("LivenessFaceVerify", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def liveness_face_verify_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.liveness_face_verify(request, runtime)

    def compare_face_verify(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.CompareFaceVerifyResponse().from_map(self.do_request("CompareFaceVerify", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def compare_face_verify_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.compare_face_verify(request, runtime)

    def describe_sdk_url(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DescribeSdkUrlResponse().from_map(self.do_request("DescribeSdkUrl", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def describe_sdk_url_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sdk_url(request, runtime)

    def describe_update_package_result(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DescribeUpdatePackageResultResponse().from_map(self.do_request("DescribeUpdatePackageResult", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def describe_update_package_result_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_update_package_result(request, runtime)

    def update_app_package(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.UpdateAppPackageResponse().from_map(self.do_request("UpdateAppPackage", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def update_app_package_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_package(request, runtime)

    def describe_app_info(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DescribeAppInfoResponse().from_map(self.do_request("DescribeAppInfo", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def describe_app_info_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_info(request, runtime)

    def contrast_face_verify(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.ContrastFaceVerifyResponse().from_map(self.do_request("ContrastFaceVerify", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def contrast_face_verify_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.contrast_face_verify(request, runtime)

    def contrast_face_verify_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="Cloudauth",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
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
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.face_contrast_file_object,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        contrast_face_verify_req.face_contrast_file = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        contrast_face_verify_resp = self.contrast_face_verify(contrast_face_verify_req, runtime)
        return contrast_face_verify_resp

    def init_device(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.InitDeviceResponse().from_map(self.do_request("InitDevice", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def init_device_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.init_device(request, runtime)

    def init_face_verify(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.InitFaceVerifyResponse().from_map(self.do_request("InitFaceVerify", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def init_face_verify_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.init_face_verify(request, runtime)

    def describe_face_verify(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DescribeFaceVerifyResponse().from_map(self.do_request("DescribeFaceVerify", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def describe_face_verify_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_face_verify(request, runtime)

    def verify_device(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.VerifyDeviceResponse().from_map(self.do_request("VerifyDevice", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def verify_device_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_device(request, runtime)

    def modify_device_info(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.ModifyDeviceInfoResponse().from_map(self.do_request("ModifyDeviceInfo", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def modify_device_info_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_device_info(request, runtime)

    def describe_verify_sdk(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DescribeVerifySDKResponse().from_map(self.do_request("DescribeVerifySDK", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def describe_verify_sdksimply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_sdk(request, runtime)

    def describe_device_info(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DescribeDeviceInfoResponse().from_map(self.do_request("DescribeDeviceInfo", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def describe_device_info_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_info(request, runtime)

    def create_verify_sdk(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.CreateVerifySDKResponse().from_map(self.do_request("CreateVerifySDK", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def create_verify_sdksimply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_verify_sdk(request, runtime)

    def create_auth_key(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.CreateAuthKeyResponse().from_map(self.do_request("CreateAuthKey", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def create_auth_key_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_auth_key(request, runtime)

    def detect_face_attributes(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DetectFaceAttributesResponse().from_map(self.do_request("DetectFaceAttributes", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def detect_face_attributes_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_face_attributes(request, runtime)

    def compare_faces(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.CompareFacesResponse().from_map(self.do_request("CompareFaces", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def compare_faces_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.compare_faces(request, runtime)

    def describe_face_usage(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DescribeFaceUsageResponse().from_map(self.do_request("DescribeFaceUsage", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def describe_face_usage_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_face_usage(request, runtime)

    def describe_verify_records(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DescribeVerifyRecordsResponse().from_map(self.do_request("DescribeVerifyRecords", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def describe_verify_records_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_records(request, runtime)

    def update_verify_setting(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.UpdateVerifySettingResponse().from_map(self.do_request("UpdateVerifySetting", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def update_verify_setting_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_verify_setting(request, runtime)

    def create_verify_setting(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.CreateVerifySettingResponse().from_map(self.do_request("CreateVerifySetting", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def create_verify_setting_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_verify_setting(request, runtime)

    def describe_verify_setting(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DescribeVerifySettingResponse().from_map(self.do_request("DescribeVerifySetting", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def describe_verify_setting_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_setting(request, runtime)

    def describe_verify_usage(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DescribeVerifyUsageResponse().from_map(self.do_request("DescribeVerifyUsage", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def describe_verify_usage_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_usage(request, runtime)

    def describe_user_status(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DescribeUserStatusResponse().from_map(self.do_request("DescribeUserStatus", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def describe_user_status_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_status(request, runtime)

    def describe_upload_info(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DescribeUploadInfoResponse().from_map(self.do_request("DescribeUploadInfo", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def describe_upload_info_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_upload_info(request, runtime)

    def describe_rpsdk(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DescribeRPSDKResponse().from_map(self.do_request("DescribeRPSDK", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def describe_rpsdksimply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rpsdk(request, runtime)

    def create_rpsdk(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.CreateRPSDKResponse().from_map(self.do_request("CreateRPSDK", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def create_rpsdksimply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rpsdk(request, runtime)

    def verify_material(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.VerifyMaterialResponse().from_map(self.do_request("VerifyMaterial", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def verify_material_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_material(request, runtime)

    def describe_verify_result(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DescribeVerifyResultResponse().from_map(self.do_request("DescribeVerifyResult", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def describe_verify_result_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_result(request, runtime)

    def describe_oss_upload_token(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DescribeOssUploadTokenResponse().from_map(self.do_request("DescribeOssUploadToken", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def describe_oss_upload_token_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_upload_token(request, runtime)

    def describe_verify_token(self, request, runtime):
        UtilClient.validate_model(request)
        return cloudauth_20190307_models.DescribeVerifyTokenResponse().from_map(self.do_request("DescribeVerifyToken", "HTTPS", "POST", "2019-03-07", "AK", None, request.to_map(), runtime))

    def describe_verify_token_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_token(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
